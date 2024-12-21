# List untuk menyimpan data administrator
admins = []

# Fungsi untuk menambah data administrator
def create_admin():
    name = input("Masukkan nama administrator: ")
    email = input("Masukkan email administrator: ")
    admins.append({"name": name, "email": email})
    print("Data administrator berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua data administrator
def read_admins():
    if not admins:
        print("Tidak ada data administrator.\n")
    else:
        print("Daftar Administrator:")
        for idx, admin in enumerate(admins, start=1):
            print(f"{idx}. Nama: {admin['name']}, Email: {admin['email']}")
        print()

# Fungsi untuk memperbarui data administrator
def update_admin():
    read_admins()
    try:
        index = int(input("Masukkan nomor administrator yang ingin diperbarui: ")) - 1
        if 0 <= index < len(admins):
            new_name = input("Masukkan nama baru: ")
            new_email = input("Masukkan email baru: ")
            admins[index] = {"name": new_name, "email": new_email}
            print("Data administrator berhasil diperbarui.\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input tidak valid.\n")

# Fungsi untuk menghapus data administrator
def delete_admin():
    read_admins()
    try:
        index = int(input("Masukkan nomor administrator yang ingin dihapus: ")) - 1
        if 0 <= index < len(admins):
            del admins[index]
            print("Data administrator berhasil dihapus.\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input tidak valid.\n")

# Menu utama
def main_menu():
    while True:
        print("=== CRUD Administrator ===")
        print("1. Tambah Administrator")
        print("2. Lihat Administrator")
        print("3. Perbarui Administrator")
        print("4. Hapus Administrator")
        print("5. Keluar") 
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            create_admin()
        elif pilihan == "2":
            read_admins()
        elif pilihan == "3":
            update_admin()
        elif pilihan == "4":
            delete_admin()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan menu utama
main_menu()
