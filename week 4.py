import random  

def pattern_puzzle():
    print("🔢 Number Pattern Puzzle!")
    patterns = [
        ([2, 4, 6, 8], 10),         # +2
        ([3, 6, 12, 24], 48),       # *2
        ([81, 27, 9, 3], 1),        # /3
        ([1, 4, 9, 16], 25),        # squares
        ([13, 11, 9, 7], 5)         # -2
    ]

    score = 0  

    for seq, answer in random.sample(patterns, 3):
        print(f"\nPattern: {seq} ?")
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if guess == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Nope! The answer was {answer}.")

    print(f"\n🏁 Puzzle Over! You got {score} out of 3 right.")


pattern_puzzle()
