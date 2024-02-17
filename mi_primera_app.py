import streamlit as st

# Título y autor
st.title("Mi app")
st.write("Esta app fue elaborada por Juan José Echavarria Araque.")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")
peso_usuario = st.text_input("Por favor, ingresa tu peso en kg")

# Imprimir mensaje de bienvenida
if nombre_usuario and peso_usuario:
    st.write(f"hola {peso_usuario} kg, tu peso es {nombre_usuario}.")
