notas = []

  

while quantidadesAlunos < 3:
  codigoAluno = input("RM: ")
  nota = float(input("digite sua nota: "))
  resultado = {
    f"aluno {quantidadesAlunos}": codigoAluno,
    "nota" : nota,
  }
  notas.append(resultado)
  quantidadesAlunos += 1
  
  
for contador in range(3):
      codigoAluno = input("RM: ")
      nota = float(input("digite sua nota: "))
      resultado = [codigoAluno,nota]
      notas.append(resultado)
      
print("quantidade de notas",len(notas))      
      



for n in notas:
 codigo_auno = n[0]
 nota = n[1]  
 print ("rm",codigo_auno, "nota",nota)
      
  
  



