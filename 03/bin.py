#!python3

import bitarray
import bitarray.util

f = open("input.txt","r")
count = 0
sums = [0] * 12
for line in f.readlines():
    bitstring = line.strip()
    for i in range(len(bitstring)):
        bit = int(bitstring[i])
        sums[i] += bit
    count += 1
gamma = bitarray.bitarray()
for i in range(len(sums)):
    sum = sums[i]
    if sum >= count/2:
        gamma.append(1)
    else:
        gamma.append(0)
    epsilon = gamma.copy()
    epsilon.invert()
    magnitude = bitarray.util.ba2int(epsilon) * bitarray.util.ba2int(gamma)
print(f"count[{count}] sums[{sums}] gamma[{gamma}] epsilon[{epsilon}] magnitude[{magnitude}]")