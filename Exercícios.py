#ex0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade=input("insira a sua idade ");
nome=input("insira o seu nome ");
print(f"o meu nome é {nome} e tenho {idade} anos");

#EX0.2: Output
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("ola mundo!");
fruta = input("banana");
print ("eu gosto de {fruta}");
#EX0.3: Input
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""

print("ola mundo!")
nome=input("insira o seu nome:");
print(f"boas ho mitra {nome} desejo te um boa pascoa!");
numero=input("insira um numero inteiro: ");
print(f"o dobro desse numero e {numero*2");

#ex1
""""""Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco"""

input("\nbem vindo ao phyton")

#ex2
""""""Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco"""
nome=input("insira o seu nome: ")
input("José, bem-vindo ao Python!\n")

#ex3
"""Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável."""

mensagem=""".__           .__  .__                         .__            .___
|  |__   ____ |  | |  |   ____   __  _  ______ |  |_______  __| _/
|  |  \_/ __ \|  | |  |  /  _ \  \ \/ \/ /  _ \|  |\_  __ \/ __ | 
|   Y  \  ___/|  |_|  |_(  <_> )  \     (  <_> )  |_|  | \/ /_/ | 
|___|  /\___  >____/____/\____/    \/\_/ \____/|____/__|  \____ | 
     \/     \/                                                 \/ """
print(mensagem)


#ex1.4
"""Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis."""
nome="biru"
idade="15"
localidade="roriz"
print(f"O meu nome é {nome} tenho {idade} anos e moro em {localidade}.")


#EX1.5
"""Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem"""
linguagem = "phyton"
nome = "Biru"
print(f"Estou a aprender {linguagem} e meu nome é {nome}")


#EX1.6
""""Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres."""

print(f"{'Bem-vindo ao Python' : <50}")
print(f"{'Bem-vindo ao Python' : ^50}")
print(f"{'Bem-vindo ao Python' : >50}")



#EX1.7
"""""Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio."""

print("ola mundo!")
raio= float("insere o valor do raio: ")
area= 3.14 *raio**2
print("O perimetro da circunferencia é: ", perimetro)



#EX1.8
""""Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
import datetime
x = datetime.datetime.now()
dia=x.strftime("%D")
mes=x.strftime("%M")
ano=x.strftime("%Y")
hora=x.strftime("%H")
minuto=x.strftime("%M")
segundo=x.strftime("%S")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}:{minuto}:{segundo}")
print(f"{mes}-{dia}-{ano} {hora}:{minuto}:{segundo}")
print(f"{dia}/{mes}/{ano}")
print(f"{hora}:{minuto}:{segundo}")




#EX1.9
"""""Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos."""

print("digite o numero do atleta: ")
numero=input()
print("digite a pontuação final: ")
pontos=input()
print(f"o atleta numero {numero} obteve {pontos} pontos")




#EX1.10
""""Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual."""

import datetime, time
data_de_nascimento="11-03-2000"
dia,mes,ano=map(int,data_de_nascimento.split("-"))
hoje=datetime.date.today()
idade=hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
print(f"A sua idade é {idade}")



#EX1.11
"""Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO)."""

valor_euro=1.20
valor_libra=float(input("insira o valor em libras: "))
valor_euro=valor_libra*valor_euro
print(f"o valor em euros e {valor_euro}")


Desafio A28
print("hello wolrd")
""""escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir e dizer se perdeu ou ganhou"""

import random
numero=int(random.randint(0,5))
#print(f"o numero secreto é: {numero}")
numeroescolhido=int(input("insira o numero escolhido: "))
if numeroescolhido > numero:
  print("o numero inserido é maior do que o meu!")
elif numeroescolhido < numero:
  print("o numero inserido é menor do que o meu!")
else:
 print("acertaste!")


#desafioA29
"""se ultrapassar os 80km/h,é multado no valor de 7 euros para cada km/h acima do limite"""

print("hello world")
velocidade=int(input("insira a velocidade: "))
multa=(velocidade)-80
valor =multa*7
if velocidade <= 80: 
   print("muito bem o senhor andou a velocidade certa nao irá levar multa")            elif velocidade > 80:
print("o malandro foi coimado em: ",multa,"km/h")



""""Exercício FP1: Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero."""

print("hello wolrd")
num=int(input(f"insira um numero: "))
if num == 0:
        print("o teu numero é zero")
elif num > 0:
       print("o teu numero é positivo")
else:
        print("o teu numero é negativo")



"""Exercício FP2: Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar."""

print("hello wolrd")

num=int(input("escreve ai um numero por favor: "))

if num % 2 ==0 :
  print("o numero é par")
else:
  print("o numero é impar")



""" Exercício FP3: Calcular a nota final de um aluno.
  Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:

  Nota inferior a 10: "Reprovado"
  Nota entre 10 e 14: "Suficiente"
  Nota entre 15 e 17: "Bom"
  Nota superior a 17: "Muito Bom"
"""

print("hello world")
nota=int(input("insire a tua nota: "))
if nota<10:
  print("reprovado")
elif nota>10 and nota<14:
  print("suficiente")
elif nota<17 and nota>15:
  print("bom")
elif nota>17 :
  print("muito bom")


""""Exercício FP4: Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15
"""

print("hello world")
temp=float(input("insira a temperatura em graus celcius: "))
F = (temp * 9/5) + 32
K = temp + 273.13
opcao = str(input("qual é a unidade que queres escolher converter? (F) Fahrenheit, (K) Kelvin ou (A) ambas : "))
if  opcao == "F":
  print (f"O valor em Fahrenheit é {F}")
elif opcao == "K":
  print (f"O valor em Kelvin é {K}")
elif opcao=="A":
  print(f"O valor em Fahrenheit é {F} e em Kelvin é {K}")
else:
  print ("Opção inválida")







""""Exercício FP5: Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""

salario=float(input("insira o seu salario: "))
imposto1= salario * 0.10
imposto2= salario * 0.20
percentagem1= salario - imposto1
percentagem2= salario - imposto2
if salario< 1000:
  print("estas sem imposto")
elif salario > 1001 and salario < 2000:
  print(f"o seu salario apos imposto: {percentagem1}")
else:
  print(f"salario apos imposto: {percentagem2}")



""""Exercício FP6: Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10."""
print("hello wolrd")
for i in range(1,11):
  print(i)    



""""Exercício FP7: Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
"""

print("hello wolrd")
soma=0
i=1
while i <= 100:
  soma+=i
  i+=1
print(f"a soma de 1 a 100 é: {soma}")


""""Exercício FP8: Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase."""

print("hello world")
frase=str(input("insere uma frase por favor: "))
vogais=0
for letra in frase:
  if letra == "a" or letra == "e" or letra== "i" or letra == "o" or letra == "u":
      vogais+=1
print(f"Número de vogais: {vogais}")    





""""Exercício FP9: Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50."""

print("hello world")

for i in range (1, 51):
  if i % 5 == 0:
    print(i)


""""Exercício FP10: Média de uma lista de números.
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números."""



num1=int(input("Introduza o número 1: "))
num2=int(input("Introduza o número 2: "))
num3=int(input("Introduza o número 3: "))
num4=int(input("Introduza o número 4: "))
num5=int(input("Introduza o número 5: "))
média= (num1 + num2 + num3 + num4 + num5) / 5
print(f"A média é:{média}")


"""Exercício FP11: Verificar se um número é primo.
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número."""
  
numero=int(input("insira um numero inteiro: "))
if numero > 1:
  for i in range(2,numero):
    if(numero % i) == 0 :
      print("nao é um numero primo")
else:
  print(numero, "é um numero primo!")





""""
Exercício FP12: Gerar uma lista de números pares.
  Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""

lista=list(range(1,21))
for i in lista:
  if i % 2 == 0:
    print(i)



""""    Exercício FP13: Inverter uma string.
    Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
    """

frase=str(input("escreve uma palavra ou uma frase: "))
string = frase[::-1]
print(f"A palavra invertida é: {string}")


""""Exercício FP14: Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10."""


numero=int(input("Introduza um número: "))
for i in range (1,11):
  tabuada= numero * i
  print(f"{numero} x {i} = {tabuada}")

""""INTRODUÇÃO
Desenvolver um programa em Python que utiliza funções para gerir o stock de materiais escolares de uma escola. O programa deverá permitir o registo, consulta e atualização do stock de forma eficiente.
PROBLEMA
A escola necessita de um sistema para gerir o stock de materiais (como canetas, cadernos, borrachas, etc.). Atualmente, o registo é feito manualmente, o que dificulta a atualização e a consulta rápida. Pretende-se um programa que automatize este processo, utilizando funções.
Requisitos
O programa deve:
Registar novos materiais no stock.
Consultar o stock de um material específico.
Atualizar a quantidade em stock (adição ou remoção).
Exibir o estado geral do stock.
"""



def adicionar_material(stock):
  nome = input("Nome do material: ")
  if nome in stock:
      print("O material já existe no stock!")
  else:
      quantidade = int(input(f"Quantidade inicial de {nome}: "))
      stock[nome] = quantidade
      print(f"{nome} adicionado com sucesso!")
    
def consultar_stock(stock):
  nome = input("Nome do material para consulta: ")
  if nome in stock:
      print(f"O stock atual de {nome} é: {stock[nome]}")
  else:
      print(f"{nome} não encontrado no stock.")


def atualizar_stock(stock):
  nome = input("Nome do material a atualizar: ")
  if nome in stock:
      operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
      quantidade = int(input("Quantidade: "))
      if operacao == "A":
          stock[nome] += quantidade
          print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
      elif operacao == "R":
          if quantidade <= stock[nome]:
              stock[nome] -= quantidade
              print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
          else:
              print("Quantidade insuficiente em stock!")
      else:
          print("Operação inválida!")
  else:
      print(f"{nome} não encontrado no stock.")


def exibir_stock(stock):
  print("\nEstado Geral do Stock:")
  print("Material\tQuantidade")
  print("-" * 30)
  for material, quantidade in stock.items():
      print(f"{material}\t\t{quantidade}")

def exportar_stock(stock):
  arquivo = open("exportar","w")
  print("\nEstado Geral do Stock:")
  print("Material\tQuantidade")
  print("-" * 30)
  for material, quantidade in stock.items():
    print(f"{material}\t\t{quantidade}",file=arquivo)
  
def main():
  stock = {}
  while True:
      print("\nGestão de Stock")
      print("1. Adicionar Material")
      print("2. Consultar Stock")
      print("3. Atualizar Stock")
      print("4. Exibir Stock Geral")
      print("5. Exportar Stock para ficheiro")
      print("6. Sair")
      opcao = input("Escolha uma opção: ")

      if opcao == "1":
          adicionar_material(stock)
      elif opcao == "2":
          consultar_stock(stock)
      elif opcao == "3":
          atualizar_stock(stock)
      elif opcao == "4":
          exibir_stock(stock)
      elif opcao == "5":
          exportar_stock(stock) 
      elif opcao == "6":
          print("Encerrando o programa...")
          break
      else:
          print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
  main()


