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

file_upload = st.file_uploader(label="Faça upload dos dados aqui", type=["csv", "xlsx"])
if file_upload:
    df = pd.read_csv(file_upload)
    st.dataframe(df)
