"""Exact integer audit of the weighted 4-cube simplex-volume identity."""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction

def det_int(rows):
    a = [list(map(int, row)) for row in rows]
    n = len(a)
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            t = next((i for i in range(k+1,n) if a[i][k]),None)
            if t is None:
                return 0
            a[k],a[t]=a[t],a[k]
            sign=-sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=pivot
    return sign*a[n-1][n-1]

v=list(product([0,1],repeat=4))
counts=Counter()
values=Counter()
for subset in combinations(v,5):
    D=abs(det_int([[1,*point] for point in subset]))
    values[D]+=1
    if D<=1:continue
    k=[sum(pt[j] for pt in subset) for j in range(4)]
    bad=tuple(j for j,a in enumerate(k) if a in (1,4))
    assert all(a in (1,2,3,4) for a in k)
    counts[bad]+=D*(D-1)
assert sum(values.values())==4368
assert counts=={():480,(0,):64,(1,):64,(2,):64,(3,):64},counts
# Averaging over independent coordinate reflections gives in each coordinate
# the factor q/2 if k=2 or3, and (1-3*q)/2 if k=1 or4.
# Thus the exact normalized gap E=(detCov-P)/prod Var is
# E(q)=480/16 * prod(q) + 64/16 * sum_j((1-3*q_j)*prod_{i!=j}q_i)
# =4*e3(q)-18*e4(q).
for q in product([Fraction(0),Fraction(1,8),Fraction(1,4)],repeat=4):
    e3=sum(q[i]*q[j]*q[k] for i,j,k in combinations(range(4),3))
    e4=q[0]*q[1]*q[2]*q[3]
    a=Fraction(480,16)*e4 + sum(Fraction(64,16)*(1-3*q[j])*__import__('math').prod(q[i] for i in range(4) if i!=j) for j in range(4))
    assert a==4*e3-18*e4
# Sharp stability polynomial is multi-affine in z_i=4q_i.
# H(z)=(23/128)*(sum z_i)/4 - (e3(z)/16 -9e4(z)/128).
# Multi-affine interpolation means checking 16 cube vertices is exhaustive.
for z in product([0,1],repeat=4):
    g=Fraction(1,16)*sum(z[i]*z[j]*z[k] for i,j,k in combinations(range(4),3))-Fraction(9,128)*__import__('math').prod(z)
    h=Fraction(23,128)*Fraction(sum(z),4)-g
    assert h>=0,(z,h)
    assert (h==0)==(sum(z) in (0,4))
assert Fraction(1)-Fraction(4)*Fraction(4,64)+Fraction(18,256)==Fraction(105,128)
print('PASS: 4368 simplices, exact determinant counts',dict(sorted(values.items())))
print('PASS: excess strata',dict(counts))
print('PASS: exact product-Bernoulli formula and sharp stability on 16 cube vertices')
