# Nesse script convertemos o tipo de dado booleano do banco de dados para o tipo booleano do Python. Para isso, usamos o método `register_converter` do módulo `sqlite3`.

# A primeira modificação ocorre nos parâmetros da criação da conexão. Precisamos passar o argumento PARSE_DECLTYPES para o parâmetro detect_types da função connect. Isso indica que o conector deve tentar fazer uma conversão dos dados, tomando como base o tipo da coluna declarada no CREATE TABLE.

# Os tipos DATE e TIMESTAMP já possuem conversores embutidos no sqlite3, porém o tipo BOOLEAN não. Para informar ao conector como fazer a conversão do tipo BOOLEAN, precisamos definir e registrar a função conversora utilizando a função interna register_converter do sqlite3.

# A função register_converter espera, como primeiro parâmetro, uma string com o tipo da coluna a ser convertido e, como segundo parâmetro, uma função que recebe o dado e retorna esse dado convertido.

# A função conv_bool, definida na linha 9, retorna True para o caso do dado ser 1, ou False, caso contrário. Com isso, convertemos os inteiros 0 e 1 para os booleanos True e False. O restante do script é igual ao anterior, porém, os dados estão convertidos para o tipo correto.

import sqlite3 as conector
from modelo import Pessoa
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES)
cursor = conexao.cursor()

# Funções conversoras
def conv_bool(dado):
   return True if dado == 1 else False

# Registro de conversores
conector.register_converter("BOOLEAN", conv_bool)

# Definição dos comandos
comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
cursor.execute(comando, {"usa_oculos": True})

# Recuperação dos registros
registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

# Fechamento das conexões
cursor.close()
conexao.close()