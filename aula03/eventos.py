import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Locais (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      endereco TEXT NOT NULL)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Eventos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      data TEXT NOT NULL,
                      local_id INTEGER NOT NULL,
                      FOREIGN KEY(local_id) REFERENCES Locais(id))''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Participantes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL,
                      evento_id INTEGER NOT NULL,
                      FOREIGN KEY(evento_id) REFERENCES Eventos(id))''')
   
    conexao.commit()
    cursor.close()

if __name__ == '__main__':
    conexao = conectar_banco('eventos.db')
    criar_tabelas(conexao)
    conexao.close()