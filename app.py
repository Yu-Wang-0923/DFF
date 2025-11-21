import streamlit as st
from dff_page_config import page_config
from data_upload import data_upload
from model_selection import model_selection

page_config()

tab_labels = [
    "Data Upload",
    "Model Selection",
    "Result Visualization",
]
tab1, tab2, tab3 = st.tabs(tab_labels)

# Data Upload
with tab1:
    data_upload()
    
# Model Selection
with tab2:
    model_selection()

# Result Visualization
with tab3:
    pass




    

