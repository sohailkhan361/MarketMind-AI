To Start:
> virtualenv .venv
> source .venv/bin/activate
> pip install -U agno
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

