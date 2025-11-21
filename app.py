import streamlit as st
from dff_page_config import page_config
from data_upload import data_upload
from dff import dff

page_config()

tab_labels = [
    "Data Upload",
    "DFF",
    "Result Visualization",
]
tab1, tab2, tab3 = st.tabs(tab_labels)

# Data Upload
with tab1:
    data_upload()
    
# Model Selection
with tab2:
    dff()

# Result Visualization
with tab3:
    pass




    

