def resta(value1,value2):
    x = value1 - value2
    print(x)

def suma(value1,value2):
    x = value1 + value2
    print(x)

def elevar_a_la_potencia(value1,value2):
    x = value1 ** value2
    print(x)

def aumentar_valor(value1):
    value1 += 1
    print(value1)

def disminuir_valor(value1):
    value1 -= 1
    print(value1)

def division_cencera(value1,value2):
    x = value1 % value2
    print(x)

def division(value1,value2):
    x = value1 / value2
    print(x)

def nombre(nombre):
    print("El nombre del ejecutardor es {}".format(nombre))

def edad(edad):
    if edad <= 18:
        edad = "Es mayor de edad"
    else:
        edad = "Es menor de edad"
    print(edad)

def Nota_Alumna(nota):
    if nota == 5:
        print("Suspes")
    if nota >= 5 and nota <= 6:
        print("Bé")
    if nota >= 6 and nota <= 8:
        print("Notable")
    if nota > 8:
        print("Excel.lent")

if __name__ == '__main__':
    usr_input = int(input("""Bienvenido a continuacion tienes todos los parámetros disponibles:
[0] Si quieres hacer una resta. 
[1] Si quieres hacer una suma.
[2] Si quieres elevar a la potencia.
[3] Si quieres aumentar el valor.
[4] Si quieres disminuir el valor.
[5] Si quieres dividir el valor.
[6] Si quieres introducir un nombre del ejecutador.
[7] Si quieres introducir una edad para saber si es mayor o menor de 18 años.
[8] Si quieres calculcar la nota de un alumno.
    
Introduce una opcion : """))

    if usr_input == 0:
        x = float(input("Introduce el primer valor : "))
        y = float(input("Introduce el segundo valor : "))
        resta(x,y)
    if usr_input == 1:
        x = float(input("Introduce el primer valor : "))
        y = float(input("Introduce el segundo valor : "))
        suma(x,y)
    if usr_input == 2:
        x = float(input("Introduce el primer valor : "))
        y = float(input("Introduce el segundo valor : "))
        elevar_a_la_potencia(x,y)
    if usr_input == 3:
        x = float(input("Introduce el valor a aumentar : "))
        aumentar_valor(x)
    if usr_input == 4:
        x = float(input("Introduce el valor a disminuir : "))
        disminuir_valor(x)
    if usr_input == 5:
        x = float(input("Introduce el primer valor : "))
        y = float(input("Introduce el segundo valor : "))
        division(x,y)
    if usr_input == 6:
        x = str(input("Introduce tu nombre : "))
        nombre(x)
    if usr_input == 7:
        x = int(input("Introduce tu edad : "))
        edad(x)
    if usr_input == 8:
        x = float(input("Introduce la nota del alumn@ : "))
        Nota_Alumna(x)

#En cuanto al digarama hecho en classe no es possible hacerlo debido que no cuento con un servidor SQL para poder hostearlo

