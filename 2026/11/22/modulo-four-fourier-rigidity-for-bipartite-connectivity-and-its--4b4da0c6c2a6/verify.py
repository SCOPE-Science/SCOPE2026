#!/usr/bin/env python3
"""Independent exact enumeration of connected-subgraph Walsh coefficients on K(4,4).
No external packages. Run with Python 3.9+.
"""
from collections import Counter
from math import factorial

M = N = 4
D = M * N
SIZE = 1 << D


def connected(mask):
    parent = list(range(M+N))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in range(M):
        for j in range(N):
            if (mask >> (i*N+j)) & 1:
                parent[root(i)] = root(M+j)
    return len({root(i) for i in range(M+N)}) == 1


def walsh(a):
    t=1
    while t<len(a):
        for base in range(0,len(a),2*t):
            for j in range(base,base+t):
                u,v=a[j],a[j+t]
                a[j]=u+v
                a[j+t]=u-v
        t*=2
    return a


def partitions(k):
    def go(labels, maximum):
        if len(labels)==k:
            yield tuple(labels)
        else:
            for j in range(maximum+2):
                yield from go(labels+[j],max(maximum,j))
    yield from go([0],0)


def inversion_tables():
    ans=[]
    for labels in partitions(M):
        b=max(labels)+1
        mu=(-1)**(b-1)*factorial(b-1)
        row=[]
        for t in range(1<<M):
            q=0
            for z in range(b):
                prod=1
                for i in range(M):
                    if labels[i]==z:
                        prod*=2 if not (t>>i)&1 else 0
                q+=prod-1
            row.append(q)
        ans.append((mu,row))
    assert len(ans)==15
    return ans


def column_type(mask,j):
    return sum(((mask>>(N*i+j))&1)<<i for i in range(M))


def formula(mask, tables):
    t=[column_type(mask,j) for j in range(N)]
    total=0
    for mu, q in tables:
        term=mu
        for x in t:
            term*=q[x]
        total+=term
    return total


def run():
    a=[int(connected(s)) for s in range(SIZE)]
    assert sum(a)==36317
    v=walsh(a)
    tables=inversion_tables()
    checks=0
    for s,z in enumerate(v):
        assert z==formula(s,tables),(s,z,formula(s,tables))
        assert z%4==1
        checks+=2
    counts=Counter(v)
    assert len(counts)==49
    assert min(abs(z) for z in v)==3
    assert sum(1 for z in v if abs(z)==3)==11664
    assert counts[0]==0
    assert max(abs(z) for z in v)==36317
    assert sum(z*z for z in v)==SIZE*36317
    assert sum(counts.values())==SIZE
    # The independently reproduced histogram is the finite certificate.
    import csv
    with open('spectrum.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['multiplier','frequency_count'])
        for z,count in sorted(counts.items()):
            w.writerow([z,count])
    print('connected=36317 frequencies=65536 levels=49 min_abs=3')
    print('min_abs_frequency_count=11664 zeros=0 rank=65536')
    print('independent_agreement_checks=',checks)
    print('parseval=passed; inversion=passed; congruence=passed')

if __name__=='__main__':
    run()
