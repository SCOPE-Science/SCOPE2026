#!/usr/bin/env python3
"""Direct finite computations for quadratic residue exponent-pair laws."""
from fractions import Fraction
from math import isqrt

def vp(n,p):
    if n==0:return None
    v=0
    while n%p==0:n//=p;v+=1
    return v

def chi(u,p):
    if u%p==0:return 0
    return 1 if pow(u%p,(p-1)//2,p)==1 else -1

def order(a,p):
    t=a%p;r=1
    while t!=1:t=t*a%p;r+=1
    return r

def condition(m,p,c):
    if m==0:return False # zero is Haar-null; not counted in the open square cylinders
    v=vp(m,p)
    return v%2==1 and chi(c*(m//(p**v)),p)==1

def direct_condition(m,p,a,d):
    if m==0:return False
    v=vp(m,p)
    w=1+v
    modulus=p**(w+1)
    number=(pow(a,d*m,modulus)-1)%modulus
    assert number%(p**w)==0,(m,p,a,d)
    if v%2==0:return False
    return chi(number//(p**w),p)==1

def mu(p):return Fraction(1,2*(p+1))

def pair(t,p):
    if t==0:return mu(p)
    a=vp(abs(t),p)
    j=a//2
    baseline=mu(p)*(1-Fraction(1,p**(2*j)))
    if a%2==0:return baseline
    seed=Fraction(p-3,4*p*p)+mu(p)/p**2
    return baseline+seed/Fraction(p**(2*j))

def direct_pair_count(t,p,r,c):
    z=p**r
    return sum(condition(m,p,c) and condition(m+t,p,c) for m in range(z))

def full7(n):
    q=n%3
    if q==1:return True
    if q==2:return False
    if n==0:return True
    return condition(n//3,7,1)

def pair7(h):
    if h%3:return Fraction(1,48)
    return (1+pair(h//3,7))/3

def main():
    seen=0
    for p in (3,7,11,19,23):
        qr={i for i in range(1,p) if chi(i,p)==1}
        lam=(p-3)//4
        for u in range(1,p):
            assert sum((x+u)%p in qr for x in qr)==lam
            seen+=1
        a=2;d=order(a,p)
        c=(pow(a,d,p*p)-1)//p
        assert c%p!=0, (p,d)
        for m in range(1,1400):
            assert condition(m,p,c)==direct_condition(m,p,a,d),(p,m)
            seen+=1
        for r in range(2,5 if p<=11 else 4):
            for t in (0,1,2,p,2*p,p*p,p*p*p,1+p):
                exact=direct_pair_count(t,p,r,c)
                target=pair(t,p)*p**r
                assert abs(exact-target)<=6*r+10,(p,r,t,exact,target)
                seen+=1
    for r in (3,4,5):
        length=3*7**r
        for h in (0,1,2,3,6,21,42,147,294,343,1029):
            observed=sum(full7(n) and full7(n+h) for n in range(length))
            target=pair7(h)*length
            assert abs(observed-target)<10*r+15,(r,h,observed,target)
            seen+=1
    assert mu(7)==Fraction(1,16)
    assert pair(7,7)==Fraction(17,784)
    assert pair7(1)==Fraction(1,48)
    assert pair7(3)==Fraction(1,3)
    assert pair7(21)==Fraction(1,3)+Fraction(17,2352)
    print('PASS',seen,'finite checks')
    print('p7 full-index square density',Fraction(17,48))
    print('p7 short-lag joint densities',[(h,str(pair7(h))) for h in [0,1,2,3,6,21,147,1029]])
    print('special prime p=3 seed',pair(3,3),'p=7 seed',pair(7,7))
if __name__=='__main__':main()
