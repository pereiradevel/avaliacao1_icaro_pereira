ni = int(input("Digite um número inteiro: "))
operacao = (ni / 5)
if operacao % 1:
    print(f"{ni} não é multiplo de 5.")
else:
    print(f"{ni} é múltiplo de 5.")
if ni > 0:
    print("Número positivo.")
else:
    print("Número negativo.")
if ni == '0':
    print("Número zero.")
#FIM