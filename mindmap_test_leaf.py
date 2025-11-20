from mindmap_leaf import (MindMapLeaf)
from mindmap_composite import MindMapComposite

if __name__ == "__main__":
    mindmap = MindMapComposite("mindmap", "circle")

    tools = MindMapComposite("tools", "bang")
    tools.add(MindMapLeaf("Pen and paper", "rectangle"))
    tools.add(MindMapLeaf("mermaid", "rectangle"))

    mindmap.add(tools)

    origins = MindMapComposite("Origins", "square")
    origins.add(MindMapLeaf("Long History", "rectangle"))
    popularisation = MindMapComposite("popularisation", "rectangle")
    popularisation.add(MindMapLeaf("British popular psycology author Tony Buzan", "rectangle"))

    origins.add(popularisation)
    mindmap.add(origins)


    mindmap.display()