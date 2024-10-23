from bond import Bond, Prompt


def create_format():
    b = Bond()
    p = Prompt(
        idea="I am building a tool to create diagrams. I need a standard JSON structure to define the diagrams. Define a JSON structure to represent diagrams, this structure should have labels for where the information on the actual diagram is supposed to be.",
        format=None,
        task=None,
        indications="Respond using JSON only.",
        random_seed=True
    )

    response = b.ask(p)

    return response


if __name__ == "__main__":
    v1 = create_format()
    v2 = create_format()
    v3 = create_format()

    print(0)