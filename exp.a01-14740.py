import random
nome = input("Insira o seu nome: ")
tent = ("Voce tem 6 tentativas para acertar o numero de 1 a 20")
print(tent)
numero = random.randint(1,20)
#print (numero)
tentativa = 6
while tentativa > 0:
  aposta = int(input("Insira um numero: "))
  if aposta == numero:
    print(f"Parabens {nome} voce acertou o numero em {tentativa} tentativas!")
    exit()
  elif aposta < numero:
    print(f"É SUPERIOR!")
    tentativa -= 1
    print (f"Ainda te restam {tentativa}")
  elif aposta > numero:
    print ("É INFERIOR")
    tentativa -= 1
    print (f"Ainda te restam {tentativa}")
print(f"Acabaram as tuas tentativas o numero correto era {numero}!")
print("Joga de novo!")
