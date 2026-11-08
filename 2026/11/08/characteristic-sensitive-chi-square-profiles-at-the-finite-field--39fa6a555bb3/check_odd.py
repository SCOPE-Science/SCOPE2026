#!/usr/bin/env python3
"""Exact finite-field prime-case checks of the Veronese convolution spectrum.
Only standard-library Python; no external data or packages.
"""
from itertools import product
from fractions import Fraction
from collections import Counter
from cmath import exp,pi

def gauss_binom(n,r,q):
    out=Fraction(1)
    for j in range(r):out *= Fraction(q**(n-j)-1,q**(r-j)-1)
    assert out.denominator==1
    return int(out)

def nondegenerate_symmetric_count(r,q):
    t=1
    for j in range(1,r+1):t *= q**j-(1 if j%2 else 0)
    return t

def symmetric_list(n,q):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    for vec in product(range(q),repeat=len(pairs)):
        a=[[0]*n for _ in range(n)]
        for (i,j),v in zip(pairs,vec): a[i][j]=a[j][i]=v
        yield vec,a

def rank(a,q):
    z=[row[:] for row in a]; n=len(z);r=0
    for j in range(n):
        k=next((k for k in range(r,n) if z[k][j]%q),None)
        if k is None:continue
        z[k],z[r]=z[r],z[k]; inv=pow(z[r][j]%q,-1,q)
        z[r]=[x*inv%q for x in z[r]]
        for k in range(n):
            if k!=r:
                t=z[k][j]
                z[k]=[(x-t*y)%q for x,y in zip(z[k],z[r])]
        r+=1
        if r==n:break
    return r

def check(n,q):
    c=Counter(); vals={}
    vectors=list(product(range(q),repeat=n))
    for vec,a in symmetric_list(n,q):
        r=rank(a,q);c[r]+=1
        s=0j
        for v in vectors:
            quad=sum(v[i]*a[i][j]*v[j] for i in range(n) for j in range(n))%q
            s+=exp(2j*pi*quad/q)
        lam=s/len(vectors)
        assert abs(abs(lam)**2-q**(-r))<1e-10,(n,q,vec,r,lam)
        vals[vec]=lam
    assert sum(c.values())==q**(n*(n+1)//2)
    for r in range(n+1):
        expect=gauss_binom(n,r,q)*nondegenerate_symmetric_count(r,q)
        assert c[r]==expect,(n,q,r,c[r],expect)
    for t in range(1,5):
        spectral=sum(c[r]*q**(-r*t) for r in range(1,n+1))
        direct=sum(abs(z)**(2*t) for key,z in vals.items() if any(key))
        assert abs(spectral-direct)<1e-9,(n,q,t,spectral,direct)
    if n==2 and q==3:
        pairs=[(i,j) for i in range(n) for j in range(i,n)]
        law=Counter()
        for v in vectors:law[tuple(v[i]*v[j]%q for i,j in pairs)]+=1
        space=list(product(range(q),repeat=len(pairs)))
        dens={x: (1 if all(z==0 for z in x) else 0) for x in space}
        for t in range(1,5):
            nxt={x:0 for x in space}
            for a,p in dens.items():
                if p==0:continue
                for b,m in law.items():
                    z=tuple((i+j)%q for i,j in zip(a,b));nxt[z]+=p*m/q**n
            dens=nxt
            chisq=sum((q**len(pairs)*dens[x]-1)**2 for x in space)/q**len(pairs)
            spect=sum(c[r]*q**(-r*t) for r in range(1,n+1))
            assert abs(chisq-spect)<1e-9,(t,chisq,spect)
    print('PASS',{'n':n,'q':q,'rank_counts':dict(sorted(c.items())),'chi2_at_n':sum(c[r]*q**(-n*r) for r in range(1,n+1))})

def check_profile(q):
    def term(r,s):
        p=1.
        for j in range(1,(r+1)//2+1):p*=1-q**(-(2*j-1))
        denom=1.
        for j in range(1,r+1):denom*=1-q**(-j)
        return p/denom*q**(-s*r-r*(r-1)/2)
    for s in (-2,0,2):
        target=sum(term(r,s) for r in range(1,60))
        v=[]
        for n in (4,7,12,20):
            total=sum(gauss_binom(n,r,q)*nondegenerate_symmetric_count(r,q)*q**(-(n+s)*r) for r in range(1,n+1)) if n+s>=0 else float('nan')
            v.append(total)
        print('profile',q,s,'limit',round(target,10),'finite_n',[round(x,10) for x in v])
        if s>=0: assert abs(v[-1]-target)<.001

if __name__=='__main__':
    for n,q in ((1,3),(2,3),(2,5),(3,3)):
        check(n,q)
    for q in (3,5):check_profile(q)
    print('VERONESE_WALK_EXACT_CHECKS_PASS')
