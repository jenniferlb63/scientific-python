import numpy as np
import pylab
# this is the SWIG generated module
import cos_doubles

x = np.arange(0, 2 * np.pi, 0.1)
y = np.zeros(len(x))  # preallocate

cos_doubles.cos_doubles_func(x, y)
pylab.plot(x, y)
pylab.show()
