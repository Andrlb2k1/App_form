# Importando o SQLite
import sqlite3 as lite

# Criando a conexão
con = lite.connect('dados.db')

# Inserir informações
lista = ["André Luiz Bristot", "andre123@gmail.com", 123456789, "27/03/2026", "Normal", "Gostaria de o consultar pessoalmente"]

with con:
    cur = con.cursor()
    query = "INSERT INTO formulario (nome, email, telefone, data, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
    cur.execute(query, lista)

# Acessar informações
with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"
    cur.execute(query)
    info = cur.fetchall()
    print(info)

# Atualizar informações
lista = ["André Bristot", 1]

with con:
    cur = con.cursor()
    query = "UPDATE formulario SET nome=? WHERE id=?"
    cur.execute(query, lista)

# Deletar informações
lista = [1]

with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query, lista)