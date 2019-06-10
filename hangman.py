import random
category = 'Dooka Dooka'
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
 ____ |
/    \|
|    ||
\ ___/|
=========''', '''

  +---+
  |   |
 ____ |
/O   \|
|    ||
\ ___/|
=========''', '''

  +---+
  |   |
 ____ |
/O  O\|
|    ||
\ ___/|
=========''', '''

  +---+
  |   |
 ____ |
/O  O\|
|  | ||
\ ___/|
=========''', '''

  +---+
  |   |
 ____ |
/O  O\|
|  | ||
\ _o_/|
=========''', '''

  +---+
  |   |
 _|__ |
/X  X\|
|  | ||
\ _o_/|
=========''']
words={
    'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
    'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
    'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
    'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordList):
    global category
    wordCategories = list(wordList.keys())
    category = random.choice(wordCategories)
    length = len(wordList[category])
    return wordList[category][random.randint(0, length-1)]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print('Your word is from the '+category+' category')
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter.upper(), end=',')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i].upper() + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter.upper(), end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    playAgain='y'
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    playAgain=input()
    return playAgain.lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
