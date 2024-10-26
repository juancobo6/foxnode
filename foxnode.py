import re

from bond import Bond, Prompt


def get_nodes(idea, bond):
    p = Prompt(
        idea=idea,
        format="""
            {
                "number_nodes": "***int***",
            }
            """,
        task="You are going to make a diagram of the given idea. First define how many nodes you will need.",
        random_seed=True
    )
    response = bond.ask(p)

    response = response['number_nodes']

    return response


def get_json(idea, nn, bond):
    p = Prompt(
        idea=idea,
        format={
            "nodes": [{"id": i, "label": f"***node{i}***"} for i in range(1, nn + 1)],
            "edges": [{"source": i, "target": i + 1, "label": f"***edge{i}***"} for i in range(1, nn)]
        }
    )
    response = bond.ask(p)

    return response


def get_mermaid(diagram_json):
    try:
        diagram_mermaid = "graph TD\n"

        nodes = {node['id']: node['label'] for node in diagram_json['nodes']}

        for edge in diagram_json['edges']:
            source = edge['source']
            target = edge['target']
            label = edge['label']
            if re.match(r"\*\*\*edge\d\*\*\*", label):
                diagram_mermaid += f'    {source}["{nodes[source]}"] --> {target}["{nodes[target]}"]\n'
            else:
                diagram_mermaid += f'    {source}["{nodes[source]}"] --> |"{label}"| {target}["{nodes[target]}"]\n'

        return f"""
```mermaid
{diagram_mermaid}
```
            """
    except:
        print("Error in generating diagram.")
        print(diagram_json)
        return "There was an error in generating the diagram."




def foxnode(idea):
    b = Bond()

    nn = get_nodes(idea, b)

    diagram_json = get_json(idea, nn, b)

    mermaid_diagram = get_mermaid(diagram_json)

    return mermaid_diagram


if __name__ == "__main__":
    SAMPLE = "The Lean Startup process is a methodology designed to help entrepreneurs build and scale their businesses more efficiently by focusing on rapid experimentation, customer feedback, and continuous learning. It starts with the creation of a minimum viable product (MVP), which is a simplified version of the product or service that solves the core problem for early adopters. Entrepreneurs then use the MVP to gather data and insights directly from real users. Through this feedback, they can quickly test assumptions, learn what works or doesn't, and make informed decisions. This process is iterative, involving cycles of building, measuring, and learning. If the initial idea doesn't meet customer needs, entrepreneurs can pivot by adjusting their business model, product features, or target audience, or they can persevere if the feedback is positive. The aim is to minimize waste by avoiding the traditional approach of investing heavily in fully developing a product before testing it in the market, allowing startups to reduce risks and respond flexibly to changing conditions. This methodology helps businesses optimize product-market fit and scale efficiently, making it adaptable to various industries and situations."
    d = foxnode(SAMPLE)

    print(d)