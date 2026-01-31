from langchain_core.messages import HumanMessage
from agents.refletion_agent import app

if __name__ == "__main__":
    initial_message = HumanMessage(
        content="AI Agents taking over content creation"
    )

    result = app.invoke([initial_message])

    print("\n--- FINAL OUTPUT ---\n")
    print(result[-1].content)
