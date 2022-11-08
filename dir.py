#------------------------------------
# Overkill file creation for Windows 
#------------------------------------
import os
import colorama
from colorama import Fore, Style

#Necessary for colorama to properly work on Windows
colorama.init()
os.system("cls" or "clear")

#Print current working directory
def main(): 
    print( "--------------------" *2)
    path = os.getcwd()
    print("Current Directory: ", path)
    print( "--------------------" *2) 
    options()

#Options to interact with
def options(): 
    print (Fore.WHITE + """\nOptions 
    [-c] --- Comma Separated Files 
    [-m] --- Enter files manually 
    [-d] --- Change Directories
    [exit] --- Exit Program
    """)
    try:
        user_selection = input(Fore.BLUE +"Select an option: " + Style.RESET_ALL)
        if user_selection == '-c':
            comma_separated_file_creation()
        elif user_selection == '-m':
            manual_file_creation()
        elif user_selection == '-d':
            change_directory()
        elif user_selection == 'exit':
            exit
        else:
            options()
    except KeyboardInterrupt: #In-case Ctrl+C is pressed
        print(Fore.RED + "\n[x]Bye!\n"  + Style.RESET_ALL)
        exit
#While loop for creating directories
def comma_separated_file_creation(): 
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
                    print(Fore.GREEN + "File created for:", unlisted_files  + Style.RESET_ALL)
                except FileExistsError: #Show error, already created file and move to next file
                    print(Fore.RED + "\t[x]File:",unlisted_files,"already exists"  + Style.RESET_ALL)
                    pass
                except KeyboardInterrupt: #Handle Ctrl+C being pressed
                  print(Fore.RED + "\n[x]Bye!\n"  + Style.RESET_ALL)
                  exit
        except KeyboardInterrupt: #In-case Ctrl+C is pressed
            print(Fore.RED + "\n[x]Bye!\n" + Style.RESET_ALL)
            break
        except FileNotFoundError: #Error if noting is entered 
            print(Fore.RED + "\t[x]Enter your files"  + Style.RESET_ALL)
            comma_separated_file_creation()()

#Manual file creation 
def manual_file_creation(): 
        while True:
            try: 
                file_creation = input(Fore.WHITE + "\nEnter the filename: ")
                if file_creation == 'exit':
                    print(Fore.GREEN + "\n\tAll your files have been created!\n"  + Style.RESET_ALL)
                    break
                elif file_creation == '': #Deals with no input
                    manual_file_creation()
                else: 
                    os.makedirs(file_creation)
                    print(Fore.GREEN + "\nFile created for:", file_creation  + Style.RESET_ALL)
            except FileExistsError:  #Handle file already being created
                print(Fore.RED + "\n[X]File:",file_creation,"already exists"  + Style.RESET_ALL)
            except KeyboardInterrupt: #Handle Ctrl+C being pressed
                print(Fore.RED + "\n[x]Bye!\n"  + Style.RESET_ALL)
                break

#Change current directory
def change_directory():
    try:
        print(Fore.BLUE +"""\nLet's change your directory!\n
                ------------------------------------------------------
                - Example Directory
                    C:\\Users\\mrjam\\OneDrive\\Desktop\\Misc\\Python
                - Enter 'back' to go back
                ------------------------------------------------------
        """  + Style.RESET_ALL)
        path = input(Fore.WHITE +"Specify a path to write to: ")
        if path == 'back':
            options()
        else:
            os.chdir(path)
            print(Fore.BLUE +"Current Directory is now: ",path + Style.RESET_ALL)
            options()
    except OSError: #Handle nothing being entered
        print(Fore.RED + "\n[x]Please enter something" + Style.RESET_ALL)
        change_directory()
    except KeyboardInterrupt:#Handle Ctrl+C being pressed
        print(Fore.RED + "\n[x]Bye!\n"  + Style.RESET_ALL)
        exit

#Gotta have ASCII art :) 
def header(): 
    print(Fore.BLUE + """
██████╗░██╗██████╗░░░░██████╗░██╗░░░██╗
██╔══██╗██║██╔══██╗░░░██╔══██╗╚██╗░██╔╝
██║░░██║██║██████╔╝░░░██████╔╝░╚████╔╝░
██║░░██║██║██╔══██╗░░░██╔═══╝░░░╚██╔╝░░
██████╔╝██║██║░░██║██╗██║░░░░░░░░██║░░░
""")

if __name__ =="__main__":
    header()
    main()
