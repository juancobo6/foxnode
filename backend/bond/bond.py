import json

from langchain_ollama import ChatOllama

from prompt import Prompt

class Bond:
    def __init__(self, model="llama3.2:1b", config=None, structured=False):
        self.model = ChatOllama(model=model, temperature=0, format="json")

    def __str__(self):
        return f"Bond({self.model})"

    def ask(self, prompt):
        return json.loads(self.model.invoke(prompt.get()).content)



