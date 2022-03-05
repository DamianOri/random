print("Type EXIT to exit.")
print("Type ERASE to erase the list.")
todo = "file path to a .txt file"        #sets todo as the file in which the list is stored
x = True                                 #for the while loop
a = open(todo, "a")                      #opens the todo file and sets it in append mode (add text to the end of the file)
while(x == True):
    stuff = input()
    if(stuff == "EXIT"):
        a.close()                        #closes the file and ends the while loop, closing the program
        x = False
    elif(stuff == "ERASE"):
        a = open(todo, "w")              #sets the todo file in write mode (overwrites the whole file)
        a.write("")                      #erases everything
        a = open(todo, "a")              #goes back to append mode
        print("List erased.")
    else:
        a.write(stuff+"\n")              #writes whatever the user wants and adds a new line so that the items are in seperate lines
