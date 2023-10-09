## Nome: Leonardo Saconato de Santana
## Turma: 08

import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (1922-2022): "))
            if 1922 <= ano <= 2022:
                return ano
            else:
                print("Por favor, digite um ano válido entre 1922 e 2022.")
        except ValueError:
            print("Erro: Digite um número válido para o ano de nascimento.")

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento()

idade_atual = calcular_idade(ano_nascimento)
print(f"Nome: {nome_completo}")
print(f"Sua idade em 2023: {idade_atual} anos")
