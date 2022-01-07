import os
import datetime

#Program ini dibuat untuk mempermudah pembelian atau penyewaan game di toko Akong

def ShowInstruction():

    """Menampilkan instruksi dan welcoming message di menu utama"""

    welcome = ("Selamat datang di Toko Game Akong").center(127)
    print(welcome)
    print("-" * 127)
    instruction = "Pilih menu dibawah"
    print(instruction)

def Menu():

    """meminta user untuk memilih salah satu dari ketiga menu; Sewa, Beli, Exit"""

    global menu
    print("[1] Sewa\n" + "[2] Beli\n" + "[3] Exit\n")
    while True:
        menu = int(input("Pilih: "))
        print("")

        if menu == 1: 
            return 1        #jika user milik angka 1, maka kode akan mengembalikan angka 1 tersebut, berlaku sama untuk baris dibawahnya
        elif menu == 2:
            return 2
        elif menu == 3:
            return 3
        else:
            print("Pilihan salah!")

def Pilihansewagame():

    """list yang dibuat untuk menampilkan game yang dapat disewa beserta kode untuk menghitung total biaya sewa"""

    global berapalamasewa, total_biaya_sewa, userpilihgamesewaan, pilihansewa1, pilihansewa2, pilihansewa3, pilihansewa4, pilihansewa5, pilihansewa6, pilihansewa7, pilihansewa8, pilihansewa9
    pilihansewa1 = [1, "[1] American Truck Simulator", "American Truck Simulator"]
    pilihansewa2 = [2, "[2] Arma: Cold War Assault", "Arma: Cold War Assault"]
    pilihansewa3 = [3, "[3] Bioshock Trilogy", "Bioshock Trilogy"]
    pilihansewa4 = [4, "[4] DOOM 64", "DOOM 64"]
    pilihansewa5 = [5, "[5] Euro Truck Simulator", "Euro Truck Simulator"]
    pilihansewa6 = [6, "[6] Far Cry Series", "Far Cry Series"]
    pilihansewa7 = [7, "[7] L.A. Noir", "L.A. Noir"]
    pilihansewa8 = [8, "[8] Life is Strange Series (Life is Strange 1 Complete Episode, Life is Strange 2 Complete Episode, Life is Strange True Colors)", "Life is Strange Series (Life is Strange 1 Complete Episode, Life is Strange 2 Complete Episode, Life is Strange True Colors)"]
    pilihansewa9 = [9, "[9] Ori Complete Bundle(Ori and the Blind Forest, Ori and the Blind Forest: Definitive Series, Ori and the Will of the Wisps)", "Ori Complete Bundle(Ori and the Blind Forest, Ori and the Blind Forest: Definitive Series, Ori and the Will of the Wisps)"]
    print("Untuk menyewa anda akan dikenakan biasa Rp. 10.000/hari untuk setiap game\n")
    print(pilihansewa1[1])
    print(pilihansewa2[1])
    print(pilihansewa3[1])
    print(pilihansewa4[1])
    print(pilihansewa5[1])
    print(pilihansewa6[1])
    print(pilihansewa7[1])
    print(pilihansewa8[1])
    print(pilihansewa9[1])
    print("")
    while menu == 1:
        userpilihgamesewaan = int(input("Game apa yang ingin disewa: "))    #berfungsi untuk menanyakan user "game mana yang ingin disewa"
        berapalamasewa = int(input("Berapa lama anda menyewa (Hari): "))    #menanyakan user berapa hari mereka akan menyewa"
        print("")
        total_biaya_sewa = 10000 * berapalamasewa
        
        if userpilihgamesewaan == 1:    
            userpilihgamesewaan = pilihansewa1[2]       #mengubah isi variabel 'userpilihgamesewaan' yang semulanya 1 menjadi American Truck Simulator, berfungsi untuk menampilkan item pada halaman Lihat keranjang
            break
        elif userpilihgamesewaan == 2:
            userpilihgamesewaan = pilihansewa2[2]
            break
        elif userpilihgamesewaan == 3:
            userpilihgamesewaan = pilihansewa3[2]
            break
        elif userpilihgamesewaan == 4:
            userpilihgamesewaan = pilihansewa4[2]
            break
        elif userpilihgamesewaan == 5:
            userpilihgamesewaan = pilihansewa5[2]
            break
        elif userpilihgamesewaan == 6:
            userpilihgamesewaan = pilihansewa6[2]
            break
        elif userpilihgamesewaan == 7:
            userpilihgamesewaan = pilihansewa7[2]
            break
        elif userpilihgamesewaan == 8:
            userpilihgamesewaan = pilihansewa8[2]
            break
        elif userpilihgamesewaan == 9:
            userpilihgamesewaan = pilihansewa9[2]
            break
        else:
            print("Pilihan salah!")
        
def Pilihanbeligame():

    """Berisi list game" yang tersedia untuk dibeli"""

    global jumlah_barang, total_biaya, pilihan_game, pilihan1, pilihan2, pilihan3, pilihan4, pilihan5, pilihan6, pilihan7, pilihan8, pilihan9, pilihan10
    
    #dibawah ini merupakan harga game yang dapat dibeli
    pilihan1 = 57250
    pilihan2 = 40000
    pilihan3 = 106500
    pilihan4 = 60000
    pilihan5 = 110250
    pilihan6 = 1500000
    pilihan7 = 120000
    pilihan8 = 260000
    pilihan9 = 360000

    print("Game tersedia untuk dibeli: \n")
    print("[1] American Truck Simulator\n", "Harga: 57.250\n")
    print("[2] Arma: Cold War Assault\n", "Harga: 40.000\n")
    print("[3] Bioshock Trilogy\n", "Harga: 106.500\n")
    print("[4] DOOM 64\n", "Harga: 60.000\n")
    print("[5] Euro Truck Simulator\n", "Harga: 110.250\n")
    print("[6] Far Cry Series (DELUXE EDITION)\n", "Harga: 1.500.000\n")
    print("[7] L.A. Noir\n", "Harga: 120.000\n")
    print("[8] Life is Strange Series (Life is Strange 1 Complete Episode, Life is Strange 2 Complete Episode, Life is Strange True Colors)\n", "Harga: 260.000\n")
    print("[9] Ori Complete Bundle(Ori and the Blind Forest, Ori and the Blind Forest: Definitive Series, Ori and the Will of the Wisps)\n", "Harga: 360.000\n")
    while menu == 2:    #menggunakan while in case user salah memasukan input
        pilihan_game = input("Game apa yang anda pilih: ")   
        #misalnya user memilih game pertama, maka yang terjadi adalah kode bertanya ke user terkait jumlah barang yang mereka beli, lalu variabel 'pilihan1' akan dikali dengan jumlah barang dan menghasilnya 'total_biaya'
        if pilihan_game == "1":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan1 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "American Truck Simulator"   #berfungsi jika user ingin melihat keranjang, maka akan ditampilkan (jumlahbarang)x American Truck Simulator = ('total_biaya')
            break
        elif pilihan_game == "2":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan2 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "Arma: Cold War Assault"
            break
        elif pilihan_game == "3":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan3 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "Bioshock Trilogy"
            break
        elif pilihan_game == "4":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan4 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "DOOM 64"
            break
        elif pilihan_game == "5":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan5 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "Euro Truck Simulator"
            break
        elif pilihan_game == "6":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan6 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "Far Cry Series"
            break
        elif pilihan_game == "7":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan7 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "L.A. Noir"
            break
        elif pilihan_game == "8":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan8 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "Life is Strange Series (Life is Strange 1 Complete Episode, Life is Strange 2 Complete Episode, Life is Strange True Colors)"
            break
        elif pilihan_game == "9":
            jumlah_barang = int(input("Berapa banyak jumlah yang diinginkan: "))
            print("")
            total_biaya = 0
            total_biaya = pilihan9 * jumlah_barang
            pilihan_game = str(jumlah_barang) + "x " + "Ori Complete Bundle(Ori and the Blind Forest, Ori and the Blind Forest: Definitive Series, Ori and the Will of the Wisps)"
            break
        else:
            print ("Pilihan salah!")

def Pilihanlanjutansewa():
    #digunakan setelah user memilih game sewaan
    
    while True:
        print("[1] Lanjut Checkout")
        print("[2] Lihat Keranjang\n")
        inputusersewa = int(input("Masukan pilihan: "))
        if inputusersewa == 1:      #halaman Lanjut Checkout
            return 1 
        elif inputusersewa == 2:    #halaman Lihat Keranjang
            print(str(userpilihgamesewaan) + " x" + str(berapalamasewa) + " hari" + " = " + str(total_biaya_sewa))
            print("")
            continue
        else:
            print("Coba cek masukan anda!")
            continue

def Pilihanlanjutanbeli():
    #digunakan setelah user memilih game
    
    while True:
        print("[1] Lanjut Checkout")
        print("[2] Lihat Keranjang\n")
        inputuserbeli = int(input("Masukan pilihan: "))
        if inputuserbeli == 1:
            return 1
        elif inputuserbeli == 2:
            print(str(pilihan_game) + " = " + str(total_biaya))
            print("")
            continue
        else:
            print("Coba cek masukan anda!")
            continue

def struk():
    print("Selamat datang di Toko Game Akong").center(50)
    print("-" * 50)
    timectl = datetime.datetime.now().center(50)
    print("")
    if menu == 1:
        print(str(userpilihgamesewaan) + " x" + str(berapalamasewa) + " hari" + " = " + str(total_biaya_sewa))
        print("")
        print("")
        print("")
        print("")
        print("Total" + " = " + str(total_biaya_sewa))
    elif menu == 2:
        print(str(pilihan_game) + " = " + str(total_biaya))
    
    
def MembersihkanLayar():
    print("")
    input("Tekan enter untuk melanjutkan...")
    os.system('cls')

while True:
    ShowInstruction()
    Menu()
    if menu == 1:
        Pilihansewagame()
        if Pilihanlanjutansewa() == 1:
            print("Total biaya sebesar: " + str(total_biaya_sewa))
            print("Terimakasih sudah berbelanja di toko kami!")
        MembersihkanLayar()
        continue
    elif menu == 2:
        Pilihanbeligame()
        if Pilihanlanjutanbeli() == 1:
            print("Total biaya sebesar: " + str(total_biaya))
            print("Terimakasih sudah berbelanja di toko kami!")
            MembersihkanLayar()
    elif menu == 3:
        print("Terima kasih sudah menggunakan layanan kami!")
        MembersihkanLayar()
        break
