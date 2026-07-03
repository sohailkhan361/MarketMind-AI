from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

from config import LLAMA_MODEL_ID

load_dotenv()

agent = Agent(
    model=Groq(id=LLAMA_MODEL_ID),
)

agent.print_response("Write a poem about the ocean.")