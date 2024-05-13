from flask import Flask, request, jsonify

app = Flask(__name__)

# Define predefined questions and answers
predefined_responses = {
    "What is your name?": "My name is ChatBot.",
    "How are you?": "I'm doing well, thank you!",
    "What can you do?": "I can help you with common questions."
    # Add more predefined questions and answers as needed
}

@app.route('/')
def chatbot():
    # Get user message from request
    # user_message = request.json.get('message') #I committed out

    # Process user message and generate chatbot response
    chatbot_response = get_response("What is your name?")

    # Return chatbot response
    return jsonify({'response': chatbot_response})

def get_response(message):
    # Check if the user message matches a predefined question
    for question, answer in predefined_responses.items():
        if message.lower() == question.lower():
            return answer
    
    # If no predefined answer matches, return a default response
    return "I'm sorry, I don't understand that question."

if __name__ == '__main__':
    app.run(debug=True)
