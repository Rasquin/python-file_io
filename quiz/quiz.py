# -----------------------------------------------------1st FUNCTION WE CREATE
def show_menu():  
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option= input("Enter option: ")
    return option
    
#print(show_menu())  # ----> That was to check that the show_menu() function works


#-------------------------------------------------------4rd FUNCTION WE CREATE

def ask_questions():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
 
    for i, text in enumerate(lines): # Our questions and our answers get appended into the two lists.
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    number_of_questions = len (questions)
    questions_and_answers = zip(questions, answers)  #zip function to put them together. 
    
    score = 0
       
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score =+ 1
            print ("Right!")
            print(score)
        else:
            print("Wrong :(")
    
    print("You got {0} correct out of {1}".format(score, number_of_questions))
    

#-------------------------------------------------------3rd FUNCTION WE CREATE

def add_question():
    print("")
    question = input("Enter a question\n>")
    
    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n>".format(question)) #we'll take the question that we'd already asked, do a blank line, a greater-than sign for a prompt
    
    file = open("questions.txt","a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

#-------------------------------------------------------2nd FUNCTION WE CREATE
def game_loop():
    while True:
        option=show_menu() # we introduce the value of the option
        if option == "1" :
            #print("You selected 'Ask questions'")
            ask_questions()
        elif option == "2" :
            # print("You selected 'Add a question'")
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")
        
game_loop()