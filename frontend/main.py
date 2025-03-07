import streamlit as st
import requests

# Configuración básica
st.set_page_config(page_title="Profesor Virtual", layout="centered")

# Título de la app
st.title("🧠 Profesor Virtual")

# Descripción
st.markdown("Bienvenido a tu profesor virtual personalizado. Escribe tu pregunta y recibirás una explicación adaptada.")

# Entrada del usuario
question = st.text_area("✏️ Escribe tu pregunta aquí:")

# Enviar la pregunta
if st.button("Obtener Respuesta"):
    if question.strip():  # Evita enviar texto vacío
        with st.spinner("Pensando..."):
            try:
                # Petición al backend
                response = requests.post(
                    "http://localhost:8000/ask",  # Endpoint del backend
                    json={"question": question}
                )

                if response.status_code == 200:
                    answer = response.json().get("answer", "No se encontró respuesta.")
                    st.success("✅ Respuesta:")
                    st.write(answer)
                else:
                    st.error(f"❌ Error en la solicitud: {response.status_code}")
            except Exception as e:
                st.error(f"❌ Error de conexión con el backend: {e}")
    else:
        st.warning("⚠️ Por favor, escribe una pregunta antes de continuar.")
