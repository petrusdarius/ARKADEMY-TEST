print ("=====BIODATA DIRI=====")
Name = input(str("Masukkan Nama="))
Age = int(input("Masukkan umur="))
Address = input(str("Masukkan alamat="))

#untuk hobi
hobi=[]
stop=False
i=0

#Isi hobi
while(not stop):
    hobi_baru=input(str("Inputkan hobi ke-{}:".format(i)))
    hobi.append(hobi_baru)
    
    i+=1
    tanya=input(str("Tambah hobi?(y/t)="))
    if(tanya=="t"):
        stop=True
    
#untuk status perkawinan
Status=input(str('is married?(married/single)='))
if(Status=="married"):
    print ("True")
else :
    print ("False")
    
#untuk list_school
sekolah=input(str("Masukkan nama sekolah="))
thn_masuk=int(input('Tahun masuk='))
thn_lulus=int(input('Tahun_lulus='))
jurusan=input(str('Jurusan='))
Education=[sekolah,thn_masuk,thn_lulus,jurusan]
#skills
kemampuan=[]
stop=False
i=0

#Isi skill
while(not stop):
    kemampuan_baru=input(str("Inputkan skill ke-{}: ".format(i)))
    kemampuan.append(kemampuan_baru)
    mastery=input(str("Level (Beginner, Advanced, Expert)="))
    
    i+=1
    tanya=input(str("Tambah skill?(y/t)="))
    if(tanya=="t"):
        stop=True
        
#untuk Interest
Interest=input(str('Interest in coding?(yes/no)='))
if(Interest=="yes"):
    print ("Yes")
else :
    print ("No")        

print ('==========BIODATA DIRI==========')
print ("Name:",Name)
print ("Age:",Age)
print ('Address:',Address)
print ('Hobbies:')
for hb in hobi:
    Hobbies=print ("-{}".format(hb))
print ('is_married:',Status)
print ('Education:',Education)
print ('Skills:')
for sk in kemampuan:
    Skills=print ("-{}".format(sk),',', 'Level: ',mastery)
print ('Interest in coding:',Interest)    

