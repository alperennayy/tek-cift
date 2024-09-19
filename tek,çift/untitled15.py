
try : 
    
    a = int(input("bir sayi giriniz : "))
    if a<0 : 
        print(f"{a} sayısı 0 dan küçük,lüfen 0 dan büyük bir sayi giriniz..")
    else : 
        if a%2==0 : 
            print(f"{a} sayısı çift bir sayi")
        else : 
            print(f"{a} sayısı tek bir sayi")
            
except ValueError : 
    print("lütfen tam sayi giriniz...")

