#!/usr/bin/env python3
"""Standalone finite checks for two standardized deletion sphere deficiency."""
import itertools, random, math

def stats(p):
    n=len(p); out=set(); sets=[]
    for i in range(n):
        for j in range(i+1,n):
            v=p[:i]+p[i+1:j]+p[j+1:]
            s={v0:k for k,v0 in enumerate(sorted(v))}
            out.add(tuple(s[v0] for v0 in v))
    J=sum(abs(p[i]-p[i+1])==1 for i in range(n-1))
    T=sum(abs(p[i]-p[i+d])<=2 for d in (1,2) for i in range(n-d))
    D=math.comb(n,2)-len(out)
    disjoint=all(not (abs(p[i]-p[i+1])==1 and abs(p[i+1]-p[i+2])==1) for i in range(n-2))
    if disjoint:
        low=(n-2)*J-math.comb(J,2)
        up=low+T+math.comb(2*T,2)**2
        assert low<=D<=up,(p,D,J,T,low,up)
    return D,J,T

def main():
    tot=0
    for n in range(4,9):
        for p in itertools.permutations(range(n)):
            stats(p); tot+=1
    rng=random.Random(12979)
    for n in (9,12,20,35):
        for _ in range(100):
            p=list(range(n));rng.shuffle(p);stats(tuple(p));tot+=1
    print('PASS',tot,'permutations; exhaustive 4..8; larger random checks')
if __name__=='__main__':main()
