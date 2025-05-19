def printf(msg):
    print(msg)

def imprimir_exclamacoes(n):
    for i in range(1, n + 1):
        printf('!' * i)

n = int(input("Digite a quantidade: "))
imprimir_exclamacoes(n)
