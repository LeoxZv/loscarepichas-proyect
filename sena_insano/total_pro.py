nombre_p = str(input("INGRESE NOMBRE DEL PRODUCTO:"))
Precio = float(input("INGRESE PRECIO DEL PRODUCTO:"))
Cantidad = int(input("Ingrese cantidad de productos:"))

valor_total = Cantidad*Precio
porcentaje = valor_total * 0.1
desc = valor_total - porcentaje
print("Por la compra de",nombre_p,"El total es:",desc)