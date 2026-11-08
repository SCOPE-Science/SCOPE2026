"""Exact checks for the exchangeable-sample richness/diversity theorem.
Run with Python 3: python check.py . No external packages required.
The proof of the universal statements is in RESULT.md; this program checks
finite profiles and independently computes the explicit mixture moments.
"""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import combinations_with_replacement


def profiles(n, low=1):
    if n == 0:
        yield ()
    else:
        for x in range(low, n+1):
            for tail in profiles(n-x, x):
                yield (x,) + tail


def pair_count(profile):
    return sum(comb(x, 2) for x in profile)


def bound_min(n, k):
    q, r = divmod(n, k)
    return (k-r)*comb(q, 2) + r*comb(q+1, 2)


def bound_max(n, k):
    return comb(n-k+1, 2)


def direct_moments(n, p):
    # Exact multinomial occupancy vector enumeration, not an invocation of the
    # symbolic covariance formula.
    res=[Q(0),Q(0),Q(0)]
    for a in range(n+1):
        for b in range(n-a+1):
            cs=(a,b,n-a-b)
            weight=Q(factorial(n), factorial(a)*factorial(b)*factorial(n-a-b))
            for i in range(3):
                weight*=p[i]**cs[i]
            k=sum(x>0 for x in cs)
            g=Q(comb(n, 2)-pair_count(cs), comb(n, 2))
            res[0]+=weight*k
            res[1]+=weight*g
            res[2]+=weight*k*g
    return tuple(res)


def exact_mixture_cov(n):
    A=(Q(1,2),Q(1,2),Q(0))
    B=(Q(9,10),Q(1,20),Q(1,20))
    u=direct_moments(n,A)
    v=direct_moments(n,B)
    return (u[2]+v[2])/2-(u[0]+v[0])*(u[1]+v[1])/4


def formula_cov_iid(p,n):
    s=sum(x*x for x in p)
    return sum(x*(1-x)**(n-2)*(2*s-(1+s)*x) for x in p)


def formula_mixture_cov(n):
    A=(Q(1,2),Q(1,2),Q(0))
    B=(Q(9,10),Q(1,20),Q(1,20))
    mk=lambda p: sum(1-(1-x)**n for x in p)
    mg=lambda p: 1-sum(x*x for x in p)
    return (formula_cov_iid(A,n)+formula_cov_iid(B,n))/2+(mk(A)-mk(B))*(mg(A)-mg(B))/4


def main():
    checks=0
    for n in range(2,7):
        pp=list(profiles(n))
        for k in range(1,n+1):
            cs=[pair_count(v) for v in pp if len(v)==k]
            assert min(cs)==bound_min(n,k)
            assert max(cs)==bound_max(n,k)
            checks+=2
        for k in range(1,n):
            assert bound_min(n,k)>=bound_max(n,k+1)
            checks+=1
    for n in range(7,121):
        x=n//2
        y=n-x
        delta=comb(n-2,2)-comb(x,2)-comb(y,2)
        assert delta>0
        assert -Q(delta,4*comb(n,2))<0
        checks+=2
    assert -Q(1,84)==-Q(1,4*comb(7,2))
    checks+=1
    for n in range(2,27):
        d=exact_mixture_cov(n)
        f=formula_mixture_cov(n)
        assert d==f,(n,d,f)
        checks+=1
    assert formula_mixture_cov(21)>0
    assert formula_mixture_cov(22)==-Q(3412690498811343615664816319,16777216000000000000000000000000)
    assert formula_mixture_cov(22)<0
    checks+=3
    assert Q(1,4)*(Q(2)-Q(3))*(Q(1,2)-Q(37,200))==-Q(63,800)
    checks+=1
    print('PASS',checks,'exact assertions; mixture n=22 covariance =',formula_mixture_cov(22))
    print('Finite exchangeable n=7 covariance =',-Q(1,84))
    print('Infinite-mixture limiting covariance =',-Q(63,800))

if __name__=='__main__':main()
