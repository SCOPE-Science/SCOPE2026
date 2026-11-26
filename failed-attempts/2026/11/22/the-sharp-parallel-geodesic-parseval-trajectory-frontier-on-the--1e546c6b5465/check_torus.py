"""Exact integer checks for the toral closed-geodesic frame theorem."""
from math import gcd, floor
from collections import defaultdict
from itertools import product

def frame_data(N,p,q):
    assert gcd(abs(p),abs(q))==1
    fibers=defaultdict(list)
    for k,l in product(range(-N,N+1), repeat=2):
        fibers[p*k+q*l].append((k,l))
    return fibers

def maximal_fiber(N,p,q):
    return max(map(len,frame_data(N,p,q).values()))

def check():
    cases=0
    for N in range(1,8):
        for p,q in product(range(-9,10), repeat=2):
            if gcd(p,q)!=1:continue
            r=maximal_fiber(N,p,q)
            expected=1+2*N//max(abs(p),abs(q))
            assert r==expected,(N,p,q,r,expected)
            for L in range(1,9):
                # Family of L disjoint parallel trajectories with uniform transverse coordinate
                # Distinct k,l in the same fiber must have distinct transverse coordinates modulo L.
                a,b=next((a,b) for a,b in product(range(-15,16),repeat=2) if p*b-q*a==1)
                fibers=frame_data(N,p,q)
                distinct=all(len({(a*k+b*l)%L for k,l in f})==len(f) for f in fibers.values())
                assert distinct==(L>=expected),(N,p,q,L,distinct,expected)
                cases+=1
        for L in range(1,2*N+6):
            s=(2*N)//L+1
            feasible=[(p*p+q*q,p,q) for p,q in product(range(-2*N-2,2*N+3),repeat=2)
                     if gcd(p,q)==1 and maximal_fiber(N,p,q)<=L]
            best=min(t[0] for t in feasible)
            expected=1 if s==1 else s*s+1
            assert best==expected,(N,L,s,best,expected)
    print('PASS: all exact alias/Parseval/fiber and minimal-winding cases',cases)
if __name__=='__main__':check()
