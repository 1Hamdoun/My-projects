print("Welcome to my math quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is 1 + 1 equal to? ")
if answer.lower() == "2":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is 5 * 4 equal to? ")
if answer.lower() == "20":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is 10/2 equal to? ")
if answer.lower() == "5":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is 10**2 equal to? ")
if answer.lower() == "100":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")