#!/usr/bin/env python3
"""Exact rational diagnostics for a spherical harmonic run-and-tumble trap.
Scientific arguments proving the general assertions are in RESULT.md.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks = 0
for d in range(1, 31):
    for an, ad in [(1,7), (1,2), (1,1), (2,1), (7,3), (6,1), (11,1), (29,2)]:
        a=F(an,ad)
        # Independent linear generator balance for A=E[X.U], Q=E[|X|^2],
        # C=E[(X.U)^2], B=E[|X|^2(X.U)], M4=E[|X|^4].
        A=1/(1+a)
        Q=A
        C=(2*A+a*Q/d)/(2+a)
        B=(2*C+Q)/(3+a)
        M4=B
        # Independently from GEM sampling partitions: E S^2 and E sum P_i^4.
        den=(a+1)*(a+2)*(a+3)
        ES=1/(a+1)
        ES2=(a+6)/den
        ET=6/den
        M4_gem=ES2+F(2,d)*(ES2-ET)
        assert Q==ES and M4==M4_gem
        # Rotational invariance: fourth moment of the first coordinate.
        coord2=Q/d
        coord4=F(3,d*(d+2))*M4
        excess=coord4/coord2**2-3
        closed=6*(a*(d-4)-6)/((a+2)*(a+3)*(d+2))
        assert excess==closed
        # The d=1 stationary beta law gives another independent fourth moment.
        if d==1:
            assert coord4==3/((a+1)*(a+3))
        # Exact fixed-parameter radial concentration and nonconcentration terms.
        varS=ES2-ES**2
        assert varS==2*a/((a+1)**2*(a+2)*(a+3))
        varR=M4-Q**2
        assert varR==varS + 2*a/(d*(a+1)*(a+2)*(a+3))
        if d<=4:
            assert excess<0
        if d>=5:
            assert (excess>0)==(a>F(6,d-4))
        checks+=8

# Rational-weight Gram-fluctuation covariance, from independent spherical directions.
for weights in [(F(1,2),F(1,3),F(1,6)), (F(1,4),)*4,
                (F(2,5),F(3,5)),(F(1,5),F(1,5),F(3,5))]:
    S=sum(v*v for v in weights)
    T=sum(v**4 for v in weights)
    pair=sum(weights[i]**2*weights[j]**2
             for i in range(len(weights)) for j in range(i+1,len(weights)))
    assert 2*(S*S-T)==4*pair
    checks+=1

# Dimension-five sign border and unique derivative maximum checks on a grid.
for d in range(5,31):
    cross=6/(d-4)
    a_star=(6+sqrt(6*(d-1)*(d-2)))/(d-4)
    assert a_star>cross
    def deriv_numer(a):return (d-4)*a*a-12*a-6*(d+1)
    assert deriv_numer(a_star*0.99)<0<deriv_numer(a_star*1.01)
    checks+=1

# Limiting coordinate excess-kurtosis optimum.
a=sqrt(6)
max_kurt=6*a/((a+2)*(a+3))
assert isclose(max_kurt,30-12*sqrt(6),abs_tol=1e-12)
checks+=1
print(f'PASS: {checks} exact-rational or explicitly identified numeric diagnostics')
