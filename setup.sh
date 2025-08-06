#!/bin/bash

# Setup script for LangChain SQL Agent
echo "🚀 Setting up LangChain SQL Agent..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if pipenv is installed, if not suggest pip
if command -v pipenv &> /dev/null; then
    echo "📦 Installing dependencies with pipenv..."
    pipenv install
    echo "🔧 To activate the virtual environment, run: pipenv shell"
else
    echo "📦 Installing dependencies with pip..."
    pip install -r requirements.txt
    echo "💡 Consider installing pipenv for better dependency management: pip install pipenv"
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "📝 Please edit .env file and add your OpenAI API key!"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OpenAI API key"
echo "2. Run the demo: python demo.py"
echo "3. Or run the main application: python main.py"
echo ""
echo "📚 For more information, see README.md"
