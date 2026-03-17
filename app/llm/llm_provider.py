import ollama


def generate_text(prompt: str):

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    output = response["message"]["content"]

    print("LLM RESPONSE:", output)

    return output