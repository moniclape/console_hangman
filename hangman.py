import random 

userlet = str(input("What difficulty level do you want to choose (easy , middle , hard?): " )) 
if userlet.strip() == "easy":
    with open('easy-words.txt', 'r') as file:
        rw = file.read().splitlines() #берет все слова из определенного документа
    rword = random.choice(rw) #рандомное слово из rw
    guesses = [] #лист где слово разделен на буквы(на _)б, и если пользователь написал правильную букву, лист изменяется
    for x in range (len(rword)):
        guesses.append("_")

elif userlet.strip() == "middle":
    with open('middle-words.txt', 'r') as file:
        rw = file.read().splitlines()
    rword = random.choice(rw)
    guesses = []
    for x in range (len(rword)):
        guesses.append("_")

elif userlet.strip() == "hard":
    with open('hard-words.txt', 'r') as file:
        rw = file.read().splitlines()
    rword = random.choice(rw)
    guesses = []    
    for x in range (len(rword)):
        guesses.append("_")

else:
    print("try again(")


chance = 7 #шансы
letguess = [] #буквы которые пользователь писал
print ("Hello! Welcome to the Hangman game!")
print ("There r " + str(len(rword)) + ", and u've " + str(chance) + " chances!")
print (*guesses)
userlet = str(input("Type a word (type \"stop\" if u want to stop): ")) #слово которое написал пользователь
letguess.append(userlet.lower())
print ("Guessed letters:")
print (*letguess, sep=", ")


while chance != 0:
    if userlet.lower() not in rword:
        chance -= 1

    print ("Chances: " + str(chance))
    i = -1
    for y in rword:
        i += 1
        if y == userlet.lower():
            guesses[i] = userlet.lower()

    print (*guesses)

    if "_" not in guesses:
        print ("U win!!!")
        break

    if chance == 0 or userlet == "stop":
        print ("U r die :(, and the word was:  " + str(rword))
        break

    userlet = str(input("Type again: "))
    print ("Guessed letters:")
    print (*letguess, sep=", ")

    if userlet.lower() in letguess or userlet == "" or userlet == " " or len(userlet) > 1:
        while userlet.lower() in letguess or userlet == "" or userlet == " " or len(userlet) > 1:
            userlet = str(input("Type another letter please: "))
            print ("Guessed letters:")
            print (*letguess, sep=", ")
    letguess.append(userlet)