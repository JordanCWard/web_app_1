import streamlit as st
import functions

# need to put this at the top so that it can be used in the function
list_of_todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    list_of_todos.append(new_todo)
    functions.write_todos(list_of_todos)


st.title("Title")
st.subheader("Sub header")
st.write("This is some more text.")

# create a list of checkboxes and remove the item once it is checked
for index, todo in enumerate(list_of_todos):
    checkbox_state = st.checkbox(todo, key=todo)
    if checkbox_state:
        list_of_todos.pop(index)
        functions.write_todos(list_of_todos)
        del st.session_state[todo]
        st.rerun()

# input box
st.text_input(label="Enter a todo: ",
              placeholder="Add new todo",
              on_change=add_todo,
              key='new_todo')

# used for testing
"""
print("Hello")
st.session_state
"""
