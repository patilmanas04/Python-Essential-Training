from abc import ABC, abstractmethod

class GraphicalFigure(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def calcArea():
        pass

class Circle(GraphicalFigure):
    def __init__(self, radius):
        self.radius = radius 

    def calcArea(self):
        return 3.14 * (self.radius**2)

class Square(GraphicalFigure):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side**2

# graphicalFiguere = GraphicalFigure()
square = Square(5)
circle = Circle(3.6)
print(square.calcArea())
print(circle.calcArea())