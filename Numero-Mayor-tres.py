""" Determina el mayor de tres numeros ingresador por el teclado"""


numero1=float(input("Ingresa el primer numero: "))
numero2=float(input("Ingresa el segundo numero: "))
numero3=float(input("Ingresa el tercer numero: "))

if numero1>numero2:
    temporal=numero1
    numero1=numero2
    numero2=temporal

if numero2>numero3:
    temporal=numero2
    numero2=numero3
    numero3=temporal

if numero3>numero1:
    temporal=numero1
    numero1=numero2
    numero2=temporal

print(f"numeros ordenados dos: {numero1},{numero2},{numero3}")
print(f"el mayor es: {numero3}")
