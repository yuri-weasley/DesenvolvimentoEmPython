import psycopg2
from psycopg2 import Error

def connect_to_db():
    try:
        # Conectar ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            host="localhost",
            database="postgresDB",
            user = "admin",
            password = "admin123"
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def create_contact(nome, telefone):
    conn = connect_to_db()
    if conn is None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO public."AGENDA" (nome, telefone) 
            VALUES (%s, %s) RETURNING id;
            """, (nome, telefone))
            contact_id = cursor.fetchone()[0]
            conn.commit()
            print(f"Contato adicionado com ID: {contact_id}")
        except Error as e:
            print(f"Erro ao criar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def read_contacts():
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            SELECT id, nome, telefone FROM public."AGENDA";
            """)
            contacts = cursor.fetchall()
            for contact in contacts:
                print(f"ID: {contact[0]}, Nome: {contact[1]}, Telefone: {contact[2]}")
        except Error as e:
            print(f"Erro ao ler contatos: {e}")
        finally:
            cursor.close()
            conn.close()

def update_contact(contact_id, novo_nome, novo_telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            UPDATE public."AGENDA" 
            SET nome = %s, telefone = %s 
            WHERE id = %s;
            """, (novo_nome, novo_telefone, contact_id))
            conn.commit()
            print(f"Contato com ID {contact_id} atualizado.")
        except Error as e:
            print(f"Erro ao atualizar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_contact(contact_id):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            DELETE FROM public."AGENDA" 
            WHERE id = %s;
            """, (contact_id,))
            conn.commit()
            print(f"Contato com ID {contact_id} deletado.")
        except Error as e:
            print(f"Erro ao deletar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Ver Contatos")
        print("3. Atualizar Contato")
        print("4. Deletar Contato")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        # A partir do Python 3.10, podemos usar match-case
        if choice == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            create_contact(nome, telefone)
        elif choice == '2':
            read_contacts()
        elif choice == '3':
            contact_id = int(input("ID do contato a ser atualizado: "))
            novo_nome = input("Novo Nome: ")
            novo_telefone = input("Novo Telefone: ")
            update_contact(contact_id, novo_nome, novo_telefone)
        elif choice == '4':
            contact_id = int(input("ID do contato a ser deletado: "))
            delete_contact(contact_id)
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()