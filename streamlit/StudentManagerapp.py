import streamlit as st
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    .card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .card-title {
        color: #64748b;
        font-size: 0.9rem;
    }

    .card-value {
        color: #0f172a;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 0.3rem;
    }

    .grade-a {
        color: #16a34a;
        font-weight: 700;
    }

    .grade-b {
        color: #2563eb;
        font-weight: 700;
    }

    .grade-c {
        color: #d97706;
        font-weight: 700;
    }

    .grade-d {
        color: #ea580c;
        font-weight: 700;
    }

    .grade-f {
        color: #dc2626;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Grade Calculation
# -----------------------------
def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


def get_status(mark):
    return "Pass" if mark >= 50 else "Fail"


# -----------------------------
# Session State
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">🎓 Student Grade Manager</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Manage student marks, grades and performance in one place.</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Add Student Section
# -----------------------------
st.subheader("Add Student")

with st.form("student_form", clear_on_submit=True):

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

    with col2:
        roll_number = st.text_input(
            "Roll Number",
            placeholder="e.g. STU001"
        )

    with col3:
        mark = st.number_input(
            "Mark",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    submitted = st.form_submit_button(
        "➕ Add Student",
        use_container_width=True
    )

    if submitted:

        if not name.strip():
            st.error("Please enter the student name.")

        elif not roll_number.strip():
            st.error("Please enter the roll number.")

        elif any(
            student["Roll Number"].lower() == roll_number.strip().lower()
            for student in st.session_state.students
        ):
            st.error("Roll number already exists.")

        else:

            grade = calculate_grade(mark)
            status = get_status(mark)

            student = {
                "Roll Number": roll_number.strip(),
                "Student Name": name.strip(),
                "Mark": mark,
                "Grade": grade,
                "Status": status
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


# -----------------------------
# Statistics
# -----------------------------
students = st.session_state.students

total_students = len(students)

if total_students > 0:

    marks = [student["Mark"] for student in students]

    average_mark = sum(marks) / total_students
    highest_mark = max(marks)
    lowest_mark = min(marks)

    pass_count = sum(
        1 for student in students
        if student["Status"] == "Pass"
    )

    fail_count = total_students - pass_count

else:

    average_mark = 0
    highest_mark = 0
    lowest_mark = 0
    pass_count = 0
    fail_count = 0


st.markdown("---")

st.subheader("Performance Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">Total Students</div>
            <div class="card-value">{total_students}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">Average Mark</div>
            <div class="card-value">{average_mark:.1f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">Highest Mark</div>
            <div class="card-value">{highest_mark}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">Passed</div>
            <div class="card-value">{pass_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">Failed</div>
            <div class="card-value">{fail_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Student Table
# -----------------------------
st.markdown("---")

st.subheader("Student Records")

if students:

    df = pd.DataFrame(students)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Roll Number": st.column_config.TextColumn(
                "Roll Number"
            ),
            "Student Name": st.column_config.TextColumn(
                "Student Name"
            ),
            "Mark": st.column_config.NumberColumn(
                "Mark",
                format="%d"
            ),
            "Grade": st.column_config.TextColumn(
                "Grade"
            ),
            "Status": st.column_config.TextColumn(
                "Status"
            )
        }
    )

else:

    st.info(
        "No student records yet. Add your first student above."
    )


# -----------------------------
# Grade Distribution
# -----------------------------
if students:

    st.markdown("---")

    st.subheader("Grade Distribution")

    grade_counts = (
        pd.DataFrame(students)["Grade"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(grade_counts)


# -----------------------------
# Clear Data
# -----------------------------
if students:

    st.markdown("---")

    if st.button("🗑️ Clear All Students"):

        st.session_state.students = []

        st.rerun()