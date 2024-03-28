from random import choice
f=open('students.csv', encoding='UTF-8')
a=f.readlines()
f.close()
shapka=a.pop(0)
a=[x.strip().split(',') for x in a]
def login(n):
    f,im,o = n[1].split()
    name = f'{f}_{im[0]}{o[0]}'
    return name
def password():
    alf='abcdefghijklmnoprpqrstuvwxyzABCDEFGHIJKLMNOPRPQRSTUVWXYZ123456789'
    c1="abcdefghijklmnoprpqrstuvwxyz"
    c2='ABCDEFGHIJKLMNOPRPQRSTUVWXYZ'
    c3='123456789'
    while True:
        pw = ''
        for i in range(8):
            pw += choice(alf)
        if any([x in c1 for x in pw]) and any([x in c2 for x in pw]) and any([x in c3 for x in pw]):
            return pw
# for i in range(len(a)):
#     print(a[i], login(a[i]), password())
f=open('students_password.csv', 'w', encoding='UTF-8')
for x in a:
    lg=login(x)
    pw=password()
    f.write(','.join(x+[lg, pw])+'\n')


