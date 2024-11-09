# Graph Python

## Prerequisites

You'll need to install networkx and matplotlib if you haven't already. You can install them with:

```
pip install networkx matplotlib
```

## Running the Code

Save your JSON data in a file (e.g., graph.json), place it in the same directory as the script, and run the script. It will display a graph with nodes and edges as described in your JSON.

```
python graph.py
```

# Graph JavaScript

This project visualizes graph data from a JSON file (`graph.json`) using D3.js. You can run the project in any workspace that supports HTML, JavaScript, and JSON files.

## Files

- **graph.json**: The JSON file containing graph data in the format of nodes and links.
- **graph.html**: The HTML file containing JavaScript to visualize the graph.

## Requirements

- **Web browser**: Any modern browser that can run JavaScript and supports SVG.
- **D3.js**: Included via CDN in `graph.html`, so no additional installation is needed.

## JSON Format

The `graph.json` file should have a structure like this:

```json
{
    "nodes": [
        { "id": "A" },
        { "id": "B" },
        { "id": "C" },
        { "id": "D" }
    ],
    "links": [
        { "source": "A", "target": "B" },
        { "source": "A", "target": "C" },
        { "source": "B", "target": "D" },
        { "source": "C", "target": "D" }
    ]
}
```

### Fields

- **nodes**: List of nodes, each with an `id` field representing the node's label.
- **links**: List of edges, with each entry having a `source` and a `target` field that references nodes by their IDs.

## How to Run in an Online Workspace

### Steps

1. **Open the Workspace**: Start a new workspace in your chosen IDE (e.g., CodeSandbox or GitHub Codespaces).
2. **Add Files**:
   - Create a new file called `graph.html` and copy the HTML/JavaScript code into it.
   - Create a new file called `graph.json` and add the JSON structure provided above.
3. **Run the Project**:
   - In CodeSandbox, just open `graph.html` in the preview panel.
   - In GitHub Codespaces or other setups, right-click `graph.html` and select an option like “Open with Live Server” if available. If not, you can preview it by opening `graph.html` directly in a web browser.
4. **View the Graph**: The workspace should display a visualization of the graph data, showing nodes and links.

### Modifying the Data

- You can edit `graph.json` to change the structure of the graph.
- Refresh the `graph.html` preview to see updated visualizations after modifying `graph.json`.

## License

This project is licensed under the MIT License. Feel free to modify and use it as you see fit!
