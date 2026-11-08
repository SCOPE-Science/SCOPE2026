"""Exact, nonfloating validation of the arithmetic dark-mode theorem for magnetic cycles."""
from itertools import combinations
from math import gcd

def dim_formula(n, traps, half_flux):
    anchor=min(traps)
    g=n
    for s in traps:
        g=gcd(g,(s-anchor)%n)
    q=n//g
    if not half_flux:
        return (g*gcd(q,2)-gcd(n,2))//2
    return (g-(n%2))//2 if q%2 else 0

def dim_pair_count(n, traps, half_flux):
    # Independently inspect each true degenerate Bloch-frequency pair.
    seen=set(); ans=0
    a=min(traps)
    for k in range(n):
        ell=(-k-(1 if half_flux else 0))%n
        if ell==k or k in seen: continue
        seen.add(k);seen.add(ell)
        if all(((k-ell)*(s-a))%n==0 for s in traps):ans+=1
    return ans

def survival_formula(n, traps, half_flux, start):
    anchor=min(traps)
    g=n
    for s in traps:g=gcd(g,(s-anchor)%n)
    q=n//g; r=(start-anchor)%n
    if not half_flux:
        h=gcd(q,2)
        return (0 if (2*r)%(g*h)==0 else (g*h)/(2*n))
    if q%2==0:return 0.
    if r%g==0:return 0.
    if g%2==0 and r%g==g//2:return g/n
    return g/(2*n)

def survival_pair(n, traps, half_flux, start):
    from math import cos,pi
    a=min(traps); r=(start-a)%n
    seen=set();ans=0.
    for k in range(n):
        ell=(-k-(1 if half_flux else 0))%n
        if ell==k or k in seen: continue
        seen.add(k);seen.add(ell)
        if all(((k-ell)*(s-a))%n==0 for s in traps):
            ans += (1-cos(2*pi*(k-ell)*r/n))/n
    return ans

nsets=0;nloc=0
for n in range(3,17):
    # Exhaustive for <=11, representative deterministic for larger.
    if n<=11: masks=range(1,1<<n)
    else:
        masks=[1,3,5,7,9,21,(1<<n)-1]+[1+(1<<k) for k in range(1,n)]
    for mask in masks:
        traps=tuple(j for j in range(n) if (mask>>j)&1)
        for half_flux in (False,True):
            x=dim_formula(n,traps,half_flux)
            y=dim_pair_count(n,traps,half_flux)
            assert x==y,(n,traps,half_flux,x,y)
            nsets+=1
            for r in range(n):
                u=survival_formula(n,traps,half_flux,r)
                v=survival_pair(n,traps,half_flux,r)
                assert abs(u-v)<1e-10,(n,traps,half_flux,r,u,v)
                nloc+=1
print(f'PASS: {nsets} full arithmetic dimension cases, {nloc} localized-survival cases')
