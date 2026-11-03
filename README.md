# 📚 Cálculo da Média do Aluno

## 1. Sobre o projeto

Este projeto foi desenvolvido em Python com o objetivo de automatizar o cálculo das médias escolares dos alunos.

O programa permite cadastrar estudantes, registrar quatro notas para cada um, calcular a média final e identificar automaticamente se o aluno foi aprovado ou reprovado.

O desenvolvimento utiliza conceitos básicos de programação, como funções, estruturas condicionais, estruturas de repetição e listas.

## 2. Funcionalidades

- Cadastro de pelo menos 3 alunos.
- Possibilidade de cadastrar quantos alunos forem necessários.
- Registro de 4 notas por aluno.
- Validação das notas, permitindo valores entre 0 e 10.
- Cálculo automático da média.
- Verificação da situação do aluno.
- Geração de relatório geral de desempenho.
- Identificação do total de alunos cadastrados.

## 3. Regra de aprovação

O programa utiliza a média 6,0 como critério para aprovação.

| Média final | Resultado |
|---|---|
| Igual ou superior a 6,0 | APROVADO |
| Inferior a 6,0 | REPROVADO |

**Fórmula utilizada:**

Média = (Nota 1 + Nota 2 + Nota 3 + Nota 4) / 4

## 4. Organização do código

O programa foi dividido em quatro funções principais:

| Função | Descrição |
|---|---|
| `calcular_media()` | Recebe as notas e calcula a média. |
| `verificar_aprovacao()` | Verifica se o aluno foi aprovado ou reprovado. |
| `cadastrar_aluno()` | Solicita o nome e as quatro notas do aluno. |
| `gerar_relatorio()` | Apresenta os resultados dos alunos cadastrados. |

Essa divisão facilita a leitura, a organização, a manutenção e a reutilização do código.

## 5. Tecnologias utilizadas

- **Linguagem:** Python 3.
- **Editor de código:** Visual Studio Code.
- **Execução:** Terminal do computador.

Não é necessário instalar bibliotecas externas para executar o programa.

## 6. Como executar o programa

1. Instale o Python 3 no computador.
2. Abra o projeto no Visual Studio Code.
3. Crie ou abra o arquivo `calculo_media.py`.
4. Insira o código-fonte do programa.
5. Salve o arquivo.
6. Abra o terminal e execute:

```bash
python calculo_media.py
```

## 7. Exemplo de funcionamento

**Dados de um aluno:**

- Nome: João
- Nota 1: 8,0
- Nota 2: 7,0
- Nota 3: 9,0
- Nota 4: 8,0

**Resultado apresentado:**

```text
RELATÓRIO DE DESEMPENHO DOS ALUNOS

Aluno: João

Nota 1: 8.0
Nota 2: 7.0
Nota 3: 9.0
Nota 4: 8.0

Média: 8.00
Situação: APROVADO
```

## 8. Possíveis melhorias futuras

O programa poderá receber novas funcionalidades, como:

- Cadastro de disciplinas.
- Identificação de turmas.
- Armazenamento dos dados em arquivos.
- Consulta de resultados anteriores.
- Geração de relatórios em PDF.
- Interface gráfica para facilitar a utilização.

## 9. Objetivo educacional

Este projeto faz parte da atividade de recuperação da Agenda 10, da disciplina de Desenvolvimento de Sistemas.

A atividade tem como objetivo demonstrar a importância da organização do código por meio de funções e procedimentos, além de aplicar conceitos de lógica de programação na resolução de uma situação do cotidiano escolar.

---

**Projeto:** Cálculo da Média do Aluno  
**Disciplina:** Desenvolvimento de Sistemas  
**Linguagem:** Python 3