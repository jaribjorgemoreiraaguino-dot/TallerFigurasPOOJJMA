class Color:
    def __init__(self, color):
        if not isinstance(color, str):
            raise TypeError("El color debe ser texto.")
        if color.strip() == "":
            raise ValueError("El color no puede estar vacío.")
        self._color = color.strip()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        if not isinstance(nuevo_color, str):
            raise TypeError("El color debe ser texto.")
        if nuevo_color.strip() == "":
            raise ValueError("El color no puede estar vacío.")
        self._color = nuevo_color.strip()

    def __str__(self):
        return f"Color: {self.color}"
