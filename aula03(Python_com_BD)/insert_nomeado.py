import sqlite3 as conector
from modelo import Pessoa
  
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()
 
# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(20000000099, 'José', '1990-02-28', False)
  
# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
cursor.execute(comando, {"cpf": pessoa.cpf,
                        "nome": pessoa.nome,
                        "data_nascimento": pessoa.data_nascimento,
                        "usa_oculos": pessoa.usa_oculos})
  
# Efetivação do comando
conexao.commit()
  
# Fechamento das conexões
cursor.close()
conexao.close()

"""
O insert nomeado é uma forma de inserir dados em um banco de dados usando parâmetros nomeados, o que torna o código mais legível e menos propenso a erros. No exemplo acima, usamos um objeto `Pessoa` para inserir seus dados na tabela `Pessoa` do banco de dados.
Os parâmetros nomeados permitem que você especifique os valores a serem inseridos de forma clara, usando chaves que correspondem aos nomes das colunas na tabela. Isso é especialmente útil quando você tem muitos campos ou quando os nomes dos campos são longos ou complexos.
Além disso, o uso de parâmetros nomeados ajuda a evitar problemas de injeção de SQL, pois os valores são tratados de forma segura pelo driver do banco de dados. Isso significa que você não precisa se preocupar com a formatação correta dos valores ou com a possibilidade de injeção de código malicioso.
O comando `INSERT INTO` é usado para adicionar novos registros a uma tabela, e os parâmetros nomeados são especificados na cláusula `VALUES` do comando. No exemplo, os valores são passados como um dicionário, onde as chaves correspondem aos nomes dos parâmetros definidos no comando SQL.
O uso de parâmetros nomeados é uma prática recomendada em Python ao trabalhar com bancos de dados, pois melhora a legibilidade do código e facilita a manutenção. Além disso, permite que você reutilize o mesmo comando com diferentes valores sem precisar reescrever a consulta SQL.
Os parâmetros nomeados são especificados no comando SQL com o prefixo `:`, e os valores são passados como um dicionário, onde as chaves correspondem aos nomes dos parâmetros. Isso permite que o código seja mais claro e fácil de manter, além de evitar problemas de injeção de SQL.
"""