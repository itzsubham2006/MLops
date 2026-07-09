import streamlit as st

st.title('Calculator')
st.write("Enter a number to calculate its square")

n = st.number_input('Enter a integer', value=1, step=1)

square = n**2

st.write(f'The square of the {n} is {square}.')