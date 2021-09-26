import random

def printHelper1(wrongGuess,rightGuess,guessTracker):
    print("The wrong guesses so far are:", wrongGuess)
    print("The right guesses so far are:", rightGuess)
    print("And the word so far is: ", guessTracker)

wheel = [300,
         500,
         450,
         500,
         800,
         "lose a turn",
         700,
         1000,
         650,
         "Bankrupt",
         900,
         500,
         350,
         600,
         500,
         400,
         550,
         800,
         300,
         700,
         900,
         500,
         5000,
         950]
presetupYN = input("Do you want to play the game with default setup paramiter? [y/n]: ")
if presetupYN == "n":
    playerOneName = str(input("Enter Player One's Name: "))
    playerTwoName = str(input("Enter Player Two's Name: "))
    playerThreeName = str(input("Enter Player Three's Name: "))
    playerNames = [playerOneName, playerTwoName, playerThreeName]

else:
    word = ["palaeopedology", "demology", "dynamogenesis"]
    wordHint = ["Science", "Occultism", "The Body"]
    playerNames = ["Robbie", "Blake", "Tim"]
winPot              = [1000, 2000, 3000]
#GAME
gameBool            = True                                                          #Starts the game
RoundNumber         = 1                                                             #Initilizes game with round 1.
playerBank          = [0,0,0]                                                       #Player 1 is playerBank[0]



turn                = 0                                                                     #Player 1's turn is 0, player 2's turn is 1, and player 3's turn is 2.
roundNumber         = 0
vowels              = "a, e, i, o, u, y"
consonants          = "b, c, d, f, g, j, k, l, m, n, p, q, s, t, v, x, z, h, r, w"
OVER                = False


while gameBool is True:
    wrongGuess = ""
    rightGuess = ""
    guessTracker = [" _ "] * len(word[roundNumber])
    randWordM = word[roundNumber]
    while roundNumber <= 1:
    #ROUND ONE and ROUND TWO
        #TURN:
        nextTurn = False
        while nextTurn is False:
            if turn == 3:
                turn = 0
            print("################################################################################################")
            print("it is ", str(playerNames[turn]), "'s turn, goodluck!")
            print(playerNames[turn], "you have: $", playerBank[turn], " in your bank.")
            print("The hint is that the word is in this category: ", wordHint[roundNumber])
            printHelper1(wrongGuess, rightGuess, guessTracker)
            # SPIN WHEEL:
            if nextTurn == False:
                print("################################################################################################")
                wheelYN = str(input(playerNames[turn] + " do you want to spin the wheel? [y/n]: ")).lower()
                if wheelYN == "y":
                    randomWheel = random.choice(wheel)
                    if randomWheel == "lose a turn" or randomWheel == "Bankrupt":
                        print("you spun the weel and got: ",randomWheel)
                        if randomWheel == "Bankrupt":
                            print('You LOOSE ALL YOUR MONEY!!!')
                            playerBank[turn]=0
                        turn = turn + 1
                        nextTurn = True
                        break
                    else:
                        print("you spun the weel and got: ", randomWheel)
                        printHelper1(wrongGuess, rightGuess, guessTracker)
                        guess = str(input(playerNames[turn] + " guess a consonant: ")).lower()
                        if (vowels.find(guess) == -1) and (wrongGuess.find(guess)== -1) and (rightGuess.find(guess) == -1):
                            if randWordM.find(guess) != -1:
                                print("Right Guess!")
                                rightGuess = rightGuess + " " + guess
                                playerBank[turn] = playerBank[turn] + randomWheel
                            else:
                                wrongGuess = wrongGuess + " " + guess
                                print("Wrong Guess!")
                                turn = turn + 1
                                nextTurn = True
                            while guess in randWordM:
                                location = randWordM.find(guess)
                                randWordM = randWordM.replace(guess, "*", 1)
                                guessTracker[location] = guess
                        elif wrongGuess.find(guess) != -1 or rightGuess.find(guess) != -1:
                            print("That has already been guessed, try again")
                        elif vowels.find(guess) != -1:
                            print("That is not a consonant, try again")
            if nextTurn == False:
                print("################################################################################################")
                BuyYN = str(input(playerNames[turn] + " do you want to buy a vowel for $250?, you have: $" + str(playerBank[turn])+"[y/n]: ")).lower()
                if BuyYN == "y" and playerBank[turn]>250:
                    printHelper1(wrongGuess, rightGuess, guessTracker)
                    guess = str(input(playerNames[turn] + " guess a vowel: ")).lower()
                    if (vowels.find(guess) != -1) and (wrongGuess.find(guess) == -1) and (rightGuess.find(guess) == -1):
                        if randWordM.find(guess) != -1:
                            print("Right Guess!")
                            rightGuess = rightGuess + " " + guess
                        else:
                            wrongGuess = wrongGuess + " " + guess
                            print("Wrong Guess!")
                            turn = turn + 1
                            nextTurn = True
                        while guess in randWordM:
                            location = randWordM.find(guess)
                            randWordM = randWordM.replace(guess, "*", 1)
                            guessTracker[location] = guess
                    elif wrongGuess.find(guess) != -1 or rightGuess.find(guess) != -1:
                        print("That has already been guessed, try again")
                    elif vowels.find(guess) == -1:
                        print("That is not a vowel, try again")
                elif BuyYN == "y" and playerBank[turn]<250:
                    print("Sorry, but you do not have enough money to buy a vowel...")
            if nextTurn == False:
                print("################################################################################################")
                print("And the word so far is: ", guessTracker)
                wordYN = str(input(playerNames[turn] + " do you want to guess the word [y/n]: ")).lower()
                if wordYN == "y":
                    guess = str(input(playerNames[turn] + " guess a word: ")).lower()
                    if guess == word[roundNumber]:
                        playerBank[turn] = playerBank[turn] + winPot[roundNumber]
                        turn = turn + 1
                        roundNumber  = roundNumber + 1
                        wrongGuess = ""
                        rightGuess = ""
                        guessTracker = [" _ "] * len(word[roundNumber])
                        randWordM = word[roundNumber]
                        print("-----------------------------------------------------------------------------------------")
                        print("ROUND OVER, proceeding to round ", roundNumber+1)
                        print("-----------------------------------------------------------------------------------------")
                        break
                    else:
                        print("You got it wrong")
                        turn = turn + 1
    while roundNumber == 2:
        reveals= ["r","s","t","l","n","e"]
        for i in range(3):
            if playerBank[i] == max(playerBank):
                turn = i
        if OVER is False:
            for i in range(len(reveals)):
                guess = reveals[i]
                while guess in randWordM:
                    location = randWordM.find(guess)
                    randWordM = randWordM.replace(guess, "*", 1)
                    guessTracker[location] = guess
            print(playerNames[turn], "you have: $",playerBank[turn]," which is the most amount of money so you will be proceeding to round 3")
            print("r,s,t,l,n, and e have already been revealed")
            print("And the word so far is: ", guessTracker)
            guess = str(input(playerNames[turn] + " guess a vowel: ")).lower()
            if (vowels.find(guess) != -1) and (wrongGuess.find(guess) == -1) and (rightGuess.find(guess) == -1):
                if randWordM.find(guess) != -1:
                    rightGuess = rightGuess + " " + guess
                else:
                    wrongGuess = wrongGuess + " " + guess
                while guess in randWordM:
                    location = randWordM.find(guess)
                    randWordM = randWordM.replace(guess, "*", 1)
                    guessTracker[location] = guess
            elif wrongGuess.find(guess) != -1 or rightGuess.find(guess) != -1:
                print("That has already been guessed, try again")
            elif vowels.find(guess) == -1:
                print("That is not a vowel, try again")
            n=3
            for i in range(n):
                guess = str(input(playerNames[turn] + " guess a consonant: ")).lower()
                if (vowels.find(guess) == -1) and (wrongGuess.find(guess) == -1) and (rightGuess.find(guess) == -1):
                    if randWordM.find(guess) != -1:
                        rightGuess = rightGuess + " " + guess
                    else:
                        wrongGuess = wrongGuess + " " + guess
                    while guess in randWordM:
                        location = randWordM.find(guess)
                        randWordM = randWordM.replace(guess, "*", 1)
                        guessTracker[location] = guess
                elif wrongGuess.find(guess) != -1 or rightGuess.find(guess) != -1:
                    print("That has already been guessed, try again")
                    n = n + 1
                elif vowels.find(guess) != -1:
                    print("That is not a consonant, try again")
                    n = n + 1
        ready = input("Are you ready to guess the final word? [y/n]: ")
        if ready == "y":
            print("And the word so far is: ", guessTracker)
            guess = str(input(playerNames[turn] + " guess a word: ")).lower()
            if guess == word[roundNumber]:
                playerBank[turn] = playerBank[turn] + winPot[roundNumber]
                roundNumber = roundNumber + 1
                win = True
                print("-----------------------------------------------------------------------------------------")
                print("YOU WIN!!!!")
                print("-----------------------------------------------------------------------------------------")
                break
            else:
                roundNumber = roundNumber + 1
                win = False
                print("-----------------------------------------------------------------------------------------")
                print("YOU LOOSE!!!!")
                print("-----------------------------------------------------------------------------------------")
                break
    while roundNumber == 3:
        f = open(r'C:\Users\Eddy Doering\PycharmProjects\Assessment6\venv\CircleofChanceResults.txt', 'w')
        if win is False:
            f.write(str(playerNames[turn]) + " Lost")
            gameBool = False
            roundNumber = roundNumber + 1
            break
        if win is True:
            f.write(str(playerNames[turn]) + " WON, and his winnings are: $" + str(playerBank[turn]))
            gameBool = False
            roundNumber = roundNumber + 1
            break


    #ROUNDTHREE
        #REVEAL R-S-T-L-N-E
        #PICK 3 more consent and 1 more vowel
        #TIMER (5 seconds to guess the word)
        #INFINITE NUMBER OF GUESSES!!! (5 seconds)
