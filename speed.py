import time
import random

def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog"
    words = text.split()

    while True:
        print("Welcome to the Speed Typing Test!")
        input("Press Enter to start...")

        random.shuffle(words)
        shuffled_text = ' '.join(words)

        print("Type the following text:")
        print(shuffled_text)

        input("Press Enter when you're ready to start typing...")

        start_time = time.time()
        user_input = input()
        end_time = time.time()

        user_words = user_input.split()

        correct_words = 0
        for word1, word2 in zip(words, user_words):
            if word1 == word2:
                correct_words += 1

        accuracy = (correct_words / len(words)) * 100
        elapsed_time = end_time - start_time
        words_per_minute = (len(user_words) / elapsed_time) * 60

        print("\nTyping test results:")
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Words per minute: {words_per_minute:.2f}")

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    speed_typing_test()

