#!/usr/bin/env python3
"""Exact-rational reproducibility checks for the priced two-community network theorem.

Run: python3 verify.py
Uses only the Python standard library. Finite checks support the proof; they do
not establish its all-parameter assertions.
"""
from fractions import Fraction as F
from itertools import combinations

checks = 0

def check(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def lap(m, a, b):
    n = 2*m
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, j in combinations(range(n), 2):
        w = b if (i < m) == (j < m) else a
        out[i][i] += w
        out[j][j] += w
        out[i][j] -= w
        out[j][i] -= w
    return out

def inverse(mat):
    n = len(mat)
    rows = [list(mat[i]) + eye(n)[i] for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j, n) if rows[k][j])
        rows[j], rows[k] = rows[k], rows[j]
        pivot = rows[j][j]
        rows[j] = [v/pivot for v in rows[j]]
        for k in range(n):
            if k == j:
                continue
            factor = rows[k][j]
            rows[k] = [rows[k][p]-factor*rows[j][p] for p in range(2*n)]
    return [row[n:] for row in rows]

def formula(m, a, b):
    return 1/a + F(4*(m-1))/(a+b)

def k_index(m, a, b):
    n = 2*m
    l = lap(m, a, b)
    A = [[l[i][j] + F(1, n) for j in range(n)] for i in range(n)]
    Ai = inverse(A)
    return n*(sum(Ai[i][i] for i in range(n))-1)

def ratio_objective(m, c, r, B=F(1)):
    q = m-1
    a = B/(m*(m+c*q*r))
    b = r*a
    return formula(m, a, b)

def gap(m, c, r, B=F(1)):
    return B*min(F(2), 1+r)/(m+c*(m-1)*r)

def matrix_spectral_checks():
    for m in range(2, 7):
        n = 2*m
        for a in (F(1,3), F(1), F(7,4)):
            for b in (F(0), F(2,3), F(5,2)):
                L = lap(m, a, b)
                sign = [1]*m + [-1]*m
                # Three spectral projectors reconstruct the complete Laplacian.
                for i in range(n):
                    for j in range(n):
                        P0 = F(1, n)
                        Pd = F(sign[i]*sign[j], n)
                        Pi = F(int(i==j)) - P0-Pd
                        rhs = 2*m*a*Pd + m*(a+b)*Pi
                        check(L[i][j] == rhs, 'L spectrum projector identity')
                check(k_index(m, a, b) == formula(m,a,b), 'Kirchhoff trace formula')

def optimality_checks():
    for m in range(2, 10):
        q = m-1
        cr = F(4*m, 4*m-3)
        cm = F(m, q)
        check(F(1) < cr < cm, 'strict threshold order')
        check(cm-cr == F(m,q*(4*m-3)), 'price interval exact width')
        for t in (F(2), F(3), F(4)):
            # Exact rational critical point r=t-1 for price c below cr.
            c = F(4*m)/(t*t+4*q)
            r0 = t-1
            check(c < cr, 'subcritical price')
            def numerator(r):
                return c*(1+r)*(1+r)-4*(m-c*q)
            check(numerator(r0)==0, 'stationarity')
            for r in (F(0), F(1,3), F(1,2), F(1), F(2), F(4), F(8)):
                check(ratio_objective(m,c,r)>=ratio_objective(m,c,r0), 'resistance global scalar min')
        for c in (cr,cr+F(1,17),cm,cm+F(1,5),F(7)):
            if c < cr:
                continue
            for r in (F(0),F(1,5),F(1),F(3),F(9)):
                check(ratio_objective(m,c,r)>=ratio_objective(m,c,F(0)), 'resistance zero-support phase')
        for c in (F(1,3),F(1),F(3,2),cr, (cr+cm)/2, cm, cm+F(1,3),F(7)):
            rgap = F(1) if c<cm else F(0)
            for r in (F(0),F(1,8),F(1,2),F(1),F(3,2),F(3),F(20)):
                check(gap(m,c,r)<=gap(m,c,rgap), 'spectral scalar max')
        # Opposite support decisions at a rational interior price.
        c = (cr+cm)/2
        check(c>=cr and c<cm, 'opposition interval')
        check(ratio_objective(m,c,F(0))<ratio_objective(m,c,F(1)), 'resistance discards')
        check(gap(m,c,F(1))>gap(m,c,F(0)), 'mixing retains')

def edge_kkt_checks():
    for m in range(2,7):
        cr = F(4*m,4*m-3)
        for c,r in ((F(1),F(1)),(cr,F(0)),(cr+F(1,4),F(0))):
            q=m-1
            a=1/(m*(m+c*q*r));b=r*a
            n=2*m
            sign=[1]*m+[-1]*m
            # L+ inverse restricted to mean-zero space: exact pseudoinverse.
            P = [[F(sign[i]*sign[j],n)/(2*m*a)
                  +(F(int(i==j))-F(1,n)-F(sign[i]*sign[j],n))/(m*(a+b))
                  for j in range(n)] for i in range(n)]
            grad = {}
            for i,j in combinations(range(n),2):
                d= -n*sum((P[k][i]-P[k][j])**2 for k in range(n))
                group='inner' if (i<m)==(j<m) else 'cross'
                if group not in grad: grad[group]=d
                check(grad[group]==d,'orbitwise derivative equality')
            multiplier = -grad['cross']
            check(grad['cross']+multiplier==0,'active cross KKT')
            residual=grad['inner']+c*multiplier
            check(residual>=0 if r==0 else residual==0,'inner KKT inequality/equality')

if __name__=='__main__':
    matrix_spectral_checks()
    optimality_checks()
    edge_kkt_checks()
    print('VERIFY_OK',checks)
