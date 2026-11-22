#!/usr/bin/env python3
"""Direct finite-field bracket census for the rank-two class-four free Lie algebra."""
from itertools import product
from collections import Counter
import random

def br(x,y,p):
    a,b,c,d,e = x[:5]
    A,B,C,D,E = y[:5]
    return ((a*B-b*A)%p,(a*C-A*c)%p,(b*C-B*c)%p,(a*D-A*d)%p,(a*E+b*D-A*e-B*d)%p,(b*E-B*e)%p)

def eta(u,v,p):
    # Projective one-dimensional subspaces, represented (1,t) and (0,1)
    n=0
    for l in [(1,t) for t in range(p)]+[(0,1)]:
        # k-linear vector u multiple of l
        if (l[0]*u[1]-l[1]*u[0])%p: continue
        # binary quadratic v = l*(rX+sY) in basis X^2,XY,Y^2
        if l[0]:
            r=v[0]
            s=(v[1]-l[1]*r)%p
            if (l[1]*s-v[2])%p: continue
        else:
            if v[0]%p: continue
        n+=1
    return n

def expected(t,p):
    w=t[0]
    if w: return p**8*(p*p-1)
    if t==tuple([0]*6): return p**12+(p+1)*(p*p-1)*p**9
    return eta(t[1:3],t[3:6],p)*(p*p-1)*p**9

def test2():
    p=2
    elements=list(product(range(p), repeat=8))
    hist=Counter(br(x,y,p) for x in elements for y in elements)
    assert len(hist)<=p**6
    for t in product(range(p), repeat=6):
        assert hist[t]==expected(t,p),(t,hist[t],expected(t,p))
    print('GF(2): all 65,536 ordered input pairs and 64 target fibers EXACTLY matched')
    print('GF(2) fiber multiplicities',sorted(Counter(hist.values()).items()))

def test3():
    p=3
    import numpy as np
    E=np.array(list(product(range(p),repeat=8)), dtype=np.int16)
    # Enumerate all y for each x, but use only a sample of all x chosen from every possible degree-one stratum.
    rng=random.Random(20261119)
    X=[E[i] for i in sorted(set([0,1,10,50,300,2500,5000,6500]+[rng.randrange(len(E)) for _ in range(80)]))]
    for x in X:
        a,b,c,d,e=[int(z) for z in x[:5]]
        vals=np.empty((len(E),6),dtype=np.int16)
        vals[:,0]=(a*E[:,1]-b*E[:,0])%p
        vals[:,1]=(a*E[:,2]-c*E[:,0])%p
        vals[:,2]=(b*E[:,2]-c*E[:,1])%p
        vals[:,3]=(a*E[:,3]-d*E[:,0])%p
        vals[:,4]=(a*E[:,4]+b*E[:,3]-e*E[:,0]-d*E[:,1])%p
        vals[:,5]=(b*E[:,4]-e*E[:,1])%p
        # consistency vs scalar bracket routine
        for j in [0,1,29,1000,6560]:
            assert tuple(vals[j])==br(x,E[j],p)
    # independently count 40 prescribed fibers using rank tests on all 6,561 x.
    def rank_mod(M,p):
        M=[list(map(lambda z:int(z)%p,row)) for row in M]
        r=0
        for j in range(len(M[0])):
            pivot=next((i for i in range(r,len(M)) if M[i][j]%p),None)
            if pivot is None: continue
            M[r],M[pivot]=M[pivot],M[r]
            inv=pow(M[r][j],-1,p)
            M[r]=[(v*inv)%p for v in M[r]]
            for i in range(r+1,len(M)):
                fac=M[i][j]
                if fac: M[i]=[(a-fac*b)%p for a,b in zip(M[i],M[r])]
            r+=1
            if r==len(M):break
        return r
    targets=[(0,)*6,(1,0,0,0,0,0),(0,0,0,1,0,1),(0,0,0,1,0,0),(0,1,0,0,0,1),(0,1,0,0,1,0)]
    targets+= [tuple(rng.randrange(p) for _ in range(6)) for _ in range(14)]
    # Rank/consistency calculation at each x independent from combinatorial count.
    counts={t:0 for t in targets}
    for x in E:
        cols=[br(x,y,p) for y in np.eye(8,dtype=np.int16)]
        M=[[cols[j][i] for j in range(8)] for i in range(6)]
        r=rank_mod(M,p)
        for t in counts:
            r2=rank_mod([M[i]+[t[i]] for i in range(6)],p)
            if r2==r: counts[t]+=p**(8-r)
    for t,n in counts.items():
        assert n==expected(t,p),(t,n,expected(t,p))
    print('GF(3): linear-system fiber counts over all 6,561 first inputs, 20 targets EXACTLY matched')
    print('GF(3) sample fibers:',[(t,counts[t]) for t in targets[:6]])

if __name__=='__main__':
    test2()
    test3()
    print('PASS')
