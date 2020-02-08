lama=input(str('Masukkan huruf/ kata/ kalimat= '))
diganti=int(input('Kata yang ingin diganti di urutan ke- :'))
pengganti=input(str('Pengganti= '))

kata=lama.split()
#print(kata)

kata[diganti]=pengganti

print (kata)