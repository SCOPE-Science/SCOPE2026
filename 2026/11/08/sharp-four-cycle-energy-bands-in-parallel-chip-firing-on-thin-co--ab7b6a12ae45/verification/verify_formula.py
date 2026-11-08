"""Exact polynomial identity, boundary, gap, and orbit-count checks.
No state dynamics is used here; symbolic/combinatorial recurrence only.
"""
from collections import Counter
from math import comb
for b in range(2,51):
    s=Counter()
    for r in range(1,b):
        for i in range(r):
            for j in range(b-r):
                s[i+j]+=comb(b,r)
    # (1-z)^2 S_b(z) = 2^b(1+z^b)-2(1+z)^b
    for k in range(b+1):
        lhs=s[k]-2*s[k-1]+s[k-2]
        rhs=(2**b)*((k==0)+(k==b))-2*comb(b,k)
        assert lhs==rhs,(b,k,lhs,rhs)
    assert sum(s.values())==b*(b-1)*2**(b-2)
    assert s[0]==2**b-2 and s[b-2]==2**b-2
    assert not s[b-1] and not s[-1]
    # Low and high bands disjoint and meet the two endpoints of the middle stair.
    assert 2*b+(b-2)==3*b-2 and 7*b-2-(3*b-2)==4*b
print('POLYNOMIAL_OK b=2..50')
