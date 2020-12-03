#1 график f()

import matplotlib as mpl                        
mpl.use('Agg')                                  # не рисовать на экране
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)                     # от -5 до 2 сделать 100 точек
y1 = -5*cos(10*x)*sin(3*x)/(x^(1/2))                    # y1 - тоже много точек
y2 = ((-5*sin(3*x)*cos(10*x)/(x^1/2))
      
fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(x, y1, color="blue", label="y(x)")      # функция y1(x), синий, надпись y(x)
ax.plot(x, y2, color="red", label="y'(x)")      # функция y2(x), красный, надпись y'(x)
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('1.png')                            # сохранить в файл 1.png




import pylab
xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]
ydata = [0.1, 0.2, 0.4, 0.8, 0.6, 0.1]
pylab.bar (xdata, ydata)
pylab.show()

#2 подсчет кол-во букв и составление гистограмы


import pylab
xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]
ydata = [0.1, 0.2, 0.4, 0.8, 0.6, 0.1]
pylab.bar (xdata, ydata)
pylab.show()


import re
from collections import Counter


new_words = []
with open('Текст.txt', 'r') as infile:
    lines = [line for line in infile.readlines() if line.strip()]

for line in lines:
    clean_line = re.sub(r'(\b(section\s[\d]{1,2})\b)', '', line)
    clean_line_2 = re.sub(r'([()])', '', clean_line)
    new_words.append(clean_line_2.lower().replace('.', '').replace(';', '').replace('\n', '').replace('-', ' ').replace(" ", ""))
    
new_words_unit = ''.join(new_words)

if len(new_words_unit) > 0:
    print (Counter(new_words_unit))







