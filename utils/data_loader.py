import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data(path="data/udemy_courses.csv"):
    """Load course data from CSV."""
    return pd.read_csv(path)

@st.cache_data
def load_similarity(path="data/cosine_sim.npy"):
    """Load cosine similarity matrix."""
    return np.load(path)
