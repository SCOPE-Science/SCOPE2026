"""Exact supplementary checks for circle heat-kernel sum-coordinate modulation.
Run: python3 check_gaussian_sum_modulation.py. Standard library only.
The universal theorem is proved by the Fourier factorization, not these finite checks.
"""
from fractions import Fraction as F
from itertools import product

def pmin(A,B):
    # 1+A*u+B*(2*u*u-1), u in [-1,1]
    vals=[1+B-A,1+B+A]
    if B>0 and abs(A)<=4*B:
        vals.append(1-B-A*A/(8*B))
    return min(vals)

def coefficient(q, coeffs, n, m):
    if n==m: return q**(n*n)
    d=n-m
    if d%2: return F(0)
    j=abs(d)//2
    if j not in coeffs: return F(0)
    return F(1,2)*coeffs[j]*q**(((n+m)//2)**2)

def factored(q,coeffs,n,m):
    if n==m: return q**(n*n)
    d=n-m
    if d%2: return F(0)
    j=abs(d)//2
    if j not in coeffs:return F(0)
    assert (n*n+m*m)%2==0
    return F(1,2)*coeffs[j]*q**(-j*j+(n*n+m*m)//2)

checks=0
for q in [F(1,2),F(2,3),F(3,5)]:
    for coeffs in [{1:F(1,5)}, {1:q}, {1:F(2,5), 2:F(1,20)}, {1:F(-1,3),2:F(1,7)}, {2:q**4}]:
        for n,m in product(range(-11,12),repeat=2):
            assert coefficient(q,coeffs,n,m)==factored(q,coeffs,n,m),(q,coeffs,n,m)
            checks+=1
for A in [F(k,10) for k in range(-20,21)]:
    for B in [F(k,10) for k in range(-15,16)]:
        # all stationary critical candidates are exact quadratic minimizations
        v=pmin(A,B)
        if B<=0:assert v==1+B-abs(A)
        if B>0 and abs(A)<=4*B:assert v==1-B-A*A/(8*B)
        checks+=1
assert pmin(F(1),F(0))==0
assert pmin(F(11,10),F(0))<0
assert pmin(F(0),F(1))==0
assert pmin(F(0),F(11,10))<0
print('PASS',checks,'exact rational identities and boundary tests')
