# Calculando desconto
preço = float(input('Digite o preço do produto: R$'))
novo = preço - (preço * 5/100)
print('O produto de R${: .2f} com o desconto de 5% sai por R${: .2f}'.format(preço,novo))