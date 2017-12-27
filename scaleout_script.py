# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats
import sys
import matplotlib.patches as mpatches

#scaleout_file = open('./scaleout.dat', 'r')
#lines = scaleout_file.readlines()
#for line_index, line in enumerate(lines):
#    for char_index, char in enumerate(line):
#        if char == '\n':
#            lines[line_index] = lines[line_index][:char_index]
#
#split_lines = []
#for level_index, level in enumerate(lines):
#    split_lines.append(level.split(";"))
#
#before = []
#after = []
#
#for level_index, level in enumerate(split_lines):
#    before.append(level[:len(level)/2])
#    after.append(level[len(level)/2:])
#
#differences2 = []
#
#for index, level in enumerate(before):
#    differences2.append([])
#    for value_index, value in enumerate(level):
#        differences2[index].append(int(after[index][value_index]) - int(value))
#print differences2

#means = []


if sys.argv[1] == '-d':
    k_value = open('./scale_k.dat', 'r')
    lines = k_value.readlines()
    differences = [line.split(', ') for line in lines]
    for index, level in enumerate(differences):
        for indexd, difference in enumerate(level):
            if level[-1] == '\n':
                differences[index][indexd] = level[:-1]
    differences = [[int(difference) for difference in level] for level in differences]
    print differences


    s_value = open('./scaleout.dat', 'r')
    lines = s_value.readlines()
    differences2 = [line.split(', ') for line in lines]
    for index, level in enumerate(differences2):
        for indexd, difference in enumerate(level):
            if level[-1] == '\n':
                differences2[index][indexd] = level[:-1]
    differences2 = [[int(difference) for difference in level] for level in differences2]
    print differences2


import numpy as np
import scipy as sp
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h

cis = []
cik = []
for level in differences:
    cik.append(mean_confidence_interval(level))

for level in differences2:
    cis.append(mean_confidence_interval(level)) 

print "cis is" + str(cis)
print "cik is " + str(cik)

fig, ax3 = plt.subplots()
ax4 = ax3.twinx()
ax3.errorbar([2, 4, 6, 8], [mean[0] for mean in cis], yerr=[[mean[0] - mean[1] for mean in cis], [mean[2] - mean[0] for mean in cis]], color = 'b', capsize=4, fmt='--', ecolor='g', capthick=2)
ax4.errorbar([2, 4, 6, 8], [mean[0] for mean in cik], yerr=[[mean[0] - mean[1] for mean in cik], [mean[2] - mean[0] for mean in cik]], color = 'r', capsize=4, fmt='--', ecolor='g', capthick=2)
ax3.set_ylim(5000, 30000)
ax4.set_ylim(5000, 30000)
ax4.spines['right'].set_visible(False)
ax4.tick_params(labelright='off')
red_patch = mpatches.Patch(color='blue', label='SCO')
blue_patch = mpatches.Patch(color='red', label='Kubernetes')
plt.legend(handles=[red_patch, blue_patch])

ax3.set_axisbelow(True)
ax3.yaxis.grid(color='gray', linestyle='dashed')
ax3.set_ylabel("Tempo (ms)")
ax3.set_xlabel(u'Número de Instâncias')


plt.show() 
