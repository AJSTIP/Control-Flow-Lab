import random
name = "Aj"
question = "My name is Aj?"
answer = ""

random_number = random.randint(1, 14)
# print(rand)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "Ask Again Later."
elif random_number == 12:
    answer = "No."
elif random_number == 13:
    answer = "Most Likley."
elif random_number == 14:
    answer = "Conentrate and ask again."
else:
    answer = "Error"

if name == "":
    print(question)
    print("Magic 8 Ball's answer: " + answer)
elif question == "":
    print("Please Make sure you Input a question for the magic 8 ball!")
else:
    print(name + " asks: " + question)
    print("Magic 8 Ball's answer: " + answer)
