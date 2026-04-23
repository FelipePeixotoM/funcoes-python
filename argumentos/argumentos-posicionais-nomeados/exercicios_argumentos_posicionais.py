"""
Exercicios com base em argumentos posicionais e nomeados, vou fazer os exercicios e ir comentando sobre eles.
"""

"""
🔹 Exercício 1 — Mensagem personalizada

Crie uma função que receba:

saudação
nome

👉 A função deve retornar uma mensagem formatada.

Tarefa:
chame a função corretamente
depois chame invertendo os argumentos

👉 Observe e comente o resultado
"""

def criar_mensagem(saudacao, nome):
    return f"{saudacao}, {nome}!"



# caso correto
print(criar_mensagem("Bem-vindo", "felipe"))

# caso incorreto (ordem invertida)
print(criar_mensagem("felipe", "Bem-vindo"))

"""
Análise:
No primeiro caso como os argumentos foram passados corretamente, tudo ok!

No segundo, os valores do argumento foram invertidos:
- "felipe" é atribuido a saudacao
- "Bem-vindo" é atribuido a nome

Isso gera um resultado incorreto, mostrando a importancia da ordem nos argumentos posicionais
"""


"""🔹 Exercício 2 — Cálculo de desconto

Crie uma função que receba:

preço
desconto (em %)

👉 A função deve retornar o valor final com desconto aplicado

Tarefa:
chame corretamente
depois troque a ordem dos argumentos

👉 Explique por que o resultado fica errado"""


def aplicar_desconto(preco, desconto):
    taxa_desconto = desconto / 100
    preco_com_desconto = preco - (preco * taxa_desconto)
    return f"R${preco_com_desconto:.2f}"

# caso correto
print(aplicar_desconto(100,10))

# caso incorreto (ordem invertida)
print(aplicar_desconto(10, 100))

"""
Análise:

# primeiro caso:

Os argumentos foram passados na ordem certa, tudo ok!

# segundo caso:

Os valores foram invertido:
- 10 foi atribuido a preco
- 100 foi atribuido a desconto
Assim gerando um resultado não esperado, o que reforça a importancia da ordem nos argumentos posicionais, principalmente quando vamos ter calculos.
"""

"""🔹 Exercício 3 — Sistema de login (nível mais alto)

Crie uma função que receba:

usuário
senha

👉 A função deve validar:

se ambos são strings
se não estão vazios
Tarefa:
chame corretamente
depois troque a ordem

👉 Explique por que isso pode ser perigoso em um sistema real"""

def verificar_string(usuario, senha):
    usuario_senha_string = all(isinstance(dado ,(str)) for dado in [usuario, senha])
    return True if usuario_senha_string else False

def verificar_dado_vazio(usuario, senha):
    dado_vazio = all(len(dado)>0 for dado in [usuario, senha])
    return True if dado_vazio else False

validacoes = {
    "verificar_str": verificar_string,
    "verificar_vazio": verificar_dado_vazio
}

def validar_entrada(usuario, senha, validacoes):
    verificar_tipo_str = validacoes["verificar_str"](usuario, senha)
    verificar_se_vazio = validacoes["verificar_vazio"](usuario, senha)
    print("Ambos dados corretos!" if verificar_tipo_str and verificar_se_vazio else "Um dos dados invalido!")

# caso correto
validar_entrada("usuario", "senha", validacoes)
# caso incorreto
# validar_entrada("usuario", validacoes, "senha")

"""
Análise:

No primeiro caso, os argumentos são passados corretamente e a função executa como esperado.

No segundo caso, a ordem dos argumentos está incorreta:
- "usuario" é atribuído corretamente
- validacoes é atribuído ao parâmetro senha
- "senha" é atribuído ao parâmetro validacoes

Isso causa erro de execução, pois a função espera um dicionário em validacoes,
mas recebe uma string.

Esse exemplo demonstra como o uso incorreto de argumentos posicionais pode
quebrar completamente a lógica do programa.
"""


