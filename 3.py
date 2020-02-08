x=input ('Masukkan kata=')
vokal='A','I','U','E','O','a','i','u','e','o'
jumvokal=''
for character in x:
    if character in vokal:
        jumvokal+=character
        y=len(jumvokal)
print ('Banyaknya huruf vokal:')
print (len(jumvokal))