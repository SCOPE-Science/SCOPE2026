"""Exact finite diagnostics for the degree-two analytic ellipse kernel.
Run with: python3 CHECK.py
Requires only the Python standard library.
The all-parameter classification follows from the algebraic proof in RESULT.md;
finite diagnostics here do not constitute an infinite certificate.
"""
from fractions import Fraction as Q
from math import sqrt

COUNT = 0

def verify(statement, description):
    global COUNT
    if not statement:
        raise AssertionError(description)
    COUNT += 1


def parameters(s, R, c2=Q(1)):
    s, R, c2 = map(Q, (s, R, c2))
    assert s > 1 and R > 1 and c2 > 0
    D = 2*s*R*R - 1
    P = D - 2*(s+1)*R
    A = 2*s*P/(c2*R*D)
    B = 2*s/c2*(1/R+2*(s+1)/D)
    C = 4*s*s*(s+1)/(c2*c2*D)
    K0 = 1+(s+1)/D
    return D, P, A, B, C, K0


def test_case(s, R, c2):
    s, R, c2 = map(Q, (s, R, c2))
    D,P,A,B,C,K0 = parameters(s,R,c2)
    a2 = c2*(R+1)/2
    b2 = c2*(R-1)/2
    mean_z2 = c2/(2*s)
    var_z = c2*R/(2*s)
    Ez4 = (3*a2*a2+2*a2*b2+3*b2*b2)/(4*s*(s+1))
    var_z2 = Ez4 - mean_z2*mean_z2
    verify(var_z2 == c2*c2*D/(4*s*s*(s+1)), 'degree-two norm')
    verify(var_z > 0 and var_z2 > 0, 'positive Gram norms')
    verify(B-A == 8*s*(s+1)/(c2*D), 'strict angular cost')
    verify((A>0)-(A<0) == (P>0)-(P<0), 'critical sign')
    x0sq = max(Q(0), -A/(2*C))
    lower = K0-A*A/(4*C) if P<0 else K0
    verify(x0sq < a2, 'stationary points inside ellipse')
    for x in [Q(0),Q(1,13),Q(3,10),Q(-1,4),Q(7,11)]:
        for y in [Q(0),Q(1,11),Q(-2,7),Q(4,9)]:
            r2=x*x+y*y
            K=1+r2/var_z+((x*x-y*y-mean_z2)**2+4*x*x*y*y)/var_z2
            expanded=K0+A*x*x+B*y*y+C*r2*r2
            verify(K==expanded, 'moment kernel vs quartic expansion')
            if P<0:
                gap=C*(r2-x0sq)**2+(B-A)*y*y
            else:
                gap=A*x*x+B*y*y+C*r2*r2
            verify(K-lower==gap and gap>=0, 'sharp sum of squares')
    if P<0:
        verify(lower<K0 and x0sq>0, 'two off-center minima')
    else:
        verify(lower==K0 and x0sq==0, 'center minimum')


for s in [Q(21,20),Q(3,2),Q(2),Q(8,3),Q(3),Q(7),Q(15)]:
    for R in [Q(11,10),Q(6,5),Q(3,2),Q(2),Q(3),Q(10)]:
        test_case(s,R,Q(1))
        test_case(s,R,Q(9,4))

# A boundary configuration with rational weight and ellipse eccentricity.
D,P,A,B,C,K0=parameters(Q(8,3),Q(3,2))
verify(P==A==0 and B>0 and C>0, 'exact fourth-order critical flatness')

# Analytic threshold and numerical check, not evidence for uniqueness.
s=2
R_star=(s+1+sqrt((s+1)**2+2*s))/(2*s)
rho_star=sqrt((R_star-1)/(R_star+1))
verify(abs(R_star-1.6513878188659974)<1e-14, 'unweighted R threshold')
verify(abs(rho_star-0.4956592188330808)<1e-14, 'unweighted aspect threshold')
print(f'PASS: {COUNT} exact arithmetic and endpoint checks')
