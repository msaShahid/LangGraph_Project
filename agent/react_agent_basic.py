from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType, tool
from langchain_community.tools import TavilySearchResults
import datetime

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
  """Return the current date and time """
  current_time = datetime.datetime.now()
  formatted_time = current_time.strftime(format)
  return formatted_time

tools = [search_tool, get_system_time]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.invoke(
    "List the major Python versions (e.g., Python 1.x, 2.x, 3.x milestones) with their official release dates. "
    "Present the result in a clear table with columns: Version, Release Date, Notes. "
    "Use the search tool to verify dates if needed. "
    "Finally, append the current system date and time using the system time tool."
)


print(response)
