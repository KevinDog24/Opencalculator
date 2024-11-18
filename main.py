from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir
from suma_avanzada import suma_multiple

def menu():
    while True:
        print("\n=== Calculadora ===")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Sumar varios números")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '6':
            break
            
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == '4':
                if num2 != 0:
                    print(f"Resultado: {dividir(num1, num2)}")
                else:
                    print("Error: No se puede dividir entre 0")
        
        elif opcion == '5':
            numeros = []
            while True:
                num = input("Ingresa un número (o 'fin' para terminar): ")
                if num.lower() == 'fin':
                    break
                numeros.append(float(num))
            print(f"Resultado: {suma_multiple(numeros)}")

if __name__ == "__main__":
    menu()