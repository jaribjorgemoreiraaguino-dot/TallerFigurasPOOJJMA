import math

class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = None
        self._ancho = None
        self.alto = alto
        self.ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que cero.")
        self._alto = valor

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que cero.")
        self._ancho = valor

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        raise NotImplementedError("Este método debe implementarse en las clases hijas.")
