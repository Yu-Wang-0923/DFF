import streamlit as st


def page_config():
    """配置页面并显示标题"""
    st.set_page_config(
        page_title="DFF", 
        page_icon=":brain:", 
        layout="centered",
    )

    # 使用HTML在Streamlit中实现剧中和换字体颜色，DFF三个字母是大号蓝色
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 10px;">
            <span style="color:#1576FA; font-size:40px; font-weight:900; letter-spacing:2px;">DFF_v0.1</span>
            <span style="color:#666666; font-size:18px; font-weight:600; margin-top:2px;">Deep Functional-mapping Framework</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        """
        For Predicting Dynamic Phenotypes and Gene–Environment Plasticity
        """
    )

