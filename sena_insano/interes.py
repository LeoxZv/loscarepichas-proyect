capital = float(input("Ingrese el capital:"))
interes = 0.02
tiempo = int(input("Ingrese el periodo de tiempo:"))

total = capital*(interes)**tiempo
print("El monto final es:",total)
