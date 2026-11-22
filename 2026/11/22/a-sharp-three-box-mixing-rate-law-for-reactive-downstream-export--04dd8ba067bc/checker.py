"""Exact-arithmetic checks for three-compartment advective-dispersive export.

Run: python3 checker.py
Only Python standard-library dependencies are used. Finite checks supplement,
but do not replace, the algebraic proof in the accompanying article.
"""
from fractions import Fraction as Q
from random import Random


def solve(M, b):
    a = [[Q(v) for v in row] + [Q(z)] for row, z in zip(M, b)]
    n = len(a)
    for k in range(n):
        h = next(i for i in range(k,n) if a[i][k])
        a[k],a[h] = a[h],a[k]
        t=a[k][k]; a[k]=[v/t for v in a[k]]
        for i in range(n):
            if i==k: continue
            t=a[i][k]
            a[i]=[x-t*y for x,y in zip(a[i],a[k])]
    return [row[-1] for row in a]


def polynomials(a,b,c):
    p0=(1+a)*(1+b)*(1+c)
    p1=a*b+b*c+2*a*c+2*(a+b+c+1)
    p2=1+a+b+c
    return p0,p1,p2


def export(a,b,c,m,j):
    p0,p1,p2=polynomials(a,b,c)
    P=p0+p1*m+p2*m*m
    numerator=[(m+1)**2, (m+1)*(m+a+1),
               (a+1)*(b+1)+(2*a+b+2)*m+m*m][j]
    return numerator/P


def stationary(a,b,c,m,j):
    M=[[1+a+m,-m,0],[-1-m,1+b+2*m,-m],[0,-1-m,1+c+m]]
    return solve(M,[Q(int(i==j)) for i in range(3)])[2]


def derivative_numer(a,b,c,j):
    p0,p1,p2=polynomials(a,b,c)
    if j==0: n0,n1,n2=Q(1),Q(2),Q(1)
    if j==1: n0,n1,n2=a+1,a+2,Q(1)
    if j==2: n0,n1,n2=(a+1)*(b+1),2*a+b+2,Q(1)
    return ((n1*p0-n0*p1), 2*(n2*p0-n0*p2), (n2*p1-n1*p2))


count=0
rng=Random(5491)
for i in range(2500):
    a,b,c,m=[Q(rng.randint(1,30),rng.randint(1,15)) for _ in range(4)]
    for j in range(3):
        assert stationary(a,b,c,m,j)==export(a,b,c,m,j)
        count+=1
    # Sign polynomials for upstream and downstream injection must be strict.
    assert all(v>0 for v in derivative_numer(a,b,c,0))
    assert all(v<0 for v in derivative_numer(a,b,c,2))
    count+=2
    # Middle-source phase condition, every positive rational a,b,c.
    c0,c1,c2=derivative_numer(a,b,c,1)
    assert c2==c*(a+b)-a*(a+1)
    assert c1==2*(a+1)*(b*c-a)
    assert c0==(a+1)*(b*c*(a+1)-a*(c+1))
    assert not(c0>0 and c1<0 and c2>0)
    assert not(c0<0 and c1>0 and c2<0)
    count+=5

# A two-compartment chain has a strictly monotonic response regardless of injection.
for a in range(1,12):
    for b in range(1,12):
        D0=(a+1)*(b+1)
        D1=a+b+1
        assert D0-D1==a*b>0
        assert D0-(a+1)*D1==-a*(a+1)<0
        count+=2

# Exact example with one strict interior maximum and identical boundary exports.
a,b,c=Q(3),Q(3),Q(1)
assert export(a,b,c,Q(0),1)==Q(1,8);count+=1
assert export(a,b,c,Q(2),1)==Q(3,22);count+=1
assert Q(1,1)/(1+a+b+c)==Q(1,8);count+=1
D=derivative_numer(a,b,c,1)
assert D==(Q(24),Q(0),Q(-6));count+=1
assert D[0]+D[1]*2+D[2]*4==0;count+=1
assert Q(3,22)>Q(1,8);count+=1
print(f"PASS: {count} exact-arithmetic assertions")
