# Importando o SQLite
import sqlite3 as lite

# Criando a conexão
con = lite.connect('dados.db')

# Inserir informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, data, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Acessar informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
           lista.append(i)
    
    return lista

# Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, data=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)

# Deletar informações
def deletar_info(i):    
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)