from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from langchain.schema import SystemMessage
from langchain.agents import AgentExecutor,create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from tools.sql import run_query_tool,list_tables,describe_tables_tool
from tools.report import write_report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler


load_dotenv()

handler = ChatModelStartHandler()

chat = ChatOpenAI(
    callbacks=[handler],
)

tables = list_tables()


prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            f"You are a helpful assistant that can run SQL queries on a SQLite database.\n"
            f"The database has tables of: {tables}\n"
            "Do not make any assumptions about what tables exist or what columns they have."
            "Instead, use the 'describe_tables' function"
            )),
        # our memory containig human and final ai messages
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        # our memory containig assistant and function messages - deleted after the final ai message is received
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    # return the messages with roles as opposed to just the text
    return_messages=True
)

tools = [run_query_tool, describe_tables_tool, write_report_tool]

agent = create_openai_functions_agent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    # verbose=True,
    memory=memory,
)

result = agent_executor.invoke({"input": "how many orders are there?write the result to an html report."})  # Example query
# print(result)

result1 = agent_executor.invoke({"input": "repeat the exact same process for users"})  # Example query
# print(result1)