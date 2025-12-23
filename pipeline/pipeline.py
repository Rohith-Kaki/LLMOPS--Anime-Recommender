from src.vector_store import VectorStore
from src.recommender import AnimeRecommender
from config.config import MODEL_NAME, GROQ_API_KEY
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeLine:
    def __init__(self, persist_dir = "chromdb"):
        try:
            logger.info("Initializing the pipeline")
            vectorstore_builder = VectorStore("", persist_dir=persist_dir)
            retriever = vectorstore_builder.load_vectorstore().as_retriever()
            self.recommender = AnimeRecommender(api_key=GROQ_API_KEY, retriever=retriever, model_name=MODEL_NAME)
        except Exception as e:
            logger.error(f"Error initialzing the pipeline {str(e)}")
            raise CustomException("Error initializing the pipeline", e)
        
    def recommend(self, query:str) -> str:
        try:
            logger.info(f"Received query: {query}")
            recommendation = self.recommender.get_recommendation(query=query)
            logger.info("Recommendation genereated successfully")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to generate Recommendation {str(e)}")
            raise CustomException("Error Recommendation", e)