f=open('students.csv', encoding='UTF-8')
a=f.readlines()
f.close()
a=[x.strip().split(',') for x in a]
shapka=a.pop(0)
for i in range(len(a)):
    if 'Хадаров Владимир' in a[i][1]:
        print(f'Ты получил: {a[i][-1]}, за проект - {a[i][2]}')
        break
d={}
for x in a:
    clas = x[3]
    score=x[-1]
    if score!='None':
        if clas not in d:
            d[clas]=[int(score)]
        else:
            d[clas]+=[int(score)]
for clas in d:
    d[clas] = round(sum(d[clas])/len(d[clas]), 3)
for i in range(len(a)):
    if a[i][-1]=='None':
        a[i][-1]=str(d[a[i][3]])
f=open('students_new.csv', 'w', encoding='UTF-8')
f.write(str(shapka)+'\n')
for x in a:
    f.write(','.join(x)+'\n')
f.close()


