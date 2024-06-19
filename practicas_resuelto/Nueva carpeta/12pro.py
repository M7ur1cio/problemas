#Calcular el salario neto

salario=float(input("Ingrese el salario bruto:"))

impr=130
ss=195
se=25

imt= impr + ss + se

if salario > 2000:
    sn = imt - salario * 0.20
    
else:
    sn= salario
    
print("Su salario neto es:", sn)

    



    


