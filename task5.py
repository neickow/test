f = open('students.csv', encoding='UTF-8')
a = f.readlines()
f.close()
shapka = a.pop(0)
a = [x.strip().split(',') for x in a]
f = open('students_with_hash.csv', 'w', encoding='UTF-8')


def hsh(n):
    fio = n[1]
    p = 67
    m = 10 ** 9 + 9
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper() + ' '
    hashfio = [alf.index(x) + 1 for x in fio]
    hs = 0
    for i in range(len(hashfio)):
        hs += hashfio[i] * (p ** i % m)
    return hs

f.write(shapka)
for x in a:
    fio = x[1]
    hs = hsh(x)
    f.write(str(hs)+','.join(x)+'\n')
