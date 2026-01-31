from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import MODEL_NAME, TEMPERATURE

def get_llm():
    return ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
    )
