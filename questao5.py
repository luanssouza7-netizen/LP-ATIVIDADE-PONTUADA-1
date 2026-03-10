import os
os.system

valor1 = int(input("Digite um numero : "))
operador =str(input("Escolha uma forma de operaçâo :(+,-,*,/)_ :"))
valor2 = int(input("Digite um numero :"))

match operador:
    case "+":
        resultado = valor1 + valor2
print(resultado)
case 
resutado = valor1 - valor2
print(resutado)
case 
resultado =  valor1 * valor2
print(resultado)
case 
resultado = valor1 / valor2
print(resultado)
case
resultado = "operador invalido"
print(f"resultado{resultado}")

    