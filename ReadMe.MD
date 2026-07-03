To Start:
> virtualenv .venv
> source .venv/bin/activate
> pip install -U agno openai
> pip install dotenv
> pip install groq


# Initialize Git
git init

# Create .gitignore
cat > .gitignore << 'EOF'

```
# Python virtual environment
.venv/

# Environment variables
.env

# Python cache
__pycache__/
*.py[cod]
*.pyo

# IDE
.vscode/

# macOS
.DS_Store
EOF

# Verify
git status
```

To Start with Finance Agents:
> pip install yfinance

To install DuckDuckGo, run the following command:
> pip install -U ddgs 
