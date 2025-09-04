import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgresDB",
    user="admin",
    password="admin123"
)
cursor = conn.cursor()

# Deletar dados da tabela
cursor.execute("""
DELETE FROM public."AGENDA"
WHERE id = 1;
""")
conn.commit()

# Ler dados da tabela para verificar a deleção
cursor.execute("""
SELECT id, nome, telefone FROM public."AGENDA";
""")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")

# Fechar a conexão
cursor.close()
conn.close()