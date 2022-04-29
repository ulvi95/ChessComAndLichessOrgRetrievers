import tkinter as tk
import urllib
import urllib.request
import sys
import os
from datetime import date

def process():
    global List_of_Players
    List_of_Players=T.get(1.0, tk.END+"-1c")
    List_of_Players=List_of_Players.splitlines()

    today = date.today()
    d1 = today.strftime("%Y-%m-%d")

    for nickname in List_of_Players:
        if (nickname != "-") and (nickname != ""):
            username = nickname #change 
            baseUrl = "http://lichess.org/games/export/" + username + "?perfType=rapid,blitz,classical"
            myPath = os.getcwd() + os.sep + "LichessOrgGames" + os.sep + username + os.sep
            if not os.path.exists(myPath):
                os.makedirs(myPath)
            filename = "lichess_" + username + "_" + d1 + ".pgn"
            fullfilename = os.path.join(myPath, filename)
            urllib.request.urlretrieve(baseUrl, fullfilename) #change
            print(filename + " has been downloaded.")
    

if __name__ == "__main__":

    root = tk.Tk()
    
    root.geometry("600x600")
    
    T = tk.Text(root, height = 16, width = 16)
    
    l = tk.Label(root, text = "Enter the list of Lichess.org Players to Process")
    l.config(font =("Courier", 14))
    
    List_of_Players = ""
    
    b1 = tk.Button(root, text = "Process", command = lambda:process())
    
    b2 = tk.Button(root, text = "Exit",
    			command = root.destroy)
    
    l.pack()
    T.pack()
    b1.pack()
    b2.pack()
    
    T.insert(tk.END, List_of_Players)
    
    tk.mainloop()


