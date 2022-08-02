import random

while True:
  
    try:
      
        print("Let's play a game.")
        print("The goal of the game is to guess which number I'm thinking. You have three lives.")
        answer = input("Are you up for it?")
        
        if answer == 'y':
          
            print("Great! Let's begin.")
            print("My number is between one and ten. If you guess right, you win.")
            print("If you guess wrong... YOU DIE. Lmao, just kidding:)")
            rand = random.randrange(1, 10)
            guess1 = int(input("Now, which number am I thinking of?"))
            
            if guess1 is rand:
              
                print("You got it! That was quick!")
                break
                
            else:
              
                print("Sorry, incorrect! Two lives left!")
                guess2 = int(input("Guess again!"))
                
                if guess2 is rand:
                  
                    print("Congrats! You got it!")
                    break
                    
                else:
                  
                    print("Wrong! Last chance!")
                    guess3 = int(input("What's your final guess?"))
                    
                    if guess3 is rand:
                      
                        print("Phew! That was close! You guessed it!")
                        break
                        
                    else:
                      
                        print("No lives left! You lose! Guess what that means!")
                        print("...Time to die.")
                        break
                        
        elif answer == 'n':
          
            print("Okay, See ya!")
            break
            
        else:
          
            ranswer = input("I need a yes or no response from you.")
            
            if ranswer == 'yes':
              
                print("Let's get started then.")
                print("My number is between one and ten. If you guess right, you win.")
                print("If you guess wrong... YOU DIE. Lmao, just kidding:)")
                rand = random.randrange(1, 10)
                guess1 = int(input("Now, which number am I thinking of?"))
                
                if guess1 is rand:
                  
                    print("You got it! That was quick!")
                    break
                    
                else:
                  
                    print("Sorry, incorrect! Two lives left!")
                    guess2 = int(input("Guess again!"))
                    
                    if guess2 is rand:
                      
                        print("Congrats! You got it!")
                        break
                        
                    else:
                      
                        print("Wrong! Last chance!")
                        guess3 = int(input("What's your final guess?"))
                        
                        if guess3 is rand:
                          
                            print("Phew! That was close! You guessed it!")
                            break
                            
                        else:
                          
                            print("No lives left! You lose! Guess what that means!")
                            print("...Time to die.")
                            break
                            
            elif ranswer == 'n':
              
                print("Goodbye.")
                
            else:
              
                franswer = input("Dude for real.")
                
                if franswer == 'yes':
                  
                    print("Let's get started then.")
                    print("My number is between one and ten. If you guess right, you win.")
                    print("If you guess wrong... YOU DIE. Lmao, just kidding:)")
                    rand = random.randrange(1, 10)
                    guess1 = int(input("Now, which number am I thinking of?"))
                    
                    if guess1 is rand:
                      
                        print("You got it! That was quick!")
                        break
                        
                    else:
                      
                        print("Sorry, incorrect! Two lives left!")
                        guess2 = int(input("Guess again!"))
                        
                        if guess2 is rand:
                          
                            print("Congrats! You got it!")
                            break
                            
                        else:
                          
                            print("Wrong! Last chance!")
                            guess3 = int(input("What's your final guess?"))
                            
                            if guess3 is rand:
                              
                                print("Phew! That was close! You guessed it!")
                                break
                                
                            else:
                              
                                print("No lives left! You lose!)
                                break
                                
                elif franswer == 'n':
                                      
                    print("Goodbye.")
                    break
                                      
                else:
                                      
                    ffranswer = input("Last warning.")
                                      
                    if ffranswer == 'yes':
                                      
                        print("Let's get started then.")
                        print("My number is between one and ten. If you guess right, you win.")
                        print("If you guess wrong... YOU DIE. Lmao, just kidding:)")
                        rand = random.randrange(1, 10)
                        guess1 = int(input("Now, which number am I thinking of?"))
                                      
                        if guess1 is rand:
                                      
                            print("You got it! That was quick!")
                            break
                                      
                        else:
                                      
                            print("Sorry, incorrect! Two lives left!")
                            guess2 = int(input("Guess again!"))
                                      
                            if guess2 is rand:
                                      
                                print("Congrats! You got it!")
                                break
                                      
                            else:
                                      
                                print("Wrong! Last chance!")
                                guess3 = int(input("What's your final guess?"))
                                      
                                if guess3 is rand:
                                      
                                    print("Phew! That was close! You guessed it!")
                                    break
                                      
                                else:
                                      
                                    print("No lives left! You lose! Guess what that means!")
                                    print("...Time to die.")
                                    break
                                      
                    elif ffranswer == 'n':
                                      
                        print("Goodbye.")
                        break
                                      
                    else:
                                      
                        print("You have successfully broken the system!")
                        break
                                      
    except SyntaxError:
        break
