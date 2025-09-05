# pip install psycopg2
# pip install faker
# pip install tk

import psycopg2

# Cria conexão
conexao = psycopg2.connect(
    database="postgresDB",
    user="admin",
    password="admin123",
    host="127.0.0.1",
    port="5432"
)
print("Conexão bem sucedida!")

# Cria um cursor
meu_cursor = conexao.cursor()

if __name__ == "__main__":
    # Cria a tabela
    meu_cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUTO (
            CODIGO SERIAL PRIMARY KEY,
            NOME VARCHAR(100) NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL,
        )
    ''')
    
    # just in case
    conexao.commit()
    print("Tabela criada com sucesso!")
    conexao.close()