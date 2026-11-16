#!/usr/bin/env python3
"""Independent integer checks for graphical inversion Walsh coefficients.
This finite checker is corroboration, not an all-length proof.
"""
import itertools
import math
import random
from functools import reduce


def inversion_masks(n):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    out = []
    for p in itertools.permutations(range(n)):
        position = [0]*n
        for k,vertex in enumerate(p):
            position[vertex] = k
        out.append(sum(1 << t for t,(i,j) in enumerate(edges)
                       if position[i] > position[j]))
    return out, len(edges)


def walsh_hadamard(a):
    a = list(a)
    step = 1
    while step < len(a):
        for start in range(0,len(a),step*2):
            for k in range(step):
                x,y=a[start+k],a[start+step+k]
                a[start+k] = x+y
                a[start+step+k] = x-y
        step*=2
    return a


def main():
    for n in range(1,7):
        masks,m = inversion_masks(n)
        f=[0]*(1<<m)
        for x in masks:
            assert f[x]==0, 'order maps non-injectively to orientations'
            f[x]=1
        values=walsh_hadamard(f)
        v=n-n.bit_count()
        q=1<<v
        assert all(z%q==0 for z in values)
        assert reduce(math.gcd,values,0)==q
        assert values[0] == math.factorial(n)
        if n>=2:
            assert all(values[b]==0 for b in range(1<<m) if b.bit_count()%2)
        # Completely independent signed inversion computation on sampled frequencies.
        rng=random.Random(17000+n)
        samples=set([0,(1<<m)-1])
        for _ in range(min(50,1<<m)):
            samples.add(rng.randrange(1<<m))
        for b in samples:
            exact=sum(1 if ((b & mask).bit_count()%2)==0 else -1 for mask in masks)
            assert exact==values[b]
        print('exhaustive',n,'frequencies',1<<m,'gcd',q,'zeros',values.count(0))
    for n in (7,8):
        masks,m = inversion_masks(n)
        q=1<<(n-n.bit_count())
        rng=random.Random(8412+n)
        for _ in range(300):
            b=rng.randrange(1<<m)
            w=sum(1 if ((b & mask).bit_count()%2)==0 else -1 for mask in masks)
            assert w%q==0
            if b.bit_count()%2: assert w==0
        print('sampled',n,'frequencies',300,'divisor',q)
    print('TRANSITIVE_TOURNAMENT_FOURIER_GCD_PASS')

if __name__=='__main__':main()
