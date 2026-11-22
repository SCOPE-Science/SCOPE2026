"""Exact checks for planar skyline--dominated-area dependence.
Standard library only. The proof is in RESULT.md; finite checks are corroboration.
"""
from fractions import Fraction as F
from math import factorial, isclose, log, sqrt
from itertools import permutations


def H(n, power=1):
    return sum((F(1, k ** power) for k in range(1, n+1)), F(0))


def exact_cov(n):
    return -((n+2)*H(n) - (n+1)*H(n,2) - n) / F((n+1)**2)


def exact_var_area(n):
    h, h2 = H(n+1), H(n+1,2)
    return ((n+1)*(2*(n+3)*h - 2*(n+1) - (n+2)*h2) - (n+2)*h*h) / F((n+1)**2 * (n+2)**2)


def exact_kernel(s,t,n):
    if s>t: s,t=t,s
    return F(s, (s+1)*(t+1)*(t+2))


def var_area_from_kernel(n):
    V = sum((exact_kernel(s,t,n) for s in range(n+1) for t in range(n+1)),F(0))
    EUS = sum((F(2,(t+1)*(t+2)) for t in range(n+1)), F(0))
    h = H(n+1)
    return (V + h*h + EUS)/F((n+1)*(n+2)) - h*h/F((n+1)**2)


def cov_from_kernel(n):
    # From the record indicator versus running rank maximum kernel
    return -sum((F(s, (s+1)*t*(t+1)*(n+1))
                 for s in range(1,n) for t in range(s+1,n+1)),F(0))


def enumerate_cov(n):
    # Conditional on the relative Y ranks, E[area] = sum of running rank maxima /(n+1)^2.
    ck=ca=cka=F(0)
    count=factorial(n)
    for perm in permutations(range(1,n+1)):
        best=0;k=0;total=0
        for v in perm:
            if v>best:
                best=v;k+=1
            total+=best
        a=F(total,(n+1)**2)
        ck+=k;ca+=a;cka+=k*a
    return cka/count -(ck/count)*(ca/count)


def main():
    checks=0
    for n in range(1,80):
        assert exact_cov(n)==cov_from_kernel(n)
        assert exact_var_area(n)==var_area_from_kernel(n)
        assert exact_var_area(n)>0
        checks+=3
        if n>=2:
            assert exact_cov(n)<0
            checks+=1
    for n in range(2,9):
        assert exact_cov(n)==enumerate_cov(n), (n,exact_cov(n),enumerate_cov(n))
        checks+=1
    for n in [100,1000,10000]:
        h=sum(1.0/i for i in range(1,n+1))
        h2=sum(1.0/(i*i) for i in range(1,n+1))
        hh=h+1.0/(n+1)
        hh2=h2+1.0/((n+1)**2)
        cov=-((n+2)*h-(n+1)*h2-n)/(n+1)**2
        varK=h-h2
        varA=((n+1)*(2*(n+3)*hh-2*(n+1)-(n+2)*hh2)-(n+2)*hh*hh)/((n+1)**2*(n+2)**2)
        rho=cov/sqrt(varK*varA)
        print('n=',n,'rho=',rho,'cov=',cov,'n^2 Var(A)/log(n)=',n*n*varA/log(n))
        assert rho<0 and varA>0
        checks+=1
    print('PASS',checks,'exact and consistency checks')
if __name__=='__main__':main()
