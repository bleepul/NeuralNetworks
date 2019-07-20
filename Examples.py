import numpy
import matplotlib.pyplot as plt

a = numpy.zeros([3, 2])
print(a)

a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 9
a[2, 1] = 12

print(a)

v = a[1, 0]
print(v)

#plt.interactive(False)
plt.imshow(a, interpolation="nearest")
plt.show()
