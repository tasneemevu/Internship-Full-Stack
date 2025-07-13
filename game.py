import random;

while True:
    my_answer = input("Choose : rock, paper, scissors: ")
    my_answer = my_answer.lower()
    computer_answer = random.choice(["rock", "paper", "scissors"])

    if my_answer!= "rock" and my_answer != "paper" and my_answer != "scissors":
        print("Wrong input")
        continue
    print(f"Computer chose: {computer_answer}")

    if my_answer == computer_answer:
        print("It's a tie!")
        continue

    elif (my_answer == "rock" and computer_answer == "scissors") or \
         (my_answer == "paper" and computer_answer == "rock") or \
         (my_answer == "scissors" and computer_answer == "paper"):
        print("You win!") 
        break
    else:
        print("You lose! Play again.") 
    