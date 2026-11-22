#!/usr/bin/env python3
"""Independent finite checks for Coxeter-period zero-Hecke stabilization."""
from itertools import product
from collections import Counter
from random import Random


def coxeter_order(signs):
    n = len(signs) + 2
    predecessor = [set() for _ in range(n)]
    for i, sign in enumerate(signs, 1):
        if sign == 1:
            predecessor[i+1].add(i)
        else:
            predecessor[i].add(i+1)
    order = []
    used = set()
    for _ in range(1, n):
        avail = [i for i in range(1, n) if i not in used and predecessor[i] <= used]
        assert avail
        j = min(avail)
        used.add(j)
        order.append(j)
    return order


def one_round(values, order):
    values = list(values)
    for j in order:
        if values[j-1] < values[j]:
            values[j-1], values[j] = values[j], values[j-1]
    return values


def direct_time(signs, data=None):
    n = len(signs)+2
    order = coxeter_order(signs)
    values = list(range(n)) if data is None else list(data)
    target = sorted(values, reverse=True)
    for t in range(1, n+1):
        values = one_round(values, order)
        if values == target:
            return t
    raise AssertionError('uniform bound failed')


def formula_time(signs):
    n = len(signs)+2
    h = [0]
    for s in signs:
        h.append(h[-1]+s)
    maxgap = max(abs(h[a-1]-h[n-a-1]) for a in range(1,n))
    assert (n+maxgap)%2==0
    return (n+maxgap)//2


def transfer_count(n, bound):
    # Exact number of orientations with stabilization time <= bound.
    if n%2==0:
        m=n//2
        k=bound-m
        if k<0:return 0
        lo,hi=-k,k
        steps=m-1
        initial_factor=1
    else:
        m=(n-1)//2
        k=bound-(m+1)
        if k<0:return 0
        lo,hi=-k-1,k
        steps=m-1
        initial_factor=2
    states={0:1}
    for _ in range(steps):
        nxt={}
        for v,w in states.items():
            for delta,weight in ((-1,1),(0,2),(1,1)):
                if lo<=v+delta<=hi:
                    nxt[v+delta]=nxt.get(v+delta,0)+w*weight
        states=nxt
    return initial_factor*sum(states.values())


def check():
    full=0
    threshold=0
    for n in range(3,12):
        freq=Counter()
        for bits in product((-1,1),repeat=n-2):
            t=direct_time(bits)
            assert t==formula_time(bits), (n,bits,t,formula_time(bits))
            freq[t]+=1
            for a in range(1,n):
                binary=[0]*a+[1]*(n-a)
                target=(n+sum(bits[:a-1])-sum(bits[:n-a-1]))//2
                assert direct_time(bits,binary)==target, (n,bits,a,target)
                threshold+=1
            full+=1
        assert sum(freq.values())==2**(n-2)
        for bound in range(1,n+1):
            assert sum(v for k,v in freq.items() if k<=bound)==transfer_count(n,bound)
        print('EXHAUSTIVE_PASS n=',n,'orientations=',2**(n-2), 'distribution=',dict(sorted(freq.items())))
    print('BINARY_THRESHOLD_PASS checks=',threshold)
    rng=Random(20261115)
    random_checks=0
    for n in (12,13,16,21,28,40,60):
        for _ in range(120):
            signs=tuple(rng.choice((-1,1)) for _ in range(n-2))
            assert direct_time(signs)==formula_time(signs)
            random_checks+=1
    print('LARGE_RANDOM_PASS checks=',random_checks)
    for n in range(3,31):
        minimum=(n+1)//2
        count=transfer_count(n,minimum)
        if n%2==0:
            assert count==2**(n//2-1)
        else:
            assert count==2*3**((n-3)//2)
        assert transfer_count(n,n-1)==2**(n-2)
    print('TRANSFER_EXTREMES_PASS n=3..30')
    print('CHECKER_PASS')

if __name__ == '__main__':
    check()
