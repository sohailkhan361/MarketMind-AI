from agno.agent import Agent
from agno.team import Team
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

from config import LLAMA_MODEL_ID
from tools import get_company_symbol

load_dotenv()

web_search_agent = Agent(
    name="Web Search Agent",
    model=Groq(id=LLAMA_MODEL_ID),
    tools=[
        DuckDuckGoTools(fixed_max_results=3, enable_search=True, enable_news=True),
    ],
    markdown=True,
    debug_mode=True,
    instructions=[
        "Always include sources",
    ],
)

finance_analyst_agent = Agent(
    name="Finance Analyst Agent",
    role="Get Financial Data and Analyst Recommendations",
    model=Groq(id=LLAMA_MODEL_ID),
    tools=[
        YFinanceTools(
            enable_stock_price=True,
            enable_analyst_recommendations=True,
            enable_company_info=True,
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

agents_team = Team(
    name="Finance Analyst & Research Team",
    members=[web_search_agent, finance_analyst_agent],
    instructions=[
        "Always include sources.", "Use tables to display data.",
    ],
    model=Groq(id=LLAMA_MODEL_ID),
    debug_mode=True,
    markdown=True
)

agents_team.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA. Show in tables.", stream=True
)