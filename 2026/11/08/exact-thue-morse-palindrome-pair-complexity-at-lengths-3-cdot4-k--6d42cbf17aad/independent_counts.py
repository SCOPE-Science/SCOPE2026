#!/usr/bin/env python3
"""Direct independent enumeration of distinct Thue--Morse palindrome pairs."""
from collections import defaultdict

def pal_pair(w):
    return any(w[:cut]==w[:cut][::-1] and w[cut:]==w[cut:][::-1]
               for cut in range(len(w)+1))

def morse_prefix(min_size):
    w='0'
    while len(w)<min_size:
        w=''.join('01' if x=='0' else '10' for x in w)
    return w

def phi4(w):
    return ''.join('0110' if x=='0' else '1001' for x in w)

# For every length L at most 192, every factor occurs inside an
# explicit large prefix (the language of the fixed point is uniformly
# recurrent). The test is supplementary to the infinite proof.
t=morse_prefix(32768)
for k in range(4):
    n=3*4**k
    found={t[i:i+n] for i in range(len(t)-n+1)}
    P={w for w in found if pal_pair(w)}
    a='010'; b='101'
    for _ in range(k):
        a=phi4(a);b=phi4(b)
    orbits=set()
    for v in (a,b):
        orbits.update(v[i:]+v[:i] for i in range(n))
    assert P==orbits, (k,len(P),len(orbits),len(P-orbits),len(orbits-P))
    assert len(P)==2*n
    print('k=',k, 'n=',n,'factors=',len(found),'palindrome pairs=',len(P))
