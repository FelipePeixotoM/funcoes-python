"""
# Argumentos posicionais

## Explicação
Argumentos posicionais são aqueles em que a ordem dos valores passados importa,
pois é ela que define qual valor será atribuído a cada parâmetro da função.

Assim, a posição do argumento determina seu significado.

Exemplo:

def criar_mensagem(parametro1, parametro2):
    ...

criar_mensagem(argumento1, argumento2)

Se a ordem dos argumentos for alterada, os valores podem ser atribuídos aos parâmetros incorretos.
"""

# Exemplo de ordem certa (comportamento correto)

def criar_mensagem(mensagem, nome):
    return f"{mensagem}, {nome}!"
print(criar_mensagem("Boa tarde", "Felipe"))

# Exemplo de ordem errada (Comportamento inesperado)

print(criar_mensagem("felipe", "Boa tarde"))

"""
Ao executar o exemplo com ordem incorreta, a função ainda é executada normalmente,
sem gerar erro.

No entanto, os valores são atribuídos aos parâmetros errados:
o valor destinado ao nome é passado para mensagem, e vice-versa.

Isso gera um resultado inesperado, mostrando que a ordem dos argumentos posicionais
é fundamental para o correto funcionamento da função.
"""

