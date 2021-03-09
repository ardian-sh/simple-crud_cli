"""
-import mysql.conecctor -> memanggil function conecctor dari modul mysql
-from mysql.connector import errorcode -> memanggil function errorcode, fungsinya untuk menampilkan
-from termcolor import colored -> hanya sebagai penanda jika terjadi error atau success akan di berikan warna tertentu
"""
import mysql.connector
from mysql.connector import errorcode
from termcolor import colored

#membuat class dengan nama connect_db
class Connect_db:
    #membuat sebuah method dengan nama con
    def con(self):
        #try -> mencoba menjalankan code yang ada pada try
        try:
            #self.mydb adalah sebuah object untuk menampung hasil dari pembuatan sebuah koneksi ke database
            self.mydb = mysql.connector.connect( host="localhost", #host database
            user="root", #usrname databse
            password="", #password databse
            database="coba") # nama database

            #jika tidak terjadi error, maka method con ini akan mengambalikan sebuah nilai
            #berupa hasil dari self.mydb menggunakan fungsi return
            return self.mydb

        #jika terjadi error pada try, maka akan di tangkap oleh except
        except mysql.connector.Error as e:

            #sebuah kondisi jika error karena kesalahan/typo dalam penyebutan usernama maupun password
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print(colored("Class Connect_db -> Something is wrong with your username or password","red"))
                exit()

            # sebuah kondisi jika error karena kesalahan/typo dalam penyebutan nama database
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print (colored("Class Connect_db -> {}".format(e.msg),"red"))
                exit()

            #jika error selain dari 2 kondisi sebelumnya
            else:
                print (colored("Class Connect_db -> {}".format(e.msg),"red"))
                exit()