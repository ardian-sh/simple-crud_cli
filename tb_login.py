"""
-import mysql.conecctor -> memanggil function conecctor dari modul mysql
-from connect_Db import Connect_db -> memanggil class connect_db di file connect_Db yang telah di buat sebelumnya
-from Validation import Validations-> memanggil class Validataions yang ada pada file Validation
-from termcolor import colored -> hanya sebagai penanda jika terjadi error atau success akan di berikan warna tertentu
-from os import system -> memanggil fungsi system pada modul os, tujuannya hanya sebagai clear/new window
"""
from connect_Db import Connect_db
import mysql.connector
from termcolor import colored
from Validation import Validations
from os import system

class Tb_Login:
    #sebuah inisialisasi bahwa class validation akan di tampung di variael valid, begitupun untuk conn
    Valid = Validations()
    conn = Connect_db()

    def login (self):
        #while adalah sebuah kondisi loop/perulangan dimana akan melakakukan
        # loop selama kondisi tersebut berinilai benar/true
        while True:
            #self.mydb adalah sebuah object untuk menampung hasil dari object conn di method con
            #karena conn adalah sebuah variabel class, maka untuk memanggil di method menggunakan self
            self.Mydb = self.conn.con()
            
            #cursor() ini adalah sebuah method dari modul myql.conecctor dimana fungsinya adalah 
            # sebagai eksekusi ke database
            self.cursor = self.Mydb.cursor()
            
            #membuat sebuah object username/password, dimana object tersebut menggunakan method validation_String()
            #yang ada pada class Validation
            self.username = self.Valid.validation_String("Username : ", True)
            self.password = self.Valid.validation_String("Password : ", True)

            #query untuk mencari username dan password
            sql = "SELECT username, password FROM login WHERE username = '{}' AND password = '{}'".format(self.username, self.password)

            try:
                #eksekusi query (cek ke database)
                self.cursor.execute(sql)

                #karena kita akan menampilkan jumlah baris/rowcount dari query diatas, tujuannya adalah 
                # untuk mengetahui apakah username dan password yang di cari ada atau tidak.
                # untuk melihat jumlah baris/rowcount cukup dengan mengunakan perulangan for
                for i in self.cursor:
                    i

                #membuat sebuah kondisi menggunakan if yaitu jika self.cursor.rowcount kurang dari 1 
                # (nilai defaultnya -1), artinya tidak ada ada data/ data tidak ditemukan. maka 
                # akan menampilkan "username atau password slah", dan akan kembali melakukan perulangan pertama (while)
                if (self.cursor.rowcount < 1):
                    print("Username atau password salah")

                #tetapi jika self.cursor.rowcount bernilai lebih dari 1 (data ditemukan), maka akan mengembalikan
                #nilai inputan hasil dari self.username
                else:
                    system("cls")
                    return self.username

            #menangkap error jika terjadi salah dalam query
            except mysql.connector.ProgrammingError as err:
                print (colored("Class Tb_login -> {}".format(err.msg),"red"))
                exit()

            #menangkap error selain salah query
            except mysql.connector.Error as err:
                print (colored("Class Tb_login -> {}".format(err.msg),"red"))
                exit()

            #jika tidak ada error/query berhasil, maka cursor dan koneksi ke database akan di tutup.
            finally:
                self.cursor.close()
                self.Mydb.close()