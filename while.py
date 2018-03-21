#soru1
sMiktari=500
bSatisFiyati=20
ciro=5000
i=1
while True:
    sMiktari=sMiktari+200
    bSatisFiyati=bSatisFiyati+10
    ciro=(sMiktari*bSatisFiyati)
    i=i+1
    if(ciro>500000):
        print(i/12,"yıl sonra ciro 500000 TL'den fazla olur",ciro)
        break
#soru2
stkMiktari=10000
satinAlinanUrun=100
satilanUrun=500
i=1
while True:
    stkMiktari=stkMiktari+(satinAlinanUrun-satilanUrun)
    i=i+1
    if (stkMiktari==0):
        print(i,".ayda işletme stokları sıfırlanır")
        break
    
#soru3
sayi=''
kalan=0
while(sayi!=0):
    sayi=int(input("Bir sayı giriniz.Çıkmak için 0'a basınız:"))
    if(sayi==0):
        print("Çıkmak istediniz.program sonlandı.")
    else:
        z=(sayi%3)
        print("Girilen sayinin 3 ile bölümünden kalan:",z)
        kalan=kalan+sayi
        print("girilen sayilarin 3'e bolumunden kalanlarin toplami:",sayi%3)

#soru4
calisanSayisi=50
haftalikMesaiSuresi=''
aylikToplamYevmiye=90*0.10
a=2520
i=22#ay
while(haftalikMesaiSuresi!=22):
    haftalikMesaiSuresi=int(input("mesai süresini giriniz:"))
    if (haftalikMesaiSuresi==22):
        print("Aylık maaşınız hesaplanamaz")
    else:
        haftalikMesaiSuresi=int(haftalikMesaiSuresi)
        a=calisanSayisi*(a+(haftalikMesaiSuresi*4*aylikToplamYevmiye))
        print("Aylık maas:",a)
        i=i+1

#soru5
gunlukPantolon=200
defoluUrunSayisi=''
i=1#gün
while(defoluUrunSayisi!=40):
    defoluUrunSayisi=int(input("defolu ürün sayısı giriniz:"))
    if (defoluUrunSayisi>=40):
        print("Defolu ürün sayınız fazladır.")
    else:
        print(i,"günlük",defoluUrunSayisi,"defolu ürün")
        i=i+1
    
    
  
      
        
        
    
  
        
        
   
    

