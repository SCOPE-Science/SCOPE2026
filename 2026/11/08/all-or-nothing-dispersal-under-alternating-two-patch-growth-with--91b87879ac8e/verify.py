#!/usr/bin/env python3
"""Exact finite checks of a two-season two-patch migration formula.

No external packages are needed. This tests identities on a reproducible
rational grid; the accompanying analytical proof covers all real parameters.
"""
from fractions import Fraction as F
from math import sqrt


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def matrices(a, b, h, p):
    M = [[1-p, h*p], [h*p, 1-p]]
    D0 = [[a, F(0)], [F(0), b]]
    D1 = [[b, F(0)], [F(0), a]]
    J = [[F(0), F(1)], [F(1), F(0)]]
    return M, D0, D1, J


def check(a, b, h, p):
    M, D0, D1, J = matrices(a, b, h, p)
    P = mm(mm(mm(M, D1), M), D0)
    N = mm(mm(J, M), D0)
    assert P == mm(N, N)
    tr = N[0][0]+N[1][1]
    det = N[0][0]*N[1][1]-N[0][1]*N[1][0]
    assert tr == h*p*(a+b)
    assert det == a*b*(h*h*p*p-(1-p)**2)
    disc = tr*tr-4*det
    assert disc == h*h*p*p*(a-b)**2 + 4*a*b*(1-p)**2
    lam = (float(tr)+sqrt(float(disc)))/2
    assert abs((lam*lam-float(tr)*lam+float(det))) < 1e-9*max(1.,lam**2)
    # The two-step Perron eigenvalue is the square of the one-step rate.
    trP = float(P[0][0]+P[1][1])
    detP = float(P[0][0]*P[1][1]-P[0][1]*P[1][0])
    rhoP = (trP+sqrt(max(0.,trP*trP-4*detP)))/2
    assert abs(rhoP-lam*lam) < 1e-8*max(1.,rhoP)
    return 7


def main():
    count=0
    vals=[F(1,8),F(1,4),F(1,2),F(3,4),F(1),F(2),F(4)]
    surv=[F(1,10),F(3,10),F(1,2),F(1)]
    ps=[F(0),F(1,9),F(1,3),F(1,2),F(4,5),F(1)]
    for a in vals:
        for b in vals:
            if a <= b:continue
            for h in surv:
                for p in ps:
                    count+=check(a,b,h,p)
                # Strict convexity is a theorem; these rational-grid chords
                # give an additional independent diagnostic.
                def gamma(p):
                    return (float(h*p*(a+b))+
                            sqrt(float(h*h*p*p*(a-b)**2 + 4*a*b*(1-p)**2)))/2
                for p in ps[1:-1]:
                    assert gamma(p) < (1-float(p))*gamma(F(0))+float(p)*gamma(F(1)) + 1e-12
                    count+=1
    a,b,h=F(4),F(1,8),F(3,10)
    assert float(h*a)>1>sqrt(float(a*b))
    assert float(h*(a+b))<2*sqrt(float(a*b))
    pcrit=(-95+sqrt(154625))/364
    assert 0<pcrit<1
    def g(p):return (float(h*(a+b))*p+sqrt(float(h*h*(a-b)**2)*p*p+4*float(a*b)*(1-p)**2))/2
    assert abs(g(pcrit)-1)<1e-12
    assert g(.5)<1 and g(.9)>1
    count+=6
    print(f'PASS: {count} exact identities / numerical diagnostics on rational cases')
    print(f'Example persistence crossover p = {pcrit:.12f}')

if __name__=='__main__':main()
