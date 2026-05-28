import streamlit as st
import os

FILE = "task.txt"

if not os.path.exists(FILE):
    open(FILE, "w").close()

def get_todos():
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def write_todos(tasks):
    with open(FILE, "w") as f:
        f.writelines([task + "\n" for task in tasks])

st.title("My to-do app")
st.subheader("This is my todo app")
st.text("This app is to increase your productivity.")
# Load and display
old_todos = get_todos()
st.write("Current todos:")
todos = [i.strip() for i in old_todos]
def add_todo():
    todo = st.session_state["new_todo"]
    if todo != "":
        todos.append(todo)
        write_todos(todos)
        st.session_state["new_todo"] = ""

for index , i  in enumerate(todos):
    if st.checkbox(i , key=f"{i}_{index}"):
        todos.remove(i)
        write_todos(todos)
        st.rerun()

    # Input field to add new todos
new_todo = st.text_input("Enter a todo" , placeholder="Enter a new todo" , on_change= add_todo,key="new_todo")
# if st.button("Add Task"):
#     current_todos = get_todos()
#     current_todos.append(new_todo)
#     write(current_todos)
#     st.rerun() # Refresh to show the new item


