#  Implement any one of the following Expert System 
#    - Stock market trading

def expert_system():
    print("📊 Stock Market Expert System")
    print("Answer the following questions:\n")

    capital = int(input("Enter your investment amount: "))
    risk = input("Enter risk level (low/medium/high): ").lower()
    experience = input("Are you beginner or experienced: ").lower()
    duration = input("Investment duration (short/long): ").lower()

    print("\n📊 Expert Advice:\n")

    # -------- Rules --------

    if risk == "low":
        print("- Invest in Blue-chip stocks")
        print("- Prefer Mutual Funds")
        print("- Avoid risky trading")

    elif risk == "medium":
        print("- Invest in diversified portfolio")
        print("- Try Index Funds or ETFs")

    elif risk == "high":
        if experience == "experienced":
            print("- Go for Direct Stock Trading")
            print("- Consider Intraday Trading")
        else:
            print("- Start with Equity Mutual Funds")
            print("- Avoid high-risk trading initially")

    if duration == "long":
        print("- Focus on long-term growth stocks")

    if capital > 100000:
        print("- You can diversify into multiple sectors")

    print("\n📊 Decision completed using rule-based system.")


# Run system
expert_system()


# Example

""" 
User: 150000
User: high
User: beginner
User: long
"""