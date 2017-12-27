import matplotlib.pyplot as plt
k2 = [13060, 10956, 10898, 6878, 11826, 5953, 10820, 5939, 8077, 12083, 10455]
s2 = [12917, 12905, 12884, 13882, 12869, 12875, 12901, 12876, 12888, 12870, 12885]
data = [k2, s2]
f, (axA, axB) = plt.subplots(2, 1, sharex=True)
axA.boxplot(data)
axB.boxplot(data)
axA.set_ylim(4000, 14000)
axB.set_ylim(9000, 13500)
axA.set_ylabel("Tempo (ms)")
axB.set_ylabel("Tempo (ms)")
axA.spines['bottom'].set_visible(False)
axB.spines['top'].set_visible(False)
axA.xaxis.tick_top()
axA.tick_params(labeltop='off')
axA.set_axisbelow(True)
axA.yaxis.grid(color='gray', linestyle='dashed')
axB.set_axisbelow(True)
axB.yaxis.grid(color='gray', linestyle='dashed')
plt.xticks([1, 2], ['Kubernetes', 'SCO'])


d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=axA.transAxes, color='k', clip_on=False)
axA.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axA.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axB.transAxes)  # switch to the bottom axes
axB.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axB.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
plt.show()
