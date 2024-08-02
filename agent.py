from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_community.llms.ollama import Ollama
from langchain.memory import ConversationBufferMemory

llm = Ollama(model="llama3:latest")

tools = load_tools(["wikipedia"], llm=llm)

memory = ConversationBufferMemory()
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    handle_parsing_errors=True
)

agent.run("who won the cricket world cup in 1983")


agent.run("who won in 2003?")

print(agent.memory.buffer)
