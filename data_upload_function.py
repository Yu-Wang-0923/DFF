import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_file(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            return None
        if len(df.columns) > 0:
            df = df.set_index(df.columns[0])
        return df
    return None


def preview_data(df, form_key=None, expander_label="Preview Data"):
    if df is not None:
        with st.expander(expander_label, expanded=False):
            st.write(f"**data shape:** {df.shape[0]} rows × {df.shape[1]} columns")
            # Ensure a unique form key for each form instance
            key = form_key or f"preview_form_{id(df)}_{hash(str(df.shape))}"
            with st.form(key=key):
                col1, col2 = st.columns(2)
                btn_5 = col1.form_submit_button("Show first 5 rows")
                btn_all = col2.form_submit_button("Show all data")
                if btn_all:
                    st.dataframe(df)
                elif btn_5:
                    st.write(df.head(5))
                # 当未点击按钮时不显示数据


def plot_pheno_data(df, form_key=None, expander_label="Show Phenotype Data Plot Options"):
    # Ensure a unique form key for each form instance
    key = form_key or f"plot_pheno_data_form_{str(hash(df.values.tobytes()))}"
    with st.expander(expander_label, expanded=False):
        with st.form(key=key):
            submit = st.form_submit_button("plot phenotype data")
            if submit:
                time_points = df.columns.astype(float)
                fig, axes = plt.subplots(9, 11, figsize=(25, 15), sharex=True, sharey=True, dpi=300)
                fig.subplots_adjust(wspace=0, hspace=0)  # 子图间距为0
                axes = axes.flatten()
                for i, (idx, row) in enumerate(df.iterrows()):
                    axes[i].scatter(time_points, row.values, marker='o', s=12, label=idx, c = 'black')
                    axes[i].tick_params(axis='both', which='major', labelsize=8)
                    axes[i].set_ylim(-0.25, 2.55)
                    axes[i].set_yticks([0.0, 1.0, 2.0])
                    axes[i].legend(loc='upper center', frameon=False, markerscale=0, handlelength=0, fontsize=10)  # 图例
                st.pyplot(fig)