#  Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

#calcular a soma de números pares
#soma de números pares em um intervalo

# Solicita os limites do intervalo
inicio = int(input("Digite um número inicial do intervalo: "))
fim = int(input("Digite um número final do intervalo: "))

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