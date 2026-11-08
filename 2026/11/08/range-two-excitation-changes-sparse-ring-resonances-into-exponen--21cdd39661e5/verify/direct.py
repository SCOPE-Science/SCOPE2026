#!/usr/bin/env python3
"""Direct exhaustive Greenberg-Hastings simulation on cyclic range-two graphs."""
from itertools import product

def step(s):
    n=len(s)
    return tuple((a+1)%3 if a else int(any(s[j]==1 for j in ((i-2)%n,(i-1)%n,(i+1)%n,(i+2)%n))) for i,a in enumerate(s))

def local_condition(s):
    n=len(s)
    return all(any(s[j]==(s[i]+1)%3 for j in ((i-2)%n,(i-1)%n,(i+1)%n,(i+2)%n)) for i in range(n))

expected={5:150,6:270,7:588,8:1548,9:4092,10:10710,11:26400}
for n in range(5,12):
    count=0
    for s in product(range(3),repeat=n):
        periodic=step(step(step(s)))==s and step(s)!=s
        prescribed=local_condition(s)
        assert periodic==prescribed,(n,s,periodic,prescribed)
        count+=periodic
    assert count==expected[n],(n,count,expected[n])
    print('n=%2d states=%d primitive_three=%d'%(n,3**n,count))
# Nearest-neighbor ring: the sharp arithmetic resonance comparison.
for n in range(3,13):
    count=0
    for s in product(range(3),repeat=n):
        if all(s[(i-1)%n]==(s[i]+1)%3 or s[(i+1)%n]==(s[i]+1)%3 for i in range(n)):
            count+=1
    assert count==(6 if n%3==0 else 0)
    print('nearest n=%2d primitive_three=%d'%(n,count))
print('DIRECT STATE AND LOCAL CONDITION CHECKS PASSED')
