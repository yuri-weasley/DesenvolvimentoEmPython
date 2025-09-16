import tkinter as tk
from tkinter import ttk
import pandas as pd

class PrincipalRAD:
    def __init__(self, win):
        # componentes
        self.lbl_nome = tk.Label(win, text="Nome do Aluno:")
        self.lblNota1 = tk.Label(win, text="Nota 1:")
        self.lblNota2 = tk.Label(win, text="Nota 2:")
        self.lblMedia = tk.Label(win, text="Média:")
        self.txtNome = tk.Entry(bd=3)
        self.txtNota1 = tk.Entry()
        self.txtNota2 = tk.Entry()
        self.btnCalcular = tk.Button(win, text="Calcular Média", command=self.fCalcularMedia)
        # ------ Componente Treeview ----------------
        self.dadosColunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

        self.treeMedias = ttk.Treeview(win, columns=self.dadosColunas, selectmode="browse", show="headings")

        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.treeMedias.yview)

        self.verscrlbar.pack(side="right", fill="x")

        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)

        self.treeMedias.heading("Aluno", text="Nome do Aluno")
        self.treeMedias.heading("Nota1", text="Nota 1")
        self.treeMedias.heading("Nota2", text="Nota 2")
        self.treeMedias.heading("Média", text="Média")
        self.treeMedias.heading("Situação", text="Situação")

        self.treeMedias.column("Aluno", width=100, minwidth=0)
        self.treeMedias.column("Nota1", width=100, minwidth=0)
        self.treeMedias.column("Nota2", width=100, minwidth=0)
        self.treeMedias.column("Média", width=100, minwidth=0)
        self.treeMedias.column("Situação", width=100, minwidth=0)

        self.treeMedias.pack(padx=10, pady=10)

        # posicionamento dos componentes da tela

        self.lbl_nome.place(x=100, y=50)
        self.txtNome.place(x=200, y=50)

        self.lblNota1.place(x=100, y=100)
        self.txtNota1.place(x=200, y=100)

        self.lblNota2.place(x=100, y=150)
        self.txtNota2.place(x=200, y=150)

        self.btnCalcular.place(x=100, y=200)

        self.treeMedias.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)

        self.id = 0
        self.iid = 0

        self.carregarDadosIniciais()
# ------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
            fsave = 'planilhaAlunos.xlsx'
            dados = pd.read_excel(fsave)
            print('***Dados disponíveis***')
            print(dados)

            u = dados.count()
            print('u '+ str(u))
            nn = len(dados['Aluno'])
            for i in range(nn):
                nome = str(dados['Aluno'][i])
                nota1 = str(dados['Nota1'][i])
                nota2 = str(dados['Nota2'][i])
                media = str(dados['Média'][i])
                situacao = str(dados['Situação'][i])

                self.treeMedias.insert("", "end", iid=self.iid, values=(nome, nota1, nota2, media, situacao))

            self.iid += 1
            self.id += 1
        except Exception as e:
            print('Ainda não existem dados para carregar')
# ------------------------------------------------------
    def fSalvarDados(self):
        try:
            fsave = 'planilhaAlunos.xlsx'
            dados = []

            for line in self.treeMedias.get_children():
                lstDados = []
                for value in self.treeMedias.item(line)['values']:
                    lstDados.append(value)

                dados.append(lstDados)

            df = pd.DataFrame(dados, columns=self.dadosColunas)

            planilha = pd.ExcelWriter(fsave)
            df.to_excel(planilha, 'Inconsistências', index=False)

            # salva o arquivo
            planilha.close()
            print('Dados salvos com sucesso')
        except Exception as e:
            print('Não foi possível salvar os dados')

# ---------------- Calcula a média e verifica a situação do aluno ----------------------------
    def fVerificaSituacao(self, nota1, nota2):
        media = (nota1 + nota2) / 2
        if media >= 7:
              return media, "Aprovado"
        elif media >= 5:
              return media, "Recuperação"
        else:
              return media, "Reprovado"
# -------------------------------------------------------------------------------------------
    def fCalcularMedia(self):
        try:
            nome = self.txtNome.get()
            nota1 = float(self.txtNota1.get())
            nota2 = float(self.txtNota2.get())
            media, situacao = self.fVerificaSituacao(nota1, nota2)

            self.treeMedias.insert("", "end", iid=self.iid, values=(nome, nota1, nota2, f"{media:.2f}", situacao))

            self.iid += 1
            self.id += 1

            self.fSalvarDados()
        except Exception as e:
            print('Erro ao calcular a média. Verifique os dados informados.')
        finally:
            self.txtNome.delete(0, tk.END)
            self.txtNota1.delete(0, tk.END)
            self.txtNota2.delete(0, tk.END)
            self.txtNome.focus()

# ---------------- Programa Principal ----------------------
janela = tk.Tk()
janela.title("Cálculo da Média do Aluno")
janela.geometry("900x600")
janela.mainloop()