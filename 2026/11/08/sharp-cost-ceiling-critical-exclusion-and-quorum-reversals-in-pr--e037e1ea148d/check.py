"""Standalone exact-rational checks for risk-weighted quorum advantage.

No external packages are needed. These finite checks supplement, not replace,
the analytic all-size arguments.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product


def psi_explicit(n,h,rho,x,y,z):
    total=Q(0)
    for m in range(n+1):
        if m != h:
            continue
        for j in range(n-m+1):
            i=n-m-j
            coeff=Q(comb(n,m)*comb(n-m,j))
            total += coeff*z**m*y**j*x**i*(1-rho**j)
    return total


def psi_closed(n,h,rho,x,y,z):
    s=n-h
    return comb(n,h)*z**h*((x+y)**s-(x+rho*y)**s)


def B(n,h):
    return Q(comb(n,h)*h**h*(n-h)**(n-h),n**n)


def F(n,h,rho):
    return B(n,h)*(1-rho**(n-h))


def checks():
    total=0
    for n in range(2,11):
        for h in range(1,n):
            for rho in [Q(1,8),Q(1,4),Q(1,2),Q(7,8)]:
                for denominator in [5,9]:
                    for X in range(denominator+1):
                        for Z in range(denominator-X+1):
                            x,z=Q(X,denominator),Q(Z,denominator)
                            y=1-x-z
                            a=psi_explicit(n,h,rho,x,y,z)
                            b=psi_closed(n,h,rho,x,y,z)
                            assert a==b, (n,h,rho,x,y,z,a,b)
                            assert 0<=a<=F(n,h,rho)
                            total+=1
                z=Q(h,n)
                assert psi_closed(n,h,rho,Q(0),1-z,z)==F(n,h,rho)
        for rho in [Q(1,8),Q(1,4),Q(1,2),Q(7,8)]:
            fs=[F(n,h,rho) for h in range(1,n)]
            assert fs[0]==max(fs)
            if n>2:
                assert all(fs[0]>v for v in fs[1:])
    assert F(4,3,Q(1,16))>F(4,2,Q(1,16))
    assert F(4,3,Q(1,8))==F(4,2,Q(1,8))
    assert F(4,3,Q(1,4))<F(4,2,Q(1,4))
    print('PASS',total,'multinomial exact-rational compositions')
    print('PASS all optimizer ceilings and M=2 optimum for n=2,...,10')
    print('PASS 5-player sharp last-step reversal at rho=1/8')
    for n in [4,5,8,16]:
        for h in range(1,n-1):
            r=B(n,h+1)/B(n,h)
            if 2*h<=n-1:
                assert r<=1
                assert all(F(n,h+1,rho)<F(n,h,rho) for rho in [Q(1,10000),Q(1,2),Q(9999,10000)])
            else:
                assert r>1
                s=n-h
                assert r < Q(s,s-1)
                assert F(n,h+1,Q(1,1000000))>F(n,h,Q(1,1000000))
                assert F(n,h+1,Q(999999,1000000))<F(n,h,Q(999999,1000000))
    print('PASS exact adjacent-quorum strict/late crossover comparisons')

if __name__=='__main__':
    checks()
