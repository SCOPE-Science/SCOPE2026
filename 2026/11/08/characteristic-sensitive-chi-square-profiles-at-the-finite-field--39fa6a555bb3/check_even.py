#!/usr/bin/env python3
"""Independent exhaustive quadratic character test, including characteristic 2."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod

def qprod_count(n,r,q):
    p=Fraction(1)
    for i in range(r):p*=Fraction(q**(n-i)-1,q**(r-i)-1)
    assert p.denominator==1
    return p.numerator

def times(a,b,q):
    if q==2:return a&b
    assert q==4
    tmp=0
    for i in (0,1):
        if a&(1<<i):tmp^=b<<i
    # x^2+x+1
    if tmp&8:tmp^=0b1110
    if tmp&4:tmp^=0b111
    return tmp

def char(x,q):
    if q==2:return 1 if x==0 else -1
    return (-1)**(int(bool(x&2))) # GF4 trace: Tr(1)=0, Tr(x)=Tr(x+1)=1

def alt_rank(coeff,n,q):
    a=[[0]*n for _ in range(n)];pairs=[(i,j) for i in range(n) for j in range(i,n)]
    for (i,j),z in zip(pairs,coeff):
        if i!=j:a[i][j]=a[j][i]=z
    r=0
    for j in range(n):
        k=next((k for k in range(r,n) if a[k][j]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        inv={2:{1:1},4:{1:1,2:3,3:2}}[q][a[r][j]]
        a[r]=[times(x,inv,q) for x in a[r]]
        for k in range(n):
            if k!=r:
                v=a[k][j]
                a[k]=[x^times(v,y,q) for x,y in zip(a[k],a[r])]
        r+=1
    return r

def theoretical(n,r,q):
    p=Fraction(1)
    for j in range(1,r+1):p*=Fraction(q**(2*j-1)-1,q**(2*j-1))
    x=Fraction(qprod_count(n,2*r,q)*q**(r*(2*r+1)))*p
    assert x.denominator==1
    return x.numerator

def test(n,q):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    vectors=list(product(range(q),repeat=n))
    counter=Counter()
    chi=0.
    for coeff in product(range(q),repeat=len(pairs)):
        v=0
        for x in vectors:
            z=0
            for (i,j),a in zip(pairs,coeff):z^=times(a,times(x[i],x[j],q),q)
            v+=char(z,q)
        lam=Fraction(v,len(vectors))
        ar=alt_rank(coeff,n,q)
        if lam:
            assert ar%2==0
            r=ar//2
            assert lam**2==Fraction(1,q**(2*r)),(n,q,coeff,ar,lam)
            counter[r]+=1
            if r:chi+=float(lam)**(2*n)
        else:
            assert any(coeff)
    assert counter[0]==1,counter
    for r in range(1,n//2+1):assert counter[r]==theoretical(n,r,q),(n,q,r,counter[r],theoretical(n,r,q))
    print('PASS even',n,q,dict(counter),'chi2_n',chi)

def check_plancherel_density(n,q):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    V=list(product(range(q),repeat=n))
    states=list(product(range(q),repeat=len(pairs)))
    law=Counter()
    for x in V:law[tuple(times(x[i],x[j],q) for i,j in pairs)]+=1
    mu={z:Fraction(1) if not any(z) else Fraction(0) for z in states}
    for t in range(1,n+3):
        nxt=Counter()
        for z,p in mu.items():
            if not p:continue
            for w,m in law.items():
                u=tuple(a^b for a,b in zip(z,w))
                nxt[u]+=p*Fraction(m,len(V))
        mu=dict(nxt)
        z=Fraction(0)
        for state in states:
            z+=(len(states)*mu.get(state,0)-1)**2
        chi=z/len(states)
        chi_fourier=Fraction(0)
        for r in range(1,n//2+1):chi_fourier+=Fraction(theoretical(n,r,q),q**(2*r*t))
        assert chi==chi_fourier,(q,n,t,chi,chi_fourier)
    print('PASS direct even Plancherel',n,q)

def limit(q,s):
    a=0.
    for r in range(1,30):
        ratio=1.
        for j in range(1,r+1):ratio*=1-q**(-(2*j-1))
        for j in range(1,2*r+1):ratio/=1-q**(-j)
        a+=ratio*q**(-2*r*s-2*r*r+r)
    return a

if __name__=='__main__':
    for n,q in ((1,2),(2,2),(3,2),(4,2),(2,4)):
        test(n,q)
    for n,q in ((2,2),(3,2),(2,4)):
        check_plancherel_density(n,q)
    for q in (2,4):
        print('even profile',q,{s:limit(q,s) for s in (-2,0,2)})
    print('VERONESE_EVEN_CHAR_EXACT_CHECKS_PASS')
