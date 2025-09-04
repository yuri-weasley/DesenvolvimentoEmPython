import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgresDB",
    user="admin",
    password="admin123"
)

cursor = conn.cursor()
cursor.execute("""
                CREATE TABLE IF NOT EXISTS public."AGENDA"
(
    id integer NOT NULL,
    nome text COLLATE pg_catalog."default" NOT NULL,
    telefone char(12) COLLATE pg_catalog."default" NOT NULL,
)
TABLESPACE pg_default;
ALTER TABLE public."AGENDA"
    OWNER to admin;
               """)

# Inserir dados na tabela
cursor.execute("""
INSERT INTO public."AGENDA" (id, nome, telefone)
VALUES (1, 'Teste 1', '1234567890'),
""")
cursor.execute("""
INSERT INTO public."AGENDA" (id, nome, telefone)
VALUES (2, 'Teste 2', '0987654321');
""")
conn.commit()

# Ler dados da tabela
cursor.execute("""
SELECT id, nome, telefone FROM public."AGENDA";
""")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")


# Fechar a conexão
cursor.close()
conn.close()