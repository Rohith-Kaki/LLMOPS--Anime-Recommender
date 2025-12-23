import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeLine
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeLine()
pipeline = init_pipeline()

st.title("Anime Recommender System")
query = st.text_input("Enter your anime preferences")
if query:
    with st.spinner("Fetching Recommendations.."):
        response = pipeline.recommend(query=query)
        st.markdown("### Recommendations")
        st.write(response)