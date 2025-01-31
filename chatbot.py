from gpt4all import GPT4All

# Load the model (ensure you have downloaded a compatible model)
model_path = "models/mistral-7b.Q4_0.gguf"  # Change to your model path
chatbot = GPT4All(model_path)

# Chat loop
print("Chatbot is ready! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot.generate(user_input)
    print("Chatbot:", response)
