from typing import List
from dotenv import load_dotenv

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END

from chains.generate_chain import generate_chain
from chains.reflect_chain import reflect_chain

load_dotenv()

State = List[BaseMessage]

graph = StateGraph(State)

GENERATE = "generate"
REFLECT = "reflect"


def generate_node(state: State) -> State:
    response = generate_chain.invoke({"messages": state})
    return state + [response]


def reflect_node(state: State) -> State:
    response = reflect_chain.invoke({"messages": state})
    return state + [HumanMessage(content=response.content)]


graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)

graph.set_entry_point(GENERATE)


def should_continue(state: State):
    if len(state) > 4:
        return END
    return REFLECT


graph.add_conditional_edges(GENERATE, should_continue)
graph.add_edge(REFLECT, GENERATE)

app = graph.compile()
