import os

from numpy import quantile
os.system(" cls || clear")

total = quantile * preco_unitario 
 
if quantidade <= 5:
 desconto_percentual= 0.02 # 2%
elif quantidade <= 10:
  desconto_percentual1 = 0.03 # 3%
else:
  desconto_percentual = 0.05 # 5%
  
  valor_desconto = total * desconto_percentual
  
  total_a_pagar = total - valor_desconto 
  
  print(f"Descriçao do produto: {nome_produto}")
  print(f"Qualidade adquirida: {quantidade}")
  print(f"Preço unitário: R${preço_unitario:.2f}")
  print(f"Total (sem desconto): R${total:.2f}")
  print(f"Desconto aplicado ({desconto_percentual * 100}%):")
  print(f"Total a pagr: R$[total_a_pagar:,2f]")