"""
Created on Tue Jan 26 2024

This script contains functions for add memory to retrieval.

Author: Ibrahim Alabi
Email: ibrahimolalekana@u.boisestate.edu
Institution: Boise State University
"""

import sys

from rag101 import NaiveRAG
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory




class ChatBot(NaiveRAG):

    def __init__(self, model=None, tokenizer=None, conversation_chain=None, model_template=None, safety_mode: bool = True):
        super().__init__(model, tokenizer)

        self.safety_mode = safety_mode
        if model_template is None:
            self.model_template = self.text_with_context_to_mixtral_template(instruction="{input}", history="{history}", safety_mode=self.safety_mode)
        else:
            self.model_template = model_template
        
        if conversation_chain is None:
            self.conversation_chain = self.create_conversation()
        else:
            self.conversation_chain = conversation_chain

    def text_with_context_to_mixtral_template(self, instruction: str, history: str, safety_mode: bool = True) -> str:

        history_instruction = f"The following is a conversation between a human and an AI assistant."

        if safety_mode:
            safety_prompt = (
                "The AI assistant always assist with care, respect, and truth. The AI assistant respond with utmost utility yet securely. "
                "The AI assistant avoids harmful, unethical, prejudiced, or negative content and ensures replies promote fairness and positivity."
            )

            instruction = f"{history_instruction} {safety_prompt}\n\nCurrent conversation: {history}\n\nHuman: {instruction}"

        else:
            instruction = f"{history_instruction}\n\nCurrent conversation: {history} \n\nHuman: {instruction}"
        
        chat = [
            {"role": "user", "content": "Hello, how are you?"},
            {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
            {"role": "user", "content": instruction}
        ]

        return self.tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=False)
    
    def create_conversation(self) -> str:

        memory = ConversationBufferMemory(memory_key="history") # let's define the memory

        # let's define the prompt using LangChain's PromptTemplate
        prompt_template = PromptTemplate.from_template(self.model_template)

        # let's link componenet with LLMChain
        conversation = LLMChain(
            llm=self.model,
            prompt=prompt_template,
            verbose=False,
            memory=memory
        )
        return conversation
    
    def qa(self, question: str) -> str:

        response = self.conversation_chain({"input": question})
        return response['text'].strip()
    

if __name__ == "__main__":
    

    bot=ChatBot()

    query = None

    if len(sys.argv) > 1:
        query = sys.argv[1]

    print(">> Bot: How can I help you today?")

    while True:
        if query is None:
            query = input(">> User: ")

            if query in ["exit", "quit", "q", "q()"]:
                print(">> Bot: Goodbye!")
                sys.exit(0)
        response = bot.qa(question=query)
        print(response)
        query = None