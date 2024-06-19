altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 and  24.9:
    clasificacion = "Normal"
elif 25 and 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"



print(f"Su IMC es:{imc:},lo que indica que tiene {clasificacion}.")
