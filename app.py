import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt

# Function to set background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    page_bg = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)

# Set background using uploaded image
set_background("image.png")

# Load course data
@st.cache_data
def load_data():
    courses = pd.read_csv("udemy_courses.csv")  # Ensure the correct local path
    return courses

# Load cosine similarity matrix
@st.cache_data
def load_similarity():
    return np.load("cosine_sim.npy")  # Adjust path if needed

# Recommend courses
def recommend_courses(course_name, courses, cosine_sim):
    if course_name not in courses['course_title'].values:
        return ["Course not found"]
    
    idx = courses[courses['course_title'] == course_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 recommendations
    
    recommended_courses = [(courses.iloc[i[0]]['course_title'], 
                            courses.iloc[i[0]]['url'], 
                            courses.iloc[i[0]]['content_duration']) for i in sim_scores]
    return recommended_courses

# Load data
courses = load_data()
cosine_sim = load_similarity()

# Streamlit UI
st.title("Course Recommendation System Dashboard")

# Dashboard Section
st.sidebar.title("Dashboard")
st.sidebar.subheader("Course Data Overview")
st.sidebar.write("Total Courses:", len(courses))
st.sidebar.write("Unique Subjects:", courses['subject'].nunique())

# Visualization: Number of Courses per Subject
st.sidebar.subheader("Courses per Subject")
subject_counts = courses['subject'].value_counts()
fig, ax = plt.subplots()
ax.bar(subject_counts.index, subject_counts.values, color=['blue', 'green', 'red', 'orange'])
plt.xticks(rotation=45)
st.sidebar.pyplot(fig)

# Course selection
st.subheader("Find Recommended Courses")
selected_course = st.selectbox("Select a Course", courses['course_title'].values)

if st.button("Recommend"):
    recommendations = recommend_courses(selected_course, courses, cosine_sim)
    st.write("### Recommended Courses:")
    for rec, link, duration in recommendations:
        st.markdown(f"- [{rec}]({link}) - ⏳ Duration: {duration} hours")
