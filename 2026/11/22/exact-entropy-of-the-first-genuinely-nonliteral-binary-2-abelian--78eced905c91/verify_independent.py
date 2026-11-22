#!/usr/bin/env python3
"""Independent brute-force prefix test and suffix automaton count."""
from itertools import product
from collections import Counter

# Direct definition includes both one-letter and two-letter multiplicities.
def twoabelian(u,v):
    return (Counter(u)==Counter(v) and
            Counter(zip(u,u[1:]))==Counter(zip(v,v[1:])))

def ok(word):
    for i in range(len(word)-7):
        if twoabelian(word[i:i+4],word[i+4:i+8]):return False
    return True

# Independent recursion counts allowed prefixes, without the polynomial.
for n in range(8,16):
    exact=sum(ok(w) for w in product((0,1),repeat=n))
    dynamic={():1}
    for _ in range(n):
        following={}
        for tail,mul in dynamic.items():
            for bit in (0,1):
                new=tail+(bit,)
                if len(new)>=8 and twoabelian(new[-8:-4],new[-4:]):continue
                key=new[-7:]
                following[key]=following.get(key,0)+mul
        dynamic=following
    assert exact==sum(dynamic.values()),(n,exact)
print('PASS: direct exhaustive and separate suffix-DP counts agree through length 15')
