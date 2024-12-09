"""
De acordo com a opção escolhida, o programa deve chamar a função calcula_area_circulo(), calcula_area_triagulo() ou calcula_area_retangulo(). Cada uma delas deve solicitar ao utilizador os parâmetros necessários para o cálculo da área. 
As funções devem retornar o valor calculado.
"""


def calcula_area_circulo():
  raio = float(input("Insira o raio do círculo: "))
  area = 3.14 * raio ** 2
  return area
def calcula_area_triangulo():
  base = float(input("Insira a base do triângulo: "))
  altura = float(input("Insira a altura do triângulo: "))
  area = (base * altura) / 2
  return area
def calcula_area_retangulo():
  base = float(input("Insira a base do retângulo: "))
  altura = float(input("Insira a altura do retângulo: "))
  area = base * altura
  return area
opcao = int(input("Qual figura deseja calcular a área?\n1. Círculo\n2. Triângulo\n3. Retângulo\n"))
if opcao == 1:
  area = calcula_area_circulo()
  print(f"A área do círculo é {area}")
elif opcao == 2:
  area = calcula_area_triangulo()
  print(f"A área do triângulo é {area}")
elif opcao == 3:
  area = calcula_area_retangulo()
  print(f"A área do retângulo é {area}")
else:
  print("Opção inválida")
