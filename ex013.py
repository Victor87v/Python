# Reajuste Salarial
sal = float(input('Digite seu salário: R$'))
novo = sal + (sal * 15/100)
print('Seu salário de R${: .2f}, com o aumento de 15%, passou a ser R${: .2f}.'.format(sal,novo))