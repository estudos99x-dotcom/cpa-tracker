import sqlite3
from datetime import datetime


conn = sqlite3.connect("banco.db", check_same_thread=False)

cursor = conn.cursor()


def criar_tabela():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        casa TEXT,
        cpa REAL,
        lucro REAL,
        prejuizo REAL,
        resultado REAL,
        data TEXT,
        hora TEXT
    )
    """)

    conn.commit()



def salvar(casa,cpa,lucro,prejuizo,resultado):

    agora = datetime.now()

    cursor.execute("""
    INSERT INTO registros
    (
    casa,
    cpa,
    lucro,
    prejuizo,
    resultado,
    data,
    hora
    )

    VALUES (?,?,?,?,?,?,?)

    """,
    (
    casa,
    cpa,
    lucro,
    prejuizo,
    resultado,
    agora.strftime("%d/%m/%Y"),
    agora.strftime("%H:%M")
    ))

    conn.commit()



def pegar_registros():

    cursor.execute("""
    SELECT *
    FROM registros
    ORDER BY id DESC
    """)

    return cursor.fetchall()