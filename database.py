import sqlite3
ligação=sqlite3.connect("despesas.db")
cursor=ligação.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS despesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT,
        valor REAL,
        data TEXT,
        estabelecimento TEXT,
        descricao TEXT
    )
""")
ligação.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#print(cursor.fetchall())
cursor.execute(""" insert into despesas
(categoria,valor,data,estabelecimento,descricao)
values("Alimentação",25.50,"6/10/2026","continente","almoço")""")
ligação.commit()
cursor.execute("select * from despesas ")
print(cursor.fetchall())
