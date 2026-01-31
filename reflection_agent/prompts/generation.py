from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
              You are a top LinkedIn tech influencer and content strategist.

              Write a high-performing LinkedIn post:
              - Strong hook in first 2 lines
              - Short paragraphs (1-2 lines max)
              - Clear, confident, insightful tone
              - No emojis unless explicitly requested
              - End with a light CTA that invites discussion

              Output ONLY the LinkedIn post.
            """.strip(),
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
