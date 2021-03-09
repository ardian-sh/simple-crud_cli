from tb_profil import Tb_profil
from tb_login import Tb_Login
from termcolor import colored
from Validation import Validations
from os import system

class Main:
    Valid = Validations()
    TbProfil = Tb_profil()
    Tblogin = Tb_Login()

    def __init__(self):
        self.User = ""
        
        #username : ardiansah
        #password : 123
        self.show_login()

    def show_login(self):
        self.User = self.Tblogin.login()
        print ("Login By : {}".format(self.User))
        self.show_menu()

    def show_menu(self):
        while True:
            self.Menu  = "Menu"
            print(self.Menu.center(20))
            print ("-------------------")
            print ("1. Tampilkan Profil")
            print ("2. Tambah Profil")
            print ("3. Edit Profil")
            print ("4. Hapus Profil")
            print ("5. Keluar")

            self.Inputan = self.Valid.validation_Menu("Pilih menu [1 - 5] : ",True,1,5)

            if (self.Inputan ==1):
                system("cls")
                self.TbProfil.show_Profil(self.Inputan)
                print("\n")
            elif (self.Inputan == 2):
                system("cls")
                self.TbProfil.insert_Profil()
                print("\n")
            elif (self.Inputan == 3):
                system("cls")
                self.TbProfil.edit_Profil()
                print("\n")
            elif (self.Inputan == 4):
                system("cls")
                self.TbProfil.delete_Profil()
                print("\n")
            else:
                system("cls")
                print("Bye bye : {}".format(self.User))
                exit()

if __name__ == "__main__":
    try:
        system("cls")
        Main()

    except Exception as err:
        print(colored("class menu -> {}".format(err),"red"))