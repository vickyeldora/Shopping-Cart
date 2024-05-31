'''
=================================================
Nama  : Vicky Eldora Wuisan

Program ini dibuat agar dapat menambahkan item ke dalam sebuah shoppingcart, lalu dapat menghapus item, melihat isi keranjang yang terdapat berbagai macam item, menjumlah total harga dari item yang telah dimasukan.
dibuat untuk mempermudah kegiatan berbelanja.
=================================================
'''

class CartItem:                                     # class 1
    """
    kelas yang merepresentasikan cart item dengan nama dan harga.
    Kelas ini memberikan cara mudahuntuk memodelkan informasi barang. 
    """
    def __init__ (self, nama, harga):
        self.nama = nama
        self.harga = harga
     
class ShoopingCart:                                 # class 2
    """
    Kelas yang merepresentasikan sebuah shopping cart yang menyimpan dan mert that stores and mengelolaabarang.
    Kelas ini memiliki function  untuk menambahkan barang, melihat barang, menghapus barang, dan menjumlah harga barang yang ada dalam shopping cart.
    """
    def __init__(self):
        self.keranjang = []                         # keranjang ini yang akan menyimpan semua barang yang nanti akan dimasukan    

    def menambahkan_item (self, item_item):                  
        '''
        function to menambahkan barang to attribute keranjang

        contoh : 
        saat menambahkan barang nanti akan diminta memasukan nama barang: dan harga barang: 
        lalu dimasukan nama barang : apel dan harga barang: 10000
        '''                           

        self.keranjang.append(item_item)            

    def menghapus_item (self, barang):                     
        '''
        method to menghapus barang dari keranjang based on nama barang.
        contoh : 
        saat menghapus barang nanti akan diminta memasukan nama barang:
        kemudain diamsukan nama barang yang ingin dihapus: apel
        kemudian muncul kalimat "apel telah dihapus"
        '''
        if len(self.keranjang)>0:                   # ketika ada barang
            print()
            for j in self.keranjang:
                if j.nama.lower() == barang.lower():
                    self.keranjang.remove(j)
                    print(barang + " telah dihapus")
                    return None
            print()
            print('Barang tidak dapat ditemukan.')
        elif len(self.keranjang) == 0:              # ketika tidak ada barang
            print()
            print('\tTidak ada barang yang dapat dihapus, harap masukan terlbeih dahulu barang.')
        else:
            return None
    
    def melihat_item (self):                        # metode untuk melihat item
        '''
        method to menampilkan barang yang ada di keranjang.
        '''
        if len(self.keranjang)>0:
            print()
            print('Barang di kerangjang: ')
            no = 0
            for i in self.keranjang:                # ketika ada barang
                no += 1
                print(f' {no} {i.nama} - Rp {i.harga}')
        else:                                       # ketika tidak ada barang
            print()
            print('\tTidak ada barang di keranjang, harap masukan terlebih dahulu barang.')

    def menjumlah_item (self):                      # metode untuk menjumlah semua harga barang yang ada di keranjang
        '''
        method to menjumlah harga barang yang ada di keranjang.
        '''
        if len(self.keranjang)>0:                   # jika ada barang
            sum = 0
            for h in self.keranjang:
                sum = sum + int(h.harga)
            return sum
        elif len(self.keranjang) == 0:              # Jika tidak ada barang
            print()
            print('\tTidak ada barang.')
            return 0

def main():
    inventory = ShoopingCart()                 

    print('''
          Selamat Datang di Keranjang Belanja Toko Makmur!
          ''')
    
    while True:                              
        print('''
            Menu:
            1. Menambah Barang
            2. Hapus Barang
            3. Tampilkan Barang di Keranjang
            4. Lihat Total Belanja
            5. Exit
              ''')
    
        choice = input('Pilih 1-5: ')               # jika memilih angka sesuai pilihan maka fungsi nya akan dijalankan
        if choice == '1':
            print()
            print('Menambahkan barang...')
            print()
            nama = input('Masukan nama barang: ')       # masukin nama barang
            harga = input('Masukan harga barang: ')

        
            barangg = CartItem(nama, harga)            
            print()
            print(f'{barangg.nama} telah dimasukan ke keranjang!')
            inventory.menambahkan_item(barangg)

        elif choice == '2':
            print()
            print('Menghapus barang...')
            print()
            barang = input('Masukan nama barang yang ingin dihapus:')
            print()
            inventory.menghapus_item(barang)

        elif choice == '3':
            inventory.melihat_item()

        elif choice == '4':
            total = inventory.menjumlah_item()
            inventory.melihat_item()
            print()
            print(f'Total harga = Rp {total}')

        elif choice == '5':
            print()
            print('''\tSampai Jumpa! Terima kasih sudah belanja di Toko Makmur.
                  ''')
            break

        else:                                      # jika tidak memilih angka yang sesuai pilihan maka akan muncul tulisan dibawah ini
            print()
            print('\tMenu yang dipilih salah! Pilih menu (1-5).')

if __name__=="__main__":                            # Untuk menghubungkan file ini dengan file lain
    main()

