#!/usr/bin/env python3
"""
Demo script showcasing the LangChain SQL Agent capabilities.
Run this script to see the agent in action with various examples.
"""

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain.schema import SystemMessage
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from tools.sql import run_query_tool, list_tables, describe_tables_tool
from tools.report import write_report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler
import time

def demo_agent():
    """Run a demonstration of the SQL agent capabilities."""
    
    # Load environment variables
    load_dotenv()
    
    # Set up the agent
    handler = ChatModelStartHandler()
    chat = ChatOpenAI(callbacks=[handler])
    tables = list_tables()
    
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessage(content=(
                f"You are a helpful assistant that can run SQL queries on a SQLite database.\n"
                f"The database has tables: {tables}\n"
                "Use the 'describe_tables' function to understand table schemas before querying."
            )),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ]
    )
    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    tools = [run_query_tool, describe_tables_tool, write_report_tool]
    
    agent = create_openai_functions_agent(llm=chat, prompt=prompt, tools=tools)
    agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory)
    
    # Demo scenarios
    scenarios = [
        {
            "title": "🔍 Database Exploration",
            "query": "What tables are in this database and what do they contain?",
            "description": "Let the agent explore the database structure"
        },
        {
            "title": "📊 User Analytics",
            "query": "How many users are registered? Create an HTML report with user statistics.",
            "description": "Generate a user analytics report"
        },
        {
            "title": "🛒 Sales Analysis", 
            "query": "What are the top 5 most popular products by order count? Include this in a sales report.",
            "description": "Analyze product popularity and generate sales report"
        },
        {
            "title": "💰 Revenue Insights",
            "query": "Calculate total revenue and create a financial summary report.",
            "description": "Generate financial insights with revenue calculations"
        }
    ]
    
    print("🚀 Starting LangChain SQL Agent Demo")
    print("=" * 50)
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{scenario['title']} (Demo {i}/{len(scenarios)})")
        print(f"Description: {scenario['description']}")
        print(f"Query: '{scenario['query']}'")
        print("-" * 50)
        
        try:
            result = agent_executor.invoke({"input": scenario["query"]})
            print(f"✅ Demo {i} completed successfully!")
            
            # Small delay between demos for better readability
            if i < len(scenarios):
                print("\n⏳ Preparing next demo...")
                time.sleep(2)
                
        except Exception as e:
            print(f"❌ Demo {i} failed: {str(e)}")
    
    print("\n🎉 Demo completed! Check the generated HTML reports in the project directory.")
    print("💡 Try running your own queries by modifying main.py")

if __name__ == "__main__":
    demo_agent()
