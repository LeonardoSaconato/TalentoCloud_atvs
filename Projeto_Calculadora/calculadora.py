def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

while True:
    print("Escolha a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "0":
        print("Encerrando o programa.")
        break
    elif escolha in ("1", "2", "3", "4"):
        try:
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            if escolha == "1":
                resultado = soma(a, b)
                print(f"Resultado: {resultado}")
            elif escolha == "2":
                resultado = subtracao(a, b)
                print(f"Resultado: {resultado}")
            elif escolha == "3":
                resultado = multiplicacao(a, b)
                print(f"Resultado: {resultado}")
            elif escolha == "4":
                resultado = divisao(a, b)
                print(f"Resultado: {resultado}")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")
    else:
        print("Essa opção não existe. Por favor, escolha uma opção válida.")
