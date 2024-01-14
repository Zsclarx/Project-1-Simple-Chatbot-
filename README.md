Chatbot using GPT-2 Model

This script defines a simple chatbot class that uses the GPT-2 model to generate responses.
The chatbot handles basic questions and provides responses based on pre-defined patterns.
If a question is not recognized, it generates a general response using the GPT-2 model.

Dependencies:
- transformers: Hugging Face Transformers library for natural language processing models.

Usage:
1. Create an instance of the Chatbot class.
2. Call the start_conversation method to initiate the chat with greetings and user interaction.

Note: Make sure to install the required dependencies before running the script.



__init__(self):

        Initializes the Chatbot instance with the GPT-2 model and tokenizer.

        Attributes:
        - model_name (str): Name of the GPT-2 model to use.
        - model (GPT2LMHeadModel): Pre-trained GPT-2 language model.
        - tokenizer (GPT2Tokenizer): Tokenizer for processing text input.
        - context (dict): Dictionary to store context or additional information during conversation.
greet(self):

        Prints a greeting message.

farewell(self):

        Prints a farewell message.
    
handle_basic_questions(self, user_input):

        Handles basic questions and provides responses.

        Parameters:
        - user_input (str): User's input or question.
   
user_interaction(self):
      
    Facilitates user interaction by handling multiple questions.
    
start_conversation(self):
       
        Initiates the conversation with a greeting, user interaction, and farewell.
        

Author: [Prakhar Pratap Singh]
Date: [1/14/2024]
