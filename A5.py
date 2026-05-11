def investment_chatbot():
    print("Welcome to Smart Investment Advisor!")
    print("You can ask me about investment options, risk levels, savings plans, or contact details.")

    while True:
        user_input = input("\nYou: ").lower()

        if "stocks" in user_input or "share market" in user_input:
            print("Chatbot: Stocks are suitable for customers looking for high returns with higher risk.")

        elif "mutual fund" in user_input:
            print("Chatbot: Mutual funds are a balanced investment option managed by professionals.")

        elif "fixed deposit" in user_input or "fd" in user_input:
            print("Chatbot: Fixed Deposits are low-risk investments with stable returns.")

        elif "gold" in user_input:
            print("Chatbot: Gold investments are considered safe during market uncertainty.")

        elif "risk" in user_input:
            print("Chatbot: Low-risk options include Fixed Deposits and Bonds, while Stocks are high-risk investments.")

        elif "save tax" in user_input or "tax" in user_input:
            print("Chatbot: ELSS Mutual Funds and PPF accounts are good tax-saving investment options.")

        elif "best investment" in user_input:
            print("Chatbot: The best investment depends on your goals, budget, and risk tolerance.")

        elif "contact" in user_input or "phone" in user_input:
            print("Chatbot: You can contact our investment advisor at +91-9876543210")

        elif "retirement" in user_input:
            print("Chatbot: For retirement planning, PPF, NPS, and Mutual Funds are recommended.")

        elif "how are you" in user_input or "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! I am here to help you with investment suggestions.")

        elif "exit" in user_input or "quit" in user_input:
            print("Chatbot: Thank you for using Smart Investment Advisor! Have a great day!")
            break

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Please ask about investments or savings options.")

investment_chatbot()