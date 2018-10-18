#Autor: David Rodriguez
#Prueba divisiones usando ciclo while

def dividir(dividendo, divisor):
    cociente = 0
    x = dividendo
    if divisor == 0:
        print("Ingrese un valor válido para el divisor")
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente+1
    print(x, "/", divisor, "=", cociente, "sobra", dividendo)

def encontrarMayor(numero):
    mayor = 0
    while numero != -1:
        if (numero > mayor) and (numero > 0):
            mayor = numero
            numero = int(input("ingresa un número(cuando termines ingresa -1):"))
        elif (numero <= mayor) and (numero > 0):
             numero = int(input("ingresa un número(cuando termines ingresa -1):"))
        elif numero == 0:
            numero = int(input("ingresa un número(cuando termines ingresa -1):"))
        elif numero < 0:
            print("Ingresa un valor positivo o -1 para terminar")
            numero = int(input("ingresa un número(cuando termines ingresa -1):"))

    if numero == -1:
        print("No hay cantidad mayor")
    else:
        print("El mayor es: ", mayor)

def main():
    print("Misión 07. Ciclos while")
    print("Autor: David Rodriguez Fragoso")
    print("Matrícula: A01748760")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    while opcion != "Salir":
            if opcion == 1:
                dividendo = int(input("Dame el dividendo: "))
                divisor = int(input("Dame el divisor: "))
                dividir(dividendo, divisor)
                opcion = int(input("Teclea tu opción: "))
            elif opcion == 2:
                numero = int(input("Ingresa un número(cuando termines ingresa -1):"))
                encontrarMayor(numero)
                opcion = int(input("Teclea tu opción: "))
            elif opcion == 3:
                print("Gracias por usar este programa, regresa pronto.")
                opcion = "Salir"
            else:
                print("ERROR, teclea 1, 2, o 3")
                opcion = int(input("Teclea tu opción: "))



main()