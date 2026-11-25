# Queue_tool
This is an unofficial and completely free python script that makes a BEEP sound when the Reforger game queue is empty and you are entering the match.

Very recommended to check if this script works on your PC.
The BEEP is not affected by the Windows app mixer volume of the game and if you minimize the game, the script will keep working.


## How can I use it?
Start the game, get in an online match with a queue and start the script.
When the queue ends and you are entering the game you will hear a BEEP sound. (Please make sure that winsound.Beep(440,550) is okay for you before running the script)


## Do I have to change the code?
No, you do not have to change anything, but I recommend checking if this exists: C:\Users\ ....\Documents\My Games\ .
 .... is your windows user name and obviously you do not have to change it.

You MUST start the script after the game opened.
If you start it before entering a queue it should work anyway.
It works only one time, and if you want to use it again you will have to restart it.
If you start the game, start the script and close the game it will stop working

## Compatibility
It does not work on any linux OS or macOS.
It works only on Windows 11.
*It may work on Windows 10 but i did not test it.
You need Python 3.14 (Other versions may work too)
This must exist: C:\Users\ ....\Documents\My Games\ .
 .... is your windows user name and you do not have to change it.
You could still have problems with the path even if you check it because the path does not finish there.  

## Libraries used
os,
time,
winsound,

Look at the license before use.
I recommend checking the script yourself before running it.
Gionni1234 25/11/2026 (DD/MM/YYYY) V0.9
