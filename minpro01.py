# Nama : Muhammad Farel Awaluddin
# NIM : 2509116055

donasi = [["Farel", 20000]]

while True:


    print("-------------------")
    print("Selamat datang Di")
    print("Sistem Pencatatan Donasi")
    print("-------------------")
    print("Silahkan pilih menu  yang ingin anda buka")
    print("A. Tambah Donasi")
    print("B. Lihat Donasi")
    print("C. Keluar")
    
    menu = input("Silahkan pilih huruf didepannya untuk lanjut (A/B/C/): ")
    if menu == "A":
        nama = input("Masukkan nama donatur:")
        jumlah = int(input("Masukkan jumlah donasi: "))
        donasi.append([nama, jumlah])
        print("Nama dan Jumlah Donasi Telah Ditambahkan")

    elif menu == "B":
        print("Daftar orang yang berdonasi")
        print(f"donatur {donasi}")

    elif menu == "C":
        print("Keluar")
        break
    
    else:
        print("Tidak Valid")
    

        

        
      


