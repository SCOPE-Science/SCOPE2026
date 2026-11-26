"""Exact rational cycle-index checks for the second-hook Fourier projector."""
from functools import lru_cache
from math import factorial
from fractions import Fraction

@lru_cache(None)
def parts(n, upper=None):
    if upper is None:upper=n
    if not n:return ((),)
    return tuple((k,)+p for k in range(min(upper,n),0,-1) for p in parts(n-k,k))

@lru_cache(None)
def no_short_cycles(n):
    if n==0:return 1
    return sum(factorial(n-1)//factorial(n-k)*no_short_cycles(n-k) for k in range(3,n+1))

def hook(n,f,t):return (f-1)*(f-2)//2-t

def analytic(n):
    neg=Fraction(0)
    for f in range(n+1):
        for t in range((n-f)//2+1):
            remainder=n-f-2*t
            weight=Fraction(no_short_cycles(remainder),factorial(remainder)*factorial(f)*2**t*factorial(t))
            neg+=max(-hook(n,f,t),0)*weight
    return (n-1)*(n-2)*neg

def classes(n):
    norm=Fraction(0);moment=Fraction(0);second=Fraction(0)
    for cyc in parts(n):
        den=1
        for k in set(cyc):den*=k**cyc.count(k)*factorial(cyc.count(k))
        x=hook(n,cyc.count(1),cyc.count(2))
        norm+=Fraction(abs(x),den)
        moment+=Fraction(x,den)
        second+=Fraction(x*x,den)
    return Fraction((n-1)*(n-2),2)*norm,moment,second

for n in range(4,13):
    a=analytic(n);b,m,s=classes(n)
    assert a==b and m==0 and s==1,(n,a,b,m,s)
    print('n=%d norm=%s (approx %.9f)'%(n,a,float(a)))
print('VERIFY_OK rational_cycle_classes=4..12 sign_support_and_orthogonality_and_formula')
