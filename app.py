import streamlit as st
from pawpal_system import Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# Initialize session state for tasks and pet
if "pet" not in st.session_state:
    st.session_state.pet = None
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# Create a Pet instance
if st.button("Add Pet"):
    st.session_state.pet = Pet(name=pet_name, age=0, breed=species)
    st.success(f"Pet '{pet_name}' added!")

st.markdown("### Tasks")
st.caption("Add a few tasks. These will feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

# Add tasks to the pet
if st.button("Add Task"):
    if st.session_state.pet:
        task = Task(description=task_title, time=None, frequency="once", priority=priority)
        st.session_state.pet.add_task(task)
        st.session_state.tasks.append(task)
        st.success(f"Task '{task_title}' added to {st.session_state.pet.name}!")
    else:
        st.error("Please add a pet first.")

# Display current tasks
if st.session_state.tasks:
    st.write("Current tasks:")
    st.table([{"Title": t.description, "Priority": t.priority} for t in st.session_state.tasks])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button calls your scheduling logic.")

# Generate schedule using the Scheduler class
if st.button("Generate Schedule"):
    if st.session_state.pet:
        scheduler = Scheduler()
        schedule = scheduler.build_schedule(st.session_state.pet.tasks)
        st.write("Generated Schedule:")
        st.table(schedule)
    else:
        st.error("Please add a pet and tasks first.")