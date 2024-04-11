def menu():
    print("[1] option 1")
    print("[2] option 2")
    print("[3] option 3")
    print("[0] option Exit the program. ")
    
def option3():
    print("option3 has been called")
    
    menu()
    option = int(input("Enter your option: "))
    
    while option != 0:
        if option == 1:
            #option 1 stuff
            print("Option 1 has been called. ")
        elif option == 2:
            #optoin 2 stuff
            print("Option 2 has been called. ")
        elif option == 3:
            option3()
        else:
            print("Invalid Option. ")
            
        print()
        menu()
        option = int(input("Enter your option: "))
        
    print("Thanks for  using this program. Goodbye. ")

