"""Reproduce complete small-star idempotent generation counts using direct matrix-algebra closure."""
from itertools import product
from math import comb, factorial


def formula(r,k,q):
    coef=[1]+[0]*r
    for h in range(2,k+1):
        w=q**h-q
        count=comb(k,h)
        old=coef[:]
        coef=[sum(old[j-t]*comb(count,t)*w**t for t in range(j+1) if t<=count) for j in range(r+1)]
    return 2**k*factorial(r)*coef[r]


def matmul(a,b,r,q):
    c=[0]*(2*r+1)
    c[0]=a[0]*b[0]%q
    for i in range(r):
        c[1+i]=a[1+i]*b[1+i]%q
        c[1+r+i]=(a[0]*b[1+r+i]+a[1+r+i]*b[1+i])%q
    return tuple(c)


def add_to_basis(vec,basis,q):
    v=list(vec)
    for p,row in basis:
        if v[p]:
            fac=v[p]
            v=[(x-fac*y)%q for x,y in zip(v,row)]
    piv=next((i for i,x in enumerate(v) if x),None)
    if piv is None:return False
    inv=pow(v[piv],-1,q)
    v=tuple(x*inv%q for x in v)
    basis.append((piv,v));basis.sort()
    return True


def generated(vals,r,q):
    n=2*r+1
    ident=tuple([1]*(r+1)+[0]*r)
    seen=[ident]
    B=[]
    add_to_basis(ident,B,q)
    pos=0
    while pos<len(seen):
        v=seen[pos];pos+=1
        for e in vals:
            for w in (matmul(v,e,r,q),matmul(e,v,r,q)):
                if add_to_basis(w,B,q):
                    seen.append(w)
                    if len(B)==n:return True
    return len(B)==n


def brute(r,k,q):
    d=2*r+1
    mats=[x for x in product(range(q),repeat=d) if matmul(x,x,r,q)==x]
    assert len(mats)==2*(q+1)**r,(r,q,len(mats))
    count=sum(generated(vals,r,q) for vals in product(mats,repeat=k))
    assert count==formula(r,k,q), (r,k,q,count,formula(r,k,q))
    print('brute pass',r,k,q,len(mats),count)


def checks():
    for r,k,q in [(1,2,2),(1,3,2),(2,2,2),(2,3,2),(1,2,3),(1,3,3)]:
        brute(r,k,q)
    # Independent weighted root/leaf enumeration
    for r,k,q in [(1,2,2),(2,3,2),(2,3,3),(3,4,3)]:
        choices=list(product((0,1),repeat=k))
        tot=0
        for leafs in product((x for x in choices if x != (0,)*k),repeat=r):
            if len(set(leafs))<r:continue
            prodw=1
            for x in leafs:
                h=sum(x)
                prodw*=q**h-q
            tot+=prodw
        assert 2**k*tot==formula(r,k,q)
        print('weighted pass',r,k,q,2**k*tot)
    # first asymptotic terms for q=2 and q=3, r=2
    for q,k in [(2,30),(3,35)]:
        r=2
        numerator=formula(r,k,q)
        den=(2*(q+1)**r)**k
        from fractions import Fraction
        defect=1-Fraction(numerator,den)
        if q==2:
            asym=Fraction(2*r*2**k,(q+1)**k)
        else:
            asym=Fraction(comb(r,2)*(q*q+1)**k,(q+1)**(2*k))
        ratio=float(defect/asym)
        assert abs(ratio-1)<0.02,(q,k,ratio)
        print('asymptotic pass',q,k,ratio)
    print('VERIFY_OK')

if __name__=='__main__':checks()
