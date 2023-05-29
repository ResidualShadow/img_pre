import openai

# Set OpenAI API Key
openai.api_key = "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"

prompt = "介绍一下四川轻化工大学"
print(prompt)
# Call ChatGPT API
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=1.3,
    max_tokens=500,
    presence_penalty=0.6,
    frequency_penalty=0.6
)
message = response.choices[0].text
print(message)
