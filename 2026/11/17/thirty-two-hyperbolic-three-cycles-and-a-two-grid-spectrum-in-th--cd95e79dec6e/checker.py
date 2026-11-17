#!/usr/bin/env python3
"""Exact exhaustive finite-branch certificate for a symmetric torus shear map.

No external dependencies; run alongside cycles.csv with Python 3.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import csv

I = ((1, 0), (0, 1))


def matmul(A, B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],
             A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0],
             A[1][0]*B[0][1]+A[1][1]*B[1][1]))


def mul(A, v):
    return (A[0][0]*v[0]+A[0][1]*v[1], A[1][0]*v[0]+A[1][1]*v[1])


def plus(u, v):
    return u[0]+v[0], u[1]+v[1]


def tent(x):
    return 2*min(x, 1-x)


def H(point):
    x,y=point
    u=(x+tent(y)) % 1
    return (u,(y+tent(u)) % 1)


def branch(j, m, l, k):
    a=2 if j==0 else -2
    d=0 if j==0 else 2
    b=2 if l==0 else -2
    e=0 if l==0 else 2
    return ((j,m,l,k), ((1,a),(b,1+a*b)),
            (d-m,b*(d-m)+e-k))

BRANCHES=[branch(*digits) for digits in product((0,1),repeat=4)]


def admissible(p, record):
    (j,m,l,k),A,c=record
    x,y=p
    if not (Q(0)<=x<1 and Q(0)<=y<1):
        return False
    if y!=Q(1,2) and (y<Q(1,2)) != (j==0):
        return False
    u=x+((2*y) if j==0 else (2-2*y))-m
    if not Q(0)<=u<1:
        return False
    if u!=Q(1,2) and (u<Q(1,2)) != (l==0):
        return False
    v=y+((2*u) if l==0 else (2-2*u))-k
    return Q(0)<=v<1


def fixed_affine(A,b):
    a11,a12=1-A[0][0],-A[0][1]
    a21,a22=-A[1][0],1-A[1][1]
    det=a11*a22-a12*a21
    assert det!=0, "An unhandled positive-dimensional branch appears"
    return (Q(a22*b[0]-a12*b[1],det),
            Q(-a21*b[0]+a11*b[1],det))


def regular_jacobian(p):
    x,y=p;u=H(p)[0]
    assert y not in (0,Q(1,2)) and u not in (0,Q(1,2))
    a=2 if y<Q(1,2) else -2
    b=2 if u<Q(1,2) else -2
    return ((1,a),(b,1+a*b))


def frac(x):
    return str(x.numerator)+"/"+str(x.denominator)


def main():
    admissible_incidence=Counter()
    local_trace_counts=Counter()
    for indices in product(range(16), repeat=3):
        A=I; offset=(0,0)
        records=[BRANCHES[i] for i in indices]
        for _, B, c in records:
            A=matmul(B,A)
            offset=plus(mul(B,offset),c)
        tr=A[0][0]+A[1][1]
        local_trace_counts[tr]+=1
        p=fixed_affine(A,offset)
        if not (0<=p[0]<1 and 0<=p[1]<1):
            continue
        orbit=[p,H(p),H(H(p))]
        if all(admissible(orbit[i],records[i]) for i in range(3)):
            assert H(orbit[-1])==p
            admissible_incidence[p]+=1
    assert sum(local_trace_counts.values())==4096
    assert local_trace_counts==Counter({-98:384,-82:768,-34:768,-2:128,
                                       22:768,38:384,102:768,198:128})
    assert sum(admissible_incidence.values())==177
    assert Counter(admissible_incidence.values())==Counter({1:97,8:2,64:1})
    points=set(admissible_incidence)
    assert len(points)==100
    fixed={p for p in points if H(p)==p}
    assert fixed==set(product((Q(0),Q(1,2)),repeat=2))
    least3=points-fixed
    assert len(least3)==96
    assert all(H(H(H(p)))==p for p in points)
    grid18={p for p in points if all((18*x).denominator==1 for x in p)}
    grid50={p for p in points if all((50*x).denominator==1 for x in p)}
    assert (len(grid18),len(grid50),len(grid18&grid50))==(28,76,4)
    assert points==grid18|grid50
    cycles=[]; visited=set()
    for p in sorted(least3):
        if p in visited:
            continue
        orbit=[p,H(p),H(H(p))]
        assert len(set(orbit))==3
        assert all(z in least3 for z in orbit)
        visited.update(orbit)
        A=I
        for z in orbit:
            A=matmul(regular_jacobian(z),A)
        tr=A[0][0]+A[1][1]
        assert A[0][0]*A[1][1]-A[0][1]*A[1][0]==1
        # Because every one-step derivative is I modulo 2, its return
        # matrix is too; the adjugate of I-A has even entries. The
        # denominator of a fixed point therefore divides |2-tr|/2.
        denominator_bound=abs(2-tr)//2
        assert abs(2-tr)%2==0
        assert all((denominator_bound*z).denominator==1
                   for point in orbit for z in point)
        cycles.append((min(orbit),tr))
    assert len(cycles)==32
    assert Counter(t for p,t in cycles)==Counter({102:16,-34:8,-98:8})
    assert visited==least3
    file=Path(__file__).with_name('cycles.csv')
    with file.open(newline='',encoding='utf-8') as stream:
        rows=list(csv.DictReader(stream))
    certified=sorted((Q(row['x']),Q(row['y']),int(row['trace'])) for row in rows)
    actual=sorted((p[0],p[1],tr)for p,tr in cycles)
    assert certified==actual, "The standalone list does not match enumeration"
    print('PASS: 4096 branch words; all return linear equations nonsingular')
    print('PASS: 177 admissible incidences, 100 distinct fixed H^3 points')
    print('PASS: 4 fixed H points, 96 least-period-3 points, 32 three-cycles')
    print('PASS: 18-grid/50-grid counts 28/76, shared 4')
    print('PASS: trace 102 (16 cycles), -34 (8), -98 (8), all hyperbolic')
    print('PASS: 32 cycle representatives agree with cycles.csv')

if __name__ == '__main__':
    main()
