# scramble
Scramble game.

The objective of the game is to order the scrambled letters of a sentence into the correct oder, by switching the places of pairs of letter, one pair at a time. In each word, the first and last letters will always be correct. There can be single-word setences.

Functionalities:
1. A new game starts each time the program is started. The word or sentence played is selected randomly by the program from one of the entries stored in a text file. The program scrambles the word or sentence in the following way: the first and last lettter of each word are kept in their place, the rest are shuffled randomly. The game starts with a score equal to the number of letters in the give word or sentence, not counting spaces. The scrambled sentence is printed at the console.

2. The user can swap two letter using the following command: swap<word1><letter1>-<word2><letter2>. The word/letter parameter pairs illustrate the indices of the word and letter to be swapped. After every swap, the updated sentence is printed to the console. In case the command is not complete, one of the indices supplied is incorrect or indicies include the first or last letter of a word, the program will provide an error message. 

3. Each time the user swaps two letters, their score is decreased by 1. The updated score is printed to the console.

4. The user can undo the last swap operation. This does not affect the score.

5. The games ends when one of the following contitions are met: player's score if 0(defeat), or the letters comprising the sentence are put into correct order(victory). In either case, the player receives a corresponding message.
