import streamlit as st
import pandas as pd

st.set_page_config(page_icon="💸", page_title="Finanças")

st.markdown(
    """
# Boas Vindas!
## Nosso APP Financeiro!
Espero que voce curta a experiencia da nossa solução para organização financeira
"""
)

# Widgt de upload de dadso
file_upload = st.file_uploader(label="Faça upload dos dados aqui", type=["csv"])

# Verifica se algum arquivo foi feito upload
if file_upload:
    # Leitura dos dados
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date

    # Exibição dos dados no App
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {
        "Valor": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
        "Data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
    }
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)

    # Visão Instituições
    exp2 = st.expander("Instituições")
    df_instituicao = df.pivot_table(
        index="Data", columns="Instituição", values="Valor", aggfunc="sum"
    )
    df_instituicao = df_instituicao.sort_index()
    # Cria a formatação para todas as colunas com o mesmo padrão
    columns_fmt2 = {
        col: st.column_config.NumberColumn(label=col, format="R$ %.2f")
        for col in df_instituicao.columns
    }
    columns_fmt2["Data"] = st.column_config.DateColumn("Data", format="DD/MM/YYYY")

    exp2.dataframe(df_instituicao, column_config=columns_fmt2)
    exp2.line_chart(df_instituicao)
