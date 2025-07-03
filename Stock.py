import streamlit as st

# Configuración de página
st.set_page_config(page_title="Tarjetas tipo métrica", layout="wide")

st.markdown("""
    <style>
        .card {
            background-color: #fff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
            margin: 0.5rem;
        }
        .label {
            font-size: 14px;
            color: #36a2cc;
            font-weight: bold;
        }
        .value {
            font-size: 32px;
            margin: 0.2rem 0;
        }
        .delta-up {
            color: green;
        }
        .delta-down {
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌤️ Dashboard con tarjetas visuales")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <div class="label">TEMPERATURE</div>
            <div class="value">70 °F</div>
            <div class="delta-up">↑ 1.2 °F</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <div class="label">WIND</div>
            <div class="value">9 mph</div>
            <div class="delta-down">↓ 8%</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <div class="label">HUMIDITY</div>
            <div class="value">86%</div>
            <div class="delta-up">↑ 4%</div>
        </div>
    """, unsafe_allow_html=True)
