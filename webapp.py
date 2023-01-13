import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    this_todo = st.session_state['new_todo'] + "\n"
    todos.append(this_todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("Todo App")
st.subheader("This is a basic Todo app")
st.write("This app is to increase productivity")

st.text_input(
    label="Enter a Todo:", placeholder="Add new todo...",
    on_change=add_todo, key="new_todo"
)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
