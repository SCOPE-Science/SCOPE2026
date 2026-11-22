#!/usr/bin/env python3
"""Exact finite checks for the quadratic-form reduction of tagged odd-part totals."""
from math import isqrt

LIMIT=2000

def product_coefficients(nmax):
    """Expand the original five-factor eta quotient modulo four, then shift."""
    a=[1]+[0]*nmax
    for scale,power in ((2,1),(3,2),(12,2),(1,-2),(6,-1)):
        for j in range(1,nmax//scale+1):
            h=scale*j
            for _ in range(abs(power)):
                if power>0:
                    for n in range(nmax,h-1,-1):
                        a[n]=(a[n]-a[n-h])%4
                else:
                    for n in range(h,nmax+1):
                        a[n]=(a[n]+a[n-h])%4
    return [0]+a[:nmax]

def quadratic_formula(n):
    """Independent pentagonal-square representation expression."""
    total=0
    bound=(isqrt(n)+1)//6+3
    for t in range(-bound,bound+1):
        x=6*t-1
        r=n-x*x
        if r<0:
            continue
        sign=-1 if t&1 else 1
        if r==0:
            total+=sign
        for d in (1,3,12):
            if r>0 and r%d==0:
                y2=r//d
                if isqrt(y2)**2==y2:
                    total+=(2 if d==1 else -2)*sign
    return total%4

def prime(n):
    if n<2:
        return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:
            return False
    return True

def prime_formula(p):
    if p%4!=1:
        return 0
    for a in range(1,isqrt(p)+1,2):
        b2=p-a*a
        if b2>0 and isqrt(b2)**2==b2:
            assert isqrt(b2)%2==0
            return 0 if a%3==0 else 2
    raise AssertionError('Two-squares representation missing for p='+str(p))

def inert_odd_divisor(n):
    q=11
    while q<=n:
        if q%12==11 and prime(q):
            v=0
            m=n
            while m%q==0:
                m//=q
                v+=1
            if v%2:
                return True
        q+=12
    return False

def run():
    a=product_coefficients(LIMIT)
    for n in range(1,LIMIT+1):
        assert a[n]==quadratic_formula(n),('quadratic identity',n,a[n],quadratic_formula(n))
    ps=[p for p in range(5,LIMIT+1) if prime(p)]
    for p in ps:
        assert a[p]==prime_formula(p),('prime formula',p,a[p],prime_formula(p))
    cases=0
    for n in range(1,LIMIT+1):
        if inert_odd_divisor(n):
            cases+=1
            assert a[n]==0,('inert obstruction',n,a[n])
        if n%4==3:
            assert a[n]==0,('three modulo four',n,a[n])
    assert a[1]==1 and a[2]==2 and a[3]==0
    print('VERIFY_OK: '+str(LIMIT)+' coefficient/representation pairs; '
          +str(len(ps))+' prime cases; '+str(cases)
          +' inert-prime obstructions; all 3 (mod 4) indices through limit')

if __name__=='__main__':
    run()
