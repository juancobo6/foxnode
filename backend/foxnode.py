from bond_foxnode import Bond, Prompt


def foxnode(idea):
    bond = Bond(model="llama3.2:3b")

    # ----------
    # TITLE
    # ----------
    task = "Find a title for the following text. The title should be a few words."
    format = {
        "title": "***title***"
    }
    prompt = Prompt(idea=idea, format=format, task=task)
    response = None
    while not response:
        response = bond.ask(prompt)
    title = response["title"]

    # ----------
    # MAIN IDEAS
    # ----------
    task = "Identify the main topics discussed in the following text. Use a few words for each topic."
    format = {
        "main_ideas": ["***main_idea1***", "***main_idea2***", "***main_idea3***", "..."]
    }
    prompt = Prompt(idea=idea, format=format, task=task, random_seed=True)
    response = None
    while not response:
        response = bond.ask(prompt)
    main_ideas = response["main_ideas"]

    # --------
    # SUBIDEAS
    # --------
    format = "{"
    for topic in main_ideas:
        format += f'"{topic}": ["***process1***", "***process2***", "***process3***", "..."],'
    format += "}"
    topic_idea = f"Identify the main concepts or processes or that take place in these ideas {main_ideas} in context of {idea}. And explain each in a few words."
    prompt = Prompt(idea=topic_idea, format=format, task=None)
    response = None
    while not response:
        response = bond.ask(prompt)
    processes_main_ideas = response

    # -------
    # MERMAID
    # -------
    mermaid = "graph TD\n"
    subgraph = 1
    total = 0
    for key, value in processes_main_ideas.items():
        mermaid += f'    subgraph subgraph{subgraph}[" "]\n'
        subgraph += 1
        mermaid += f'    direction LR\n'
        nodes = []
        for index in range(len(value)):
            total += 1
            mermaid += f'    {total}["{value[index]}"]\n'
            nodes.append(total)
        mermaid += f'    end\n'
    mermaid += f'    title["{title}"]\n'

    subgraph = 1
    for key in processes_main_ideas.keys():
        mermaid += f'    title -->|{key}| subgraph{subgraph}\n'
        subgraph += 1

    return mermaid

if __name__ == "__main__":
    idea = """Biology is the scientific study of living organisms and their interactions 
    with each other and their environment. It encompasses a wide range of topics, including 
    genetics, evolution, ecology, and physiology, among others. Through the application of 
    scientific principles and methods, biologists investigate the structure, function, growth, 
    development, reproduction, and survival of all living things, from bacteria to humans. 
    The field of biology seeks to understand the complex relationships between organisms and 
    their environment, and to develop new technologies and treatments for human health and 
    environmental conservation."""

    t = foxnode(idea)
