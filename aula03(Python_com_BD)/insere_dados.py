import sqlite3 as conector
 
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()
 
# Execução de um comando: SELECT... CREATE ...
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    VALUES (12345678900, 'João', '2000-01-31', 1);'''
  
cursor.execute(comando)
  
# Efetivação do comando
conexao.commit()
  
# Fechamento das conexões
cursor.close()
conexao.close()

"""
Observe que alteramos a formatação da data para se adequar ao padrão de alguns bancos de dados, como MySQL e PostgreSQL. Para o SQLite será indiferente, pois o tipo DATE será convertido por afinidade para NUMERIC, que pode ser de qualquer classe. Na prática, será convertido para classe TEXT.
"""