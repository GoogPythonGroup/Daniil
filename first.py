# coding: utf8
x = int(raw_input(u'Введи число от 1 до 9: '))
while x>=10 or x==0:
    print(u'Ввести все таки нужно от 1 до 9...')
    x = int(raw_input(u'Попробуй все заново с числами от 1 до 9: '))
if x>0 and x<=3:
    s = raw_input(u'Введи еще разок свое число от 1 до 3: ')
    n = int(raw_input(u'Сколько раз тебе повторить это число? \n Мне надо вот столько: '))
    print(s * n)
elif x>=4 and x<=6:
    m = int(raw_input(u'В какую степень мне надо возвести твое число? \n В вот такую: '))
    print(x ** m)
elif x>=7 and x<=9:
    for c in range(10):
        x=x+1
        print (x)
else:
    print u"Ошибка ввода!"
