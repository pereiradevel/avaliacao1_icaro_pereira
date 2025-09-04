alunos = int(input("Quantos alunos tem na turma? "))
quantidade = alunos + 1
notaaluno = 0
for i in range(1,quantidade):
    notas = float(input(f"Digite a nota do aluno {i}: "))
    notaaluno += notas
media = (notaaluno / alunos)
print(f"Media da turma foi: {media}.")
if notas >= 6:
    print(f"{i} foram aprovados.")
#Testando GIT