f=open('students.csv', encoding='UTF-8')
a=f.readlines()
f.close()
a=[x.strip().split(',') for x in a]
shapka=a.pop(0)
while True:
    proj = input('Введите номер проекта: ')
    if proj=='СТОП':
        break
    for i in range(len(a)):
        if a[i][2] == proj:
            f, im, o = a[i][1].split()
            name = f'{im[0]}. {f}'
            print(f'Проект № {int(a[i][2])} делал: {name} он(а) получил(а) оценку - {int(a[i][-1])}')
            break
    else:
        print('Ничего не найдено')


