maksFib = int(input("masukkan batas fibonacci= "))
m=int(input('banyak baris= '))
n=int(input('banyak kolom= '))
a, b = 0,1
fibSeri =[ ]
while b < maksFib:
    fibSeri.append(b)
    a,b = b, a+b

x=fibSeri
print (x)

for i in range(m):
    fibSeri.append(x)
    print (a)

