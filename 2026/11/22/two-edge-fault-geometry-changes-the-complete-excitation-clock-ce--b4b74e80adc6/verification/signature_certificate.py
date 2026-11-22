#!/usr/bin/env python3
"""Exact surjection-weighted finite-signature certificate for 3-color excitation."""
from itertools import combinations, product
from collections import defaultdict

TABLES = {
 'adjacent': {
   (0,1):(1,0,0), (0,3):(6,33,27),
   (1,1):(15,8,0), (1,3):(2,8,0),
   (2,1):(21,8,0), (2,3):(4,8,0),
   (3,1):(16,8,0), (3,3):(4,8,0),
   (4,1):(10,0,0), (4,3):(2,0,0)},
 'disjoint': {
   (0,1):(1,0,0), (0,3):(66,147,81),
   (1,1):(31,16,0), (1,3):(16,16,0),
   (2,1):(35,16,0), (2,3):(24,16,0),
   (3,1):(30,16,0), (3,3):(24,16,0),
   (4,1):(8,0,0), (4,3):(8,0,0)}
}
DEFECTS={'adjacent':((0,1),(1,2)), 'disjoint':((0,1),(2,3))}

def update(state,missing):
    output=[]
    for i,v in enumerate(state):
        if v==1: output.append(2)
        elif v==2: output.append(0)
        else: output.append(1 if any(x==1 and j!=i and frozenset((i,j)) not in missing for j,x in enumerate(state)) else 0)
    return tuple(output)

def temporal_class(state,missing):
    seen={};t=0
    while state not in seen:
        assert t<=20
        seen[state]=t
        state=update(state,missing);t+=1
    return seen[state], t-seen[state]

def exact_signature_table(name):
    r=3 if name=='adjacent' else 4
    missing={frozenset(e) for e in DEFECTS[name]}
    total=defaultdict(lambda:[0,0,0])
    for special in product(range(3),repeat=r):
        for k in (1,2,3):
            for symbols in combinations(range(3),k):
                # One representative per present color in the universal-core twin class.
                state=special+symbols
                tau,p=temporal_class(state,missing)
                total[tau,p][k-1]+=1
    return {a:tuple(v) for a,v in total.items()}

def exact_population(name,n):
    r=3 if name=='adjacent' else 4
    k=n-r
    assert k>=1
    w=(1,2**k-2,3**k-3*2**k+3)
    return {cell:sum(x*y for x,y in zip(co,w)) for cell,co in TABLES[name].items()}

def closed_formula(name,n):
    q=2**n;z=3**n
    if name=='adjacent':
        return {(0,1):1,(0,3):z-6*q+21,
                (1,1):q-1,(1,3):q-14,
                (2,1):q+5,(2,3):q-12,
                (3,1):q,(3,3):q-12,
                (4,1):10,(4,3):2}
    return {(0,1):1,(0,3):z-6*q+15,
            (1,1):q-1,(1,3):q-16,
            (2,1):q+3,(2,3):q-8,
            (3,1):q-2,(3,3):q-8,
            (4,1):8,(4,3):8}

def main():
    for name in ('adjacent','disjoint'):
        got=exact_signature_table(name)
        assert got==TABLES[name],(name,got)
        print(name,'signature classes',sum(map(sum,got.values())),'nonempty rows',len(got))
        for cell in sorted(got):print(cell,got[cell])
        for n in range(5,35):
            actual=exact_population(name,n);closed=closed_formula(name,n)
            assert actual==closed,(name,n)
            assert sum(actual.values())==3**n
            assert all(v>=0 for v in actual.values())
            assert closed[(0,3)]%3==0
        print(name,'30 exact symbolic instantiations verified; algebraic coefficient table proves all n >= 5')
    print('SIGNATURE_CERTIFICATE_OK')
if __name__=='__main__':main()
