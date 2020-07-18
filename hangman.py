import random

hangman_words = ["python", "kotlin", "java", "javascript"]
random_hangman_word = random.choice(hangman_words)
dash = ["-"] * (len(random_hangman_word))

print("H A N G M A N\n")
n = 8
k = []
m = ''
while m != 'exit':
    m = input('Type "play" to play the game, "exit" to quit: ')
    if m != 'exit':
        while n > 0:
            rand_hm_wrd_lst = random_hangman_word.split()
            s = "".join(dash)
            # print([char for char in s])
            print("".join(dash))
            letter = input("Input a letter: ")

            if len(letter) < 2:
                if letter.isalpha() and letter.islower():
                    if letter in k:
                        print('You already typed this letter\n')
                    elif letter not in random_hangman_word:
                        n = n - 1
                        if n == 0:
                            print("No such letter in the word")
                        else:
                            print("No such letter in the word\n")
                    elif letter in [char for char in s]:
                        if n == 0:
                            print('You already typed this letter')
                        else:
                            print('You already typed this letter\n')
                    elif '-' not in [char for char in s] and [char for char in s].__len__() == len(random_hangman_word):
                        print('You guessed the word!\nYou survived!')
                    else:
                        for item in range(len(random_hangman_word)):
                            if random_hangman_word[item] == letter:
                                dash[item] = letter
                                print('')
                    k.append(letter)
                else:
                    print('It is not an ASCII lowercase letter\n')
                    k.append(letter)
            else:
                print('You should input a single letter\n')
                k.append(letter)
        else:
            print("You are hanged!")
    else:
        break
import random

hangman_words = ["python", "kotlin", "java", "javascript"]
random_hangman_word = random.choice(hangman_words)
dash = ["-"] * (len(random_hangman_word))

print("H A N G M A N\n")
n = 8
k = []
m = ''
while m != 'exit':
    m = input('Type "play" to play the game, "exit" to quit: ')
    if m != 'exit':
        while n > 0:
            rand_hm_wrd_lst = random_hangman_word.split()
            s = "".join(dash)
            # print([char for char in s])
            print("".join(dash))
            letter = input("Input a letter: ")

            if len(letter) < 2:
                if letter.isalpha() and letter.islower():
                    if letter in k:
                        print('You already typed this letter\n')
                    elif letter not in random_hangman_word:
                        n = n - 1
                        if n == 0:
                            print("No such letter in the word")
                        else:
                            print("No such letter in the word\n")
                    elif letter in [char for char in s]:
                        if n == 0:
                            print('You already typed this letter')
                        else:
                            print('You already typed this letter\n')
                    elif '-' not in [char for char in s] and [char for char in s].__len__() == len(random_hangman_word):
                        print('You guessed the word!\nYou survived!')
                    else:
                        for item in range(len(random_hangman_word)):
                            if random_hangman_word[item] == letter:
                                dash[item] = letter
                                print('')
                    k.append(letter)
                else:
                    print('It is not an ASCII lowercase letter\n')
                    k.append(letter)
            else:
                print('You should input a single letter\n')
                k.append(letter)
        else:
            print("You are hanged!")
    else:
        break
