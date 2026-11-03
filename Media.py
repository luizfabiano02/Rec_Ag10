
# ==========================================
#       CÁLCULO DA MÉDIA DO ALUNO
# ==========================================

# Função para calcular a média das 4 notas
def calcular_media(notas):
    return sum(notas) / len(notas)


# Função para verificar a situação do aluno
def verificar_aprovacao(media):
    if media >= 6.0:
        return "APROVADO"
    else:
        return "REPROVADO"


# Função para cadastrar um aluno
def cadastrar_aluno(): #tentei treinar esse comando, mas não consegui. a IA precisou corrigir. os comadno ainda não foram ensinados no curso

    nome = input("\nDigite o nome do aluno: ").strip()

    while not nome:
        print("O nome não pode ficar vazio!")
        nome = input("Digite o nome do aluno: ").strip()

    notas = []

    # Solicita as 4 notas do aluno
    for i in range(4):

        while True:
            try:
                nota = float(input(f"Digite a {i + 1}ª nota: ").replace(",", "."))

                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Digite uma nota entre 0 e 10.")

            except ValueError:
                print("Valor inválido! Digite uma nota numérica.")

    # Calcula a média e verifica a aprovação
    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)

    # Retorna os dados do aluno
    return {
        "nome": nome,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }


# Função para gerar o relatório geral
def gerar_relatorio(alunos):

    print("\n")
    print("=" * 75)
    print("             RELATÓRIO DE DESEMPENHO DOS ALUNOS")
    print("=" * 75)

    for aluno in alunos:

        print(f"\nAluno: {aluno['nome']}")

        for i, nota in enumerate(aluno["notas"], start=1):
            print(f"Nota {i}: {nota:.1f}", end=" | ")

        print(f"\nMédia: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situacao']}")
        print("-" * 75)

    print("\nTotal de alunos cadastrados:", len(alunos))
    print("=" * 75)


# ==========================================
#             PROGRAMA PRINCIPAL
# ==========================================

print("=" * 50)
print("          CÁLCULO DA MÉDIA DO ALUNO")
print("=" * 50)

alunos = []

# Cadastro obrigatório de pelo menos 3 alunos
while len(alunos) < 3:

    print(f"\nCadastro do aluno {len(alunos) + 1}")
    aluno = cadastrar_aluno()
    alunos.append(aluno)

# Permite cadastrar alunos adicionais
while True:

    resposta = input(
        "\nDeseja cadastrar mais um aluno? (S/N): "
    ).strip().upper()

    if resposta == "S":

        print(f"\nCadastro do aluno {len(alunos) + 1}")
        aluno = cadastrar_aluno()
        alunos.append(aluno)

    elif resposta == "N":
        break

    else:
        print("Resposta inválida! Digite S ou N.")

# Gera o relatório final
gerar_relatorio(alunos)

print("\nPrograma finalizado com sucesso!")
