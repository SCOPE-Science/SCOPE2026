"""Standalone supplementary arithmetic checks for elliptope projection instability.
Uses only the Python standard library. Mathematical asymptotics and the
projection tangent-limit theorem are proved in RESULT.md, not by this script.
"""
from fractions import Fraction
from math import sqrt

def formulas(n, r):
    k = n - 2
    b = k*(k-1)//2
    vals = [Fraction(1)] + [r]*(2*k) + [r*r]*b
    Q = sum(v*v for v in vals)
    S = sum(vals)
    exact_row = 1 + (S - 2)/Q
    claimed = 1 + (2*k*r + b*r*r - 1)/(1+2*k*r*r+b*r**4)
    assert exact_row == claimed
    q = vals
    # Row of tangent hyperplane projector, associated with pair (1,2).
    row = [1-Fraction(1,Q)] + [-a/Q for a in q[1:]]
    assert sum(abs(t) for t in row) == claimed
    # Sign vector optimizes the row exactly.
    sign = [Fraction(1)] + [-Fraction(1)]*(len(vals)-1)
    assert sum(a*b for a,b in zip(row,sign)) == claimed
    return float(claimed)

def gram_checks(n, r):
    # Exact Gram block formula, with a^2=1/(1+(kr)^2), c^2=(kr)^2*a^2/4.
    k = n - 2
    a2 = Fraction(1,1)/(1+(k*r)**2)
    c2 = (k*r)**2*a2/Fraction(4)
    ca = k*r*a2/Fraction(2)
    firstpair = 2*c2-1
    mixed = -ca
    lastpair = (k*a2-1)/(k-1)
    C = [[Fraction(1) if i==j else (firstpair if i<2 and j<2 else (lastpair if i>=2 and j>=2 else mixed)) for j in range(n)] for i in range(n)]
    v = [Fraction(1),Fraction(1)]+[r]*k
    for i in range(n):
        assert sum(C[i][j]*v[j] for j in range(n))==0
    # Check all positive eigenvalues via symmetry-mode decomposition.
    assert 2*(1-c2)>0
    assert k*(1-a2)/(k-1)>0
    assert 2*c2+k*a2>0
    assert (2*c2)*(k*a2)-2*k*ca**2==0
    return C

def asymptotic():
    s = 2**0.25
    c = (2-sqrt(2))/4
    def F(k):
        r=s/sqrt(k)
        b=k*(k-1)/2
        return (2*k*r+b*r*r-1)/(1+2*k*r*r+b*r**4)
    ks=[50,200,1000,5000,20000,100000]
    ratios=[F(k)/(k+2) for k in ks]
    assert all(c < val < 0.23 for val in ratios)
    assert abs(ratios[-1]-c)<0.002
    # The derivative of f(y)=y/(2+4y+y^2) has sign 2-y^2.
    for y in [0.01, 0.1, 1.0, 1.4, 2.0, 10.0]:
        der=(2-y*y)/(2+4*y+y*y)**2
        assert (der>0)==(y<sqrt(2))
    return ratios[-1]

def main():
    cases=0
    for n in range(4,27):
        for a,b in [(1,8),(1,3),(2,3),(3,4),(1,1),(3,2),(7,3)]:
            r=Fraction(a,b)
            L=formulas(n,r)
            gram_checks(n,r)
            assert L>=0
            cases+=1
    estimate=asymptotic()
    print(f'PASS: {cases} exact rational tangent-row and Gram certificates; asymptotic check {estimate:.12f}; limit {(2-sqrt(2))/4:.12f}')
if __name__=='__main__': main()
