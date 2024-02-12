import streamlit as st

# Definir las categorías y conversiones disponibles
categorias = {
    "Conversiones de temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius",
                                    "Celsius a Kelvin", "Kelvin a Celsius"],
    "Conversiones de longitud": ["Pies a metros", "Metros a pies",
                                 "Pulgadas a centímetros", "Centímetros a pulgadas"],
    "Conversiones de peso/masa": ["Libras a kilogramos", "Kilogramos a libras",
                                  "Onzas a gramos", "Gramos a onzas"],
    "Conversiones de volumen": ["Galones a litros", "Litros a galones",
                                "Pulgadas cúbicas a centímetros cúbicos",
                                "Centímetros cúbicos a pulgadas cúbicas"],
    "Conversiones de tiempo": ["Horas a minutos", "Minutos a segundos",
                               "Días a horas", "Semanas a días"],
    "Conversiones de velocidad": ["Millas por hora a kilómetros por hora",
                                  "Kilómetros por hora a metros por segundo",
                                  "Nudos a millas por hora",
                                  "Metros por segundo a pies por segundo"],
    "Conversiones de área": ["Metros cuadrados a pies cuadrados",
                             "Pies cuadrados a metros cuadrados",
                             "Kilómetros cuadrados a millas cuadradas",
                             "Millas cuadradas a kilómetros cuadrados"],
    "Conversiones de energía": ["Julios a calorías", "Calorías a kilojulios",
                                "Kilovatios-hora a megajulios",
                                "Megajulios a kilovatios-hora"],
    "Conversiones de presión": ["Pascales a atmósferas", "Atmósferas a pascales",
                                "Barras a libras por pulgada cuadrada",
                                "Libras por pulgada cuadrada a bares"],
    "Conversiones de tamaño de datos": ["Megabytes a gigabytes", "Gigabytes a terabytes",
                                         "Kilobytes a megabytes", "Terabytes a petabytes"]
}

# Título y descripción
st.title("Conversor Universal")
st.write("Esta aplicación le permite realizar conversiones en diferentes categorías.")

# Selección de categoría y conversión
categoria_seleccionada = st.selectbox("Seleccione una categoría", list(categorias.keys()))
conversion_seleccionada = st.selectbox("Seleccione una conversión", categorias[categoria_seleccionada])

# Entrada del valor a convertir
valor_a_convertir = st.number_input("Ingrese el valor a convertir")

# Realizar la conversión
if st.button("Convertir"):

    # Temperatura
    if conversion_seleccionada == "Celsius a Fahrenheit":
        resultado = (valor_a_convertir * 9/5) + 32
    elif conversion_seleccionada == "Fahrenheit a Celsius":
        resultado = (valor_a_convertir - 32) * 5/9
    elif conversion_seleccionada == "Celsius a Kelvin":
        resultado = valor_a_convertir + 273.15
    elif conversion_seleccionada == "Kelvin a Celsius":
        resultado = valor_a_convertir - 273.15
    
    # Longitud
    elif conversion_seleccionada == "Pies a metros":
        resultado = valor_a_convertir * 0.3048
    elif conversion_seleccionada == "Metros a pies":
        resultado = valor_a_convertir / 0.3048
    elif conversion_seleccionada == "Pulgadas a centímetros":
        resultado = valor_a_convertir * 2.54
    elif conversion_seleccionada == "Centímetros a pulgadas":
        resultado = valor_a_convertir / 2.54

    # Peso/masa
    elif conversion_seleccionada == "Libras a kilogramos":
        resultado = valor_a_convertir * 0.453592
    elif conversion_seleccionada == "Kilogramos a libras":
        resultado = valor_a_convertir / 0.453592
    elif conversion_seleccionada == "Onzas a gramos":
        resultado = valor_a_convertir * 28.3495
    elif conversion_seleccionada == "Gramos a onzas":
        resultado = valor_a_convertir / 28.3495

    # Volumen
    elif conversion_seleccionada == "Galones a litros":
        resultado = valor_a_convertir * 3.78541
    elif conversion_seleccionada == "Litros a galones":
        resultado = valor_a_convertir / 3.78541
    elif conversion_seleccionada == "Pulgadas cúbicas a centímetros cúbicos":
        resultado = valor_a_convertir * 16.3871
    elif conversion_seleccionada == "Centímetros cúbicos a pulgadas cúbicas":
        resultado = valor_a_convertir / 16.3871

    # Tiempo
    elif conversion_seleccionada == "Horas a minutos":
        resultado = valor_a_convertir * 60
    elif conversion_seleccionada == "Minutos a segundos":
        resultado = valor_a_convertir * 60
    elif conversion_seleccionada == "Días a horas":
        resultado = valor_a_convertir * 24
    elif conversion_seleccionada == "Semanas a días":
        resultado = valor_a_convertir * 7

    
    st.write(f"El resultado de la conversión es: {resultado}")
