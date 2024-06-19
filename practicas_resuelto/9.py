#Escribe un programa que solicite un carácter al usuario y determine si es una letra (a-z,
#A-Z) o un dígito (0-9).
pal= input("ingrese una letra o numero: ")
if pal.isalpha():
    print('pertenece a-z')
elif pal.isdigit():
    print ('pertenece 0-9')

else:
    print ('pertenece A-Z')
    