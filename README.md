# chat

``
import openai
import os

openai.api_key = os.environ["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"]

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

``
