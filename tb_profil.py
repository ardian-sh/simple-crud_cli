from connect_Db import Connect_db
import mysql.connector
from termcolor import colored
from prettytable import PrettyTable
from Validation import Validations
from os import system

class Tb_profil:

    Valid = Validations()
    conn = Connect_db()

    #method untuk menampilkan data, dimana pada method ini mempunyai 1 argument yaitu noid
    #mtujuannya adalah karena method ini akan dipakai untuk menampilkan data secara keseluruhan
    #(jika noid = 1) dan dipakai menampilkan data berdasarkan id (jika noid != 1)
    #nilai 1 ini didpat dari inputan pada method show_menu() di class main()
    def show_Profil(self, noid):
        #self.mydb adalah sebuah object untuk menampung hasil dari object conn di method con
        #karena conn adalah sebuah variabel class, maka untuk memanggil di method menggunakan self
        self.Mydb = self.conn.con()

        #cursor() ini adalah sebuah method dari modul myql.conecctor dimana fungsinya adalah 
        # sebagai eksekusi ke database
        self.cursor = self.Mydb.cursor()

        if(noid == 1):
            #quey untuk menampilkan data secara keseluruhan
            sql = "SELECT * FROM profil"

            print("Tampil Profil")
            print("**************")

        else:
            #quey untuk menampilkan data berdasarkan id
            sql = "SELECT * FROM profil WHERE id ={} LIMIT 1".format(noid)

            print("Tampil Profil No Id : {}".format(noid))
            print("**************")

        try:
            self.cursor.execute(sql)

            #PrettyTable adalah modul dari prettytable dimana tujuannya untuk 
            #mempercantik tampilan agar lebih rapih
            t = PrettyTable(['No Id','Nama', 'Alamat', 'Jenis Kelamin'])
            
            #menampilkan data menggunakan perulangan for
            for (no_id,nama, alamat, jenis_kelamin) in self.cursor:
                t.add_row([no_id,nama, alamat, jenis_kelamin])
            print(t)

        except mysql.connector.ProgrammingError as err:
            print (colored("Class Tb_profil -> {}".format(err.msg),"red"))
            exit()

        except mysql.connector.Error as err:
            print (colored("Class Tb_profil -> {}".format(err.msg),"red"))
            exit()

        #jika tidak ada error/query berhasil, maka cursor dan koneksi ke database akan di tutup.
        finally:
            self.cursor.close()
            self.Mydb.close()

    #method ini berfungsi untuk insert data ke database
    def insert_Profil(self):
        self.Mydb = self.conn.con()
        self.cursor = self.Mydb.cursor()

        print("Tambah Profil")
        print("**************")
        
        #langkah pertama adalah membuat variabel nama/alamat/jenis_kelamin untuk menampung hasil dari
        #method self.Valid.validation_String/elf.Valid.validation_StringOption
        self.nama = self.Valid.validation_String("Nama : ",True)
        self.alamat = self.Valid.validation_String("Alamat : ", True)
        self.jenis_kelamin = self.Valid.validation_StringOption("Jenis Kelamin [L/P] : ", True, "L","P")
        system("cls")

        #kemudian semua variabel tersebut dimasukan kedalam query database untuk insert data
        sql = ("INSERT INTO profil "
                    "(nama, alamat, jenis_kelamin) "
                    "VALUES (%s, %s, %s)")
        values = (self.nama, self.alamat, self.jenis_kelamin)

        try:
        #menggunakan try, akan dicoba untuk mengeksekusi query tersebut
            #ekseskusi query menggunakan self.cursor.execute
            self.cursor.execute(sql, values)

            #eksekusi ke databse/insert data
            self.Mydb.commit()

            #jika berhasil akan menampilkan sebuah pesan
            print(colored("\n{} Record has been successfully inserted".format(self.cursor.rowcount),"green"))

        #jika ada error pada try akan di tanggkap terserbut menggunakan except
        except (mysql.connector.IntegrityError, mysql.connector.DataError) as err:
            print (colored("Class Tb_profil -> Insert failed in atribute class Tb_profil, typo or incomplete -> {}".format(err),"red"))
            #jika error maka query tadi akan dikembalikan seperti sebelumnya/dibatalkan menggunakan rollback
            self.Mydb.rollback()
            exit()

        except mysql.connector.ProgrammingError as err:
            print (colored("Class Tb_profil -> Insert failed in values, typo or incomplete -> {}".format(err),"red"))
            self.Mydb.rollback()
            exit()

        except mysql.connector.Error as err:
            print (colored("Class Tb_profil -> {}".format(err.msg),"red"))# error message
            self.Mydb.rollback()
            exit()

        #jika tidak ada error/query berhasil, maka cursor dan koneksi ke database akan di tutup.
        finally:
            self.cursor.close()
            self.Mydb.close()

    #program untuk mencari id, karena untk mengedit atau menghapus data dibutuhkan sebuah identitas
    #yang akan dijadikan sebagai ciri bahwa data ke n yang akan di edit/dihapus

    #untuk method ini sama halnya seprti pada method login
    def search_Id(self):
        while True:
            self.Mydb = self.conn.con()
            self.cursor = self.Mydb.cursor()

            self.id = self.Valid.validation_Int("No Id : ", True)
            sql = "SELECT id FROM profil WHERE id = {}".format(self.id )
            try:
                self.cursor.execute(sql)

                for i in self.cursor:
                    i
                if(self.cursor.rowcount < 1):
                        print("No id tidak ditemukan")
                else:
                    system("cls")
                    return self.id

            except mysql.connector.ProgrammingError as err:
                print (colored("Class Tb_profil -> {}".format(err.msg),"red"))
                exit()

            except mysql.connector.Error as err:
                print (colored("Class Tb_profil -> {}".format(err.msg),"red"))
                exit()

            #jika tidak ada error/query berhasil, maka cursor dan koneksi ke database akan di tutup.
            finally:
                self.cursor.close()
                self.Mydb.close()

    #method untuk mengedit profil
    def edit_Profil(self):
        
        #memanggil method search_id, kemudian hasilnya akan di simpan didalam variabel self.id
        self.id = self.search_Id()
        
        #self.id ini akan digunanakn sebagai argumen pada method show_profil
        self.show_Profil(self.id)

        print("\nEdit profil : {}".format(self.id))
        print("**************")
        
        self.Mydb = self.conn.con()
        self.cursor = self.Mydb.cursor()

        self.nama = self.Valid.validation_String("Nama : ",True)
        self.alamat = self.Valid.validation_String("Alamat : ", True)
        self.jenis_kelamin = self.Valid.validation_StringOption("Jenis Kelamin [L/P] : ", True, "L","P")
        system("cls")

        #query untuk update data
        sql = ("UPDATE profil SET nama='%s', alamat='%s', jenis_kelamin='%s' WHERE id ='%s'" % (self.nama, self.alamat, self.jenis_kelamin, self.id))

        try:
            self.cursor.execute(sql)

            self.Mydb.commit()

            print(colored("\n{} Record has been successfully Update".format(self.cursor.rowcount),"green"))


        except (mysql.connector.IntegrityError, mysql.connector.DataError) as err:
            print (colored("Class Tb_profil -> Update failed in atribute class Tb_profil, typo or incomplete -> {}".format(err),"red"))
            self.Mydb.rollback()
            exit()

        except mysql.connector.ProgrammingError as err:
            print (colored("Class Tb_profil -> Update failed in values, typo or incomplete -> {}".format(err),"red"))
            self.Mydb.rollback()
            exit()

        except mysql.connector.Error as err:
            print (colored("Class Tb_profil -> {}".format(err.msg),"red"))# error message
            self.Mydb.rollback()
            exit()

        #jika tidak ada error/query berhasil, maka cursor dan koneksi ke database akan di tutup.
        finally:
            self.cursor.close()
            self.Mydb.close()

    #method untuk menghapus data tertentu, sama halnya seprti method insert data, perbedannya hanya 
    # terletak pada querynya saja
    def delete_Profil(self):
        self.id = self.search_Id()
        self.show_Profil(self.id)

        print("\nDelete profil")
        print("**************")

        self.confirm = self.Valid.validation_ConfirmDelete("Apakah yakin ingin menghapus No id {}? [Y/T] : ".format(self.id), True, "Y", "T")

        if (self.confirm == "Y"):

            self.Mydb = self.conn.con()
            self.cursor = self.Mydb.cursor()

            sql = ("DELETE FROM profil WHERE id = '%s'" % (self.id))
            try:
                self.cursor.execute(sql)
                self.Mydb.commit()
                print(colored("\n{} Record has been successfully Delete".format(self.cursor.rowcount),"green"))

            except (mysql.connector.IntegrityError, mysql.connector.DataError) as err:
                print (colored("Class Tb_profil -> Delete failed in atribute class Tb_profil, typo or incomplete -> {}".format(err),"red"))
                self.Mydb.rollback()
                exit()

            except mysql.connector.ProgrammingError as err:
                print (colored("Class Tb_profil -> Delete failed in values, typo or incomplete -> {}".format(err),"red"))
                self.Mydb.rollback()
                exit()

            except mysql.connector.Error as err:
                print (colored("Class Tb_profil -> {}".format(err.msg),"red"))# error message
                self.Mydb.rollback()
                exit()

            #jika tidak ada error/query berhasil, maka cursor dan koneksi ke database akan di tutup.
            finally:
                self.cursor.close()
                self.Mydb.close()
        else:
            print("No id {} tidak di hapus".format(self.id))