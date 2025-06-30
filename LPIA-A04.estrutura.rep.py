#calcular a soma de números pares
#soma de números pares em um intervalo
#pedir 2 números inteiros

# Solicita os limites do intervalo
inicio = int(input("Digite um número inicial: "))
fim = int(input("Digite um número final: "))

soma = 0
tem_par = False

# Loop para iterar pelos números do intervalo, inclusive
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma += numero
        tem_par = True

# Verificação com o bloco else
if tem_par:
    print(f"A soma dos números pares entre {inicio} e {fim} é: {soma}")
else:
    print("Não há números pares nesse intervalo.")