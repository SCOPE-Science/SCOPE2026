#!/usr/bin/env python3
"""Independent direct-word and formal-series checks of the circular census.

All operations are integer-exact and require only Python's standard library.
"""
from collections import Counter

# Coefficients of t^j in 1-P(t,u).
A={1:Counter({1:1}),2:Counter({1:1,3:1}),3:Counter({3:1})}
C={0:Counter()}
for m in range(1,12):
    val=Counter()
    for j,a in A.items():
        if j>m: continue
        for w0,c0 in C[m-j].items():
            for w1,c1 in a.items():
                val[w0+w1]+=c0*c1
        if j==m:
            for w1,c1 in a.items(): val[w1]+=2*m*c1
    C[m]=val

def direct(n):
    out=Counter()
    primitives=Counter()
    for v in range(1<<n):
        s=f'{v:0{n}b}'
        if any(''.join(s[(i+j)%n] for j in range(4)) in ('0000','0110','1001','1111') for i in range(n)):
            continue
        ones=s.count('1')
        out[ones]+=1
        if all(s!=s[:d]*(n//d) for d in range(1,n) if n%d==0):
            primitives[ones]+=1
    return out,primitives

for n in range(1,17):
    observed,primitives=direct(n)
    expected=Counter() if n%2 else C[n//2]
    assert observed==expected,(n,observed,expected)
    if n%2: assert not primitives
    if n%2==0:
        assert set(observed)==set(range((n+3)//4,3*n//4+1)),(n,observed)
        assert sum(primitives)>0
    print(n,sorted(observed.items()),'primitive',sum(primitives.values()))
print('ALL DIRECT CHECKS PASS')
