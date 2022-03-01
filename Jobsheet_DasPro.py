#Program Menghitung Luas dan Keliling Bangun Datar

def LuasBujurSangkar(sisi):
    luas = sisi*sisi
    return luas
def KelilingBujurSangkar(sisi):
    keliling = 4*sisi
    return keliling
def LuasPersegiPanjang(panjang,lebar):
    luas = panjang*lebar
    return luas
def KelilingPersegiPanjang(panjang,lebar):
    keliling = 2*(panjang+lebar)
    return keliling
def LuasSegitiga(alas,tinggi):
    luas = 0.5*alas*tinggi
    return luas
def KelilingSegitiga(a,b,c):
    keliling = a+b+c
    return keliling
def LuasLingkaran(r):
    luas = 3.14*r**2
    return luas
def KelilingLingkaran(r):
    keliling = 2*3.14*r
    return keliling
def LuasJajarGenjang(alas,tinggi):
    luas = alas*tinggi
    return luas
def KelilingJajarGenjang(alas,tinggi):
    keliling = 2*(alas+tinggi)
    return keliling

pilihan=1
while pilihan!=0:
    print("1. Menghitung Luas Bujur Sangkar")
    print("2. Menghitung Keliling Bujur Sangkar")
    print("3. Menghitung Luas Perasegi Panjang")
    print("4. Menghitung Keliling Persegi Panjang")
    print("5. Menghitung Luas Segitiga")
    print("6. Menghitung Keliling Segitiga")
    print("7. Menghitung Luas Lingkaran")
    print("8. Menghitung Keliling Lingkaran")
    print("9. Menghitung Luas Jajar Genjang")
    print("10. Menghitung Keliling Jajar Genjang")
    
    pilihan=int(input("Masukkan nomor pilihan anda :"))
    print ()
    print ()
    if pilihan==1:
        print("Luas Bujur Sangkar")
        print()
        sisi=int(input("Masukkan sisi :"))
        print("Luas adalah : %d" %LuasBujurSangkar(sisi))
        print()
    elif pilihan==2:
        print("Keliling Bujur Sangkar")
        print()
        sisi=int(input("Masukkan sisi"))
        print("Keliling adalah :%d" %KelilingBujurSangkar(sisi))
        print()
    elif pilihan==3:
        print("Luas Persegi Panjang")
        print()
        panjang=int(input("Masukkan panjang"))
        lebar=int(input("Masukkan lebar"))
        print("Luas adalah :%d" %LuasPersegiPanjang(panjang,lebar))
        print()
    elif pilihan==4:
        print("Keliling Persegi Panjang")
        print()
        panjang=int(input("Masukkan panjang"))
        lebar=int(input("Masukkan lebar"))
        print("Keliling adalah :%d" %KelilingPersegiPanjang(panjang,lebar))
        print()
    elif pilihan==5:
        print("Luas Segitiga")
        print()
        alas=int(input("Masukkan alas"))
        tinggi=int(input("Masukkan tinggi"))
        print("Luas adalah :%d" %LuasSegitiga(alas,tinggi))
        print()
    elif pilihan==6:
        print("Keliling Segitiga")
        print()
        a=int(input("Masukkan a"))
        b=int(input("Masukkan b"))
        c=int(input("Masukkan c"))
        print("Keliling adalah : %d" %KelilingSegitiga(a,b,c))
        print()
    elif pilihan==7:
        print("Luas Lingkaran")
        print()
        r=int(input("Masukkan jari jari"))
        print("Luas adalah: %d" %LuasLingkaran(r))
        print()
    elif pilihan==8:
        print("Keliling Lingkaran")
        print()
        r=int(input("Masukkan jari jari"))
        print("Keliling adalah: %d" %KelilingLingkaran(r))
        print()
    elif pilihan==9:
        print("Luas Jajar Genjang")
        print()
        alas=int(input("Masukkan alas"))
        tinggi=int(input("Masukkan tinggi"))
        print("Luas adalah : %d" %LuasJajarGenjang(alas,tinggi))
        print()
    elif pilihan==10:
        print("Keliling Jajar Genjang")
        print()
        alas=int(input("Masukkan alas"))
        tinggi=int(input("Masukkan tinggi"))
        print("Keliling adalah : %d" %KelilingJajarGenjang(alas,tinggi))
        print()
    else :
        print("Anda salah memasukkan angka")
        
        
