#!/usr/bin/env python3
"""Independent incidence-trace verifier for two nonparallel affine lines."""
from itertools import combinations
from collections import Counter

def fops(q):
    if q==4:
        def add(a,b): return a^b
        def mul(a,b):
            out=0
            while b:
                if b&1:out^=a
                b>>=1;a<<=1
                if a&4:a^=7
            return out
    else:
        def add(a,b):return (a+b)%q
        def mul(a,b):return (a*b)%q
    return add,mul

def lines_and_concepts(q):
    add,mul=fops(q)
    P=[(a,b) for a in range(q) for b in range(q)]
    ix={p:i for i,p in enumerate(P)}
    # A complete affine-plane set of lines from parameterized slopes.
    Ln=[]
    for c in range(q):
        Ln.append((('vertical',),frozenset(ix[(c,y)] for y in range(q))))
    for m in range(q):
        for b in range(q):
            Ln.append(((m,),frozenset(ix[(x,add(mul(m,x),b))] for x in range(q))))
    concepts=set()
    for i,j in combinations(range(len(Ln)),2):
        if Ln[i][0]!=Ln[j][0]:concepts.add(frozenset(Ln[i][1]|Ln[j][1]))
    return P,list(concepts)

def traces(cls,S):
    T={frozenset(x for x in S if x in c) for c in cls}
    return len(T)==2**len(S)

def run():
    for q in [2,3,4,5,7]:
        P,C=lines_and_concepts(q)
        counts={}
        if q<=3:
            for k in range(0,min(6,q*q+1)):
                counts[k]=sum(traces(C,S) for S in combinations(range(q*q),k))
            exp=1 if q==2 else 4
            assert counts == ({0:1,1:4,2:0,3:0,4:0} if q==2 else {0:1,1:9,2:36,3:72,4:54,5:0})
            assert counts[exp]>0 and counts.get(exp+1,0)==0,(q,counts)
        if q>=4:
            # Axes coordinate x=0 and y=0.
            for b2 in range(2,q):
                S=[(0,0),(0,1),(0,2),(1,0),(b2,0)]
                j={p:i for i,p in enumerate(P)}
                X=[j[p] for p in S]
                if traces(C,X):break
            else:raise AssertionError(('no five-point witness',q))
            print('WITNESS',q,S)
        print('FINITE_TWO_NONPARALLEL_LINE_TRACES_PASS',q,'points',len(P),'concepts',len(C),'exhaustive',counts)
    print('ALL_TWO_NONPARALLEL_LINE_TRACES_PASS')
if __name__=='__main__':run()
