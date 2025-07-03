import streamlit as st

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌤️ Weather Dashboard")

# Métricas principales
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="TEMPERATURE", value="70 °F", delta="+1.2 °F")

with col2:
    st.metric(label="WIND", value="9 mph", delta="-8%", delta_color="inverse")

with col3:
    st.metric(label="HUMIDITY", value="86%", delta="+4%")
