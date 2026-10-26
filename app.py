
import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾")
st.title("🐾 PawPal+")
st.write("Create a daily care schedule for your pet.")

owner_name = st.text_input("Owner name", "Jordan")
pet_name = st.text_input("Pet name", "Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.subheader("Add Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task_title = st.text_input("Task title", "Morning walk")
task_time = st.time_input("Task time")
duration = st.number_input("Duration (minutes)", 1, 240, 20)
priority = st.selectbox("Priority", ["low", "medium", "high"])

if st.button("Add Task"):
    st.session_state.tasks.append({
        "title": task_title,
        "time": task_time.strftime("%H:%M"),
        "duration": duration,
        "priority": priority
    })
    st.success("Task added!")

if st.session_state.tasks:
    st.table(st.session_state.tasks)

st.subheader("Daily Schedule")

if st.button("Generate Schedule"):
    owner = Owner(owner_name)
    pet = Pet(pet_name, species, 1)

    for item in st.session_state.tasks:
        task = Task(item["title"], item["time"])
        pet.add_task(task)

    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    st.write("### Your Schedule")

    for name, task in scheduler.sort_by_time():
        st.write(f"{task.time} - {name}: {task.description}")

    if scheduler.detect_conflicts():
        st.warning("Some tasks are scheduled at the same time!")
    else:
        st.success("No scheduling conflicts detected.")
