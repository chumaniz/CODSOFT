import random 

print('Welcome to a simple gamme of RPS!\n')
print('Here are the rules: \n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print('''Enter your choice please
          1-Rock
          2-Paper
          3-Scissors
          ''')
    
    choice = int(input("Enter your choice: "))
    # If conitions are met, then the loop will be deemed true

    # Validating user choices
    if choice == 1:
        choice_item = 'rock'
    elif choice == 2:
        choice_item = 'paper'
    elif choice == 3:
        choice_item = 'scissors'
    else:
        print("Please pick a valid choice!\n")


    # Print user choice
    print('Your choice is, \n' + choice_item)
    print("Alright, turn over, now for the PC...\n")

    # The computer will pick at random
    pc_turn = random.randint(1,3)

    while pc_turn == choice:
        pc_turn = random.randint(1,3)

    # Validating the choice of computer
    if pc_turn == 1:
        pc_item = 'Rock'
    elif pc_turn == 2:
        pc_item = 'Paper'
    elif pc_turn == 3:
        pc_item = 'Scissors'
    else:
        print("Pick a valid answer please PC\n")

    print("PC's choice is...", pc_item)
    print("Alright, now its PC vs You\n")

    # Validating a draw
    if choice == pc_turn:
        print("It is a draw\n", end="")
        result="DRAW"

    # Validating a win
    if choice == 1 and pc_turn ==2:
        print("PC wins using...paper!", end="")
        result="Paper" 
    elif choice == 2 and pc_turn ==1:
        print("You win using...paper!\n", end="")
        result="paper" 
    
    if choice==2 and pc_turn==3:
        print('PC wins using...scissors!\n',end="")
        result='Scissors'
    elif choice==3 and pc_turn==2:
        print('You win using Scissors!\n',end="")
        result='scissors'

    if choice==3 and pc_turn==1:
        print("PC wins with...rock!\n", end="")
        result="Rock"
    elif choice==1 and pc_turn==3:
        print("You win with...rock!\n", end="")
        result="rock"
    

     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>\n")
    if result == choice_item:
        print("<== User wins ==>\n")
    else:
        print("<== Computer wins ==>\n")
    print("Do you want to play again? (Y/N)\n")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans =='n':
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")

