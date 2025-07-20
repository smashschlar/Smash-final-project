import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.contect.stip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break 

        response = chat_with_gpt(user_input)
        print("Chatbot", response)