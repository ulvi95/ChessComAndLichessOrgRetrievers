import tkinter as tk
import urllib
import urllib.request
import sys
import os
import json

def process():
    global List_of_Players
    global pgn_games
    List_of_Players=T.get(1.0, tk.END+"-1c")
    List_of_Players=List_of_Players.splitlines()

    for nickname in List_of_Players:
        if (nickname != "-") and (nickname != ""):
            username = nickname.lower() #change 
            baseUrl = "https://api.chess.com/pub/player/" + username + "/games/"
            archivesUrl = baseUrl + "archives"
            
            #read the archives url and store in a list
            f = urllib.request.urlopen(archivesUrl)
            archives = f.read().decode("utf-8")
            archives = archives.replace("{\"archives\":[\"", "\",\"")
            archivesList = archives.split("\",\"" + baseUrl)
            archivesList.remove('')
            archivesList[len(archivesList)-1]=archivesList[len(archivesList)-1][0:7]
            
            
            
            #download all the archives
            for i in range(len(archivesList)):
                myPath = os.getcwd() + os.sep + "ChessComGames" + os.sep + username + os.sep
                if not os.path.exists(myPath):
                    os.makedirs(myPath)
                url = baseUrl + archivesList[i]
                f = urllib.request.urlopen(url)
                test = json.load(f)
                List_of_Players = test
                for i in range(len(test['games'])):
                    if('pgn' in test['games'][i]):
                        if((test['games'][i]['rules'] == 'chess') and (test['games'][i]['time_class'] != 'bullet')):
                            pgn_games = pgn_games+(test['games'][i]['pgn'])+"\n\n"
            filename = "ChessCom_"+username+".pgn"
            fullfilename = os.path.join(myPath, filename)
            file_results_log = open(fullfilename,"w+", encoding="utf-8")
            file_results_log.write(pgn_games)
            file_results_log.close()
            pgn_games=""
                #print(filename + " has been downloaded.")
            print("All files have been downloaded.")
    

if __name__ == "__main__":

    root = tk.Tk()
    
    root.geometry("600x600")
    
    T = tk.Text(root, height = 16, width = 16)
    
    l = tk.Label(root, text = "Enter the list of Chess.com Players to Process")
    l.config(font =("Courier", 14))
    
    List_of_Players = ""
    pgn_games = ""
    
    b1 = tk.Button(root, text = "Process", command = lambda:process())
    
    b2 = tk.Button(root, text = "Exit",
    			command = root.destroy)
    
    l.pack()
    T.pack()
    b1.pack()
    b2.pack()
    
    T.insert(tk.END, List_of_Players)
    
    tk.mainloop()