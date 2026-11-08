"""Finite-field checks for a simultaneous additive automorphism-witness theorem."""
from itertools import product
from math import factorial
from fractions import Fraction
from collections import Counter
import random

def det2(a,p):
    return (a[0]*a[3]-a[1]*a[2])%p

def invertibles(p):
    return [a for a in product(range(p),repeat=4) if det2(a,p)]

def good(B,As,p):
    return all(det2(tuple((x+y)%p for x,y in zip(B,A)),p)!=0 for A in As)

def sample_noncyclic(p,exhaustive):
    gl=invertibles(p)
    assert len(gl)==(p*p-1)*(p*p-p)
    k=p-1
    if exhaustive:
        lists=product(gl,repeat=k)
    else:
        rng=random.Random(20261104+p)
        lists=(tuple(rng.choice(gl) for _ in range(k)) for _ in range(125))
    count=0
    mini=None
    for As in lists:
        count+=1
        v=sum(good(B,As,p) for B in gl)
        assert v>0, (p,As)
        mini=v if mini is None else min(mini,v)
    if exhaustive:
        assert count==len(gl)**k
    print(f'GL2 p={p} k={k} tuples={count} minimum_witnesses={mini}')

def scalar_probability(p,r):
    n=p-1
    choices=list(product(range(1,p),repeat=n))
    successes=[sum(u not in {(-a)%p for a in seq} for u in range(1,p)) for seq in choices]
    good_count=sum(int(v>0) for v in successes)
    expected=Fraction(1,1)-Fraction(factorial(n),n**n)
    assert Fraction(good_count,len(choices))==expected
    # Distinct scalar-exponent components have independent diagonal images.
    total=len(choices)**r
    good=good_count**r
    assert Fraction(good,total)==expected**r
    if r<=2:
        freq=Counter({1:1})
        for _ in range(r):
            nextfreq=Counter()
            for a,c in freq.items():
                for b in successes:
                    nextfreq[a*b]+=c
            freq=nextfreq
        assert sum(freq.values())==total
        print(f'cyclic-singleton p={p} r={r} probability={good}/{total}={expected**r} witness_counts={dict(sorted(freq.items()))}')
    else:print(f'cyclic-singleton p={p} r={r} probability={good}/{total}={expected**r}')

if __name__=='__main__':
    sample_noncyclic(2,True)
    sample_noncyclic(3,True)
    sample_noncyclic(5,False)
    for p in (2,3,5,7):
        for r in (1,2):
            scalar_probability(p,r)
    # Explicit distinct-exponent example (C3 x C9). There are 108 automorphisms,
    # with a 27-element kernel and two independent GL1(F3) factors.
    p=3
    maps=[(a,b,c,d) for a in (1,2) for b in range(3) for c in range(3) for d in range(9) if d%3]
    assert len(maps)==108
    freq=Counter()
    for B1 in maps:
        for B2 in maps:
            n1=sum(int((a+B1[0])%3!=0 and (a+B2[0])%3!=0) for a in (1,2))
            n2=sum(int((d+B1[3])%3!=0 and (d+B2[3])%3!=0) for d in (1,2))
            freq[27*n1*n2]+=1
    assert freq=={0:8748,27:2916},freq
    print(f'Aut(C3 x C9) ordered_pairs={len(maps)**2} witness_count_distribution={dict(sorted(freq.items()))}')
    print('VERIFY_OK')
