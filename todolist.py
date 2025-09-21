import streamlit as st

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List")

# Input to add a task
new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.success(f"Added task: {new_task}")
    else:
        st.warning("Task cannot be empty")

# Display tasks and handle deletion
st.subheader("Your Tasks")
delete_index = None
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {task}")
    if col2.button("Delete", key=f"del_{i}"):
        delete_index = i

# Remove the task after the loop
if delete_index is not None:
    st.session_state.tasks.pop(delete_index)
    st.rerun()  # ✅ use st.rerun instead of st.experimental_rerun
