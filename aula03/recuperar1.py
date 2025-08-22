# No exemplo a seguir, vamos mostrar como recuperar todos os registros da tabela Pessoa.

# Observe que estamos selecionando todas as pessoas da tabela, visto que não há cláusulas WHERE. Porém, estamos recuperando apenas os dados das colunas nome e oculos.

import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Definição dos registros
comando = '''SELECT nome, oculos FROM Pessoa;'''
cursor.execute(comando)

# Recuperação dos dados
registros = cursor.fetchall()
print("Tipo retornado pelo fetchall():", type(registros))

for registro in registros:
    print("Tipo:", type(registro), "- Conteúdo:", registro)

# Fechamento das conexões
cursor.close()
conexao.close()