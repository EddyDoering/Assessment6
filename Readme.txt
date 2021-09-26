Welcome to my circle of chance gameeee!

INTRODUCTION:
Three players will compete against weach other in a high stakes game of chance and skill, and will give each contenstant an opprutunity to win it big if they manange to stay on top until round 3 and are able to guess the final queston. In this readme I will walk you through setting up your own game of......... WHEEL!!!!...... OF!!!....... CHANCE!!!

SET UP:
As the host of this fantastic game you will have a few responsibilities:

First, you will need three words and a hint for each word in the form of a what general category the word falls into. Otherwise you can use the words that I have provided for you to use. When running the program just select "y" for the first prompt to ensure you use the presets.

Secondly, you will need three friends to play. If you ran a the game with defaults you will have have Robbie, Blake, and Tim as the default players.

Thirdly, you need a Python 3 IDE of your choice to run your code. I perfer pycharm, but you could use IDLE which is installed with python 3 by default. 

RUNNING GAME AND RULES:
Wheel of Chance is a game of three rounds. Rounds one and two are played by all three players. Round 3 is only played by the player with the most money from the previous two rounds. The goal of each round is to guess a word. The person who guesses the word is awarded $1000 for round one, $2000 for round two, and $3000 for round three. The active player has three options during their turn:

1. Spin the wheel of chance then Guess a consonant.
2: Buy a vowel for $250
3: Guess the word.

SPINNING THE WHEEL:
The wheel is broken into 24 pannels, and spun to a random panel when this option is choosen, 22 of these panels are monetary values and one lose a turn, and a bankrupt. If a monetary value is spun then that is added to the players bank if they successfully guess a consonant, otherwise their turn is over. If loose a turn is spun the players turn is over and the next player becomes the active player. If Bankrupt is spun then the active players bank is set to 0 and their turn is over. to reiterate if the active player successfully guesses a consonant in the word they are able to continue their turn and again choose to either spin the wheel, buy a vowel, or guess the word.

BUY A VOWEL:
A player wishing to buy a vowel must have a minimum of $250 in their bank. It costs $250 to buy a vowel and this amount is removed from the active players bank. Once the active player buys the vowl they can guess a vowel, and if it is in the word they can continue their turn by choose to either spin the wheel, buy a vowel, or guess the word.

GUESS THE WORD:
This is the riskiest option. If the active player successfully guesses the word he wins that round and adds $1000 to his bank for round 1, $2000 for round 2, and $3000 for round 3. If the guess is unsuccessful then the turn goes to the next player.

ROUND THREE:
Only the player with the most money proceeds to round 3. Round three starts with "r","s","t","l","n", and "e" revealed, and the player can select 3 consonants and 1 vowel. He then gets one guess for the final word. If he correctly guesses the word he adds $3000 to his bank and the game is over. Otherwise he looses it all and walks home empty handed.

A .txt file receipt will be printed by the program with the players winnings if he won, or a thank you for playing if he lost.


