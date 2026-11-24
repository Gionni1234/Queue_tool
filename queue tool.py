# Gionni1234 24/11/2026 (DD/MM/YYYY) V0.9
#Read the license and the README file before use
#Please make sure that winsound.Beep(440,550) is okay for you before running the script and check the other things that are on the README file
#I recommend reading and checking this script before running it.

import os
import time
import winsound

log_path=rf"C:\Users\{os.environ.get('USERNAME')}\Documents\My Games\ArmaReforger\logs"
file_path=rf"{log_path}\{max(os.listdir(log_path))}\console.log"
keyword = "Server Join"

with open(file_path, "r", encoding="utf-8", errors="replace") as file:
    file.seek(0,2)
    print("Program started\n Please make sure that winsound.Beep(440,550) is okay for you before running the script.")
    while True:
        sentence = file.readline()
        if keyword in sentence:
            print("Game started.\nProgram finished")
            #Beep
            winsound.Beep(440, 550)#Please make sure that winsound.Beep(440,550) is okay for you before running the script.
            break
        elif sentence=="":
            time.sleep(0.5)
        else:
            time.sleep(0.1)



