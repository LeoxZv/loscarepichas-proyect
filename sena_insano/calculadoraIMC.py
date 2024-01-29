#Escribe un programa que calcule el IMC de una persona (IMC = peso / ALTURA^2) LUEGO INDIQUE SI LA PERSONA ESTA SOBREPESO O BAJO DE PESO
Peso = float(input("Digita tu peso:"))
altura = float(input("Digita tu altura:"))

Calcular = Peso / (altura*altura)
print("Tu IMC es de:",Calcular)