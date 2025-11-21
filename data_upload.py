import streamlit as st
from data_upload_function import load_file, preview_data


def data_upload():
    st.subheader("Upload Your Data")
    with st.expander("Data Format Specification"):
        st.markdown(
            """
            - **Phenotype Data:** 
            - **Genotype Data:** 
            - **Environmental Data:** 
            """
        )
    
    tab1_labels = [
        "File Upload",
        "Phenotype Data",
        "Genotype Data",
        "Environmental Data",
    ]
    tab1_1, tab1_2, tab1_3, tab1_4 = st.tabs(tab1_labels)
    with tab1_1:
        st.markdown(
            """
            Please upload the following three types of data:
            """
        )
        pheno_file = st.file_uploader("Phenotype Data", type=["csv", "xlsx"])
        geno_file = st.file_uploader("Genotype Data", type=["csv", "xlsx"])
        env_file = st.file_uploader("Environmental Data", type=["csv", "xlsx"])
        pheno_df = load_file(pheno_file)
        geno_df = load_file(geno_file)
        env_df = load_file(env_file)
    with tab1_2:
        preview_data(pheno_df)
    with tab1_3:
        preview_data(geno_df)
    with tab1_4:
        preview_data(env_df)

