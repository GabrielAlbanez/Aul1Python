npc = [
   {"nome" : "gabriel","idade" : 15,},
   {"nome" : "fernando","idade" : 15,},
   {"nome" : "isabella","idade" : 35,}
]

print(npc)


for data in npc:
  nome = data["nome"]
  idade = data["idade"]
  print("nome",nome,"idade",idade)