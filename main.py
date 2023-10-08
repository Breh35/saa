import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


uzunluk = int(input("kac karakter uzunluk olan sifre istiyorsun?"))


sifre = ""

for i in range(uzunluk):
    sifre += random.choice(karakterler)

print(sifre)
