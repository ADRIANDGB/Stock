import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuración inicial
st.set_page_config(page_title="Gráficas Interactivas", layout="wide")
st.title("📊 Galería de Gráficas Interactivas con Plotly")

# Datos simulados
np.random.seed(42)
df_line = pd.DataFrame({
    "Día": pd.date_range("2024-01-01", periods=30),
    "Ventas": np.random.randint(100, 500, size=30)
})

df_bar = pd.DataFrame({
    "Producto": ["A", "B", "C", "D"],
    "Ventas": np.random.randint(1000, 3000, size=4)
})

df_pie = pd.DataFrame({
    "Categoría": ["Infraestructura", "Operación", "Mantenimiento", "Otros"],
    "Porcentaje": [35, 25, 20, 20]
})

df_scatter = pd.DataFrame({
    "Horas de uso": np.random.normal(10000, 2500, 100),
    "Probabilidad de falla": np.random.beta(2, 5, 100),
    "Tipo": np.random.choice(["LED", "Sodio", "Halógeno"], 100)
})

# Línea
st.subheader("📈 Línea – Ventas por Día")
fig1 = px.line(df_line, x="Día", y="Ventas", markers=True, title="Tendencia de Ventas")
st.plotly_chart(fig1, use_container_width=True)

# Barras
st.subheader("📊 Barras – Ventas por Producto")
fig2 = px.bar(df_bar, x="Producto", y="Ventas", color="Producto", title="Ventas por Producto", text_auto=True)
st.plotly_chart(fig2, use_container_width=True)

# Pastel
st.subheader("🥧 Pie Chart – Distribución de Costos")
fig3 = px.pie(df_pie, values="Porcentaje", names="Categoría", title="Distribución de Costos", hole=0.4)
st.plotly_chart(fig3, use_container_width=True)

# Dispersión
st.subheader("📌 Dispersión – Horas vs. Probabilidad de Falla")
fig4 = px.scatter(df_scatter, x="Horas de uso", y="Probabilidad de falla", color="Tipo",
                  size="Probabilidad de falla", title="Relación entre Uso y Falla")
st.plotly_chart(fig4, use_container_width=True)
