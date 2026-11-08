#!/usr/bin/env python3
"""Exact rational-integer verification of 2x2 rank-one projector pair sums."""
from collections import Counter
from itertools import product


def valuation(a,p,k):
    if a==0: return k
    v=0
    while a%p==0:
        a//=p;v+=1
    return v


def legendre_unit(d,p):
    s=pow(d%p,(p-1)//2,p)
    return 1 if s==1 else -1


def representation(a,b,c,p,k):
    """a,b,c identify T=S-I=[[a,b],[c,-a]] modulo p**k."""
    q=p**k
    if (a,b,c)==(0,0,0): return p**(2*k-1)*(p+1)
    j=min(valuation(a,p,k),valuation(b,p,k),valuation(c,p,k))
    m=k-j; pp=p**m
    a//=p**j;b//=p**j;c//=p**j
    D=(a*a+b*c)%pp
    if j:
        if D%p==0: return 2*p**(k+j)
        return p**(k+j-1)*(p-legendre_unit(D,p))
    if D%p==0: return 2*p**k
    eps=legendre_unit(D,p)
    if eps==-1: return p**(k-1)*(p+1)
    t=valuation((1-D)%q,p,k)
    if t==k: return (p+k*(p-1))*p**(k-1)
    return (t+1)*(p-1)*p**(k-1)


def run(p,k):
    q=p**k; h=(pow(2,-1,q)**2)%q
    E=[(a,b,c) for a,b,c in product(range(q),repeat=3)
       if (a*a+b*c-h)%q==0]
    counts=Counter(((a+x)%q,(b+y)%q,(c+z)%q) for a,b,c in E for x,y,z in E)
    assert len(E)==p**(2*k-1)*(p+1)
    assert len(counts)==q**3
    formula_counts=Counter()
    for a,b,c in product(range(q),repeat=3):
        v=representation(a,b,c,p,k)
        assert counts[(a,b,c)]==v,(p,k,a,b,c,v,counts[(a,b,c)])
        formula_counts[v]+=1
    emin=min(counts.values())
    expected_min=(p+1 if p==3 else p-1)*p**(k-1)
    assert emin==expected_min
    mincount=(((p-3)//2)*(p*p+p)*p**(3*k-3) if p>=5 else
       (6 if k==1 else 42*3**(3*k-4)))
    assert formula_counts[emin]==mincount
    energy=sum(v*v for v in counts.values())
    energy_formula=p**(5*k-3)*(p**3+7*p*p+5*p-1)-3*p**(4*k-2)*(p+1)
    assert energy==energy_formula
    assert sum(r*n for r,n in formula_counts.items())==len(E)**2
    print('p',p,'k',k,'points',len(E),'targets',len(counts),'energy',energy,'min',emin,'minimum_count',mincount,'OK',flush=True)

if __name__=='__main__':
    for p,k in [(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(11,1),(13,1)]:run(p,k)
    print('PROJECTOR_PAIR_CONVOLUTION_PASS')
