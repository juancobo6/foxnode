from bond import Bond
from bond import Prompt


def dict_to_mermaid(diagram_dict):
    # Start of the mermaid flowchart syntax
    mermaid_syntax = '''```mermaid
flowchart TD\n'''

    # Add nodes
    nodes = diagram_dict['nodes']
    for node in nodes:
        mermaid_syntax += f"    {node['id']}[{node['label']}]\n"

    # Add edges
    edges = diagram_dict['edges']
    for edge in edges:
        mermaid_syntax += f"    {edge['source']} --> {edge['target']}[{edge['label']}]\n"

    # End of the mermaid code block
    mermaid_syntax += '```'

    return mermaid_syntax

if __name__ == "__main__":
    diagram_dict = {
        "nodes": [
            {"id": 1, "label": "***node1***"},
            {"id": 2, "label": "***node2***"},
            {"id": 3, "label": "***node3***"},
            {"id": 4, "label": "***node4***"},
            {"id": 5, "label": "***node5***"},
            {"id": 6, "label": "***node6***"},
        ],
        "edges": [
            {"source": 1, "target": 2, "label": "***edge1***"},
            {"source": 2, "target": 3, "label": "***edge2***"},
            {"source": 3, "target": 4, "label": "***edge3***"},
            {"source": 4, "target": 5, "label": "***edge4***"},
            {"source": 5, "target": 6, "label": "***edge5***"},
        ],
    }

    prompt = Prompt(
        idea="The Lean Startup process is a methodology designed to help entrepreneurs build and scale their businesses more efficiently by focusing on rapid experimentation, customer feedback, and continuous learning. It starts with the creation of a minimum viable product (MVP), which is a simplified version of the product or service that solves the core problem for early adopters. Entrepreneurs then use the MVP to gather data and insights directly from real users. Through this feedback, they can quickly test assumptions, learn what works or doesn't, and make informed decisions. This process is iterative, involving cycles of building, measuring, and learning. If the initial idea doesn't meet customer needs, entrepreneurs can pivot by adjusting their business model, product features, or target audience, or they can persevere if the feedback is positive. The aim is to minimize waste by avoiding the traditional approach of investing heavily in fully developing a product before testing it in the market, allowing startups to reduce risks and respond flexibly to changing conditions. This methodology helps businesses optimize product-market fit and scale efficiently, making it adaptable to various industries and situations.",
        task="Extract the main points of the following idea to make a diagram.",
        format=diagram_dict,
    )

    bond = Bond()

    response = bond.ask(prompt)

    print(response)