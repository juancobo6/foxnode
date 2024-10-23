def main():
    diagram_mermaid = """  
        ```mermaid
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
    ```
    """
    return diagram_mermaid

if __name__ == "__main__":
    print(main())