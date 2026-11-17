"""Exact integer and rational checks for the 3D heterochaos baker map's fiber laws."""
from fractions import Fraction
from itertools import product
from math import comb, isclose, log, sqrt, pi

def fiber_interval(word):
    a,b=Fraction(0),Fraction(1)
    for digit in word:
        if digit==0: a,b=a/2,b/2
        elif digit==1: a,b=(a+1)/2,(b+1)/2
        else:
            if b<=Fraction(1,2): a,b=2*a,2*b
            elif a>=Fraction(1,2): a,b=2*a-1,2*b-1
            else:
                assert a==0 and b==1
                a,b=Fraction(0),Fraction(1)
    return a,b

def length_formula(word):
    s=m=0
    for d in word:
        s+=(1 if d==2 else -1)
        m=max(m,s)
    return Fraction(1,2**(m-s))

def exact_count(n):
    return sum(2**j*(comb(n,j)-(comb(n,j-1) if j else 0)) for j in range(n//2+1))

counts=[]
for n in range(10):
    full=0
    for word in product(range(3),repeat=n):
        a,b=fiber_interval(word)
        assert (b-a)==length_formula(word), (n,word,a,b)
        full+=(b-a==1)
    assert full==exact_count(n),(n,full,exact_count(n))
    counts.append(full)
assert counts==[1,1,3,5,15,29,87,181,543,1181]
# Weighted Dyck counts of balanced nonpositive paths of length 2m.
for m in range(1,7):
    c=0
    for word in product(range(3),repeat=2*m):
        s=0
        valid=True
        for d in word:
            s+=(1 if d==2 else -1)
            if s>0:valid=False;break
        c+=(valid and s==0)
    assert c==2**m*comb(2*m,m)//(m+1)
assert isclose(log(2*sqrt(2))/log(3), 0.946394630357186, abs_tol=1e-12)
print('HETEROCHAOS_SATURATION_BALLOT_DIMENSION_CHECK_OK')
print('saturation counts n=0..9:',counts)
print('dimension:',2+log(2*sqrt(2))/log(3))
print('asymptotic even/odd constants:',12*sqrt(2/pi),16/sqrt(pi))
