# Pedro Henrique Oliveira Lima


# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(a, b):

    # Realizar as operações
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b

    # Verificar divisão por zero
    if b != 0:
        divisao = a / b
    else:
        divisao = 0

    # Retornar os resultados
    return soma, subtracao, multiplicacao, divisao
    

# Teste a sua função aqui (caso ache necessário)
