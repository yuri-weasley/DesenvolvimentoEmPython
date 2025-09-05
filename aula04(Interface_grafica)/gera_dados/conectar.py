import psycopg2

# Criar conexão
conexao = psycopg2.connect(
    database="postgresDB",
    user="admin",
    password="admin123",
    host="127.0.0.1",
    port="5432"
)
print("Conexão bem sucedida!")

# Criar cursor
meu_cursor = conexao.cursor()