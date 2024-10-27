from bond import Bond, Prompt


def get_ideas(idea, bond):
    p = Prompt(
        idea=idea,
        format="""
            {
                "main_ideas": ["***main_idea1***", "***main_idea2***", "***main_idea3***", ...],
            }
            """,
        task="Extract the main ideas of the following text.",
        random_seed=True
    )
    response = None
    while not response:
        response = bond.ask(p)

    return response["main_ideas"]

def get_nodes(ideas, bond):
    p = Prompt(
        idea=ideas,
        format="""
            {
                "summarized_ideas": ["***main_idea1***", "***main_idea2***", "***main_idea3***", ...],
            }
        """,
        task="Summarize the following ideas. Use a single sentence for each idea.",
    )
    response = None
    while not response:
        response = bond.ask(p)

    return response["summarized_ideas"]

def get_mermaid(ideas):
    diagram_mermaid = "graph LR\n"
    for i in range(len(ideas) - 1):
        diagram_mermaid += f'    {i+1}["{ideas[i]}"] --> {i+2}["{ideas[i+1]}"]\n'

    return diagram_mermaid

def foxnode(idea):
    bond = Bond()

    ideas = get_ideas(idea, bond)

    nodes = get_nodes(ideas, bond)

    mermaid = get_mermaid(nodes)

    return mermaid

if __name__ == "__main__":
    bond = Bond()
    idea = "Biology is the scientific study of living organisms and their interactions with each other and their environment. It encompasses a wide range of topics, including genetics, evolution, ecology, and physiology, among others. Through the application of scientific principles and methods, biologists investigate the structure, function, growth, development, reproduction, and survival of all living things, from bacteria to humans. The field of biology seeks to understand the complex relationships between organisms and their environment, and to develop new technologies and treatments for human health and environmental conservation."

    diagram = foxnode(idea)

    with open("diagram.md", "w") as f:
        f.write(diagram)



