secret_word = "giraffe"
guess = ""
tries = 0
tries_limit = 4
out_of_tries = False

while guess != secret_word and not out_of_tries:
    if tries < tries_limit:
        guess = input("Enter guess: ")
        tries += 1
    else:
        out_of_tries = True

if out_of_tries:
    print("You are out of tries!")
else:
    print("Congrats! You have guessed the secret word")
