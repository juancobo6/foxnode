import time

from bond_foxnode import Bond, Prompt
from foxnode import foxnode


disciplines = [
    "Physics",
    "Chemistry",
    "Biology",
    "Astronomy",
    "Geology",
    "Environmental Science",
    "Oceanography",
    "Meteorology",
    "Ecology",
    "Genetics",
    "Botany",
    "Zoology",
    "Microbiology",
    "Biochemistry",
    "Molecular Biology",
    "Neuroscience",
    "Materials Science",
    "Paleontology",
    "Anthropology",
    "Sociology",
    "Psychology",
    "Computer Science",
    "Mathematics",
    "Statistics",
    "Engineering",
    "Geophysics",
    "Astrophysics",
    "Biophysics",
    "Pharmacology",
    "Toxicology"
]

if __name__ == "__main__":
    for discipline in disciplines:
        print(discipline)

        idea = f"Redact a brief description of the field of {discipline}. Do not use more than 200 words. Do not use bullet points, make the text a single paragraph."

        b = Bond()
        p = Prompt(
            idea=idea,
            format={
                "description": "***description***"
            }
        )
        response = None
        while not response:
            response = b.ask(p)

        idea = response['description']

        start = time.time()

        print(f"Start")
        diagram = foxnode(idea)
        print(f"End: {time.time() - start}")

        with open(f"sample_diagrams/{discipline}.md", "w") as f:
            f.write(f"""
# {discipline}
{idea}

{diagram}
            """)

    print(0)
