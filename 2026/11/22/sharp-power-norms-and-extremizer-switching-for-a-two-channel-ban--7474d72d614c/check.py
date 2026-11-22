#!/usr/bin/env python3
"""Finite diagnostics for the two-channel projection-delay identity (not an infinite proof)."""
import math
import random
P = lambda x: ((x[0]+x[1])/2, (x[0]+x[1])/2)
Q = lambda x: ((x[0]-x[1])/2, (x[1]-x[0])/2)

def norm(x,p):
    vals = [abs(t) for z in x for t in z]
    return max(vals,default=0.) if p == math.inf else sum(t**p for t in vals)**(1/p)

def shifted(x,k,first=True):
    # first: P+S^k Q; else Q+S^k P
    N=len(x)
    zero=(0j,0j)
    y=[]
    for n in range(N+k):
        u=x[n] if n<N else zero
        v=x[n-k] if 0<=n-k<N else zero
        a = P(u) if first else Q(u)
        b = Q(v) if first else P(v)
        y.append((a[0]+b[0],a[1]+b[1]))
    return y

def close(x,y,tol=2e-10):
    return abs(x-y)<=tol*max(1.,abs(x),abs(y))

rng=random.Random(20261108)
checks=0
exponents=(1.,1.25,1.5,1.75,2.,2.5,3.,4.,7.,math.inf)
for k in (1,2,3,5):
    for p in exponents:
        target=2**abs(1-2/p)
        for _ in range(100):
            x=[(complex(rng.uniform(-1,1),rng.uniform(-1,1)),
                 complex(rng.uniform(-1,1),rng.uniform(-1,1))) for i in range(12)]
            y=shifted(x,k)
            assert norm(y,p)<=target*norm(x,p)*(1+1e-11)
            checks+=1
        if p<2:
            x=[(1.+0j,0j)]
        elif p>2:
            x=[(0j,0j) for _ in range(k+1)]
            x[0]=(1.+0j,-1.+0j)
            x[k]=(1.+0j,1.+0j)
        else:
            x=[(1.+1j,-1.+2j)]
        assert close(norm(shifted(x,k),p),target*norm(x,p))
        checks+=1
    for _ in range(30):
        x=[(complex(rng.randint(-3,3),rng.randint(-3,3)),
             complex(rng.randint(-3,3),rng.randint(-3,3))) for n in range(8)]
        s=shifted(x,1)
        t=shifted(s,k)
        u=shifted(x,k+1)
        assert all(close(abs(t[n][j]-u[n][j]),0.) for n in range(len(u)) for j in (0,1))
        checks+=1
        a=shifted(x,1,True)
        b=shifted(a,1,False)
        shifted_x=[(0j,0j)]+x
        assert all(close(abs(b[n][j]-shifted_x[n][j]),0.) for n in range(len(shifted_x)) for j in (0,1))
        checks+=1
    for p in (1.5,3.,4.):
        for _ in range(80):
            s=sorted(rng.sample(range(18),5))
            # greedily enforce S intersect (S+k) empty
            E=[]
            for n in s:
                if n-k not in E and n+k not in E: E.append(n)
            a=[0j]*25;b=[0j]*25
            for n in E:
                z=complex(rng.uniform(-1,1),rng.uniform(-1,1))
                eps=rng.choice((-1,1))
                if p<2:
                    a[n]=eps*z;b[n]=z
                else:
                    b[n]=z;a[n+k]=eps*z
            x=[(a[n]+b[n],a[n]-b[n]) for n in range(25)]
            assert close(norm(shifted(x,k),p),2**abs(1-2/p)*norm(x,p))
            checks+=1
print('HAAR_SHIFT_CHECK_OK',checks)
