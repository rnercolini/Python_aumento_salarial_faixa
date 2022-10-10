# Calcula o aumento salarial conforme faixa de salário.
salario = float(input('Digite o valor do salário atual: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O novo valor do salário será de R${:.2f}'.format(novo))
