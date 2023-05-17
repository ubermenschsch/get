import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from textwrap import wrap


with open('settings.txt') as settings:
    settings = [float(i) for i in settings.read().split('\n')]

data_volt = np.loadtxt('data.txt', dtype=int) * settings[1]
data_time = np.array([i * settings[0] for i in range(data_volt.size)])


fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

ax.axis([data_time.min(), data_time.max()+1, data_volt.min(), data_volt.max()+0.2])

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.set_title("\n".join(wrap('График напряжения от времени при зарядке/разярядке конденсатора', 90)), loc = 'center')
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

ax.plot(data_time, data_volt, c='black', linewidth=1, label = 'V(t)')
ax.scatter(data_time[0:data_volt.size:20], data_volt[0:data_volt.size:20], marker = 's', c = 'blue', s=10)

ax.legend(shadow = False, loc = 'right', fontsize = 45)



fig.savefig('graph.png')
fig.savefig('graph.svg')
