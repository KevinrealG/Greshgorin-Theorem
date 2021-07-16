import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
ax.axis([0, 100, 0, 100])
ax.set_aspect("equal")

axcolor = 'skyblue'
sl1 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
sl2 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
sl3 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

slider_r1 = Slider(sl1, 'r1', 0.0, 50.0, 25)
slider_r2 = Slider(sl2, 'r2', 0.0, 50.0, 25)
slider_d = Slider(sl3, 'dist', 0.0, 100.0, 50)

circ1 = plt.Circle((25,50), 25, ec="k")
circ2 = plt.Circle((75,50), 25, ec="k")
ax.add_patch(circ1)
ax.add_patch(circ2)
plt.show()
