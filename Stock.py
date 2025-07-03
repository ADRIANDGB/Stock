import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌤️ Weather Monitoring Dashboard")

# Sección de métricas
st.subheader("Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="TEMPERATURE", value="70 °F", delta="+1.2 °F")

with col2:
    st.metric(label="WIND", value="9 mph", delta="-8%", delta_color="inverse")

with col3:
    st.metric(label="HUMIDITY", value="86%", delta="+4%")

# Simulación de datos para heatmap
st.subheader("Heatmap")
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
hours = list(range(24))
data = np.random.rand(len(days), len(hours))

df_heat = pd.DataFrame(data, index=days, columns=hours)

fig_heatmap = px.imshow(
    df_heat,
    labels=dict(x="Hour", y="Day", color="Temperature"),
    x=hours,
    y=days,
    color_continuous_scale="YlGnBu"
)
st.plotly_chart(fig_heatmap, use_container_width=True)

# Donut chart de humedad por sectores
st.subheader("Donut chart")

humidity_sources = pd.DataFrame({
    "Source": ["Evaporation", "Rainfall", "Plants", "Other"],
    "Percent": [35, 30, 25, 10]
})

fig_donut = px.pie(
    humidity_sources,
    values="Percent",
    names="Source",
    hole=0.5,
    title="Sources of Humidity",
    color_discrete_sequence=px.colors.sequential.Blues_r
)
st.plotly_chart(fig_donut, use_container_width=True)
