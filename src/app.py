import streamlit as st

st.title("Suma tres numeros")

st.write("## Usando `number_input`")

numero1 = st.number_input("Introduce un numero: ", step=1)
numero2 = st.number_input("Introduce el siguiente numero: ", step=1)
numero3 = st.number_input("Introduce el ultimo numero de la suma: ", step=1)


suma = numero1 + numero2 + numero3

if suma:
    st.write("La suma de los tres numero es ", suma)


st.divider()

st.write("## Usando `st.slider`")

p1 = st.slider("Introduce un numero: ", step=1)
p2 = st.slider("Introduce el siguiente numero: ", step=1)
p3 = st.slider("Introduce el ultimo numero de la suma: ", step=1)

suma_p = p1 + p2 + p3

if suma_p:
    st.write("El numero es ", suma_p)