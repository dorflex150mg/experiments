import numpy as np
import scipy as sp
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h 




with open('./attestation_time.dat', 'r') as attestation_time_file:
    attestation_time_lines = attestation_time_file.readlines()
    before = []
    after = []
    differences = []
    before = [line.split(";")[0] for line in attestation_time_lines]
    for line in attestation_time_lines:
        if len(line.split(';')) >= 2:
            print line.split(';')
            after.append(line.split(";")[1])
    for index, value in enumerate(before):
        differences.append(after[index] - before)
    fake_differences = []
    for i in differences:
        fake_differences.append(i - 1000)
    cis_fake = []

    cis = []
    
#    for level in differences:
#        cis.append(mean_confidence_interval(level))
#    
#    for level in fake_differences:
#        cis.append(mean_confidence_interval(level))
    
    plt.figure()
    data = [differences, differences]
    plt.boxplot(data)
    plt.show()

