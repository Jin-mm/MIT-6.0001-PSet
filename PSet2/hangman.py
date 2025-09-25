# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
	if letters_guessed[-1] not in secret_word:
		return False
	else:
		return True


def get_guessed_word(secret_word, letters_guessed):
	elements = [" _ "] * len(secret_word)
	def find(s, ch):
		return [i for i, ltr in enumerate(s) if ltr == ch]	
	for letter in letters_guessed:
		if letter in secret_word:
			ind = find(secret_word, letter)
			for i in ind:
				elements[i] = letter
	elements = "".join(elements)
	return elements

			
def get_available_letters(letters_guessed):
	all_letters = string.ascii_lowercase
	for letter in letters_guessed:
		all_letters = all_letters.replace(letter, "")
	return all_letters
	
    

def hangman(secret_word):
	print("Welcome to the game Hangman!")
	print("I am thinking of a word that is", len(secret_word), "letters long.")
	guess = 6
	warning = 3
	letters_guessed = []
	vowels = ["a", "e", "i", "o", "u"]
	unique = len(set(secret_word))
	guessed_for_now = ""
	
	while guess > 0:
		print("---------------------")
		print("You have", warning, "warnings left.")
		print("You have", guess, "guesses left.")
		print("Available letters:", get_available_letters(letters_guessed))
		
		# check if the user has successfully guessed the secret word.
		if guessed_for_now == secret_word:
			total_score = str(guess* unique)
			print("---------------------")
			print("Congratulations, you won!" + "\n" + "You total score for this game is " + total_score)
			break
		else:
			letter = input("Please guess a letter: ")
			if str.isalpha(letter):
				letter = str.lower(letter)
				if letter in letters_guessed:
					print("The letter has already been guessed before!")
					warning -=1
					if warning < 0:
						warning = 0
						guess -= 1
					continue   #  continues with the next iteration of the loop. this makes sure nothing else below runs for this input
				else:
					letters_guessed.append(letter)
				if is_word_guessed(secret_word, letters_guessed):
					guessed_for_now = get_guessed_word(secret_word, letters_guessed)
					print("Good guess:", guessed_for_now)
				elif letter in vowels:
					guess -= 2
					print("Oops, that letter is not in my word and it is a vowel:", guessed_for_now)
				else:
					guess -= 1 
					print("Oops, that letter is not in my word:", guessed_for_now)
			else:
				print("You can only input an alphabet!")
				warning -= 1
				if warning <= 0:
					warning = 0
					guess -= 1
	
	if guess <= 0:
		print("---------------------")
		print("Too bad you have run out of guesses :<" + "\n" + "The secret word is " + secret_word)
	
		
			
		
		



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i, l in enumerate(my_word):
        if l.isalpha() and other_word[i] != l:
            return False
    return True


def show_possible_matches(my_word):
	matched_words = []
	for word in wordlist:
		other_word = word
		if match_with_gaps(my_word, other_word):
			matched_words.append(word)
	if len(matched_words) == 0:
		return "No matches found"
	else:
		matched_words = " ".join(matched_words)
		return(matched_words)




def hangman_with_hints(secret_word):
	print("Welcome to the game Hangman!")
	print("I am thinking of a word that is", len(secret_word), "letters long.")
	guess = 6
	warning = 3
	letters_guessed = []
	vowels = ["a", "e", "i", "o", "u"]
	unique = len(set(secret_word))
	guessed_for_now = ""
	
	while guess > 0:
		print("---------------------")
		print("You have", warning, "warnings left.")
		print("You have", guess, "guesses left.")
		print("Available letters:", get_available_letters(letters_guessed))
		
		# check if the user has successfully guessed the secret word.
		if guessed_for_now == secret_word:
			total_score = str(guess* unique)
			print("---------------------")
			print("Congratulations, you won!" + "\n" + "You total score for this game is " + total_score)
			break
		else:
			letter = input("Please guess a letter: ")
			if str.isalpha(letter):
				letter = str.lower(letter)
				if letter in letters_guessed:
					print("The letter has already been guessed before!")
					warning -=1
					if warning < 0:
						warning = 0
						guess -= 1
					continue   #  continues with the next iteration of the loop. this makes sure nothing else below runs for this input
				else:
					letters_guessed.append(letter)
				if is_word_guessed(secret_word, letters_guessed):
					guessed_for_now = get_guessed_word(secret_word, letters_guessed)
					print("Good guess:", guessed_for_now)
				elif letter in vowels:
					guess -= 2
					print("Oops, that letter is not in my word and it is a vowel:", guessed_for_now)
				else:
					guess -= 1 
					print("Oops, that letter is not in my word:", guessed_for_now)
					
			elif letter == "*":
				guessed_for_now = get_guessed_word(secret_word, letters_guessed)
				print(show_possible_matches(guessed_for_now))
				
			else:
				print("You can only input an alphabet!")
				warning -= 1
				if warning <= 0:
					warning = 0
					guess -= 1
	
	if guess <= 0:
		print("---------------------")
		print("Too bad you have run out of guesses :<" + "\n" + "The secret word is " + secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
# To test part 2, comment out the pass line above and
# uncomment the following two lines.
    
	# secret_word = choose_word(wordlist)
	# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
