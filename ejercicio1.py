#Compra en oxxo 3 productos, usar float, boolean e int
print("Bienvenido al oxxo, tenemos 4 cajas pero solo funciona UNA")

#P1 unidades P2 peso P3 tarjeta de puntos, calcular total
CostoP1 = float(input("Costo del producto: "))
UnidadesP1 = int(input("Cantidad de weas, joputa:"))

CostoP2 = float(input("Costo del producto: "))
UnidadesP2 = float(input("Peso:"))

Total = CostoP1*UnidadesP1+CostoP2*UnidadesP2

TarjetaPuntos = input("Usa tarjeta de puntos?")

if TarjetaPuntos == "Si":
    Total = Total * .9

print("El total es",(Total))