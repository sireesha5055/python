def is_isogram(word):
    # Convert the word to lowercase and remove spaces and hyphens
    word = word.lower().replace(' ', '').replace('-', '')

    # Create a set of unique letters in the word
    unique_letters = set(word)

    # Compare the length of the word with the length of unique letters
    if len(word) == len(unique_letters):
        return 'Yes'
    else:
        return 'No'

# Get input from the user
input_word = input("Enter a word or phrase: ")

# Check if the input is an isogram and print the result
print(is_isogram(input_word))


