#   Develop an elementary chatbot for any suitable customer interaction application.

def chatbot():
    print("Chatbot: Hello! I can help you with investment suggestions.")
    print("Type 'exit' anytime to stop.\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Chatbot: Thank you! Happy investing")
            break

        elif "invest" in user or "suggest" in user:
            print("Chatbot: Sure! I need some details.")

            amount = int(input("Enter amount: "))
            risk = input("Risk (low/medium/high): ").lower()
            duration = input("Duration (short/long): ").lower()

            print("\nBased on your inputs, I suggest:")

            # Decision logic
            if risk == "low":
                if duration == "short":
                    print("- Savings Account\n- Fixed Deposit")
                else:
                    print("- Fixed Deposit\n- Government Bonds\n- PPF")

            elif risk == "medium":
                if duration == "short":
                    print("- Debt Mutual Funds\n- Hybrid Funds")
                else:
                    print("- Mutual Funds\n- Index Funds\n- SIP")

            elif risk == "high":
                if duration == "short":
                    print("- Intraday Trading (risky)")
                else:
                    print("- Stocks\n- Equity Mutual Funds\n- Crypto")

            if amount > 100000:
                print("- Real Estate (optional)")

            print("\nChatbot: You can ask again or type 'exit'.")

        elif "hi" in user or "hello" in user:
            print("Chatbot: Hello! Ask me about investment suggestions.")

        else:
            print("Chatbot: I can help with investment suggestions. Try typing 'invest'.")


# Run chatbot
chatbot()


# Example

""" 
You: hi
Bot: Hello! How can I help you?

You: what is delivery time
Bot: Delivery usually takes 3-5 days.

You: payment options
Bot: We accept UPI, cards, and net banking.

You: bye
Bot: Thank you! Have a nice day 
"""