import streamlit as st
import function

todos=function.gettodos()

st.title("This is my todo app")
st.subheader("below are your todos :")

for todo in todos:
    st.checkbox(todo)

# for index, todo in enumerate(todos):
#     st.checkbox(todo, key=f"todo_{index}")  to avoid the error of duplicate keys

st.text_input(label="",placeholder="enter a new todo")