from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 4 * self.ancho

    def __str__(self):
        return f"Cuadrado | lado: {self.ancho} | {Color.__str__(self)} | área: {self.area()} | perímetro: {self.perimetro()}"
