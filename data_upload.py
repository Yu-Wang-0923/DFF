import streamlit as st
from data_upload_function import load_file, preview_data, plot_pheno_data


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
        # 缓存数据 如果数据不为空，则缓存
        if pheno_df is not None:
            st.session_state["pheno_df"] = pheno_df
        if geno_df is not None:
            st.session_state["geno_df"] = geno_df
        if env_df is not None:
            st.session_state["env_df"] = env_df
    with tab1_2:
        preview_data(pheno_df, form_key="preview_pheno_form")
        if pheno_df is not None:
            plot_pheno_data(pheno_df.iloc[0:99, :], form_key="first_env_form", expander_label="Phenotype Data - Environment 1")
            plot_pheno_data(pheno_df.iloc[99:198, :], form_key="second_env_form", expander_label="Phenotype Data - Environment 2")
            plot_pheno_data(pheno_df.iloc[198:297, :], form_key="third_env_form", expander_label="Phenotype Data - Environment 3")
            plot_pheno_data(pheno_df.iloc[297:396, :], form_key="fourth_env_form", expander_label="Phenotype Data - Environment 4")
    with tab1_3:
        preview_data(geno_df, form_key="preview_geno_form")
    with tab1_4:
        preview_data(env_df, form_key="preview_env_form")

