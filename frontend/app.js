import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';

// add event listener to the button so we can avoid using btn.onclick directly in the html problems 
const btn = document.getElementById('btn');
btn.addEventListener('click', generateDiagram);

const diagramDiv = document.getElementById('diagram');


async function generateDiagram() {
    const promptInput = document.getElementById('promptInput').value;
    console.log(promptInput);
    try{
        /* JUST DO A normal get without sending any param */
        const response = await fetch('http://localhost:3001/generate_diagram', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify( {prompt: promptInput} ),
        });
        const result = await response.json();
        const diagramMermaid = result.diagram;
        console.log(diagramMermaid);

        diagramDiv.innerHTML = `<pre class="mermaid">${diagramMermaid}</pre>`;
        await mermaid.run();
    }
    catch(err){
        console.log(err);
    }
}