# Create multiple folders in current directory
import os

def main():
    print("\n" + "----------------" *3)
    print("Hello, I'm here to help you make files.")
    print("Enter 'stop' to stop the program!")
    print("----------------" *3)

def creating_files():
    while True:
        try: 
            file_creation = input("\nEnter the filename: ")
            if file_creation == 'stop':
                break
            else: 
                os.makedirs(file_creation)
        except FileExistsError:
            print("\n[X] This file already exists, please choose a different name!")
        except KeyboardInterrupt:   
            print("\n[X] Enter 'stop' to exit")

def end_statement():
    print("\nAll your files have been created")

main()
creating_files()
end_statement()