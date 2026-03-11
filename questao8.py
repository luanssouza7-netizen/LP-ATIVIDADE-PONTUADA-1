import os
os.system(" cls || clear")

tabela_precos = { 
"verde": 10.00,
"azul": 20.00,
"amarelo" : 30.00,
"vermelho" : 40.00,
}
cor_digitada = input("Digite a cor do CD (Verde, Azul, AMarelo ou Vermelho): ").lower()

if cor_digitada in tabela_precos:
    preco = tabela_precos[cor_digitada]
    
    print(f"O preço do CD {cor_digitada} é de R$ {preco:.2f}")
    
else:
    print("Cor inválida. Por favor , digite uma das cores listradas")