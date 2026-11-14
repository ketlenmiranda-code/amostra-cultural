# Lista de dicionários contendo os dados dos alunos
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 5.0},
    {"nome": "Carla", "nota": 9.2},
    {"nome": "Diego", "nota": 6.8},
    {"nome": "Elena", "nota": 7.5}
]

nota_corte = 7.0

print(f"--- Alunos Aprovados (Nota >= {nota_corte}) ---")

# Filtra e exibe apenas os alunos que atingiram a média
for aluno in alunos:
    if aluno["nota"] >= nota_corte:
        print(f"Aluno(a): {aluno['nome']} | Nota: {aluno['nota']}")


