from math import *
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft

duration = 0.03
sample_rate = 44100
freq = 2000
num_samples = int(duration * sample_rate)
sample = []
for i in range(num_samples):
    # sample.append(sin(2 * pi * i / (sample_rate/freq)) + sin(2 * pi * i / (sample_rate/1000)))
    x = sin(2 * pi * i / (sample_rate/1209))
    y = sin(2 * pi * i / (sample_rate/697))
    sample.append((x+y)/2)
plt.plot(sample)
plt.show()