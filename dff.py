import streamlit as st
from data_upload_function import preview_data
from dff_function import get_gorwth_label


def dff():
    st.subheader("DFF")

    tab2_labels = [
        "gorwth label",
        "classification",
        "regression",
    ]
    tab2_1, tab2_2, tab2_3 = st.tabs(tab2_labels)

    with tab2_1:
        pheno_df = st.session_state["pheno_df"]
        
        gorwth_label = None
        if "gorwth_label" not in st.session_state:
            gorwth_label = get_gorwth_label(pheno_df)
            if gorwth_label is not None:
                st.session_state["gorwth_label"] = gorwth_label
        if "gorwth_label" in st.session_state:
            preview_data(st.session_state["gorwth_label"], form_key="preview_gorwth_label_form", expander_label="Preview Growth Label")
        else:
            preview_data(gorwth_label, form_key="preview_gorwth_label_form", expander_label="Preview Growth Label")

    with tab2_2:
        pass

    with tab2_3:
        pass