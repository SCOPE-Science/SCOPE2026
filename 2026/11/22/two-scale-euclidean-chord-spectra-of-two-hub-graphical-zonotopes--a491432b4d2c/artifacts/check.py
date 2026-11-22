#!/usr/bin/env python3
"""Reproduce a two-point chord enumerator for a complete bipartite graphical zonotope.
No third-party dependencies. This program checks finite cases, not the limiting proof.
"""
from itertools import product
from collections import Counter, defaultdict
from math import comb

P=[(1,1),(-1,-1),(1,-1)]
M=[(1,1),(-1,-1),(-1,1)]
C=[(1,1),(-1,-1)]
ALPH=(P,M,C)
COEF=(1,1,-1)

def vertices(n):
    # Independent brute-force sign orientations, excluding directed 4-cycles.
    out=[]
    for signs in product(((1,1),(1,-1),(-1,1),(-1,-1)),repeat=n):
        if ((1,-1) in signs) and ((-1,1) in signs):
            continue
        # doubled Euclidean coordinates are integral; retain unique vertex.
        a=sum(v[0] for v in signs)
        b=sum(v[1] for v in signs)
        leaf=tuple(-v[0]-v[1] for v in signs)
        out.append((a,b)+leaf)
    assert len(out)==len(set(out))
    return out

def direct_chords(n):
    V=vertices(n)
    counter=Counter()
    for i,v in enumerate(V):
        for w in V[i+1:]:
            diff=[x-y for x,y in zip(v,w)]
            k=sum(x*x for x in diff)
            assert k%4==0
            counter[k//4]+=1
    return counter

def exact_chords(n):
    all_hist=Counter()
    # A dictionary (hub1diff, hub2diff, leaf_sq) to integer multiplicities.
    for i,X in enumerate(ALPH):
        for j,Y in enumerate(ALPH):
            one=Counter()
            for a,b in X:
                for c,d in Y:
                    one[((a-c)//2,(b-d)//2,((a+b-c-d)**2)//4)]+=1
            running={(0,0,0):1}
            for _ in range(n):
                nxt=defaultdict(int)
                for (x,y,s),cnt in running.items():
                    for (dx,dy,ds),num in one.items():
                        nxt[(x+dx,y+dy,s+ds)]+=cnt*num
                running=nxt
            for (x,y,s),val in running.items():
                all_hist[x*x+y*y+s]+=COEF[i]*COEF[j]*val
    N=2*3**n-2**n
    all_hist[0]-=N
    assert all(v>=0 and v%2==0 for v in all_hist.values()),(n,all_hist)
    hist=Counter({k:v//2 for k,v in all_hist.items() if v})
    assert sum(hist.values())==comb(N,2)
    return hist

def check():
    total_pairs=0
    for n in range(2,7):
        V=vertices(n)
        d=direct_chords(n)
        e=exact_chords(n)
        assert d==e, (n,d,e)
        total_pairs+=len(V)*(len(V)-1)//2
        # Known extremal diameter: twice the squared distance from the
        # origin to the all-aligned signed-degree vertex.
        assert max(d)==2*n*(n+2), (n,max(d))
        N=len(V)
        total_radius=3**n*n*(n+20)//9 - 3*n*2**(n-1)
        assert sum(k*v for k,v in e.items()) == N*total_radius
    for n in range(7,13):
        e=exact_chords(n)
        assert min(e)==2
        assert max(e)==2*n*(n+2)
        N=2*3**n-2**n
        total_radius=3**n*n*(n+20)//9 - 3*n*2**(n-1)
        assert sum(k*v for k,v in e.items()) == N*total_radius
    print('BICLIQUE_TWO_POINT_PASS brute_force_n=2..6 checked_pairs=',total_pairs,'transfer_n=2..12')

if __name__=='__main__': check()
