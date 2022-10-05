#I made this to help people that uses minecraft DLL cheats such as NullDLL, MoonDLL, Fox or any other cheat.

#This will basically run the command "rundll32.exe dllyoudrag.dll asd" so you can just do that instead of using this dll executor.

import os

dll_file = input("Drag your dll file: ")

try:
    os.system("rundll32.exe "+dll_file+"do not close this window")
except:
    print("Failed")
    input("Press anything to exit...")