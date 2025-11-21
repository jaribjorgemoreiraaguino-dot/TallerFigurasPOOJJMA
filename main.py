from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia

def sumar_areas(lista):
    total = 0
    for figura in lista:
        total += figura.area()
    return total

def sumar_perimetros(lista):
    total = 0
    for figura in lista:
        total += figura.perimetro()
    return total

if __name__ == "__main__":
    print("Creando figuras...\n")

    figuras = []

    c1 = Cuadrado(5, "Rojo")
    c2 = Cuadrado(8, "Azul")
    r1 = Rectangulo(4, 10, "Verde")
    r2 = Rectangulo(3, 6, "Negro")
    cir = Circunferencia(5, "Amarillo")

    figuras.extend([c1, c2, r1, r2, cir])

    for f in figuras:
        print(f)

    print("\nSumas generales:")
    print("Área total:", sumar_areas(figuras))
    print("Perímetro total:", sumar_perimetros(figuras))

    print("\nPrueba de errores:")
    try:
        c1.ancho = -9
    except Exception as e:
        print("Error capturado correctamente:", e)
