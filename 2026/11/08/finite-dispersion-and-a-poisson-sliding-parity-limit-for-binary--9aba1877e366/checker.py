"""Finite exact checks for the binary burst-deletion spectrum theorem.
No external dependencies; standard Python 3.10+.
"""
from fractions import Fraction
from itertools import product


def ball(x, b):
    return {x[:i] + x[i+b:] for i in range(len(x)-b+1)}


def formula(x,b):
    return 1+sum(x[i] != x[i+b] for i in range(len(x)-b))


def moments_formula(n,b,p):
    N=n-b
    a=1-2*p
    mean=1+Fraction(N,2)*(1-a**b)
    variance=Fraction(N,4)*(1-a**(2*b))
    variance+=sum((Fraction(N-h,2)*(a**(2*h)-a**(2*b))) for h in range(1,min(b,N-1)+1))
    return mean,variance


def moments_exact(n,b,p):
    # The chain starts from a fair bit and flips independently on each of n-1 transitions.
    mean=Fraction(0); second=Fraction(0)
    for eps in product((0,1),repeat=n-1):
        weight=p**sum(eps)*(1-p)**(n-1-sum(eps))
        x=(0,)
        for e in eps: x+=(x[-1]^e,)
        v=len(ball(x,b))
        mean+=weight*v
        second+=weight*v*v
    return mean, second-mean*mean


def run():
    cases=0
    for n in range(2,10):
        for b in range(1,n+1):
            for x in product((0,1),repeat=n):
                assert len(ball(x,b))==formula(x,b),(n,b,x)
                cases+=1
            for p in (Fraction(1,4),Fraction(2,5),Fraction(1,2)):
                assert moments_exact(n,b,p)==moments_formula(n,b,p),(n,b,p)
    print('PASS: exact distinct-output checks', cases)
    print('PASS: exact moment checks',sum(range(2,10))*3,'parameter pairs')
    for n,b,p in [(8,3,Fraction(1,4)),(9,6,Fraction(2,5)),(7,2,Fraction(1,2))]:
        print('example',n,b,str(p),*(str(y) for y in moments_exact(n,b,p)))

if __name__=='__main__': run()
