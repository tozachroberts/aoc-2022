#!python3

import bitarray
import bitarray.util

f = open("input.txt","r")
bitarrays = []
for line in f.readlines():
    bitstring = line.strip()
    bitarrays.append(bitarray.bitarray(bitstring))
omask = bitarray.bitarray()
bit_index = 0
matching_bitarrays = bitarrays.copy()
while(len(matching_bitarrays) > 1):
    sum = 0
    for ba in matching_bitarrays:
        bit = ba[bit_index]
        sum += bit
    if sum >= len(matching_bitarrays)/2:
        omask.append(1)
    else:
        omask.append(0)
    bit_index += 1
    matching_bitarrays = [ba for ba in bitarrays if ba[0:bit_index] == omask]
if len(matching_bitarrays) != 1:
    raise Exception(f"More than one matching for o: omask[{omask}] matching[{matching_bitarrays}]")
o_ba = matching_bitarrays[0]
o = bitarray.util.ba2int(o_ba)

comask = bitarray.bitarray()
bit_index = 0
matching_bitarrays = bitarrays.copy()
while(len(matching_bitarrays) > 1):
    sum = 0
    for ba in matching_bitarrays:
        bit = ba[bit_index]
        sum += bit
    if sum < len(matching_bitarrays)/2:
        comask.append(1)
    else:
        comask.append(0)
    bit_index += 1
    matching_bitarrays = [ba for ba in bitarrays if ba[0:bit_index] == comask]
if len(matching_bitarrays) != 1:
    raise Exception(f"More than one matching for co: comask[{comask}] matching[{matching_bitarrays}]") 
co_ba = matching_bitarrays[0]
co = bitarray.util.ba2int(co_ba)
score = o * co
print(f"omask[{omask}] o_ba[{o_ba}] o[{o}] comask[{comask}] co_ba[{co_ba}] co[{co}] score[{score}]")