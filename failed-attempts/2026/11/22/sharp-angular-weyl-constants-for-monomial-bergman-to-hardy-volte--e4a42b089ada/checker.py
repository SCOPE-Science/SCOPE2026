"""Finite arithmetic and asymptotic diagnostics for monomial Bergman-to-Hardy Volterra singular values."""
from __future__ import annotations
from math import gamma, lgamma, log, exp, sqrt
from fractions import Fraction
from itertools import product


def squared_singular(d: int, alpha: float, a: tuple[int,...], k: tuple[int,...]) -> float:
    assert len(a)==len(k)==d and sum(a)>0 and all(v>=0 for v in a+k)
    m=sum(a); n=sum(k)
    L=2*log(m/(n+m))+lgamma(d)-lgamma(d+alpha+1)
    L+=lgamma(d+alpha+1+n)-lgamma(d+n+m)
    L+=sum(lgamma(kj+aj+1)-lgamma(kj+1) for kj,aj in zip(k,a))
    return exp(L)


def weyl_constant(d,alpha,a):
    m=sum(a); q=2*d/(1-alpha)
    C=m*sqrt(gamma(d)/gamma(d+alpha+1))
    K=C**q/d*exp(sum(lgamma(1+aj*q/2) for aj in a)-lgamma(d+m*q/2))
    return q,K


def lattice_points_degree(d,n):
    if d==1:
        yield (n,)
    elif d==2:
        for j in range(n+1): yield (j,n-j)
    elif d==3:
        for i in range(n+1):
            for j in range(n-i+1): yield (i,j,n-i-j)
    else: raise ValueError('This finite checker intentionally uses at most three dimensions')


def count(d,alpha,a,t,cap):
    count=0
    for n in range(cap+1):
        for k in lattice_points_degree(d,n):
            if squared_singular(d,alpha,a,k)>t*t:count+=1
    return count


def fraction_sq(d,alpha,a,k):
    assert isinstance(alpha,int) and alpha>=0
    m=sum(a);n=sum(k)
    from math import factorial
    return (Fraction(m*m,(n+m)**2)
      * Fraction(factorial(d-1)*factorial(d+alpha+n),factorial(d+alpha)*factorial(d+n+m-1))
      * Fraction(__import__('math').prod(factorial(kj+aj)//factorial(kj) for kj,aj in zip(k,a)),1))


def run():
    for d,alpha,a in ((1,0,(2,)),(2,0,(1,1)),(2,1,(2,0)),(3,0,(1,0,1))):
        for n in range(0,8):
            for k in lattice_points_degree(d,n):
                exact=float(fraction_sq(d,alpha,a,k))
                approx=squared_singular(d,float(alpha),a,k)
                assert abs(exact-approx)<3e-12*max(exact,1e-12),(d,a,k,exact,approx)
        print('Exact arithmetic agrees with gamma formula:',d,alpha,a)
    d,alpha,a=2,0.,(1,1);q,K=weyl_constant(d,alpha,a)
    assert abs(K-1/15)<1e-14
    for t in (0.15,0.10,0.07):
        num=count(d,alpha,a,t,800)
        ratio=num*t**q/K
        print('d2 mixed monomial cutoff:',t,num,'Weyl ratio:',round(ratio,7))
        assert (0.86 if t==0.15 else 0.92 if t==0.10 else 0.95)<ratio<1.05
    d,alpha,a=2,0.,(2,0);q,K=weyl_constant(d,alpha,a)
    assert abs(K-0.4)<1e-13
    num=count(d,alpha,a,0.13,500)
    print('d2 coordinate square cutoff:', num,'Weyl ratio:',num*.13**q/K)
    assert .9<num*.13**q/K<1.08
    d,alpha,a=3,0.,(1,0,1);q,K=weyl_constant(d,alpha,a)
    for t in (.21,.15):
        num=count(d,alpha,a,t,200)
        ratio=num*t**q/K
        print('d3 mixed monomial cutoff:',t,num,'Weyl ratio:',round(ratio,6))
        assert 0.65<ratio<1.1
    print('All finite diagnostics passed. Infinite conclusions use analytic arguments, not these tests.')

if __name__=='__main__':run()
