import streamlit as st

def main():
    st.set_page_config(page_title="To-Do List", layout="centered")

    st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }

    .container {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: 300px;
    }

    h1 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }

    .input-container {
        display: flex;
        margin-bottom: 10px;
    }

    input[type="text"] {
        flex: 1;
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px 0 0 4px;
        font-size: 14px;
    }

    button {
        padding: 8px 12px;
        border: none;
        background-color: #4CAF50;
        color: white;
        border-radius: 0 4px 4px 0;
        cursor: pointer;
        font-size: 14px;
    }

    button:hover {
        background-color: #45a049;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        padding: 10px;
        background-color: #f9f9f9;
        border-bottom: 1px solid #ddd;
        cursor: pointer;
    }

    li:last-child {
        border-bottom: none;
    }

    li:hover {
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>To-Do List</h1>", unsafe_allow_html=True)

    task_input = st.text_input("Add a new task:")
    if st.button("Add"):
        if task_input.strip() != "":
            st.session_state.tasks.append(task_input.strip())

    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    for task in st.session_state.tasks:
        if st.button(f"Delete {task}"):
            st.session_state.tasks.remove(task)

    st.markdown("<ul>", unsafe_allow_html=True)
    for task in st.session_state.tasks:
        st.markdown(f"<li>{task}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
