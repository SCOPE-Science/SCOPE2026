#!/usr/bin/env python3
"""Independent exhaustive verification for connected forcing on one-hub cycle spiders."""
from itertools import combinations_with_replacement
from collections import Counter
from math import prod,comb

def graph(c,arms):
    adj=[set() for _ in range(c)]
    for i in range(c):
        a,b=i,(i+1)%c;adj[a].add(b);adj[b].add(a)
    for p in arms:
        last=0
        for _ in range(p):
            w=len(adj);adj.append({last});adj[last].add(w);last=w
    return [sum(1<<v for v in nbr) for nbr in adj]

def connected(M,A):
    if M==0:return False
    seen=M & -M
    while True:
        out=seen;rest=seen
        while rest:
            bit=rest&-rest;rest-=bit;out|=A[bit.bit_length()-1]&M
        if out==seen:return seen==M
        seen=out

def force(M,A):
    full=(1<<len(A))-1
    while M!=full:
        W=full^M;new=0;B=M
        while B:
            bit=B&-B;B-=bit
            nb=A[bit.bit_length()-1]&W
            if nb and not nb&(nb-1):new|=nb
        if not new:return False
        M|=new
    return True

def mult(P,Q):
    R=Counter()
    for i,a in P.items():
        for j,b in Q.items():R[i+j]+=a*b
    return R

def add(P,Q):
    R=Counter(P)
    for i,v in Q.items():R[i]+=v
    return R

def expected(c,arms):
    F=Counter({j:j+1 for j in range(1,c-1)});F[c-1]=1
    H=[Counter({j:1 for j in range(1,p+1)}) for p in arms]
    U=Counter()
    for omit in [-1]+list(range(len(arms))):
        W=Counter({0:1})
        for i,h in enumerate(H):
            if i!=omit:W=mult(W,h)
        U=add(U,W)
    return mult(Counter({1:1}),mult(F,U))

def main():
    cases=0;tot=0
    for t in (2,3,4,5):
        for arms in combinations_with_replacement((1,2,3),t):
            for c in (3,4,5,6):
                N=c+sum(arms)
                if N>15:continue
                A=graph(c,arms); got=Counter()
                for mask in range(1,1<<N):
                    if connected(mask,A) and force(mask,A):got[mask.bit_count()]+=1
                want=expected(c,arms)
                assert got==want,(c,arms,got,want)
                assert min(got)==t+1 and got[t+1]==2*t
                assert sum(got.values())==comb(c,2)*(prod(arms)+sum(prod(arms[k] for k in range(t) if k!=j) for j in range(t)))
                cases+=1;tot+=(1<<N)-1
    assert cases>30
    print('INDEPENDENT_FULL_SUBSET_CENSUS_PASS',cases,'graphs',tot,'subsets')
    for t in range(2,100):
        # special one length-2 arm, remaining length-1 arms: quadratic z^2+t*z+t
        # discriminant t*(t-4), sharp threshold t=4.
        assert (t*t-4*t>=0)==(t>=4)
    print('SHARP_ONE_SUBDIVIDED_ARM_DISCRIMINANT_PASS')
    print('VERIFY_OK')
if __name__=='__main__':main()
