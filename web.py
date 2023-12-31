import streamlit as st
from functions import get_todos, write_todos


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    st.session_state["new_todo"] = ""


todos = get_todos("todos.txt")

st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state