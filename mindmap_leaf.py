class MindMapLeaf:

    def __init__(self, name:str, shape:str):
        self.name = name
        self.shape = shape

    @staticmethod
    def get_shape_representation(shape:str):
        shape_d = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}((",
            "rectangle": "{}",
        }
        return shape_d.get(shape, "{}")


    def display(self, indent=0):
        print(" " * indent + str(self))

    def __str__(self):
        shape_representation = (self.get_shape_representation(self.shape))
        return shape_representation.format(self.name)

if __name__ == "__main__":
    mml = MindMapLeaf("Research", "cloud")

    mml.display(4)

    def get_shape(self):
        return self.shape
