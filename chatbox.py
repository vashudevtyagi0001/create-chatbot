# Import the required libraries
import random

# Define a dictionary of rules
rules = {
    
    'hi': 'Hello! What\'s up?',
    
    'how are you': 'I\'m doing well, thanks for asking!',
    'what is your name': 'My name is ChatBot',
    'what can you do': 'I can help you with a variety of tasks, such as answering questions, providing information, and more!',
    'exit': 'Goodbye! It was nice chatting with you.',
    'thanks': 'You\'re welcome!',
    'help': 'What do you need help with?',
   'who are you': 'I am a computer program designed to simulate conversation and answer questions to the best of my ability.',
     'can you recommend a book': 'I\'d be happy to recommend a book! What type of book are you interested in?',
    'default': 'I didn\'t understand that. Can you please rephrase?',
   'can you write a poem': 'Here\'s a short poem: "Roses are red, violets are blue, I\'m a chatbot, and I\'m here for you!"',
}

# Define a function to process user input
def process_input(input_text):
    # Convert input to lowercase
    input_text = input_text.lower()
    
    # Check if input matches a rule
    for rule, response in rules.items():
        if input_text == rule:
            return response
    
    # If no rule matches, return the default response
    return rules['default']

# Define a function to handle user input
def chatbot():
    print('Welcome to the chatbot! Type "exit" to quit.')
    
    while True:
        user_input = input('> ')
        response = process_input(user_input)
        print(response)
        
        if user_input.lower() == 'exit':
            break

# Run the chatbot
chatbot()