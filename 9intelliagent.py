def intelligent_agent():
    print("Intelligent Number Guessing Agent")
    print("Think of a number between 1 and 100.")
    print("I will guess your number using your feedback.")
    print("Enter H for Higher, L for Lower, C for Correct.")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print("\nMy guess is:", guess)

        feedback = input(
            "Is your number Higher (H), Lower (L), "
            "or Correct (C)? "
        ).strip().lower()

        if feedback == "c":
            print("Agent: Correct! I guessed your number.")
            print("Number of attempts:", attempts)
            return

        elif feedback == "h":
            low = guess + 1

        elif feedback == "l":
            high = guess - 1

        else:
            print("Invalid input! Enter H, L, or C.")
            attempts -= 1

    print("Agent: Your feedback is inconsistent!")


intelligent_agent()