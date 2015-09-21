"""
Linewidth
=========

Plot various linewidth with matplotlib.
"""

import pylab as pl

size = 256, 16
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = pl.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
pl.axes([0, .1, 1, .8], frameon=False)

for i in range(1, 11):
    pl.plot([i, i], [0, 1], color='b', lw=i/2.)

pl.xlim(0, 11)
pl.ylim(0, 1)
pl.xticks(())
pl.yticks(())

pl.show()
