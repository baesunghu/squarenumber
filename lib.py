import random
import win32print
import time
isPrinting = False
PrinterList = []

class lib():

    def __init__(self,level):
        self.level = level
    def print_menu(self):
        print("===================================================================================================================")
        print("|                                                                ___.                                                |")
        print("|   ______________ _______ _______   ____     ____  __ __  _____\_ |__   ___________     _________    _____   ____  |")
        print("|  /  ___/ ____/  |  \__  \\_  __ \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \   / ___\__  \  /     \_/ __ \  |")
        print("|  \___< <_|  |  |  // __ \|  | \/\  ___/  |   |  \  |  /   Y Y  \ \_\ \  ___/|  | \/  / /_/  > __ \|  Y Y  \  ___/  |")
        print("| /____  >__   |____/(____  /__|    \___  > |___|  /____/|__|_|  /___  /\___  >__|     \___  (____  /__|_|  /\___  >|")
        print("|      \/   |__|          \/            \/       \/            \/    \/     \/        /_____/     \/      \/     \/ |")
        print("|  ____                                                                                                             |")
        print("| /_   |       ____ _____    _________.__.                                                                          |")
        print("|  |   |     _/ __ \\__  \  /  ___<   |  |                                                                           |")
        print("|  |   |     \  ___/ / __ \_\___ \ \___  |                                                                          |")
        print("|  |___| /\   \___  >____  /____  >/ ____|                                                                          |")
        print("|        \/       \/     \/     \/\/                                                                                |")
        print("| ________       .__                     .___                                                                       |")
        print("| \_____  \      |  |__ _____ _______  __| _/                                                                       |")
        print("|  /  ____/      |  |  \\__  \\_  __ \/ __ |                                                                          |")
        print("| /       \      |   Y  \/ __ \|  | \/ /_/ |                                                                        |")
        print("| \_______ \ /\  |___|  (____  /__|  \____ |                                                                        |")
        print("|         \/ \/       \/     \/           \/                                                                        |")
        print("| ________                  .__  __                                                                                 |")
        print("| \_____  \      ________ __|__|/  |_                                                                               |")
        print("|   _(__  <     / ____/  |  \  \   __\                                                                              |")
        print("|  /       \   < <_|  |  |  /  ||  |                                                                                |")
        print("| /______  / /\ \__   |____/|__||__|                                                                                |")
        print("|        \/  \/    |__|                                                                                             |")
        print("===================================================================================================================")
        print("choice one")
        userinput=int(input("|--> "))
        return userinput
    def PrintAndChoicePrinters(self,numberOfPrinters:int):
        while True:
            print("------------------------------------------------------------------------------------")
            printers=win32print.EnumPrinters(numberOfPrinters)
            PrinterList=[i[1] for i in printers]
            # print(PrinterList)
            for i,element in enumerate(PrinterList):
                print('{}. {}'.format(i+1,element))
            userinputofnumber=input('이중에서 하나를 고르시오')


            if(userinputofnumber.isdigit()):
                target=PrinterList[int(userinputofnumber)-1]
                return target
            else:
                print("다시 입력하시오")
            


    def PrintFile(self,filename:str,target:str):
        win32api.ShellExecute(0, 'print', filename,
                    f'/d:"{target}"', '.', 0)

            