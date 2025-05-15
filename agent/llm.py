
from langchain_google_genai import ChatGoogleGenerativeAI
from agent.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=GEMINI_API_KEY)
