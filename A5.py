#   Develop an elementary chatbot for any suitable customer interaction application.

def restaurant_chatbot():
    print("Welcome to the Keshav's Restaurant!")
    print("You can ask me about the menu, cost, contact details or reservations!")
    
    while True:
        user_input = input("\nYou: ").lower()
        
        if "menu" in user_input:
            print("Chatbot: Our menu includes pasta, pizza, salads, and desserts.")
        
        elif "cost" in user_input or "price" in user_input or "how much" in user_input:
            print("Chatbot: The average cost per person is around 400 rupees.")
        
        elif "contact" in user_input or "phone" in user_input:
            print("Chatbot: You can contact us at +91-1234567890")
        
        elif "reservation" in user_input or "book" in user_input:
            print("Chatbot: To make a reservation, please call us at +91-1234567890 or visit our website at https://kkrestraunts.io")
        
        elif "hours" in user_input or "timing" in user_input:
            print("Chatbot: We are open from 11 AM to 10 PM, Monday to Sunday.")
        
        elif "how are you" in user_input or "how's it going" in user_input or "sup" in user_input:
            print("Chatbot: I'm just a bot, but I'm here to help you! How can I assist you today?")
        
        elif "meow" in user_input:
            print("Meow meow meow!")

        elif "exit" in user_input or "quit" in user_input:
            print("Chatbot: Thank you for chatting with us! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")

restaurant_chatbot()
