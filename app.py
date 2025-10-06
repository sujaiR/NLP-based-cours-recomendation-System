import streamlit as st
import matplotlib.pyplot as plt

# Import custom modules
from utils.background import set_background
from utils.data_loader import load_data, load_similarity
from utils.recommender import recommend_courses

# --- UI Setup ---
set_background("images/image.png")
st.title("🎓 Course Recommendation System Dashboard")

# --- Load Data ---
courses = load_data()
cosine_sim = load_similarity()

# --- Sidebar: Dashboard ---
st.sidebar.title("Dashboard")
st.sidebar.subheader("📊 Course Data Overview")
st.sidebar.write("Total Courses:", len(courses))
st.sidebar.write("Unique Subjects:", courses['subject'].nunique())

# Visualization: Number of Courses per Subject
st.sidebar.subheader("Courses per Subject")
subject_counts = courses['subject'].value_counts()

fig, ax = plt.subplots()
ax.bar(subject_counts.index, subject_counts.values, color=['blue', 'green', 'red', 'orange'])
plt.xticks(rotation=45)
st.sidebar.pyplot(fig)

# --- Main Section: Recommendation ---
st.subheader("🔍 Find Recommended Courses")
selected_course = st.selectbox("Select a Course", courses['course_title'].values)

if st.button("Recommend"):
    recommendations = recommend_courses(selected_course, courses, cosine_sim)
    st.write("### Recommended Courses:")
    for rec, link, duration in recommendations:
        st.markdown(f"- [{rec}]({link}) - ⏳ Duration: {duration} hours")
