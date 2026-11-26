#!/usr/bin/env python3
"""Direct finite-dimensional matrix checks for critical joint time/Fourier sampling."""
import math
import cmath
import random
try:
    import numpy as np
except ImportError:
    raise SystemExit('numpy is required for direct matrix spectral checks')

def evec(n,k):
    return np.exp(2j*np.pi*np.arange(n)*k/n)/np.sqrt(n)

def formula(n,a,b):
    c=abs(math.cos(math.pi*((a*b)%n)/n))
    tmin=2*(1-c)/n
    return 1-math.sqrt(max(0.0,1-tmin)), 1+math.sqrt(max(0.0,1-tmin))

def gram(n,t0,t1,k0,k1):
    a=np.zeros((n,n),dtype=complex)
    a[0,t0]=1
    a[1,t1]=1
    j=2
    for k in range(n):
        if k in (k0,k1): continue
        a[j,:]=np.conjugate(evec(n,k)); j+=1
    assert j==n
    return a.conj().T@a

def count_theory(n):
    optimal=0;singular=0
    for a in range(1,n):
        for b in range(1,n):
            r=a*b % n
            if r==0: singular+=1
            if n%2==0 and r==n//2 or n%2 and r in ((n-1)//2,(n+1)//2):
                optimal+=1
    return n*n*optimal//4,n*n*singular//4

def phi(n):return sum(math.gcd(k,n)==1 for k in range(1,n+1))

def analytic_counts(n):
    if n%2: op=n*n*phi(n)//2
    else: op=n*n*sum(d*phi(n//d) for d in range(1,n//2+1) if (n//2)%d==0)//4
    sing=n*n*sum(phi(n//d)*(d-1) for d in range(1,n) if n%d==0)//4
    return op,sing

checks=0
rng=random.Random(9001)
for n in range(4,20):
    if n%2: optc=math.sin(math.pi/(2*n))
    else:optc=0
    expected=1-math.sqrt(1-2*(1-optc)/n)
    values=[];maxset=[];sing=0
    for t0 in range(n):
        for t1 in range(t0+1,n):
            for k0 in range(n):
                for k1 in range(k0+1,n):
                    a=(t1-t0)%n;b=(k1-k0)%n
                    low,high=formula(n,a,b)
                    if (a*b)%n==0:sing+=1
                    if abs(low-expected)<1e-10:maxset.append((t0,t1,k0,k1))
                    assert low<=expected+1e-10
                    checks+=1
    assert (len(maxset),sing)==analytic_counts(n),(n,len(maxset),sing,analytic_counts(n))
    checks+=2
    # Full matrix independent test: all pairs for n<=9 and random 60 otherwise
    tests=[(t0,t1,k0,k1) for t0 in range(n) for t1 in range(t0+1,n) for k0 in range(n) for k1 in range(k0+1,n)] if n<=8 else [(lambda tt,ff:(tt[0],tt[1],ff[0],ff[1]))(sorted(rng.sample(range(n),2)),sorted(rng.sample(range(n),2))) for _ in range(60)]
    for t0,t1,k0,k1 in tests:
        G=gram(n,t0,t1,k0,k1)
        w=np.linalg.eigvalsh(G)
        lo,hi=formula(n,t1-t0,k1-k0)
        assert abs(w[0]-lo)<3e-11, (n,t0,t1,k0,k1,w[0],lo)
        assert abs(w[-1]-hi)<3e-11
        assert abs(w[0]+w[-1]-2)<3e-11
        checks+=3

print('CRITICAL_MIXED_FOURIER_SAMPLING_CHECKS_PASSED',checks)
