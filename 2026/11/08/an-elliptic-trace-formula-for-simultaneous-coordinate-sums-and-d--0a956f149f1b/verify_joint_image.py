"""Exact elementary checks for the simultaneous modular-hyperbola coordinate images.
Python 3 standard library; no external data files or packages.
"""
from math import gcd, isqrt


def factor(n):
    a=[]; p=2
    while p*p <= n:
        if n%p==0:
            k=0
            while n%p==0:n//=p;k+=1
            a.append((p,k))
        p=3 if p==2 else p+2
    if n>1:a.append((n,1))
    return a


def chi(t,p):
    t%=p
    if not t:return 0
    r=pow(t,(p-1)//2,p)
    assert r in (1,p-1)
    return 1 if r==1 else -1


def local(p,k):
    assert p>=3 and p%2==1 and k>=1
    e=chi(2,p); d=int(p%4==1)
    a=-sum(chi(t*t*t-t,p) for t in range(p))
    num=p-5-2*d-2*(1+d)*e-a
    assert num%4==0
    g=num//4
    assert g>=0
    q=1+sum(((p-1)//2)*p**(k-2*j-1) for j in range(1,(k-1)//2+1))
    return p**(k-1)*g+(1+d)*(1+e)*q


def predicted(n):
    result=1
    for p,k in factor(n):result*=local(p,k)
    return result


def direct(n):
    units=range(1,n)
    S=set(); D=set()
    for x in units:
        if gcd(x,n)==1:
            inv=pow(x,-1,n)
            S.add((x+inv)%n)
            D.add((x-inv)%n)
    return len(S&D)


def main():
    cases=0
    for n in range(3,1301,2):
        observed=direct(n); expect=predicted(n)
        assert observed==expect,(n,observed,expect,factor(n))
        assert (observed==0)==(n%3==0),(n,observed)
        cases+=1
    powers=0
    for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
        k=1
        while p**k<=90000:
            n=p**k
            assert direct(n)==local(p,k),(p,k)
            k+=1;powers+=1
    assert predicted(7)==2 and predicted(49)==2 and predicted(343)==8
    assert predicted(9)==0 and predicted(11)==2 and predicted(121)==22
    print('VERIFY_OK odd_moduli_3..1299=%d prime_powers=%d zero_iff_3_divides=PASS exact_count=PASS elliptic_trace_and_singular_lifts=PASS' % (cases,powers))

if __name__=='__main__':main()
