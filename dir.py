#File Creation
import os

#Print current working directory
def main():
    print( "--------------------" *2)
    path = os.getcwd()
    print("Current Directory: ", path)
    print( "--------------------" *2)
    options()

#Options to interact with
def options():
    print ("""\nOptions 
    [-c] --- Comma Seperated Files (working-on)
    [-f] --- Read from a file (un-built)
    [-m] --- Enter files manually 
    [-d] --- Change Directories
    [exit] --- Exit Program
    """)
    try:
        user_selection = input("Select an option: ")
        if user_selection == '-c':
            comma_seperated_file_creation()
        elif user_selection == '-f':
            print("Not built yet :)")
        elif user_selection == '-m':
            manual_file_creation()
        elif user_selection == '-d':
            change_directory()
        elif user_selection == 'exit':
            exit
        else:
            user_selection = input("Select an option: ")
    # Error handling
    except FileNotFoundError:
        print()
    except KeyboardInterrupt:
        print("\n[x]Bye!\n")
        exit

#While loop for creating directories
def comma_seperated_file_creation():
    while True:
        try: 
            print("\n\tExample: File1,File2,File3")
            file_creation = input("\nEnter the filenames: ")
            if file_creation == 'exit':
                print("\n\tAll your files have been created!\n")
                break
            elif file_creation == 'd':
                os.makedirs(file_creation)
            else: 
                print("\n[x]Didn't work :(")
                print("\tExample: File1,File2,File3")
                file_creation = input("\nEnter the filename: ")
        #Handle file already being created
        except FileExistsError:
            print("\n[X] This file already exists, please choose a different name!")
        #Handle Ctrl+C being pressed
        except KeyboardInterrupt:
            print("\n[x]Bye!\n")
            break

#Manual file creation 
def manual_file_creation(): 
        while True:
            try: 
                file_creation = input("\nEnter the filename: ")
                if file_creation == 'exit':
                    print("\n\tAll your files have been created!\n")
                    break
                elif file_creation == '':
                    file_creation = input("\nEnter the filename: ")
                else: 
                    os.makedirs(file_creation)
            #Handle file already being created
            except FileExistsError:
                print("\n[X] This file already exists, please choose a different name!")
            #Handle Ctrl+C being pressed
            except KeyboardInterrupt:
                print("\n[x]Bye!\n")
                break

#Change current directory
def change_directory():
    try:
        print("""\nLet's change your directory!\n
                ------------------------------------------------------
                - Example Directory
                    C:\\Users\\mrjam\\OneDrive\\Desktop\\Misc\\Python
                - Enter 'back' to go back
                ------------------------------------------------------
        """)
        path = input("Specify a path to write to: ")
        if path == 'back':
            options()
        else:
            os.chdir(path)
            print("Current Directory is now: ",path)
            options()
    #Handle the file already being created 
    except FileNotFoundError:
        print("\n[x]File not found")
        change_directory()
    #Handle OSError
    except OSError:
        print("\n[x]Please enter something")
        change_directory()
    #Handle Ctrl+C being pressed
    except KeyboardInterrupt:
        print("\n[x]Bye!\n")
        exit

#Gotta have ASCII art :)
def header():
    print("""

██████╗░██╗██████╗░░░░██████╗░██╗░░░██╗
██╔══██╗██║██╔══██╗░░░██╔══██╗╚██╗░██╔╝
██║░░██║██║██████╔╝░░░██████╔╝░╚████╔╝░
██║░░██║██║██╔══██╗░░░██╔═══╝░░░╚██╔╝░░
██████╔╝██║██║░░██║██╗██║░░░░░░░░██║░░░
""")

#Run these modules
header()
main()