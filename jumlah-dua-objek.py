# Ini adalah program untuk menghitung jumlah barang/objek yang dimiliki oleh dua orang (A dan B) dari selisih dengan nilai tertentu.
# Contoh soal:
# Perbandingan kelereng Egi dan Legi adalah 3 : 2.
# Jika selisih kelereng mereka 8, jumlah kelereng Egi dan Legi berapa? 

print("\nIni adalah program untuk menghitung jumlah barang/objek yang dimiliki oleh dua orang (A dan B) dari selisih dengan nilai tertentu.")
class Perselisihan:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c		
	def jumlahkan(self):
		x = self.a + self.b
		y = self.a - self.b
		z = x / y
		j = z * self.c
		print("Jumlah objek milik A dan milik B adalah =",j)

a = float(input("Masukkan perbandingan objek milik A :"))
b = float(input("Masukkan perbandingan objek milik B :"))
c = float(input("Masukkan selisih dari objek milik A dan milik B:"))

hitung = Perselisihan(a,b,c)
hitung.jumlahkan()