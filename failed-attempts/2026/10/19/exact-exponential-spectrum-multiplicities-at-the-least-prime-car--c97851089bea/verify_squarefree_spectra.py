#!/usr/bin/env python3
"""Exact cyclotomic checks for the prime-cardinality squarefree Fourier theorem."""
import itertools
import random
from collections import Counter
from math import prod
from sympy import Poly, Symbol, cyclotomic_poly

x=Symbol('x')

def make_reduced(N):
    mod=Poly(cyclotomic_poly(N,x),x,domain='ZZ')
    d=mod.degree()
    vec=[]
    for i in range(N):
        v=Poly(x**i,x,domain='ZZ').rem(mod)
        vec.append(tuple(int(v.nth(j)) for j in range(d)))
    return vec

def actual_zero(a,k,vec,N):
    z=[0]*len(vec[0])
    for v in a:
        row=vec[(k*v)%N]
        for j,w in enumerate(row): z[j]+=w
    return not any(z)

def spectrum_predictions(a, primes):
    p=primes[0]
    if set(v%p for v in a)!=set(range(p)):
        return 0
    s=[r for r in primes[1:] if len({v%r for v in a})==1]
    return prod(primes[1:])*prod(r**(p-1) for r in s)

def pair_pred(a,b,primes):
    p=primes[0]
    return (len({v%p for v in a})==p and len({v%p for v in b})==p
         and all(len({v%r for v in a})==1 or len({v%r for v in b})==1 for r in primes[1:]))

def exact_case(primes):
    p=primes[0]; N=prod(primes);vec=make_reduced(N)
    aa=list(itertools.combinations(range(N),p))
    zero={a:{k for k in range(1,N) if actual_zero(a,k,vec,N)} for a in aa}
    counts=Counter()
    pair_num=0
    for a in aa:
        num=0
        for b in aa:
            observed=all(((v-u)%N) in zero[a] for u,v in itertools.combinations(b,2))
            predicted=pair_pred(a,b,primes)
            assert observed==predicted,(primes,a,b,observed,predicted)
            num+=int(observed)
        assert num==spectrum_predictions(a,primes),(a,num,spectrum_predictions(a,primes))
        counts[num]+=1;pair_num+=num
    Q=N//p
    expected=Q*prod(2*r**p-r for r in primes[1:])
    assert pair_num==expected
    predicted=Counter()
    for mask in itertools.product((0,1),repeat=len(primes)-1):
        s=[r for r,t in zip(primes[1:],mask) if t]
        v=Q*prod(r**(p-1) for r in s)
        ct=prod((r if t else r**p-r) for r,t in zip(primes[1:],mask))
        predicted[v]+=ct
    predicted[0]=len(aa)-Q**p
    assert counts==predicted,(counts,predicted)
    print('EXACT',primes,'A=',len(aa),'ordered spectral pairs=',pair_num,'multiplicities=',dict(sorted(counts.items())))

exact_case([2,3])
exact_case([2,3,5])
exact_case([3,5])

# Independent all-character checks at a larger squarefree order, not relying on the
# finite pigeonhole counting formulas in the prediction implementation.
primes=[3,5,7];N=prod(primes);p=3
v=make_reduced(N); rng=random.Random(270522)
for j in range(1700):
    a=tuple(sorted(rng.sample(range(N),p)))
    k=rng.randrange(1,N)
    exp_zero=(len({a0%p for a0 in a})==p and k%p!=0
       and all((k%r==0 or len({a0%r for a0 in a})==1) for r in primes[1:]))
    assert actual_zero(a,k,v,N)==exp_zero,(a,k,exp_zero)
for j in range(250):
    a=tuple(sorted(rng.sample(range(N),p)))
    b=tuple(sorted(rng.sample(range(N),p)))
    observed=all(actual_zero(a,(t-s)%N,v,N) for s,t in itertools.combinations(b,2))
    assert observed==pair_pred(a,b,primes),(a,b)
print('SAMPLED [3,5,7]: 1700 exact Fourier vanishing tests and 250 exact pairs')
print('VERIFY_OK')
