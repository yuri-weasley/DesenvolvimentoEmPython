import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd

# Dicionário de usuários para autenticação
usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"},
}

def abrir_tela_login():
    login_win = tk.Tk()
    login_win_title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Usuário:").pack()
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack()

    tk.Label(login_win, text="Senha:").pack()
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack()

    def valida_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            tipo_usuario = usuarios[usuario]["tipo"]
            login_win.destroy()
            iniciar_sistema(tipo_usuario)
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")

    tk.Button(login_win, text="Login", command=valida_login).pack(pady=10)
    login_win.mainloop()

def iniciar_sistema(tipo_usuario, usuario):
    janela = tk.Tk()
    janela.title("Sistema de Gerenciamento de Notas")
    janela.geometry("820x600")

    colunas = ("Aluno", "Nota 1", "Nota 2", "Média")
    treeMedias = ttk.Treeview(janela, columns=colunas, show='headings')

    for coluna in colunas:
        treeMedias.heading(coluna, text=coluna)
        treeMedias.column(coluna, width=100)

    treeMedias.pack(padx=10, pady=10,)
    scrollbar = ttk.Scrollbar(janela, orient=tk.VERTICAL, command=treeMedias.yview)
    treeMedias.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    carregar_dados(treeMedias, usuario, tipo_usuario)
    
    if tipo_usuario == "professor":
        tk.Button(janela, text="Cadastrar aluno", command=lambda: cadastrar_aluno(treeMedias)).pack()
        tk.Button(janela, text="Excluir aluno", command=lambda: excluir_aluno(treeMedias)).pack()
    janela.mainloop()

def carregar_dados(treeMedias, usuario, tipo_usuario):
    try: 
        df = pd.read_excel("planilhaAlunos.xlsx")
        treeMedias.delete(*treeMedias.get_children())

        if tipo_usuario == "professor":
            for _, row in df.iterrows():
                treeMedias.insert("", "end", values=(row["Aluno"], row["Nota 1"], row["Nota 2"], row["Média"], row["Situação"]))
        else:
            aluno_data = df[df["Aluno"] == usuario]
            for _, row in aluno_data.iterrows():
                treeMedias.insert("", "end", values=(row["Aluno"], row["Nota 1"], row["Nota 2"], row["Média"], row["Situação"]))
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo planilhaAlunos.xlsx não encontrado.")

def cadastrar_aluno(treeMedias):
    nome = simpledialog.askstring("Cadastro", "Nome do aluno:")
    nota1 = simpledialog.askfloat("Cadastro", "Nota 1:")
    nota2 = simpledialog.askfloat("Cadastro", "Nota 2:")
    media, situacao = verificar_situacao(nota1, nota2)

    treeMedias.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))
    salvar_dados(treeMedias)

def excluir_aluno(treeMedias):
    if usuarios["professor"]["tipo"] != "professor":
        messagebox.showerror("Erro", "Apenas professores podem excluir alunos.")
        return
    
    selected_item = treeMedias.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Nenhum aluno selecionado.")
        return
    
    treeMedias.delete(selected_item)
    salvar_dados(treeMedias)

def salvar_dados(treeMedias):
    dados = []
    for line in treeMedias.get_children():
        valores = treeMedias.item(line)["values"]
        dados.append(valores)

    df = pd.DataFrame(dados, columns=["Aluno", "Nota 1", "Nota 2", "Média", "Situação"])
    df.to_excel("planilhaAlunos.xlsx", index=False, engine='openpyxl')
    print("Dados salvos com sucesso!")

def verificar_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        return media, "Aprovado"
    elif media >= 5:
        return media, "Recuperação"
    else:
        return media, "Reprovado"
    
abrir_tela_login()