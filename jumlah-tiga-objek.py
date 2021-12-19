# Ini adalah program untuk menghitung jumlah barang/ objek yang dimiliki oleh seseorang (B) dari tiga orang (A,B,C) yang memiliki selisih dengan nilai tertentu.
# Contoh soal:
# Perbandingan jumlah kelereng Amat dengan Cemen adalah 7:5.
# Sedangkan, perbandingan jumlah kelereng Bagio dan Amat adalah 3:4.
# Jika selisih jumlah kelereng Amat dan Cemen adalah 16 buah, berapa banyaknya kelereng Bagio ?

print("\nIni adalah program untuk menghitung jumlah barang/objek yang dimiliki oleh seseorang (B) dari tiga orang (A,B,C) yang memiliki selisih dengan nilai tertentu.")
class Perselisihan:
	def __init__(self,a1,a2,b,c,d):
		self.a1 = a1
		self.a2 = a2
		self.b = b
		self.c = c
		self.d = d
	def jumlahkan(self):
		x = self.a1 * self.a2
		y = self.b * self.a1
		z = self.c * self.a2
		j = y / (x - z) * self.d
		print("Jumlah objek milik B adalah =",j)

a1 = float(input("Masukkan perbandingan objek milik A terhadap objek milik C:"))
c = float(input("Masukkan perbandingan objek milik C:"))
b = float(input("Masukkan perbandingan objek milik B terhadap objek milik A :"))
a2 = float(input("Masukkan perbandingan objek milik A terhadap objek milik B:"))
d = float(input("Masukkan selisih dari objek milik A dan milik B:"))

hitung = Perselisihan(a1,a2,b,c,d)
hitung.jumlahkan()