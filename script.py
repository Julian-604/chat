import openai

openai.api_key = "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"

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.6,
    )
    message = response.choices[0].text

    return message

search = str(input(":"))

response = ask_gpt(search)
print(response)
