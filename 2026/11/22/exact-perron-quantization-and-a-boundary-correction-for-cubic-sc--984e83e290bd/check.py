"""Reproduce the exact cubic Greville collocation rows and Perron root.
Python 3 standard library only; run: python check.py
"""
from fractions import Fraction as Q
from math import atan, cos, pi, sin


def bspline(j, p, x, knots):
    if p == 0:
        return Q(int(knots[j] <= x < knots[j + 1]))
    left = Q(0) if knots[j+p] == knots[j] else ((x-knots[j]) / (knots[j+p]-knots[j])) * bspline(j, p-1, x, knots)
    right = Q(0) if knots[j+p+1] == knots[j+1] else ((knots[j+p+1]-x) / (knots[j+p+1]-knots[j+1])) * bspline(j+1, p-1, x, knots)
    return left + right


def collocation(n):
    assert n >= 6
    knots = [Q(0)] * 4 + [Q(i) for i in range(1, n)] + [Q(n)] * 4
    greville = [sum(knots[i+1:i+4])/3 for i in range(n+3)]
    return [[bspline(j, 3, greville[i], knots) for j in range(1,n+2)] for i in range(1,n+2)]


def theta(n):
    assert n >= 6
    def residual(th):
        c = cos(th)
        g = (9*c*c + 7*c - 4) / (3*(3*c+1))
        delta = atan(sin(th) / g)
        return (n - 2)*th + 2*delta - pi
    low,high = 0., pi/(n-2)
    for _ in range(75):
        m=(low+high)/2
        if residual(m)<0:low=m
        else:high=m
    return (low+high)/2


def check_one(n):
    A=collocation(n)
    z=Q(0)
    expect1={0:Q(61,108),1:Q(43,324),2:Q(1,162)}
    expect2={0:Q(1,4),1:Q(7,12),2:Q(1,6)}
    for i,expected in [(0,expect1),(1,expect2)]:
        assert all(A[i][j]==expected.get(j,z) for j in range(n+1))
    for i in range(2,n-1):
        assert all(A[i][j]==({i-1:Q(1,6),i:Q(2,3),i+1:Q(1,6)}.get(j,z)) for j in range(n+1))
    for i in range(n+1):
        for j in range(n+1):
            assert A[i][j] == A[n-i][n-j]
        assert A[i][i] > 0
    th=theta(n)
    lam=(2+cos(th))/3
    v=[0.]*(n+2)
    for i in range(2,n+1):
        v[i]=cos((i-(n+2)/2)*th)
    h=(lam+3)/(3*(9*lam-5))
    v[1]=h*v[2];v[n+1]=h*v[n]
    assert min(v[1:])>0
    max_res=max(abs(sum(float(A[i-1][j-1])*v[j] for j in range(1,n+2))-lam*v[i]) for i in range(1,n+2))
    assert max_res<6e-13,(n,max_res)
    return lam,max_res


def main():
    checks=0
    for n in range(6,29):
        lam,res=check_one(n)
        checks+=1
        if n in (6,8,12,20,28): print(f'n={n:2d}  Perron={lam:.15f}  max_residual={res:.2g}')
    for n in (40,60,100,200):
        th=theta(n)
        gap=(1-cos(th))/3
        expansion=pi*pi/(6*n*n)-pi**4/(72*n**4)-pi**4/(9*n**5)
        # Finite-n remainder is O(n^-6); the bound below is a numerical diagnostic, not a proof.
        assert abs(gap-expansion)<(200/n**6), (n,gap,expansion)
        checks+=1
    print('PASS:',checks,'independent n-specific matrix/quantization and asymptotic diagnostics')

if __name__=='__main__': main()
