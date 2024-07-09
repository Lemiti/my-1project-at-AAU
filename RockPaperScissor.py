from getpass import getpass #this library(getpass) is used to hide text which are inputed.
import random# used to generate random letters for the computer
print("Hello everyone!")

Intro = input("Do you want to play Rock Paper Scissor?\n -")
if Intro == "yes" or Intro=="Yes":   
    choice=input("DO YOU WANT TO PLAY WITH AI OR YOU FREIND? PRESS \"1\"FOR FRIEND AND PRESS \"2\" FOR AI \n>>")
    if choice == "1": #the following code will be excuted only if the user want to play with friend   
        player_1 = input("Input your name please player1.\n-").upper()
        player_2 = input("Input your name bellow please player2.\n-").upper()
        print("You ""\033[34m",player_1,"\033[0mand\033[35m ",player_2,"\033[0mare about to start the game now.") # '\033_m' is used to color our names.
        print("You have to choose only R for rock, P for paper and S for scissor.")
        
        
        score_p1 = 0 #score_p1  will count the score for player_1
        score_p2 = 0 #score_p2 will count the score for player_2
        draw_score = 0 # this one will count only the draw       
        while True:
            permission = input("Do you want to continue?\n ?") #per stands for permission
            if permission == "Yes" or permission == "yes":
                print(player_1, "put your choice bellow.")
                choice_1 = getpass(" >").upper()
                print( player_2, "put your choice bellow.")
                choice_2 = getpass(" >").upper()
                
                x=(player_1 ,"chose",choice_1,"and",player_2,"chose",choice_2)
                
                if choice_1 in ("R","P","S") and choice_2 in ("R","P","S"):
                    if choice_1 == choice_2:

                        draw_score += 1
                        print("DRAW")
                        print(x)
                    elif choice_1 == "R" and choice_2 == "S":
                        score_p1 += 1
                        print(player_1, "is winner. Congrats ", player_1, "!")
                        print(x)
                    elif choice_1 == "P" and choice_2 == "R":
                        score_p1 += 1
                        print(player_1, "is winner. Congrats ", player_1, "!")
                        print(x)
                    elif choice_1 == "S" and choice_2 == "P":
                        score_p1 += 1
                        print(player_1, "is winner. Congrats ", player_1, "!", score_p1, ":",score_p2)
                        print(x)
                    else:
                        score_p2 += 1
                        print(player_2, "is winner. Congrats ", player_2, "!", score_p2, ":", score_p1)
                        print(x)
                                    #The above "if else" condition is used to check the winner and store the score
                                    
                                    #The bellow "if else" condition is used to end the game and announce the winner. 
                    if score_p1 == 3:
                        print(player_1," is winner with score ",score_p1, ":",score_p2)
                        break
                       
                    elif score_p2 == 3:
                        print(player_2," is winner with score ",score_p2, ":",score_p1)
                        break
                    
                    else:
                        continue
                    
                else:
                    print("You put invalid choice. Please choose only from R, S and P.")
                  
            elif permission == "no" or permission == "No": #this thing has to end and display the result of the game
                #print("Your score were ",score_p1,":",score_p2,"\n Have a good time!")
                break

            else:
                print("You didn't insert an appropriate answer.")
                continue
        print(player_1,"score was:",score_p1,"and",score_p2,"for",player_2)
        print("you guys drew each other score of:",draw_score)
                
    elif choice=="2": # The following will be excuted only if the user want to play with the AI and choose the appropriate key
           
        AIname = "AiRobot" 
        player1=input("Please put your name bellow \n>>")
        print("Hello! ",player1,". You are going to play with ",AIname,".")
        print()
        
        AIscore = 0 #Scores for the AI
        player1_score = 0 #Scores for the player
        draw_score=0
        while True:
            permission = input("DO YOU WANT TO CONTINUE THE GAME?\n>>")
            if permission=="yes" or permission=="Yes":
                print(player1, "put your choice bellow.")
                choice_1 = input(" >").upper()
                AIchoice="RPS"#change into AIname              #this function makes the choice for the robot
                choice_2=(random.choice(AIchoice))
                if choice_1 in ("R","P","S") and choice_2 in ("R","P","S"):
                    if choice_1 == choice_2:

                        draw_score += 1
                        print("DRAW")
                    elif choice_1 == "R" and choice_2 == "S":
                        player1_score += 1
                        print("You win this game")
                    elif choice_1 == "P" and choice_2 == "R":
                        player1_score += 1
                        print("You win this game")
                    elif choice_1 == "S" and choice_2 == "P":
                        player1_score+= 1
                        print("You win this game", player1_score, ":",AIscore)
                    else:
                        AIscore += 1
                        print("You lost this round", AIscore, ":", player1_score)
                                    #The above "if else" condition is used to check the winner and store the score
                                    
                                    #The bellow "if else" condition is used to end the game and announce the winner. 
                    if player1_score == 3:
                        print(player1," is winner with score ",player1_score, ":",AIscore)
                        break
                       
                    elif AIscore == 3:
                        print(AIname," is winner with score ",AIscore, ":",player1_score)
                        break
                    
                    else:
                        continue
                else:
                    print("You have inserted an invalid key.")
                    continue
            elif permission == "no" or permission == "No":
                print("Goodbye",player1)
            else:
                print("You didn't insert an appropriate answer.")
            continue
    else:
       print()
elif Intro == "no":
      print("Have a good time! See you when you want to play.")
else:
      print("You did'nt answer my question in appropriate way. Goodbye!")    

