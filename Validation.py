from termcolor import colored
from os import system

class Validations:
    def validation_Menu(self, Ask, inmandatory, StartNumber, StopNumber):
        self.ask = Ask
        self.inmandatory = inmandatory
        self.startNumber = StartNumber
        self.stopNumber = StopNumber
        while True:
            Asking = input(self.ask)
            if (Asking == "" and self.inmandatory==True):
                print(colored("Inputan tidak boleh kosong", "magenta"))
                print("\n")
            else:
                try:
                    Asking = int(Asking)
                    if (Asking < self.startNumber or Asking > self.stopNumber):
                        print (colored("Inputan harus diantara {} - {}".format(StartNumber, StopNumber), "magenta"))
                    else:
                        return Asking
                except:
                    print(colored("Inputan Harus bernilai angka","magenta"))

    def validation_Int(self, Ask, inmandatory):
        self.ask = Ask.replace(" : ","")
        self.inmandatory = inmandatory
        while True:
            Asking = input(Ask)
            if (Asking == "" and self.inmandatory==True):
                print (colored("{} tidak boleh kosong".format(self.ask),"magenta"))
            else:
                try:
                    Asking = int(Asking)
                    if (Asking < 1):
                        print (colored("{} harus lebih dari 0".format(self.ask),"magenta"))
                    else:
                        return Asking
                except:
                    print(colored("{} Harus bernilai angka".format(self.ask),"magenta"))

    def validation_String(self, Ask, inmandatory):
        self.ask = Ask
        self.inmandatory = inmandatory
        while True:
            Asking = input(Ask)
            if (Asking == "" and self.inmandatory==True):
                #asK = self.ask
                self.ask = self.ask.replace(" : ","")
                print (colored("{} tidak boleh kosong".format(self.ask),"magenta"))
            else:
                try:
                    return Asking
                except Exception as e:
                    print("class Validations -> ".format(e))

    def validation_StringOption(self, Ask, inmandatory,L, P):
        self.ask = Ask
        self.inmandatory = inmandatory
        self.L = L
        self.P = P
        while True:
            Asking = input(Ask)
            if (Asking == "" and self.inmandatory==True):
                self.ask = self.ask.replace("[L/P] : ","")
                print ("{}tidak boleh kosong".format(self.ask))
            else:
                try:
                    if (Asking == self.L):
                        return "Laki - laki"
                    elif (Asking == self.P):
                        return "Perempuan"
                    else:
                        print("{} harus antara {} atau {}".format(self.ask,self.L, self.P))
                except Exception as e:
                    print("class Validations -> ".format(e))

    def validation_ConfirmDelete(self, Ask, inmandatory,Y, T):
        self.ask = Ask
        self.inmandatory = inmandatory
        self.y = Y
        self.t = T
        while True:
            Asking = input(Ask)
            if (Asking == "" and self.inmandatory==True):
                self.ask = self.ask.replace("[L/P] : ","")
                print ("{}tidak boleh kosong".format(self.ask))
            else:
                try:
                    if (Asking == self.y):
                        return "Y"
                    elif (Asking == self.t):
                        return "T"
                    else:
                        print("{} harus antara {} atau {}".format(self.ask,self.y, self.t))
                except Exception as e:
                    print("class Validations -> ".format(e))