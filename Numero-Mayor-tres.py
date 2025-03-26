""" Determina el mayor de tres numeros ingresador por el teclado"""

def intercambiar_valores(numero1,numero2):
    temporal = numero1
    numero1 = numero2
    numero2 = temporal
    return numero1, numero2

numero1=float(input("Ingresa el primer numero: "))
numero2=float(input("Ingresa el segundo numero: "))
numero3=float(input("Ingresa el tercer numero: "))

if numero1>numero2:
    numero1, numero2 = intercambiar_valores(numero1,numero2)

if numero2>numero3:
    numero2, numero3 = intercambiar_valores(numero2, numero3)

if numero1>numero2:
    numero1, numero2 = intercambiar_valores(numero1, numero2)

print(f"numeros ordenados dos: {numero1},{numero2},{numero3}")
print(f"el mayor es: {numero3}")
