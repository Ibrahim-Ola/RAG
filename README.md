# Retrieval Augmented Generation (RAG)

## Overview

This repository contains an introduction to Retrieval Augmented Generation (RAG) using the [LangChain](https://python.langchain.com/docs/get_started/introduction) framework. For this project, I will use the Mixtral8x7b open source Large Language Model (LLM) and see how to  "augment" its knowledge using user-specific (private) data. This project is divided into three parts:

1. RAG101: This is a beginner's level introduction to RAG with LangChain. You will learn how to:
    * Load open source models using the Huggingface API in Langchain.
    * Prompt your loaded models.
    * Augment the LLM's knowledge with private data in a "naive way".
    * Go to [RAG101](https://github.com/Ibrahim-Ola/RAG/blob/main/RAG101/RAG101.ipynb).  

2. RAG102: This part introduces the key componenet of a conversation - memory. You will learn:
    * The different kinds of memory algorithm  supported by LangChain.
    * Add memory to retrievals in LangChain to enable conversation.
    * Go to [RAG102](https://github.com/Ibrahim-Ola/RAG/blob/main/RAG102/RAG102.ipynb).



## Usage

### 1. Setup the environment

```{bash}
mkdir RAG
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

### 2. Clone the Repository

```{bash}
git clone https://github.com/Ibrahim-Ola/RAG.git
cd RAG
```

### 3. Install Source Code in Editable Mode 

```{bash}
pip install -e .
```

### 4. Deactivate Environment

After running the experiments, you can deactivate the virtual environment by running the command below.

```{bash}
deactivate
```