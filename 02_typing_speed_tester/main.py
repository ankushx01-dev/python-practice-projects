from time import time
import random as r

# Function to calculate typing mistakes
def mistake(original_text, user_text):
    
    error = 0

    # Compare each character from both texts
    for i in range(len(original_text)):

        try:
            # Increase error count if characters do not match
            if original_text[i] != user_text[i]:
                error += 1

        # Handle case where user input is shorter
        except IndexError:
            error += 1

    return error


# Function to calculate typing speed
def speed_time(start_time, end_time, user_input):

    # Total time taken
    total_time = end_time - start_time

    # Round time to 2 decimal places
    total_time = round(total_time, 2)

    # Calculate typing speed
    speed = len(user_input) / total_time

    return round(speed, 2)


# Sentences for typing test
test_sentences = [
    "Welcome to the typing speed tester",
    "If you like this project star my repository",
    "Python projects help improve programming skills",
    "Consistency is important for learning coding"
]

# Select a random sentence
selected_text = r.choice(test_sentences)

# Display title
print("\n***** Typing Speed Tester *****\n")

# Display sentence
print(selected_text)
print()

# Start timer
start_time = time()

# Take user input
user_input = input("Type the above sentence:\n\n")

# End timer
end_time = time()

# Display typing speed
print("\nTyping Speed:", speed_time(start_time, end_time, user_input), "characters/sec")

# Display total errors
print("Errors:", mistake(selected_text, user_input))