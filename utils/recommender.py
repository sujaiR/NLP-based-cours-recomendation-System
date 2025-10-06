def recommend_courses(course_name, courses, cosine_sim):
    """Recommend top 5 similar courses based on cosine similarity."""
    if course_name not in courses['course_title'].values:
        return ["Course not found"]

    idx = courses[courses['course_title'] == course_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 recommendations

    recommended_courses = [
        (
            courses.iloc[i[0]]['course_title'],
            courses.iloc[i[0]]['url'],
            courses.iloc[i[0]]['content_duration']
        )
        for i in sim_scores
    ]
    return recommended_courses
