#Escribe un programa que solicite el precio de un producto y determine el precio final
#después de aplicar un descuento del 10% si el precio es mayor a $100.
prod= float (input("ingrese un numero: " ))
if prod >100:
    cs= (prod*0.10)
    print (f'producto con descuento:{cs}')
else:
    print (f'suproducto es {prod}')