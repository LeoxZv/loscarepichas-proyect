producto = str(input("Ingrese su producto:"))
precio = int(input("Ingrese el valor del producto:"))
descuento = int(input("Ingrese el descuento:"))

descuento = descuento/100

total_final = float(precio * descuento)
print("su total es:",total_final)