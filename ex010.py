# Conversor de Moedas
valor = float(input('Quanto reais você tem na carteira? R$'))
dolar = valor/5.09
print('Com RS{} você pode comprar US${: .2f}'.format(valor, dolar))