"""
🚀 Agora: Exercícios de Argumentos Nomeados
"""

"""
🧠 Exercício 1 — Perfil de usuário

Crie uma função que receba:

nome
idade
cidade

👉 Tarefa:

faça uma chamada usando posicionais
faça uma chamada usando nomeados fora de ordem

👉 Objetivo:
mostrar que nomeados ignoram ordem
"""

def cadastrar_usuario(nome, idade, cidade):
    return f"{nome} | {idade} | {cidade}"

# caso 1 - argumentos posicionais
print(cadastrar_usuario("Felipe", 29, "Rio de janeiro"))

# caso 2 - argumentos nomeados (na ordem)
print(cadastrar_usuario(nome="Felipe", idade=29, cidade="Rio de janeiro"))

# caso 3 - argumentos nomeados (fora de ordem)
print(cadastrar_usuario(idade=29, cidade="Rio de janeiro", nome="Felipe"))

"""
Análise:

# Caso 1:
Uso de argumentos posicionais. Funciona corretamente, mas a leitura pode
ficar menos clara conforme o número de parâmetros aumenta.

# Caso 2:
Uso de argumentos nomeados na ordem. Código mais legível.

# Caso 3:
Uso de argumentos nomeados fora de ordem. Funciona normalmente,
mostrando que a ordem não importa nesse caso.

Argumentos nomeados aumentam a clareza e reduzem a dependência da ordem.
"""

"""🧠 Exercício 2 — Configuração de envio (muito bom)

Crie uma função que receba:

destinatario
mensagem
urgente (padrão = False)

👉 Tarefa:

chame passando só os obrigatórios
chame usando urgente=True com nomeado

👉 Objetivo:
mostrar clareza e uso com valor padrão"""

def config_envio(destinatario, mensagem, urgente=False):
    return f"{mensagem} para {destinatario} ** URGENTE" if urgente else f"{mensagem} para {destinatario}"

# caso 1 - argumentos posicionais
print(config_envio("felipe", "teste de envio!"))
# caso 2 - argumentos nomeados
print(config_envio(destinatario="Felipe", mensagem="teste de envio!"))
# caso 3 - argumentos mesclados
print(config_envio("Felipe", "teste de envio!", True))
# caso 4 - argumetnos nomeados
print(config_envio(destinatario="Felipe", mensagem="teste de envio!", urgente=True))

"""
Análise:

# caso 1:
Uso de argumetnto posicional. Funciona, mas prejudica a leitura do codigo
# caso 2:
Uso de argumento nomeado. Melhora a legibilidade e clareza do codigo
# Caso 3:
Uso de argumentos posicionais incluindo o parâmetro opcional.
Funciona, mas a leitura pode ficar menos clara.
# caso 4:
Uso de argumentos nomeados, podemos notar a diferença de legibilidade no codigo.
"""

"""

🧠 Exercício 3 — Relatório financeiro (nível mais alto)

Crie uma função que receba:

titulo
valor
imposto (padrão = 0)

👉 Tarefa:

faça uma chamada confusa com posicionais
depois refatore usando nomeados

👉 Objetivo:
mostrar quando nomeados são melhores
"""

def relatorio_financeiro(titulo, valor, imposto=0):
    return f"{titulo} | {valor} | {imposto}%"

# caso 1 - argumentos posicionais
print(relatorio_financeiro("Banco do Brasil", 54))
#caso 2 - argumentos posicionais - incluindo parametro opcional
print(relatorio_financeiro("Banco do Brasil", 54, 15))
# caso 3 - argumentos posicionais e nomeados
print(relatorio_financeiro("Banco do Brasil", valor=54, imposto=15))
# caso 4 - argumentos nomeados
print(relatorio_financeiro(titulo="Banco do Brasil", valor=54, imposto=15))

"""
Análise:

# caso 1:
Uso de argumentos posicionais, notamos falta de clareza e dificuldade de leitura
# caso 2:
Uso de argumentos posicionais, incluindo parametro opcional, se nota quanto mais argumentos aumenta
a dificuldade de leitura e clareza
# caso 3:
Uso de argumentos misto, Podemos notar que melhora a clareza do codigo
# caso 4:
Uso de argumentos nomeados. Notamos a diferença de legibilidade
"""

