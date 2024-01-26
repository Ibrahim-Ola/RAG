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

