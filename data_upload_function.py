import streamlit as st
import pandas as pd


def load_file(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file)
    return None


def preview_data(df):
    if df is not None:
        set_index = st.checkbox(
            """
            Set first column as index
            """,
            value=True,
        )
        if set_index and len(df.columns) > 0:
            df = df.set_index(df.columns[0])
        st.dataframe(df)
        st.write(f"**data shape:** {df.shape[0]} rows ×  {df.shape[1]} columns")
    else:
        st.info("No data uploaded.")

