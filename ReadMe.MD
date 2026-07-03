# MarketMind AI

MarketMind AI is a Python-based proof-of-concept project that demonstrates how to build finance-focused AI agents using the Agno framework and Groq models. The repository starts with a simple single-agent example and grows into a multi-agent system that can research the web and analyze financial data for companies.

## Objective

The main goal of this project is to showcase how agentic AI can be used for financial research and market analysis. It combines:

- conversational AI agents powered by large language models,
- live financial data from Yahoo Finance,
- web search capabilities for additional context,
- and multi-agent collaboration for richer analysis.

This makes the project useful as a learning example, prototype, or foundation for building more advanced finance assistants.

## Project Description

MarketMind AI illustrates a practical workflow for building AI agents that can answer finance-related questions with context. Instead of relying on a single static prompt, the project uses specialized agents with specific roles:

- one agent can respond to general prompts with a Groq-backed LLM,
- another can retrieve stock market data and analyst recommendations,
- and a team of agents can combine web research with financial analysis.

The project is intentionally simple and modular so that each stage of the workflow can be understood easily.

## Tech Stack

This project uses the following technologies:

- Python 3.x
- Agno: an agent framework for building AI agents and teams
- Groq: LLM inference provider for fast model access
- Yahoo Finance API via the YFinance tool integration
- DuckDuckGo search integration for web research
- python-dotenv for environment variable management
- virtualenv for isolated Python environments

## Project Structure

- config.py: central configuration file containing the model identifier.
- 1_simple_groq_agent.py: a minimal example that creates a single agent and asks it to generate a response.
- 2_finance_analyst_agent.py: a finance-specific agent that uses Yahoo Finance tools to analyze stock recommendations and fundamentals.
- 3_finance_multiple_agents.py: a multi-agent team with a web search agent and a finance analyst agent working together.

## Framework Overview

The project is built around the Agno framework, which provides a simple way to define:

- Agents with instructions and roles
- Tools that extend an agent’s capabilities
- Teams that coordinate multiple agents
- Structured response formatting for better readability

In this repository, each agent is configured with:

- a model,
- a set of tools,
- custom instructions,
- and optional debug/markdown settings.

This is a strong example of an agentic architecture where specialized agents collaborate to solve a task.

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -U agno
pip install python-dotenv
pip install groq
pip install yfinance
pip install -U ddgs
pip install -U 'agno[os]'
```

### 3. Configure environment variables

Create a .env file in the project root with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The model used in this project is defined in config.py and currently points to:

```python
LLAMA_MODEL_ID = "llama-3.3-70b-versatile"
```

## Running the Project

### Example 1: Simple Groq Agent

Run:

```bash
python 1_simple_groq_agent.py
```

This script demonstrates the simplest form of an Agno agent using Groq.

### Example 2: Finance Analyst Agent

Run:

```bash
python 2_finance_analyst_agent.py
```

This script creates a financial analyst agent that can:

- look up ticker symbols for companies,
- fetch stock prices,
- retrieve analyst recommendations,
- and summarize fundamentals.

### Example 3: Multi-Agent Finance Team

Run:

```bash
python 3_finance_multiple_agents.py
```

This script creates a team of two agents:

- a Web Search Agent for gathering external information,
- and a Finance Analyst Agent for retrieving financial data.

Together, they provide a more complete research workflow.


### To run FastAPI 
```bash
fastapi dev workbench.py
```


## Module Details

### 1_simple_groq_agent.py

A beginner-friendly example that introduces the Agno framework and a basic Groq-backed agent. It is useful for confirming that the environment is configured correctly.

### 2_finance_analyst_agent.py

This module extends the concept of a single agent into a finance-focused use case. It includes:

- a helper function for mapping company names to stock symbols,
- YFinance tools for financial analysis,
- and instructions that guide the agent to respond in a structured way.

### 3_finance_multiple_agents.py

This module demonstrates multi-agent collaboration. It uses:

- DuckDuckGo tools for web search,
- YFinance tools for financial analysis,
- and a Team object to coordinate different specialist agents.

## Why This Project Matters

This repository is a compact demonstration of how modern AI agents can be assembled for practical work such as:

- financial research,
- market summaries,
- investment analysis support,
- and multi-source information gathering.

It is a useful starting point for anyone interested in building AI-powered financial assistants.

## Suggested Next Steps

You can extend this project by:

- adding more financial tools and indicators,
- integrating a database or vector store for historical context,
- adding support for portfolio analysis,
- or deploying the agents as a web app or API service.

## Git Ignore Example

A simple .gitignore should include:

```gitignore
.venv/
.env
__pycache__/
*.py[cod]
*.pyo
.vscode/
.DS_Store
```

## Screenshots

The screenshots below are ordered by capture time from oldest to newest.

![Screenshot 1](assets/Screenshot%202026-07-03%20at%2011.05.56%E2%80%AFPM.png)

![Screenshot 2](assets/Screenshot%202026-07-03%20at%2011.06.05%E2%80%AFPM.png)

![Screenshot 3](assets/Screenshot%202026-07-03%20at%2011.06.17%E2%80%AFPM.png)

![Screenshot 4](assets/Screenshot%202026-07-03%20at%2011.37.24%E2%80%AFPM.png)

![Screenshot 5](assets/Screenshot%202026-07-03%20at%2011.37.33%E2%80%AFPM.png)

![Screenshot 6](assets/Screenshot%202026-07-03%20at%2011.37.45%E2%80%AFPM.png)

![Screenshot 7](assets/Screenshot%202026-07-03%20at%2011.37.54%E2%80%AFPM.png)

![Screenshot 8](assets/Screenshot%202026-07-03%20at%2011.38.01%E2%80%AFPM.png)

![Screenshot 9](assets/Screenshot%202026-07-03%20at%2011.38.09%E2%80%AFPM.png)

![Screenshot 10](assets/Screenshot%202026-07-03%20at%2011.38.17%E2%80%AFPM.png)

![Screenshot 11](assets/Screenshot%202026-07-03%20at%2011.38.25%E2%80%AFPM.png)

![Screenshot 12](assets/Screenshot%202026-07-03%20at%2011.38.35%E2%80%AFPM.png)

![Screenshot 13](assets/Screenshot%202026-07-03%20at%2011.38.43%E2%80%AFPM.png)

