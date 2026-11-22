#!/usr/bin/env python3
"""Direct-equation enumeration for nilpotent-projection Schrödinger bracket fibers.

No formulas are used during enumeration. Tests finite prime fields; the accompanying
proof establishes the result for all odd prime powers and all n.
"""
from itertools import product
from collections import Counter

def legendre(a,p):
    a%=p
    if not a:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def square_count(p,n,b):
    k=n//2
    if n%2==0:
        eps=legendre((-1)**k,p)
        return p**(n-1)+(p-1)*eps*p**(k-1) if b%p==0 else p**(n-1)-eps*p**(k-1)
    return p**(n-1) if b%p==0 else p**(n-1)+legendre((-1)**k*b,p)*p**k

def bracket_sl2(x,y,p):
    a,b,c=x;d,e,f=y
    return ((b*f-e*c)%p,(2*(a*e-d*b))%p,(2*(c*d-a*f))%p)

def mul(x,u,p):
    a,b,c=x;s,t=u
    return ((a*s+b*t)%p,(c*s-a*t)%p)

def direct_oneblock(x,y,p):
    # No triangular restriction used: calculate the entire semidirect bracket.
    ans=Counter()
    for u in product(range(p),repeat=2):
        yu=mul(y,u,p)
        for v in product(range(p),repeat=2):
            xv=mul(x,v,p)
            w=((xv[0]-yu[0])%p,(xv[1]-yu[1])%p)
            z=(u[0]*v[1]-u[1]*v[0])%p
            ans[(w,z)]+=1
    return ans

def distribution(p,n):
    allsl=list(product(range(p),repeat=3))
    bases=[(x,y) for x in allsl for y in allsl if bracket_sl2(x,y,p)==(0,1,0)]
    assert len(bases)==p*(p*p-1), (p,len(bases))
    # For n >=2, use the product structure across distinct Heisenberg pairs,
    # but calculate every one-pair distribution from the original equations.
    full=Counter()
    for x,y in bases:
        D=direct_oneblock(x,y,p)
        current=Counter({((),0):1})
        for i in range(n):
            nxt=Counter()
            for (wseq,c0),old in current.items():
                for (wi,ci),new in D.items():
                    nxt[(wseq+(wi,),(c0+ci)%p)] += old*new
            current=nxt
        for key,cnt in current.items():
            full[key]+=cnt*p*p # both central input coordinates are free
    assert sum(full.values()) == p**(4*n+3)*(p*p-1)
    for wseq in product(list(product(range(p),repeat=2)),repeat=n):
        gamma=[a for a,b in wseq]
        gammap=[b for a,b in wseq]
        for c in range(p):
            if any(gammap):
                exp=p**(2*n+2)*(p*p-1)
            else:
                exp=p**(n+3)*(p*p-1)*square_count(p,n,sum(a*a for a in gamma)-2*c)
            got=full.get((wseq,c),0)
            assert got==exp,(p,n,wseq,c,got,exp)
    levels=Counter(full.values())
    if 0 not in levels:
        omitted=p**(2*n+1)-len(full)
        if omitted:levels[0]=omitted
    assert sum(levels.values())==p**(2*n+1)
    print('verified p=',p,'n=',n,'targets=',p**(2*n+1),'levels=',sorted(levels.items()))

if __name__=='__main__':
    for p,n in [(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)]:
        distribution(p,n)
    print('SCHRODINGER_FULL_NILPOTENT_SLICE_OK')
