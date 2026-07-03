
def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Accenture": "ACN",
        "IBM": "IBM",
        "Wipro": "WIT",
        "HCL": "HCLTECH",
        "NVIDIA": "NVDA",
        "Cognizant": "CTSH",
        "TCS": "TCS",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")