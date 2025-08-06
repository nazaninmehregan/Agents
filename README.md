# 🤖 LangChain SQL Agent with Custom Tools

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)

An intelligent SQL query agent built with LangChain that can understand natural language requests, execute SQL queries, and generate beautiful HTML reports. This project demonstrates AI agent capabilities including function calling, memory management, and custom tool integration.

## 🌟 Features

- **🧠 Natural Language to SQL**: Convert plain English questions into SQL queries
- **🔍 Smart Database Exploration**: Automatically discover and describe database schema
- **📊 HTML Report Generation**: Create formatted reports from query results
- **💾 Conversation Memory**: Maintains context across multiple interactions
- **🛠️ Custom Tool Integration**: Extensible architecture with custom LangChain tools
- **🎨 Beautiful Console Output**: Color-coded message display with boxen formatting
- **⚡ Real-time Debugging**: Custom callback handlers for monitoring AI interactions

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  LangChain Agent │───▶│   Custom Tools  │
│ Natural Language│    │   (GPT-4 Based)  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │ Conversation    │    │ SQL Database    │
                       │ Memory Buffer   │    │ & HTML Reports  │
                       └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13
- OpenAI API Key
- pipenv or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/langchain-sql-agent.git
   cd langchain-sql-agent
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   pipenv shell
   ```
   
   Or with pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Add your OpenAI API key to .env
   echo "OPENAI_API_KEY=your_openai_api_key_here" >> .env
   ```

4. **Run the agent**
   ```bash
   python main.py
   ```

## 💡 Usage Examples

### Basic Database Queries
```python
# Ask natural language questions
"How many users are in the database?"
"What are the top 5 most popular products?"
"Show me all orders from the last month"
```

### Report Generation
```python
# Generate HTML reports
"Create a report showing user statistics and save it as an HTML file"
"Generate a sales report with charts for the top products"
```

### Database Exploration
```python
# Let the agent explore your database
"What tables are available in this database?"
"Describe the structure of the users table"
"Show me the relationships between tables"
```

## 🛠️ Custom Tools

### SQL Query Tool
- **Purpose**: Execute SQL queries safely on SQLite database
- **Features**: Error handling, query validation
- **Schema**: Pydantic-based argument validation

### Table Description Tool
- **Purpose**: Explore database schema and relationships
- **Features**: Multi-table analysis, SQL structure inspection
- **Use Case**: Helps agent understand data before querying

### Report Writer Tool
- **Purpose**: Generate formatted HTML reports
- **Features**: Custom styling, data visualization
- **Output**: Professional-looking reports saved to disk

## 🎨 Custom Handlers

### ChatModelStartHandler
- **Real-time message monitoring**
- **Color-coded output with boxen**
- **Function call visualization**
- **Debug information display**


## 🎯 Key Components

### Agent Configuration
- **LLM**: OpenAI GPT-4 with function calling
- **Memory**: Conversation buffer for context retention
- **Prompt**: Custom system prompt with database context
- **Tools**: SQL execution, schema exploration, report generation

### Database Schema
The included sample database contains:
- **Users**: Customer information and authentication
- **Products**: Product catalog with pricing
- **Orders**: Transaction records
- **Addresses**: Customer shipping information
- **Carts**: Shopping cart functionality

## 📊 Sample Output

```
========= Sending Messages =========

┌─ human ─────────────────────────────────────────┐
│ How many orders are there? Write a report.      │
└─────────────────────────────────────────────────┘

┌─ ai ────────────────────────────────────────────┐
│ Running tool run_sqlite_query with args         │
│ {"query": "SELECT COUNT(*) FROM orders"}        │
└─────────────────────────────────────────────────┘

┌─ tool ──────────────────────────────────────────┐
│ [(1247,)]                                       │
└─────────────────────────────────────────────────┘

┌─ ai ────────────────────────────────────────────┐
│ Running tool write_report with args             │
│ {"filename": "orders_report.html", "html": ... }│
└─────────────────────────────────────────────────┘
```
