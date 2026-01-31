from prompts.generation import generation_prompt
from llms.gemini import get_llm

llm = get_llm()

generate_chain = generation_prompt | llm
