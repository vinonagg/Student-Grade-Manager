import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

.title{
    text-align:center;
    color:#1E3A8A;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:20px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:45px;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------

st.markdown("<p class='title'>🎓 Student Grade Manager</p>",
            unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Built using Python & Streamlit</p>",
            unsafe_allow_html=True)

st.write("")

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.image("https://img.icons8.com/color/96/student-center.png", width=90)

st.sidebar.title("Student Information")

name = st.sidebar.text_input("Student Name")

roll = st.sidebar.text_input("Roll Number")

department = st.sidebar.selectbox(
    "Department",
    ["Computer Science",
     "Information Technology",
     "Mechanical",
     "Civil",
     "Electronics"]
)

# ----------------------------
# Marks
# ----------------------------

st.header("📚 Enter Subject Marks")

col1, col2 = st.columns(2)

with col1:

    english = st.number_input("English",0,100)

    maths = st.number_input("Mathematics",0,100)

    science = st.number_input("Science",0,100)

with col2:

    social = st.number_input("Social",0,100)

    computer = st.number_input("Computer",0,100)

# ----------------------------
# Calculate
# ----------------------------

if st.button("Calculate Result"):

    total = english + maths + science + social + computer

    percentage = total / 5

    if percentage >=90:
        grade="A+"

    elif percentage >=80:
        grade="A"

    elif percentage >=70:
        grade="B"

    elif percentage >=60:
        grade="C"

    elif percentage >=50:
        grade="D"

    else:
        grade="Fail"

    st.success("Result Generated Successfully")

    st.write("")

    c1,c2,c3=st.columns(3)

    c1.metric("Total Marks",total)

    c2.metric("Percentage",f"{percentage:.2f}%")

    c3.metric("Grade",grade)

    st.write("")

    df=pd.DataFrame({

        "Student Name":[name],

        "Roll Number":[roll],

        "Department":[department],

        "English":[english],

        "Mathematics":[maths],

        "Science":[science],

        "Social":[social],

        "Computer":[computer],

        "Total":[total],

        "Percentage":[round(percentage,2)],

        "Grade":[grade]

    })

    st.subheader("📋 Student Report Card")

    st.dataframe(df,use_container_width=True)

    csv=df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "⬇ Download Report",
        csv,
        "Student_Report.csv",
        "text/csv"
    )

st.write("")
st.write("---")
st.caption("© 2026 Student Grade Manager | Built with ❤️ using Python & Streamlit")