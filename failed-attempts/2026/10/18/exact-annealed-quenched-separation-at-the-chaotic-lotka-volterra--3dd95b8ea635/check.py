"""Exact Fourier-polynomial check for the displayed first and second moments.
No probabilistic simulation or numerical limit is used for the integer identities.
"""
from collections import defaultdict
from fractions import Fraction

def multiply(a, b):
    c = defaultdict(int)
    for j, x in a.items():
        for k, y in b.items():
            c[j+k] += x*y
    return {k:v for k,v in c.items() if v}

def factors(step):
    s=1<<step
    first={-s:-1,0:2,s:-1}
    second={-2*s:1,-s:-4,0:6,s:-4,2*s:1}
    return first,second

A,B=1,0
one,two={0:1},{0:1}
for n in range(1,10):
    first,second=factors(n-1)
    one=multiply(one,first)
    two=multiply(two,second)
    A,B=6*A-4*B,2*A-4*B
    assert one.get(0,0)==2**n,(n,'first',one.get(0,0))
    assert two.get(0,0)==A,(n,'second',two.get(0,0),A)
    # The exact normalized logarithmic variance is pi^2 times this coefficient.
    coeff=Fraction(3*n-4,3)+Fraction(2**2,3*2**n)
    covariance_sum=Fraction(n,3)+sum(Fraction(2*(n-k),3*2**k) for k in range(1,n))
    assert coeff==covariance_sum
print('PASS: 9 exact Fourier-constant-term first/second moment cases and 9 log-covariance identities')
