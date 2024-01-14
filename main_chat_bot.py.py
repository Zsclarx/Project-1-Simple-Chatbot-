from transformers import GPT2LMHeadModel, GPT2Tokenizer

class Chatbot:
    def __init__(self):
        self.model_name = "gpt2"
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.context = {}

    def generate_response(self, user_input):
        input_ids = self.tokenizer.encode(user_input, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def greet(self):
        print("Hello! I'm your advanced chatbot. How can I assist you today?")

    def farewell(self):
        print("Goodbye! If you have more questions, feel free to ask.")

    def handle_basic_questions(self, user_input):
        basic_questions = [
            "how are you",
            "your name",
            "what do you do",
            "where are you",
            "thank you"
        ]
        if any(q in user_input.lower() for q in basic_questions):
            if "how are you" in user_input.lower():
                print("I'm just a chatbot, but thanks for asking!")
            elif "your name" in user_input.lower():
                print("You can call me Personalized_Bot.")
            elif "what do you do" in user_input.lower():
                print("I'm here to assist you with any questions you may have.")
            elif "where are you" in user_input.lower():
                print("I exist in the digital realm, ready to chat with you.")
            elif "thank you" in user_input.lower():
                print("You're welcome! If you need more help, feel free to ask.")
        else:
            print("Unfortunately, I am not trained for such questions. Let me try to provide a general response.")
            response = self.generate_response(user_input)
            print(response)

    def user_interaction(self):
        for _ in range(5): #Here 5 is number of questions we can implement it to run until a farewell is encountered!
            user_response = input("What can I do for you today? ")
            self.context['user_input'] = user_response
            self.handle_basic_questions(user_response)

    def start_conversation(self):
        self.greet()
        self.user_interaction()
        self.farewell()


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_conversation()
