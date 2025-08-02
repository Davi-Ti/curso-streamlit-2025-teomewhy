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
file_upload = st.file_uploader(label="Faça upload dos dados aqui", type=["csv", "xlsx"])

# Verifica se algum arquivo foi feito upload
if file_upload:
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"]).dt.date

    columns_fmt = {
        "Valor": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
        "Data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
    }
    st.dataframe(df, hide_index=True, column_config=columns_fmt)

    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")
    st.dataframe(df_instituicao, column_config=columns_fmt)
