import os, sys
import json
from tqdm import tqdm

def query(vuln, k, shot_key):
    shots = [lib['lib_name'] for lib in vuln[shot_key][:k]]
    prompt = 'Below is a Java vulnerability description. Please identify the software name affected by it. ' + \
        f'Input: {vuln["desc"]}. Top {k} search results are {shots} ' + \
        'What is affected packages? Please output in the Maven identifier format "maven:group id:artifact id". '
#     return prompt
    return requestChatCompletion(prompt, t=0, engine='gpt-35-turbo') #also use GPT4
    
def raw_query(vuln, shot_key):
    shots = [lib['lib_name'] for lib in vuln[shot_key][:k]]
    prompt = 'Below is a Java vulnerability description. Please identify the software name affected by it. ' + \
        f'Input: {vuln["desc"]}. ' + \
        'What is affected packages? Please output in the Maven identifier format "maven:group id:artifact id". '
#     return prompt
    return requestChatCompletion(prompt, t=0, engine='gpt-35-turbo') #also use GPT4


input_folder = '.'
train_path = os.path.join(input_folder, 'train.json')
valid_path = os.path.join(input_folder, 'valid.json')
test_path = os.path.join(input_folder, 'test.json')

with open(train_path, 'r') as f:
    train = json.load(f)
with open(valid_path, 'r') as f:
    valid = json.load(f)
with open(test_path, 'r') as f:
    test = json.load(f) 
vulns = train+valid+test


for k in [0,1,2,3,5,10,20]:
    target_folder = '.'
    target_path = os.path.join(target_folder, f'{k}_res.json')
    total_res = []
    for vuln in tqdm(vulns):
        top_res = query(vuln, k, 'top_k') if k > 0 else raw_query(vuln, 'top_k')
        rerank_res = query(vuln, k, 'rerank_k') if k > 0 else raw_query(vuln, 'rerank_k')
        total_res.append({'cve_id': vuln['cve_id'], 'top_res': top_res, 'rerank_res': rerank_res})
    with open(target_path, 'w') as f:
        json.dump(total_res, f)