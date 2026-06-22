import streamlit as st

from casas import CASAS
from database import (
    criar_tabela,
    salvar,
    pegar_registros
)


criar_tabela()


st.set_page_config(
    page_title="CPA Tracker",
    layout="wide"
)


st.title("📊 CPA TRACKER")


# -------------------

st.sidebar.header("Adicionar")


casa = st.sidebar.selectbox(
    "Casa",
    CASAS.keys()
)


cpa = CASAS[casa]


st.sidebar.success(
    f"CPA automático: R$ {cpa}"
)


tipo = st.sidebar.radio(
    "Resultado",
    [
        "Lucro",
        "Prejuízo"
    ]
)


valor = st.sidebar.number_input(
    "Valor",
    min_value=0.0
)



if st.sidebar.button("Salvar"):

    lucro = 0
    prejuizo = 0


    if tipo == "Lucro":
        lucro = valor

    else:
        prejuizo = valor


    resultado = (
        cpa
        +
        lucro
        -
        prejuizo
    )


    salvar(
        casa,
        cpa,
        lucro,
        prejuizo,
        resultado
    )


    st.sidebar.success(
        "Salvo!"
    )



# -------------------

dados = pegar_registros()



total_cpa = sum(
    x[2] for x in dados
)


total_lucro = sum(
    x[3] for x in dados
)


total_prejuizo = sum(
    x[4] for x in dados
)


saldo = sum(
    x[5] for x in dados
)



col1,col2,col3,col4 = st.columns(4)


col1.metric(
    "CPA",
    f"R$ {total_cpa}"
)


col2.metric(
    "Lucros",
    f"R$ {total_lucro}"
)


col3.metric(
    "Prejuízos",
    f"R$ {total_prejuizo}"
)


col4.metric(
    "Saldo",
    f"R$ {saldo}"
)



st.divider()


st.subheader(
    "Histórico"
)


for item in dados:


    st.write(
f"""
### {item[1]}

💰 CPA: R$ {item[2]}

📈 Lucro: R$ {item[3]}

📉 Prejuízo: R$ {item[4]}

🔥 Resultado:
**R$ {item[5]}**

📅 {item[6]} - {item[7]}

---
"""
)