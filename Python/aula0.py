#isso é um comentário
#variável - uma caixinha para guardar uma informação
#regras para criação de variáveis
#o nome da variável é aquilo que ela vai guardar
#o python é case sensitive,ou seja, letras maiusculas são diferentes de letras minusculas

# nome =
# Nome =

# nome_de_usuario =
# nomedeusuario =
# nomeDeUsuario =

#tipos de informação:
#texto - string - tudo o que está entre aspas é considerado um texto
nome = "Nath"
# numero inteiro - positivos e negativos 
idade = 23
#numero "quebrado" - float - precisa digitar com ponto, e não com virgula
altura = 1.75
#valores booleanos - True (sim) e False (não)
eh_habilitada = False


#operadores de comparação
# print("Nath")
# print(5==6)
# print(7>4)
# print(4<100)
# print(10!=5)
# print(5>=5)
# print(9<=12)

#como pedir uma informação ao usuário:
#input() - dentro dos parenteses do input, entre aspas colocamos a frase que o usuário vai ver
# nome = input("Digite o seu nome: ")
# print(nome)

# idade = int(input("Digite a sua idade: "))
# print(idade)

# altura = float(input("Digite a sua altura: "))
# print(altura)

#peça dois numeros inteiros ao usuario e mostre o resultado da soma na tela

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos números é:", soma)

altura1 = float(input("Digite sua primeira altura: "))
altura2 = float(input("Digite sua segunda altura: "))
soma_alturas = altura1 + altura2
print("A soma das alturas é:", soma_alturas)

frutaA = str(input("Digite o nome da primeira fruta: "))
frutaB = str(input("Digite o nome da segunda fruta: "))
print("As frutas digitadas foram:", frutaA, "e", frutaB)

#subtração
numero_da_sorte1 = int (input ("Qual o seu primeiro número da sorte?"))
numero_da_sorte2 = int (input ("Qual é o seu segundo número da sorte?"))
subtração = numero_da_sorte1 - numero_da_sorte2
print ("A diferença dos numeros é:" , subtração)

idade = int(input ("Qual a sua idade?:"))
print (idade, "anos")

name = str (input ("What is your name:"))
age = int (input ("How old are you?"))

if age >= 18:
    print ("You can drive!")
else:
    print ("Sorry! You cant drive!")

#multiplicação
numberX = int (input ("Give me any number:"))
numberY = int (input("Give me another number:"))
multiplication = numberX * numberY
print ("When you multiply both numbers youll get:", multiplication)

#divide
numberA = int(input ())