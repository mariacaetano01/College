from tkinter import *
from tkinter.ttk import *


def new_game():
    # choose new game name and open file
    new_game_file = Tk()
    new_game_file.title("Farm: New Game")
    new_game_file.geometry("200x200")
    
    new_name_text = "Text your name to load game"
    Label(new_game_file, text=new_name_text).pack()
    new_game_name = StringVar()
    Entry(new_game_file, textvariable=new_game_name).pack()
    
    print (str(new_game_name.get()))
    
    # STOPED HERE!!!! PROBLEMS WITH PY_VAR0 INSTEAD OF VAR NAME
    def new_game_root():
        new_game_win = Tk()
        new_game_win.title(f"{new_game_name}'s Farm")
        new_game_win.geometry('400x200')
        new_game_file.destroy()
        
    Button(new_game_file, text="Play", command=new_game_root).pack()
    
main_window = Tk()
main_window.title("Virtual Farm")
main_window.geometry("350x350")

# Texto de entrada
texto = """Choose an option
(change this later)
"""
t = Text(main_window, height=5, width=30)
t.insert(INSERT, texto)
t.pack()

# Botões do menu iniciar
new_game = Button(main_window, text="New Game", command=new_game).pack()
load_game = Button(main_window, text="Load Game").pack()

mainloop()

