import secrets

class Prompt:
    def __init__(
            self,
            idea,
            format,
            task="Extract a the main points of the following idea.",
            indications="Use the provided template for your answer, write the answers in the ***labels*** marked as such. Respond using JSON only.",
            random_seed=False,
    ):
        self.idea = idea
        self.task = task
        self.format = format
        self.indications = indications
        if random_seed:
            self.random_seed = secrets.token_urlsafe(10)
        else:
            self.random_seed = None

    def __str__(self):
        return f"{self.random_seed}\n{self.task}\n{self.idea}\n{self.format}\n{self.indications}"

    def get(self):
        return str(self)


