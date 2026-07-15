print("hello word")
for i in range (10):
    if i % 2 == 0:
        print(i)
    elif i ==3:
        print(i, "bu 3'tür.")
    else:
        print("bu değer tek sayı:",i)

liste = ["kedi",7, 2, False]
print("liste", liste)

liste2 =[1, 3, 5, 7]
for i in liste2:
    print(i)
print(liste2)
liste2.append("son eleman")
liste2.insert(1,2)
liste2.remove(5)

print(liste2)

liste2.pop()
x = liste2.pop()
print(x)
print(liste)

liste2[2] ="3." 
print(liste2)

print(bool(liste2))

print(liste2[1:3])
# TUPLE
tpl = (1,3)
print(tpl)

tpl2 = (5, )

tuple3 = ("kedi,""köpek","fare")
a,b,c = tuple3
print(tuple3)
print(a," - ",b," - ",c) 

#Dict - sözlük
kisi= {
    "ad": "özkan",
    "yas": 29,
    "il": "Antalya"
    }
kisi["meslek"] = "ögretmen"
del kisi["il"]
print(kisi)

for a, b in kisi.items():
    print("key:", a, " - value: ", b)

print(kisi["ad"])
print(kisi.get("soyad","soyad adında bi key bulunmadı!"))
print(kisi.keys())
print(kisi.values())

kume = {3, 3, 5, 6, "test"}
print(kume1)
print(kume2)
print(kume1 | kume2)
print(kume1 & kume2 )
print(kume1 - kume2 )

kume1.discard(3)
kume1.add(33)
print(kume1)



     
