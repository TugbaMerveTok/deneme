#111111111111111111111111111111111
def katmaDegerCiroHesapla(a,b,c,d,e):
    f=a-(b+c+d+e)
    if (f>1000):
        print("İşletme katma değer cirosu yüksek")
    elif(500<f<999):
        print("İşletme katma değer cirosu normal")
    else :
        print("İşletme katma değer cirosu düşük")
a=int(input("Toplam Satış Miktarınız:"))
b=int(input("Hammadde Maliyeti:"))
c=int(input("Bakım Onarım Giderleriniz:"))
d=int(input("Sevkiyat Giderleriniz:"))
e=int(input("Satın Alınan Hizmet Giderleriniz:"))
katmaDegerCiroHesapla(a,b,c,d,e)

#22222222222222222222
def musterilerleCalısmaSuresiHesapla2016(x,y):
    global z
    z=x/y
    print("2016 Müşteri Çalışma Süresi:",z)
    return z
def musterilerleCalısmaSuresiHesapla2017(a,b):
    global t
    t=a/b
    print("2017 Müşteri Çalışma Süresi:",t)
    return t
def musteriFark(t,z):
    w=t-z
    print("2016-2017 Yılları Arası Müşteri Farkı:",w)
    return w

x=int(input("2016 yılında çalışılan süre:"))
y=int(input("2016 yılında toplam müşteri sayısı:"))
a=int(input("2017 yıında çalışılan süre:"))
b=int(input("2017 yılında toplam müşteri sayısı:"))

muCSX=musterilerleCalısmaSuresiHesapla2016(x,y)
muCSA=musterilerleCalısmaSuresiHesapla2017(a,b)
musteriF=musteriFark(t,z)

#333333333333333333333333
def gelirHesapla(yG,fG,uSG,yG2,sG,eTG,uSG2):
    global toplamGelir
    toplamGelir=yG+fG+uSG+yG2+sG+eTG+uSG2
    return toplamGelir
def giderHesapla(cM,kG,dM,cM2,kG2,bM):
    global toplamGider
    toplamGider=cM+kG+dM+cM2+kG2+bM
    return toplamGider
def isletmeKarıHesapla(toplamGelir,toplamGider):
    kar=toplamGelir-toplamGider
    if (kar>5000):
        print("İşletme çok karlı")
    elif(1000<kar<5000):
        print("İşletme karı normal")
    else:
        print("İşletme yeterince karda değil")
        
yG=int(input("İlk 6 Aylık Yazılım Geliriniz:"))
fG=int(input("İlk 6 Aylık Finansman Geliriniz:"))
uSG=int(input("İlk 6 Aylık Ürün Satış Geliriniz:"))
yG2=int(input("Son 6 Aylık Yazılım Geliriniz:"))
sG=int(input("Son 6 Aylık Sponsor Geliriniz:"))
eTG=int(input("Son 6 Aylık E-Ticaret Geliriniz:"))
uSG2=int(input("Son 6 Aylık Ürün Satış Geliriniz:"))
cM=int(input("İlk 6 Aylık Çalışan Maaşlarınız:"))
print("Lütfen giderlerinizi giriniz:")
kG=int(input("İlk 6 Aylık Kira Gideriniz:"))
dM=int(input("İlk 6 Aylık Donanım Maliyetiniz:"))
cM2=int(input("Son 6 Aylık Çalışan Maaşlarınız:"))
kG2=int(input("Son 6 Aylık Kira Gideriniz:"))
bM=int(input("Son 6 Aylık Bakım Maliyetiniz:"))
gelir=gelirHesapla(yG,fG,uSG,yG2,sG,eTG,uSG2)
gider=giderHesapla(cM,kG,dM,cM2,kG2,bM)
isletmeKarıHesapla(gelir,gider)

#44444444444444444
def ortalamaStok():
    a=384
    b=500
    c=260
    z=a+b+c
    print("Dönembaşı Koltuk Sayısı:",a)
    print("Dönembaşı Yatak Sayısı:",b)
    print("Dönembaşı Dolap Sayısı:",c)
    print("Dönembaşı Stok Miktarı:",z)
    k=120
    l=250
    m=125
    y=k+l+m
    print("Dönemsonu Koltuk Sayısı:",k)
    print("Dönemsonu Yatak Sayısı:",l)
    print("Dönemsonu Dolap Sayısı:",m)
    print("Dönemsonu Stok Miktarı:",y)
    x=(z+y)/2
    print("Ortalama Stok Değeri:",x)
