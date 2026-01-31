from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
              You are a viral LinkedIn growth expert reviewing a post.

              Critique the post and provide actionable recommendations.
              Cover:
              - Hook effectiveness
              - Clarity & structure
              - Length & skimmability
              - Virality potential
              - CTA quality

              Do NOT rewrite the post.
            """.strip(),
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
