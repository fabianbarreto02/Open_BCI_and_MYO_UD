import time
import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig=plt.figure()
ax=fig.add_subplot(111)
i=0
x,y=[],[]

while True:
    x.append(i)
    y.append(psutil.cpu_percent())
    ax.clear()
    ax.plot(x,y, color='b')
    print(psutil.cpu_percent())
    time.sleep(0.1)
    plt.show()
    i+=1