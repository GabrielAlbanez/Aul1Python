
import os

calculosFeiots = []

def dataUser(x, y, operator):
    resposta = None
    if operator == "1":
        resposta = x + y
    elif operator == "2":
        resposta = x - y
    elif operator == "3":
        resposta = x / y
    elif operator == "4":
        resposta = x * y
    print(resposta)
    return resposta

contador = 1

while True:
    os.system('cls')
    print("conta ",contador)
    x = float(input("digite um valor para o numero x: "))
    y = float(input("digite um valor para o numero y: "))
    operacao = input("digite qual operação vc quer que seja feita, 1) adição, 2 ) subtração, 3 ) divisão, 4 ) mutiplicação : ").lower()
    resultado = dataUser(x, y, operacao)
    calculosFeiots.append({
        "x": x,
        "y": y,
        "operacao": operacao,
        "resposta": resultado
    })
    pergunta = input("para continuar fazer as operações digite : continuar, caso queria para digite : pare: ")
    contador+= 1
    if pergunta == "pare":
        os.system('cls')
        break

conta = 0

for calculo in calculosFeiots:
    conta = conta + 1
    valorX = calculo["x"]
    valorY = calculo["y"]
    operacao = calculo["operacao"]
    nomeOperador = ""
    if(operacao == "1"):
      nomeOperador = "adição"
    elif(operacao == "2"):
      nomeOperador = "subtração"
    elif(operacao == "3"):
      nomeOperador = "divisão"
    elif(operacao == "4"):
      nomeOperador = "mutiplicação"
    
       
      
    valorResposta = calculo["resposta"]
    print("conta:", conta)
    print("x:", valorX, "y:", valorY, "operacao:", nomeOperador, ", resposta:", valorResposta)
    print("--------------------------------")

  


    
    
     
  
  
  














# alunos = []


# for i in range(3):
#   os.system('cls')
#   nome = input("digite seu nome: ")
#   idade = input("digite sua idade:")
#   resposta  = [nome,idade]
#   alunos.append(resposta)
  
  
  
# for al in alunos:
#   nomeAluno = al[0]
#   idadeAluno = al[1]
#   print("Aluno: ",nomeAluno,"idadade: ",idadeAluno)

