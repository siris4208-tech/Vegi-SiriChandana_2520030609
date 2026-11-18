
import ollama

# Step 1: Send a question to the AI model
response = ollama.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence? Explain in simple words."
        }
    ]
)

# Step 2: Display the AI response
print("\nLLM Response:")
print(response["message"]["content"])
