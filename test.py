from vicky_eldora_app import CartItem, ShoopingCart
import unittest

class TestAddNumbers(unittest.TestCase):

  def setUp(self):
    self.cartt = ShoopingCart()


  def test_menambahkan_item(self):
      new_item = CartItem("apel", 4000)
      self.cartt.menambahkan_item(new_item)
      # untuk mengecek apakah benar function yang telah dibuat. 
      # Menambahkan 1 item, hasil akhirnya harusnya berhasil menambahkan item dari yang tadiya 0 item pada cartnya menjadi 1 item
      self.assertEqual(len(self.cartt.keranjang), 1)


  def test_meghapus_item(self):
      new_item = CartItem("mangga", 4000)
      new_item2 = CartItem("jeruk", 6000)
      self.cartt.menambahkan_item(new_item)
      self.cartt.menambahkan_item(new_item2)
      self.cartt.menghapus_item("jeruk")
      # untuk mengecek apakah benar function yang telah dibuat. 
      # Terdapat 3 item lalu menghapus 1 item, hasil akhirnya harusnya berhasil dihapus itemnya sehingga yang tadinya ada 3 item menjadi 2 item
      self.assertEqual(len(self.cartt.keranjang), 1)
  
  def test_menjumlah_item(self):

    test_inventory = ShoopingCart()
    test_inventory.keranjang.append(CartItem("anggur", "2000"))
    test_inventory.keranjang.append(CartItem("pisang", "2100"))
    # untuk mengecek apakah benar function yang telah dibuat
    # anggur =2000
    # pisang = 2100
    # harga anggur + pisang = 2000 + 2100 = 4100
    self.assertEqual(ShoopingCart.menjumlah_item(test_inventory), 4100)


if __name__ == '__main__' :
  unittest.main()