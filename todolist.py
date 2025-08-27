import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List")

new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.success(f"Added task: {new_task}")
    else:
        st.warning("Task cannot be empty")

st.subheader("Your Tasks")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {task}")
    if col2.button("Delete", key=i):
        st.session_state.tasks.pop(i)
        st.experimental_rerun()
