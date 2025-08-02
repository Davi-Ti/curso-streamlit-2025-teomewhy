import streamlit as st
import pandas as pd

st.set_page_config(page_icon="💸", page_title="Finanças")

st.markdown(
    """
# Boas Vindas!
## Nosso APP Financeiro!
Espero que você curta a experiência da nossa solução para organização financeira
"""
)

# Widget de upload de arquivo
file_upload = st.file_uploader(label="Faça upload dos dados aqui", type=["csv"])

# Verifica se o arquivo foi carregado
if file_upload:

    # Leitura do Dados
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date

    # Exibir os dados
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {"Valor": st.column_config.NumberColumn("Valor", format="R$ %.2f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)

    # Visao Instituições
    exp2 = st.expander("Instituições")
    df_instituicao = df.pivot_table(
        index="Data", columns="Instituição", values="Valor", aggfunc="sum"
    )
    df_instituicao = df_instituicao.sort_index()

    columns_fmt2 = {
        col: st.column_config.NumberColumn(label=col, format="R$ %.2f")
        for col in df_instituicao.columns
    }

    exp2.dataframe(df_instituicao, column_config=columns_fmt2)
    exp2.line_chart(df_instituicao)
