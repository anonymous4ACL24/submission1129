## This is our code used for VulLibGen

#### FastChat

Folder `FastChat` corresponds to our framework for LLM fine-tuning and inference.
It comes from a open-source repository `https://github.com/fastify/fastify`, and we just reuse its training scripts under `FastChat/scripts`.

#### scripts
Here includes our scripts for local search and input generation.

Specifically, `post.py` corresponds to our local search scripts for Java, and `post_{ecosystem}` corresponds to our local search scripts for the rest three programming languages.

`maven_scanner.ipynb` corresponds to the scan results of package names in Maven.

#### Checkpoints and LLMs

Due to the space limit, we do not include the raw models of four used LLMs and their checkpoints.
With the fine-tuning and inference scripts and datasets, the results of VulLibGen can be easily reproduced.

#### Baselines
Our baselines can be found in the following repo:
FastXML, LightXML: https://github.com/soarsmu/ICPC_2022_Automated-Identification-of-Libraries-from-Vulnerability-Data-Can-We-Do-Better
Chronos: https://github.com/soarsmu/Chronos
VulLibMiner: https://github.com/q5438722/VulLibMiner