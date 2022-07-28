import os
import shutil
import argparse

files_list = os.listdir("files")  # List of the files and folders contained in the 'files' folder

extensions = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Docs": [".doc", ".txt", ".odt"],
    "Audio": [".mp3"]
}


def files_order(file_to_move):
    """the function is defined to work along with the argparse module, it takes one argument (input from the command
    line), which will be parsed. The argument must be a valid file name. The function will then identify it and, in case
    it's a file, it will automatically move it in a directory based on the file's extension E.g. .txt will be moved in
    the doc directory, .mp3 will be moved in the audio directory. If a directory does not exist, the function will
    automatically create it and then move the file in it. If the file will be correctly moved, the function return a
    string stating the directory from which the file was taken, and the directory in which the file was moved. If the
    argument passed is not a valid name or the file does not exist in the files directory, the function will return a
    string stating that the file does not exist indeed."""
    cwd = os.getcwd()  # Path of the current working directory
    if os.path.isfile(f"files/{file_to_move}"):

        """
        ho eliminato il ciclo, al posto di controllare che esiste un file che si chiami come il nome fornito dall' 
        utente controllo direttamente che quel file esista e se esiste utilizzo le sue info per (eventualmente) creare
        una cartella e stampare informazioni
        """
        file_name, extension = os.path.splitext(file_to_move)  # Isolating the file extension
        for key in extensions:  # Looping over the dictionary, "key" will be equal to the dictionary key on each loop
            if extension in extensions[key]:  # Checking that the file extension is in my dictionary

                # Checking that there is a directory named after the dictionary key, if it does not exist, I create it.
                if not os.path.isdir(f"files/{key}"):
                    os.makedirs(f"files/{key}")
                src = f"files/{file_to_move}"  # Creating a variable with the path of origin
                dst = f"files/{key}/{file_to_move}"  # And one with the destination path
                shutil.move(src=src, dst=dst)  # Moving the file from source to destination
                file_info = f"{file_name} type: {key} size: {os.path.getsize(dst)}B"  # The information in the file
                return f"{file_info} was correctly moved from {cwd}/{src} to {cwd}/{dst}"
    else:
        return f"{file_to_move} does not exist"

    """
    l' else di prima aspettava di verificare che l' intero ciclo finisse, e nel caso di risposta negativa veniva 
    eseguito, l' ho inserito come else clause del ciclo for perché se indentavo come else clause dell' if statement
    di controllo, mi veniva stampato per ogni ciclo del file.  Però come nell' esempio dei commenti, l' else viene 
    eseguito comunque a fine ciclo a meno che non ci sia una prova di interruzione. La mia idea era quella di 
    utilizzare return come prova del successo o meno del ciclo (e come prova di interruzione). Nel caso in cui  non 
    avessi avuto un return, allora sarebbe stato eseguito l' else clause. Forse questo è un caso particolar in cui me 
    la sono cavata grazie alla presenza di return, che deve essere univoco, ma invece che comunicare subito che il file
    non esiste, lo script eseguiva prima tutto il ciclo, con un carico inutile, per poi comunicare all' utente che 
    il file non esiste. Di norma l' else di un for loop viene sempre eseguito ad esaurimento ciclo a meno che non 
    incontri un break statement, che avrei dovuto implementare.  la clausola diventi falsa (while loop)
     
     Ora è semplicemente un else in alternativa al False state dell' if statement di controllo 
     per l' esistenza del file fornito dall' utente
    """


# Creating an object of type ArgumentParser to which I will associate the various arguments and options that I want to use
parser = argparse.ArgumentParser(
    description="""
The script will move a file from his original directory to another based on its extension. If the directory doesn't
exist, the script will automatically create one, named with the extension's type name. E.g. .mp3 -->Audio, .txt -->Docs
""")

# Using parser.add_argument, I add the required and optional parameters that need to be written in the cmd. 
# In this case I will add the name of the file I want to move, as well as the parameter of the function defined at the 
# Beginning of the script. The function I created takes only one argument, so I add it making it mandatory to insert it 
# In order for the script to work correctly, in case of missing data, the user will be warned
parser.add_argument(
    # The argument is implicitly required as it is declared as a positional argument and not as a series of flags 
    # Therefore the "required = True" parameter is not necessary, since it is only needed in the case of optional arguments
    "file_to_move",  # The argument received as input by the user which will then be processed by the function
    type=str,  # The type of the argument
    # A brief description of what the entered argument represents
    help="This is the name of the file to move, type the name of the file with its extension E.g. 'Hello.txt'"
)

# After defining the assignment of the arguments, I proceed with the actual assignment by calling parse_args on the created object (parser)
args = parser.parse_args()

# Then I call the defined function passing args.file_to_move as argument, in this way the instructions defined by the argparse module 
# Will be applied on the parameter passed to the function, in order to view the result, I send it to print
print(files_order(args.file_to_move))