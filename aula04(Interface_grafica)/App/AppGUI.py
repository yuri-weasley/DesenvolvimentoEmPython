import tkinter as tk
from tkinter import ttk
from AppBD import AppBD

class PrincipalBD:
    def __init__(self, root):
        self.root = root
        self.app_bd = AppBD()
        self.title = "Gerenciador de Produtos"

        # Componentes da interface
        self.lblCodigo = tk.Label(root, text="Código")
        self.lblCodigo.grid(row=0, column=0)
        self.txtCodigo = tk.Entry(root)
        self.txtCodigo.grid(row=0, column=1)

        self.lblNome = tk.Label(root, text="Nome")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblPreco = tk.Label(root, text="Preço")
        self.lblPreco.grid(row=2, column=0)
        self.txtPreco = tk.Entry(root)
        self.txtPreco.grid(row=2, column=1)

        self.btnCadastrar = tk.Button(root, text="Cadastrar", command=self.fCadastrarProduto)
        self.btnCadastrar.grid(row=3, column=0)
        self.btnAtualizar = tk.Button(root, text="Atualizar", command=self.fAtualizarProduto)
        self.btnAtualizar.grid(row=3, column=1)
        self.btnDeletar = tk.Button(root, text="Deletar", command=self.fDeletarProduto)
        self.btnDeletar.grid(row=4, column=0)
        self.btnLimpar = tk.Button(root, text="Limpar", command=self.fLimparCampos)
        self.btnLimpar.grid(row=4, column=1)

        self.tree = ttk.Treeview(root, columns=("Código", "Nome", "Preço"), show='headings')
        self.tree.heading("Código", text="Código")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preço", text="Preço")
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.bind("<ButtonRelease-1>", self.fApresentarRegistrosSelecionados)

        self.fCarregarDadosiniciais()

    def fCadastrarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.app_bd.inserir_dados(nome, preco)
        self.tree.insert("", "end", values=(codigo, nome, preco))
        self.fLimparCampos()

    def fAtualizarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.app_bd.atualizar_dados(codigo, nome, preco)
        self.fCarregarDadosiniciais()
        self.fLimparCampos()

    def fDeletarProduto(self):
        codigo = self.txtCodigo.get()
        self.app_bd.deletar_dados(codigo)
        self.fCarregarDadosiniciais()
        self.fLimparCampos()

    def fLimparCampos(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)

    def fApresentarRegistrosSelecionados(self, event):
        item = self.tree.selection()[0]
        valores = self.tree.item(item, 'values')
        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.insert(tk.END, valores[0])
        self.txtNome.delete(0, tk.END)
        self.txtNome.insert(tk.END, valores[1])
        self.txtPreco.delete(0, tk.END)
        self.txtPreco.insert(tk.END, valores[2])

    def fCarregarDadosiniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        registros = self.app_bd.selecionar_dados()
        for registro in registros:
            self.tree.insert("", "end", values=registro)

# Criando a interface gráfica
root = tk.Tk()
app_bd = AppBD()
app_gui = PrincipalBD(root, app_bd)
root.mainloop()