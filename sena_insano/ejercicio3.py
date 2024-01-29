#inserta el valor del cilindro por teclado area, altura
pi= 3.1416
radio = float(input("Ingrese el valor del volumen:"))
altura = float(input("Ingrese el valor de la altura:"))

area = 2*pi * radio * altura
print("El valor del area es:",area)

volumen = pi * (radio**0.5) * altura
print("El volumen es de:",volumen)