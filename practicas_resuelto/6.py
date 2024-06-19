#Escribe un programa que solicite la edad del usuario y clasifique la edad en una de las
#siguientes categorías: "Infantil" (0-12), "Adolescente" (13-19), "Adulto" (20-59) y "Adulto
#mayor" (60 o más)
eda=int(input( ingresa tu edad ))
if eda >= 0 and eda <= 12:
    print ('Infantil')
    if eda >=13 and eda <= 19:
        print ('Adolescente')
        if eda >= 20 and eda <= 59:
            print ('Adulto')
else:
    print ('adulto mayor')
        
    