class PersegiPanjang :
  def __init__(self,panjang,lebar):
    self.panjang = panjang
    self.lebar = lebar

  def hl(self):
    return self.panjang * self.lebar

  def hk(self):
    return 2 * (self.panjang + self.lebar)
  
  def __str__(self):
    return f"Persegi panjang,panjang {self.panjang} cm, dan lebar{self.lebar} cm"


input_panjang = int(input("Masukan Panjang : "))
input_lebar = int(input("Masukan lebar : "))

if input_panjang > 0 and input_lebar > 0 :
  PP = PersegiPanjang()
  print(PP)
  print("Keliling : ",PP.hk())
  print("Luas: ",PP.hl())
else :
  print("Angka yang dimasukan tidak bisa")
          

