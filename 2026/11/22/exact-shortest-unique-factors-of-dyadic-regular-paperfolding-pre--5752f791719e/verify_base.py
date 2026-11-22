#!/usr/bin/env python3
"""Finite truth table used in the paperfolding shortest-unique-factor proof."""
from collections import Counter

def pf(n):
    return bytes(int(((j // (j & -j)) % 4) == 1) for j in range(1, n+1))

def unique_starts(word, length):
    c = Counter(word[i:i+length] for i in range(len(word)-length+1))
    return [i for i in range(len(word)-length+1) if c[word[i:i+length]] == 1]

for k, expected in ((6, (5, [43, 47])), (7, (9, [87, 95])), (8, (17, [175, 191]))):
    w=pf(1<<k)
    first=next((l, unique_starts(w,l)) for l in range(1,len(w)+1) if unique_starts(w,l))
    assert first == expected, (k,first)
    print(f'order={k} length={len(w)} shortest={first[0]} zero_based_starts={first[1]}')
w=pf(256)
a = {w[i:i+7] for i in range(0,len(w)-6,2)}
b = {w[i:i+7] for i in range(1,len(w)-6,2)}
assert len(a)==12 and len(b)==16 and a.isdisjoint(b)
print(f'length_seven_parity even={len(a)} odd={len(b)} intersection={len(a&b)}')
c=Counter(w[i:i+16] for i in range(len(w)-15))
hist=sorted(Counter(c.values()).items())
assert len(c)==64 and hist == [(3,16),(4,47),(5,1)], hist
print(f'length_sixteen_factors={len(c)} occurrence_histogram={hist}')
print('BASE_CERTIFICATE_PASS')
