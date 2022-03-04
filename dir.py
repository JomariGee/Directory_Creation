#File Creation
import os
import colorama
from colorama import Fore

def main(): #Print current working directory
    print( "--------------------" *2)
    path = os.getcwd()
    print("Current Directory: ", path)
    print( "--------------------" *2) 
    options()

def options(): #Options to interact with
    print (Fore.WHITE + """\nOptions 
    [-c] --- Comma Seperated Files 
    [-m] --- Enter files manually 
    [-d] --- Change Directories
    [exit] --- Exit Program
    """)
    try:
        user_selection = input(Fore.BLUE +"Select an option: " + Fore.WHITE)
        if user_selection == '-c':
            comma_seperated_file_creation()
        elif user_selection == '-m':
            manual_file_creation()
        elif user_selection == '-d':
            change_directory()
        elif user_selection == 'exit':
            exit
        else:
            options()
    except KeyboardInterrupt: #In-case Ctrl+C is pressed
        print(Fore.RED + "\n[x]Bye!\n" + Fore.WHITE)
        exit

def comma_seperated_file_creation(): #While loop for creating directories
    while True:
        try: 
            print("""
            Example: File1,File2,File3
            Hit Ctrl+C to exit
            """)
            file_creation = input(Fore.WHITE +"Enter the filename: ").split(",") #Drop the comma off filenames for creation
            for unlisted_files in file_creation: #Loop through each split string to create files
                try:
                    os.mkdir(unlisted_files)
                    print(Fore.GREEN + "File created for:", unlisted_files + Fore.WHITE)
                except FileExistsError: #Show error, already created file and move to next file
                    print(Fore.RED + "\t[x]File:",unlisted_files,"already exists" + Fore.WHITE)
                    pass
                except KeyboardInterrupt: #Handle Ctrl+C being pressed
                  print(Fore.RED + "\n[x]Bye!\n" + Fore.WHITE)
                  exit
        except KeyboardInterrupt: #In-case Ctrl+C is pressed
            print(Fore.RED + "\n[x]Bye!\n"+ Fore.WHITE)
            break
        except FileNotFoundError: #Error if noting is entered 
            print(Fore.RED + "\t[x]Enter your files" + Fore.WHITE)
            comma_seperated_file_creation()

def manual_file_creation(): #Manual file creation 
        while True:
            try: 
                file_creation = input(Fore.WHITE + "\nEnter the filename: ")
                if file_creation == 'exit':
                    print(Fore.GREEN + "\n\tAll your files have been created!\n" + Fore.WHITE)
                    break
                elif file_creation == '': #Deals with no input
                    manual_file_creation()
                else: 
                    os.makedirs(file_creation)
                    print(Fore.GREEN + "\nFile created for:", file_creation + Fore.WHITE)
            except FileExistsError:  #Handle file already being created
                print(Fore.RED + "\n[X]File:",file_creation,"already exists" + Fore.WHITE)
            except KeyboardInterrupt: #Handle Ctrl+C being pressed
                print(Fore.RED + "\n[x]Bye!\n" + Fore.WHITE)
                break

def change_directory():#Change current directory
    try:
        print(Fore.BLUE +"""\nLet's change your directory!\n
                ------------------------------------------------------
                - Example Directory
                    C:\\Users\\mrjam\\OneDrive\\Desktop\\Misc\\Python
                - Enter 'back' to go back
                ------------------------------------------------------
        """ + Fore.WHITE)
        path = input(Fore.WHITE +"Specify a path to write to: ")
        if path == 'back':
            options()
        else:
            os.chdir(path)
            print(Fore.BLUE +"Current Directory is now: ",path)
            options()
    except OSError: #Handle nothing being entered
        print(Fore.RED + "\n[x]Please enter something" + Fore.WHITE)
        change_directory()
    except KeyboardInterrupt:#Handle Ctrl+C being pressed
        print(Fore.RED + "\n[x]Bye!\n" + Fore.WHITE)
        exit
 
def header(): #Gotta have ASCII art :)
    print(Fore.BLUE + """
██████╗░██╗██████╗░░░░██████╗░██╗░░░██╗
██╔══██╗██║██╔══██╗░░░██╔══██╗╚██╗░██╔╝
██║░░██║██║██████╔╝░░░██████╔╝░╚████╔╝░
██║░░██║██║██╔══██╗░░░██╔═══╝░░░╚██╔╝░░
██████╔╝██║██║░░██║██╗██║░░░░░░░░██║░░░
""")

#These modules are ran
header()
main()
