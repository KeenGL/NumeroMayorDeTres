'''
Determina el mayor de 3 numeros ingresados por el teclado
'''
class ordenadoTresNumeros:
    def __init__(self,numero1,numero2,numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def intercambio_valores(self,numero1,numero2):
        temporal = numero1
        numero1 = numero2
        numero2 = temporal
        return numero1,numero2
    def ingresar_numeros(self):

        self.numero1=int(input("\nIngresa el primer numero: "))
        self.numero2=int(input("Ingresa el segundo numero: "))
        self.numero3=int(input("Ingresa el tercer numero: "))

    def ordenar_numeros(self):
        if self.numero1>self.numero2:
            self.numero1,self.numero2=self.intercambio_valores(self.numero1,self.numero2)


        if self.numero2>self.numero3:
            self.numero2,self.numero3=self.intercambio_valores(self.numero2,self.numero3)

        if self.numero1>self.numero2:
            self.numero1,self.numero2=self.intercambio_valores(self.numero1,self.numero2)

    def imprimir_numeros(self):
        print(f" {self.numero1},{self.numero2},{self.numero3}")

if __name__=="__main__":
    numero1 =5
    numero2=10
    numero3=1
    numeros = ordenadoTresNumeros(numero1,numero2,numero3)

    print("\nNumeros desordenados")
    numeros.imprimir_numeros()

    print("\nNumeros ordenados")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros()

    numeros.ingresar_numeros()
    print("\nNumeros desordenados")
    numeros.imprimir_numeros()

    print("\nNumeros ordenados__")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros()


