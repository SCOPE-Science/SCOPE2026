"""Supplementary exact arithmetic checks for the canonical cross-polytope width."""
from fractions import Fraction
from itertools import product
for m in range(2, 31):
    target_sq=Fraction(m,4*(m-1))
    for k in (0,1,2,m-1):
        eps=[-1 if (j+k)%3 == 0 else 1 for j in range(m)]
        for i in range(m):
            y=[Fraction(1,2) if j==i else Fraction(-eps[i]*eps[j],2*(m-1)) for j in range(m)]
            assert sum(eps[j]*y[j] for j in range(m)) == 0
            assert sum(map(abs,y)) == 1
            assert sum((Fraction(j==i)-y[j])**2 for j in range(m)) == target_sq
    for a in range(0,1001):
        t=Fraction(a,2000)
        assert (1-t)**2+t*t/Fraction(m-1) >= target_sq
print('CHECK_OK: exact rational witnesses and scalar lower bound for m=2..30')
