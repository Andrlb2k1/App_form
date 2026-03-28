# Importando o Tkinter
from tkinter import *

# Importando o ttk
from tkinter import ttk

# Importando o messagebox
from tkinter import messagebox

# Importando o Tkcalendar
from tkcalendar import Calendar, DateEntry

# Importando a "view"
from view import *

# Cores
co0 = "#f0f3f5"  # Branca 1
co1 = "#feffff"  # Branca 2
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # Laranja
co6 = "#038cfc"  # Azul
co7 = "#ef5350"  # Vermelha
co8 = "#263238"  # Preta
co9 = "#e9edf5"  # Branca 3

# Criando a janela
janela = Tk()
janela.title("")
janela.geometry("1043x453")
janela.configure(bg=co9)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief="flat")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief="flat")
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label de cima
app_nome = Label(frame_cima, text="Formulário de Consultoria", anchor=NW, font=("Ivy 13 bold"), width=310, height=50, bg=co2, fg=co1, relief="flat")
app_nome.place(x=10, y=20)

# Função "inserir"
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    data = e_cal.get()
    estado = e_estado.get()
    sobre = e_sobre.get()

    lista = [nome, email, telefone, data, estado, sobre]

    if nome == "":
        messagebox.showerror("Erro!", "O nome deve ser preenchido!")
    elif email == "":
        messagebox.showerror("Erro!", "O email deve ser preenchido!")
    elif telefone == "":
        messagebox.showerror("Erro!", "O telefone deve ser preenchido!")
    elif data == "":
        messagebox.showerror("Erro!", "A data da consulta deve ser preenchida!")
    elif estado == "":
        messagebox.showerror("Erro!", "O estado da consulta deve ser preenchido!")
    else:
        inserir_info(lista)
        messagebox.showinfo("Sucesso!", "Os dados foram inseridos com sucesso!")
    
    e_nome.delete(0, "end")
    e_email.delete(0, "end")
    e_tel.delete(0, "end")
    e_cal.delete(0, "end")
    e_estado.delete(0, "end")
    e_sobre.delete(0, "end")

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

# Configurando o frame de baixo
# Nome
l_nome = Label(frame_baixo, text="Nome *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_nome.place(x=15, y=40)

# Email
l_email = Label(frame_baixo, text="Email *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_email.place(x=15, y=100)

# Telefone
l_tel = Label(frame_baixo, text="Telefone *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_tel.place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_tel.place(x=15, y=160)

# Data da consulta
l_cal = Label(frame_baixo, text="Data da consulta *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_cal.place(x=15, y=190)
e_cal = DateEntry(frame_baixo, width=12, bg="darkblue", fg="white", borderwidth=2, date_pattern="dd/mm/y")
e_cal.place(x=15, y=220)

# Estado
l_estado = Label(frame_baixo, text="Estado da consulta *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify="left", relief="solid")
e_estado.place(x=160, y=220)

# Sobre
l_sobre = Label(frame_baixo, text="Informação extra", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_sobre.place(x=15, y=260)
e_sobre = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_sobre.place(x=15, y=290)

# Botões
# Botão para inserir
b_inserir = Button(frame_baixo, command=inserir, text="Inserir", width=10, font=("Ivy 9 bold"), bg=co6, fg=co1, relief="raised", overrelief="ridge")
b_inserir.place(x=15, y=340)

# Botão para atualizar
b_atualizar = Button(frame_baixo, text="Atualizar", width=10, font=("Ivy 9 bold"), bg=co2, fg=co1, relief="raised", overrelief="ridge")
b_atualizar.place(x=110, y=340)

# Botão para deletar
b_deletar = Button(frame_baixo, text="Deletar", width=10, font=("Ivy 9 bold"), bg=co7, fg=co1, relief="raised", overrelief="ridge")
b_deletar.place(x=205, y=340)

# Frame Tree
def mostrar():
    lista = mostrar_info()

    # Lista para cabeçalho
    tabela_head = ["Id", "Nome", "Email", "Telefone", "Data", "Estado", "Sobre"]

    # Criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # Vertical Scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # Horizontal Scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h=[30, 170, 140, 100, 120, 50, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in lista:
        tree.insert("", "end", values=item)

# Chamando a função "mostrar"
mostrar()

# Visualizar a janela
janela.mainloop()