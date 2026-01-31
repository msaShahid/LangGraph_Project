from prompts.reflection import reflection_prompt
from llms.gemini import get_llm

llm = get_llm()

reflect_chain = reflection_prompt | llm
