from src.data_loader import DataLoader
from src.vector_store import VectorStore
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv
load_dotenv()
logger = get_logger(__name__)

def main():
    try:
        logger.info("started build Pipeline")
        loader = DataLoader(original_csv='data/anime_with_synopsis.csv', processed_csv='data/updated.csv')
        processed_csv = loader.load_and_process()
        logger.info("data loaded and processed successfully")
        logger.info("Building the VectorStore")
        vectorstore = VectorStore(csv_path=processed_csv)
        vectorstore.build_save_vectorestore()
        logger.info("Vector Store build successfully")
    except Exception as e:
        logger.error("Failed to run main")
        raise CustomException("Failed to build main", e)
    
if __name__ == "__main__":
    main()
