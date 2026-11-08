#!/usr/bin/env python3
"""Uniformly sample a minimum radius-one identifying code of K(2,n).

Uses just the Python standard library. A vertex is a ternary string with
unequal adjacent symbols. A code is a set of such strings of length n.
"""
import random
from itertools import product

def vertices(n):
    return [''.join(w) for w in product('012',repeat=n)
            if all(w[i]!=w[i+1] for i in range(n-1))]

def sample(n, rng=None):
    if n < 2: raise ValueError('n must be at least 2')
    if rng is None: rng = random.SystemRandom()
    if n == 2:
        return set(rng.choice((('01','12','20'), ('02','21','10'))))
    H = vertices(n - 2)
    D = vertices(n - 1)
    incoming = {x: sorted(w for w in D if w[1:] == x) for x in H}
    outgoing = {x: sorted(w for w in D if w[:-1] == x) for x in H}
    # Each digit is a bijection between incoming and outgoing edges at x.
    patterns = []
    for a,b in (('0','1'),('0','2'),('1','2')):
        v = ''.join(a if i%2 == 0 else b for i in range(n-1))
        w = ''.join(b if i%2 == 0 else a for i in range(n-1))
        required = {}
        for source,target in ((v,w),(w,v)):
            x = source[1:]
            i = incoming[x].index(source)
            j = outgoing[x].index(target)
            required[x] = i ^ j
        assert len(required) == 2
        patterns.append(required)
    if n == 3:
        admissible = [dict(zip(H, bits)) for bits in product((0,1),repeat=3)
                      if all(any(dict(zip(H,bits))[x]!=v for x,v in req.items())
                             for req in patterns)]
        assert len(admissible) == 4
        switches = rng.choice(admissible)
    else:
        switches = {}
        for required in patterns:
            x,y=tuple(required)
            assert x not in switches and y not in switches
            allowed=[(p,q) for p,q in product((0,1),repeat=2)
                     if (p,q)!=(required[x],required[y])]
            switches[x],switches[y]=rng.choice(allowed)
        for x in H:
            if x not in switches: switches[x]=rng.randrange(2)
    code = set()
    for x in H:
        for i in range(2):
            p = incoming[x][i]; q = outgoing[x][i ^ switches[x]]
            code.add(p + q[-1])
    return code

if __name__=='__main__':
    from verify import identify
    rng = random.Random(2021)
    for n in range(2,9):
        for _ in range(8):
            s=sample(n,rng)
            assert len(s)==3*2**(n-2)
            assert identify(n,s)
    print('UNIFORM_SAMPLER_CONSTRUCTION_OK')
