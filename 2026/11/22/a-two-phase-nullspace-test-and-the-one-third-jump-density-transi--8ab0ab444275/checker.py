"""Finite numerical consistency checks for a cosine nullspace criterion.
Uses only Python's standard library. Checks do not certify the infinite theorem.
"""
import math
import random


def rho(n, s, eps):
    vals = sorted((abs(math.cos((2*j+eps)*math.pi/n)) for j in range(n)), reverse=True)
    return sum(vals[:s])/sum(vals)


def phase_ratio(n, s, phase):
    vals = sorted((abs(math.cos(2*math.pi*j/n+phase)) for j in range(n)), reverse=True)
    return sum(vals[:s])/sum(vals)


def test():
    rng=random.Random(271828)
    checks=0
    for n in range(6,202,2):
        for s in range(1,n+1):
            exact=max(rho(n,s,0),rho(n,s,1))
            for _ in range(8):
                ph=rng.uniform(-math.pi,math.pi)
                actual=phase_ratio(n,s,ph)
                if actual>exact+3e-12:
                    raise AssertionError(('phase maximum',n,s,ph,actual,exact))
                checks+=1
        # sampled location of failure threshold and asymptotic crosscheck
        crit=next(s for s in range(2,n+1) if max(rho(n,s,0),rho(n,s,1))>=.5-2e-13)
        if crit!=math.ceil(n/3):
            raise AssertionError(('critical numeric discrepancy',n,crit))
        checks+=1
        # Fourier frequencies coprime to n permute phase grids, hence rho unchanged.
        for k in range(1,n//2):
            if math.gcd(k,n)!=1: continue
            eps=0
            for s in sorted(set((2, n//3, n//2, n-1))):
                orig=rho(n,s,eps)
                vals=sorted((abs(math.cos(2*math.pi*k*j/n)) for j in range(n)),reverse=True)
                pert=sum(vals[:s])/sum(vals)
                if abs(orig-pert)>3e-12: raise AssertionError(('frequency permute',n,k,s))
                checks+=1
    for n in (60,120,240,480,960):
        s=round(.27*n)
        a=max(rho(n,s,0),rho(n,s,1))
        b=math.sin(.5*math.pi*s/n)
        if abs(a-b)>4.0/n: raise AssertionError(('Riemann limit',n,s,a,b))
        checks+=1
    # Explicit ambiguity/failure under the deleted mode.
    for n in range(6,102,2):
        s=next(s for s in range(2,n+1) if max(rho(n,s,0),rho(n,s,1))>=.5-2e-13)
        eps=max((0,1),key=lambda v:rho(n,s,v))
        y=[math.cos((2*j+eps)*math.pi/n) for j in range(n)]
        top=sorted(range(n),key=lambda j:-abs(y[j]))[:s]
        pos=[j for j in top if y[j]>1e-8]
        neg=[j for j in top if y[j]<-1e-8]
        if not pos or not neg: raise AssertionError(('missing sign',n,s))
        g=[0.0]*n
        for j in pos:g[j]=-len(neg)
        for j in neg:g[j]=len(pos)
        if abs(sum(g))>1e-10:raise AssertionError(('not cyclic',n,s))
        norm0=sum(abs(v) for v in g)
        norm1=sum(abs(v+1e-5*w) for v,w in zip(g,y))
        if norm1>norm0+1e-7:raise AssertionError(('no decrease',n,s,norm0,norm1))
        checks+=1
    print('PASS', checks, 'finite consistency comparisons')
if __name__=='__main__': test()
