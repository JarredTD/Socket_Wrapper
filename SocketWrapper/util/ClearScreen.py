from os import system, name

def clear():
    '''
    Checks what OS the user is on, and runs the appropriate command to clear the terminal
    '''
    if name == 'nt':
        _ = system('cls')
    else: # For mac and linux(here, os.name is 'posix')
        _ = system('clear')