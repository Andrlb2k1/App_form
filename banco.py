# Importando o SQLite
import sqlite3 as lite

# Criando a conexão
con = lite.connect('dados.db')

# Criando a tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, data DATE, estado TEXT, assunto TEXT)")