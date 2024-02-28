import os

mensagens = []

nome = input("Nome: ")
# quando usamos o true server para fazer um loop infinito
while True:
   # esse os server para realizarmos tarefas do sistema operacional, no caso aq estamos usando para limpar
   # o terminal
  os.system('cls')
  
  if len(mensagens) > 0:
    for m in mensagens:
      print(m['nome'], "-", m['texto'])
  
  print("--------------------------------")
  
  # obtendo un texto
  
  texto = input("mensagen: ")
  
  if(texto == "fim"):
    # break encessa o loop indenpende de quaquer coisa mesmo se for um loop infinito
    break
  
  mensagens.append({
    "nome" : nome,
    "texto" : texto
  })
  
  
  

print(os.name)




