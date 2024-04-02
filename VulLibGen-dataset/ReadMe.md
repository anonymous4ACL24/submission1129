## This is our dataset used for VulLibGen

#### advisory-dataset

Folder `advisory-dataset` corresponds to the dataset extract from github advisory.
For reproduction, users can clone the repository from `https://github.com/advisories` and run the scripts in `dataset_extractor.ipynb`.

Then, `{ecosystem}_reports.json` corresponds to the raw reports of each programming language (ecosystem), and `combined_reports.json` combines the vulnerability reports of four used programming languages.

#### VulLib

Folder `VulLib` corresponds to the Java dataset. It is extended from the Java vulnerability reports in GitHub Advisory and proposed by a recent work, VulLibMiner.
It also includes the TF-IDF and BERT's retrieval results in this dataset.

Additionally, it also includes the `maven_corpus.json`, as the descriptions of maven packages.

#### retrieval

Folder `retrieval` includes the retrieval results of the rest three programming languages (the results of Java vulnerabilities are included by VulLib).


#### inputs

Folder `inputs` corresponds to our inputs used for model training and inference.
Due to the space limit, we only list the inputs under the setting: using one package name retrieved by BERT as our RAG result.

Specifically, the input format follows the conversation format of FastChat (`https://github.com/fastify/fastify`).


#### maven-response

Folder `maven-response` includes ChatGPT and GPT4's response on Java vulnerabilities.
Specifically, `{number}_res_{model}.json` corresponds to the results with {number} RAG inputs on {model}.

#### chatgpt/gpt4-output

Folder `chatgpt-output` and `gpt4-output` includes ChatGPT and GPT4's response on vulnerabilities of the rest three programming languages.
Specifically, `raw_{ecosystem}_res.json` and `{ecosystem}_res.json` corresponds to the results without/with RAG under {ecosystem}.