"""Exact small-order binary-cut verification of centered finite summation."""
from fractions import Fraction
from itertools import combinations

EXPECTED = {
    2: {1: Fraction(1,2)},
    3: {1: Fraction(2,3), 2: Fraction(2,3)},
    4: {1: Fraction(5,6), 2: Fraction(3,4), 3: Fraction(5,6)},
    5: {1: Fraction(1), 2: Fraction(14,15),3: Fraction(14,15),4:Fraction(1)},
}

def gini(v):
    return sum(abs(b-a) for i,a in enumerate(v) for b in v[i+1:])

def integrate_centered(x):
    n=len(x)
    mean=sum(x, Fraction(0))/n
    total=Fraction(0)
    y=[]
    for z in x:
        total += z-mean
        y.append(total)
    assert total == 0
    return y

count=0
for n, expectations in EXPECTED.items():
    values={}
    for k in range(1,n):
        best=Fraction(0)
        for subset in combinations(range(n),k):
            x=[Fraction(int(i in subset)) for i in range(n)]
            observed=gini(integrate_centered(x)) / gini(x)
            best=max(best,observed)
            count+=1
        values[k]=best
    assert values==expectations,(n,values,expectations)
print('ALL_EXACT_SMALL_BINARY_CUTS_PASSED',count)
for n in range(2,60):
    x=[Fraction(1)]+[Fraction(0)]*(n-1)
    ratio=gini(integrate_centered(x))/gini(x)
    assert ratio == Fraction(n+1,6)
    assert Fraction(n+1,6) <= Fraction((n*n)//4,n)
print('ALL_EXACT_SINGLETON_WITNESSES_AND_DIMENSION_BOUNDS_PASSED',58)
print('ALL_CENTERED_PRIMITIVE_GINI_CHECKS_PASSED')
