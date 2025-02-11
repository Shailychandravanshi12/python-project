import random

# List of words for the game
words = ["python", "developer", "hangman", "automation", "programming", "software"]

# Select a random word
word_to_guess = random.choice(words)
hidden_word = ["_"] * len(word_to_guess)  # Display underscores instead of letters
attempts = 6  # Maximum wrong guesses allowed
guessed_letters = set()

print("🎯 Welcome to Hangman! 🎯")
print(" ".join(hidden_word))

while attempts > 0 and "_" in hidden_word:
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input! Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter!")
        continue



    guessed_letters.add(guess)

    if guess in word_to_guess:
        print("✅ Correct!")
        # Reveal the guessed letter in the word
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                hidden_word[i] = letter
    else:
        attempts -= 1
        print(f"❌ Wrong! {attempts} attempts left.")

    print(" ".join(hidden_word))

# Game Over Conditions
if "_" not in hidden_word:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n💀 Game Over! The word was:", word_to_guess)
