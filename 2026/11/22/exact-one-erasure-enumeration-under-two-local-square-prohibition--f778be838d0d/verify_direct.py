#!/usr/bin/env python3
"""Independent literal enumeration of one-hole words (stdlib only)."""
from itertools import product
EXPECTED = [0,1,4,12,16,32,40,66,100,152,224,336,500]

def admissible(w):
    for k in (2,3):
        for i in range(len(w)-2*k+1):
            if all(w[i+j] == w[i+k+j] or '?' in (w[i+j], w[i+k+j])
                   for j in range(k)):
                return False
    return True

for n in range(1,len(EXPECTED)):
    count = 0
    for gap in range(n):
        for v in product('01', repeat=n-1):
            w = v[:gap] + ('?',) + v[gap:]
            count += admissible(w)
    assert count == EXPECTED[n], (n, count, EXPECTED[n])
print('PASS: exhaustive independently computed counts through length 12')
