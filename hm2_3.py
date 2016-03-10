# coding: utf8
x = 'toyota this is car, subaru the same machine. lexus can be machine; mazda it is certainly not the car!'
p = raw_input(u'Введите символ по которому надо разделить: ')
xp = x.split(p)
print min(xp)