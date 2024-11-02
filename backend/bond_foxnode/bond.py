import json

from langchain_ollama import ChatOllama


class Bond:
    def __init__(self, model="llama3.2:1b"):
        self.model = ChatOllama(model=model, temperature=0, format="json")

    def __str__(self):
        return f"Bond({self.model})"

    def ask(self, prompt):
        try:
            response = json.loads(self.model.invoke(prompt.get()).content)
            return response
        except:
            return None