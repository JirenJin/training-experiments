#! /usr/bin/env python
# -*-coding:utf8 -*-

import sys

from matplotlib import pyplot as plt

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = list(f)

lines = [line.strip() for line in lines]
print len(lines)
x = range(1, len(lines) + 1)
plt.plot(x, lines)
plt.show()
