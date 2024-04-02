#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os, sys
import json, jsonlines


# In[3]:


input_folder = '{path_to_libgen}/Documents/Lab/libgen/advisory-dataset/'
maven_report_path = os.path.join(input_folder, 'maven_reports.json')
npm_report_path = os.path.join(input_folder, 'npm_reports.json')
pypi_report_path = os.path.join(input_folder, 'pypi_reports.json')
go_report_path = os.path.join(input_folder, 'go_reports.json')


# In[12]:


rerank_folder = '{path_to_libgen}/Documents/Lab/libgen/ChatGPT/rerank_1/'
# maven_rerank_path = os.path.join(rerank_folder, 'maven_rerank_1.json')
npm_rerank_path = os.path.join(rerank_folder, 'npm_rerank_1.json')
pypi_rerank_path = os.path.join(rerank_folder, 'pypi_rerank_1.json')
go_rerank_path = os.path.join(rerank_folder, 'go_rerank_1.json')


# In[16]:


# with open(maven_rerank_path, 'r') as f:
#     maven_rerank = json.load(f)
with open(npm_rerank_path, 'r') as f:
    npm_rerank = json.load(f)
with open(pypi_rerank_path, 'r') as f:
    pypi_rerank = json.load(f)
with open(go_rerank_path, 'r') as f:
    go_rerank = json.load(f)


# In[14]:


with open(maven_report_path, 'r') as f:
    maven_report = json.load(f)
with open(npm_report_path, 'r') as f:
    npm_report = json.load(f)
with open(pypi_report_path, 'r') as f:
    pypi_report = json.load(f)
with open(go_report_path, 'r') as f:
    go_report = json.load(f)


# In[15]:


def raw_query(vuln, language, recommend):
    if language == 'maven':
        prompt = 'Below is a Java vulnerability description. Please identify the software name affected by it. ' +             f'Input: {vuln["details"]}. Top 1 search result is {recommend}. ' +             'What is affected packages? Please outputs as the format "maven:group id:artifact id". '
    elif language == 'npm':
        prompt = 'Below is a JavaScript vulnerability description. Please identify the software name affected by it. ' +             f'Input: {vuln["details"]}. Top 1 search result is {recommend}. ' +             'What is affected packages? Please outputs as the format "npm:library name". '
    elif language == 'pypi':
        prompt = 'Below is a Python vulnerability description. Please identify the software name affected by it. ' +             f'Input: {vuln["details"]}. Top 1 search result is {recommend}. ' +             'What is affected packages? Please outputs as the format "pypi:library name". '
    elif language == 'go':
        prompt = 'Below is a Go vulnerability description. Please identify the software name affected by it. ' +             f'Input: {vuln["details"]}. Top 1 search result is {recommend}. ' +             'What is affected packages? Please outputs as the format "go:library name". '
#     return prompt
    return requestChatCompletion(prompt, t=0, engine='gpt-35-turbo')


# In[22]:


reports_combined = [npm_report, pypi_report, go_report]
rerank_combined = [npm_rerank, pypi_rerank, go_rerank]
for language, reports, rerank in zip(['maven', 'npm', 'pypi', 'go'], reports_combined, rerank_combined):
    target_folder = '.'
    target_path = os.path.join(target_folder, f'{language}_res.json')
    total_res = []
    reranks = rerank['train'] + rerank['valid'] + rerank['test']
    for vuln, lib in zip(reports, reranks):
        top_res = raw_query(vuln, language, lib[1])
        total_res.append({'id': vuln['id'], 'raw_res': top_res})
    with open(target_path, 'w') as f:
        json.dump(total_res, f)

