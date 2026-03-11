import os
os.system(" cls || clear")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota"))

media = (nota1 + nota2)
print(f"A media aritmética é: {media:.2f}")

if media >= 6.0:
  print("Aluno esta aprovado")
elif media > 4.0:
    print("Aluno esta reprovado. ")
