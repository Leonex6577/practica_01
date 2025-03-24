nume1 = int(input("1:"))
nume2 = int(input("2:"))

def suma(num1, num2):
    sumat = num1 + num2 
    print(f"La suma es {sumat}")
    
def resta(num1, num2):
    rest = num1 - num2
    print(f"La resta es {rest}")
    
def multiplicacion(num1, num2):
    multipli = num1 * num2
    print(f"La multiplicacion es {multipli}")  
    
def division(num1, num2):
    divit = num1 / num2
    print(f"La division es {divit}")
    
if __name__ == "__main__":
    suma(nume1, nume2)
    resta(nume1, nume2)
    multiplicacion(nume1, nume2)
    division(nume1, nume2)