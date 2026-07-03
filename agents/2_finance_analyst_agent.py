from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

from config import LLAMA_MODEL_ID
from tools import get_company_symbol

load_dotenv()

agent = Agent(
    model=Groq(id=LLAMA_MODEL_ID),
    tools=[
        YFinanceTools(
            enable_stock_price=True,
            enable_analyst_recommendations=True,
            enable_stock_fundamentals=True,
        ),
        get_company_symbol,
    ],
    markdown=True,
    debug_mode=True,
    instructions=[
        "You are an expert financial analyst.",
        "Use the get_company_symbol tool to get the symbol for any company, even if it is not a public company.",
        "Use tables to display data.",
    ],
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA. Show in tables.", stream=True
)