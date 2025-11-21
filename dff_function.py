import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def get_gorwth_label(df, threshold=0.5):
    with st.form(key="growth_label_form"):
        st.write("Set threshold for growth labeling:")
        threshold = st.number_input("Threshold", min_value=0.0, max_value=10.0, value=float(threshold), step=0.01)
        submit = st.form_submit_button("Generate Growth Label")
        if submit:
            df_label = pd.DataFrame((df.ge(threshold).any(axis=1)).astype(int), columns=["grow_label"])
            grow_count = df_label['grow_label'].sum()
            nongrow_count = len(df_label) - grow_count

            col1, col2 = st.columns([2, 1])  # UI并列：左侧信息，右侧饼图

            with col1:
                st.write(f"Total growth count: {grow_count}, label is 1")
                st.write(f"Total non-growth count: {nongrow_count}, label is 0")

            with col2:
                fig, ax = plt.subplots(figsize=(1.5, 1.5))
                ax.pie(
                    [grow_count, nongrow_count], 
                    labels=['Growth (1)', 'Non-Growth (0)'], 
                    autopct='%1.1f%%', 
                    colors=['#66b3ff', '#ff9999'],
                    textprops={'fontsize': 6}
                )
                st.pyplot(fig)

            return df_label
