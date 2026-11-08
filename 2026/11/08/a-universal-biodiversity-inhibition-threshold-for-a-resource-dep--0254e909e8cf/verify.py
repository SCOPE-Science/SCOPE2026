#!/usr/bin/env python3
"""Finite-state rational verification of a basal-resource/specialist-guild model.

No network access or third-party dependencies. Run: python3 verify.py
"""
from fractions import Fraction as F
from math import pi, sqrt


def solve(A, b):
    """Exact Gaussian elimination with pivoting for rational matrices."""
    n = len(b)
    M = [[F(x) for x in A[i]] + [F(b[i])] for i in range(n)]
    for j in range(n):
        k = next(i for i in range(j, n) if M[i][j])
        M[j], M[k] = M[k], M[j]
        pivot = M[j][j]
        M[j] = [x / pivot for x in M[j]]
        for i in range(n):
            if i != j:
                h = M[i][j]
                if h:
                    M[i] = [x - h*y for x, y in zip(M[i], M[j])]
    return [r[-1] for r in M]


def direct_stationary(m, c, e, u, v, k):
    # States: 0 is resource absent, 1+j is resource present with j consumers.
    n = m+2
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    Q[0][1] = c
    for j in range(m+1):
        z = 1+j
        Q[z][0] = e+k*j
        if j < m: Q[z][z+1] = (m-j)*u
        if j > 0: Q[z][z-1] = j*v
    for i in range(n):
        Q[i][i] = -sum(Q[i])
    A = [[Q[i][j] for i in range(n)] for j in range(n)]
    A[-1] = [F(1)]*n
    b = [F(0)]*(n-1)+[F(1)]
    pi_vec = solve(A, b)
    assert all(p >= 0 for p in pi_vec) and sum(pi_vec) == 1
    p = sum(pi_vec[1:]); q = sum(j*pi_vec[j+1] for j in range(m+1))
    return p, q


def independent_renewal(m, c, e, u, v, k):
    # Exact resolvent of the no-catastrophe count process killed at e+k*j.
    B = [[F(0) for _ in range(m+1)] for _ in range(m+1)]
    for j in range(m+1):
        birth = (m-j)*u; death = j*v
        B[j][j] = e+k*j+birth+death
        if j < m: B[j][j+1] = -birth
        if j > 0: B[j][j-1] = -death
    L = solve(B, [F(1)]*(m+1))[0]
    p = c*L/(1+c*L)
    q = c*(1-e*L)/(k*(1+c*L))
    return L,p,q


def float_L(m,c,e,u,v,k):
    # Independent numerical tridiagonal resolvent for large m, O(m).
    a=[0.0]*(m+1);b=[0.0]*(m+1);d=[0.0]*(m+1)
    for j in range(m+1):
        a[j]=-j*v;d[j]=-(m-j)*u
        b[j]=e+k*j+(m-j)*u+j*v
    cc=[0.0]*(m+1);yy=[0.0]*(m+1)
    cc[0]=d[0]/b[0];yy[0]=1/b[0]
    for j in range(1,m+1):
        den=b[j]-a[j]*cc[j-1]
        cc[j]=d[j]/den;yy[j]=(1-a[j]*yy[j-1])/den
    for j in range(m-1,-1,-1):
        yy[j]-=cc[j]*yy[j+1]
    return yy[0]


def main():
    trials=0; order_checks=0
    cases=[(F(3,2),F(5,4),F(2,3),F(7,5),F(k)) for k in (F(1,2),F(11,4),F(4))]
    cases += [(F(1),F(2),F(5,3),F(1,4),F(3)),
              (F(5,4),F(1,3),F(4,5),F(11,7),F(7,3)),
              (F(3,7),F(8,5),F(9,4),F(2,7),F(13,6))]
    for c,e,u,v,k in cases:
        prev_q=prev_L=None
        prev_S=None
        for m in range(11):
            p1,q1=direct_stationary(m,c,e,u,v,k)
            L,p2,q2=independent_renewal(m,c,e,u,v,k)
            assert (p1,q1)==(p2,q2)
            assert (c+e)*p1+k*q1==c
            S=p1+q1
            assert S-c/(c+e)==(1-k/(c+e))*q1
            assert S-c/k==c*(k-c-e)*L/(k*(1+c*L))
            if m:
                assert L < prev_L and q1 > prev_q
                assert (S-prev_S)*(c+e-k)>=0
                if k!=c+e: assert (S-prev_S)*(c+e-k)>0
                order_checks+=1
            prev_L,prev_q,prev_S=L,q1,S
            trials+=1
        assert k!=c+e or all(direct_stationary(m,c,e,u,v,k)[0]+direct_stationary(m,c,e,u,v,k)[1]==c/(c+e) for m in range(4))
    c=e=u=v=k=1.0
    expected=sqrt(pi/(2*k*u))
    ratios=[]
    for m in [100,400,1600]:
        L=float_L(m,c,e,u,v,k)
        ratio=L*sqrt(m)/expected
        ratios.append(ratio)
        assert 0.7 < ratio < 1.1
    assert ratios[0] < ratios[1] < ratios[2] < 1.0
    print('PASS:',trials,'exact stationary/renewal comparisons;',order_checks,'strict monotonicity comparisons')
    print('large-guild L_m*sqrt(m)/sqrt(pi/(2*k*u)):', [(m,round(x,8)) for m,x in zip((100,400,1600),ratios)])

if __name__=='__main__': main()
