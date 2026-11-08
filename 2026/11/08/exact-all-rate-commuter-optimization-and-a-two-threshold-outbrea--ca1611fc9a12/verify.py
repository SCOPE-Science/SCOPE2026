"""Exact consistency checks for a two-patch SIR commuter threshold.

Uses only Python's standard library. These checks are not substitutes for
proof of the universal derivative-sign statements in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def source_q(N1, N2, x, y, l1, m1, l2, m2, gamma, R1, R2):
    # Original six-group residence balances and two-patch reproduction matrix.
    H1, H2 = l1 + m1, l2 + m2
    N11, N12 = m1*x/H1, l1*x/H1
    N22, N21 = m2*y/H2, l2*y/H2
    N1r, N2r = N1-x, N2-y
    P1, P2 = N1r+N11+N21, N2r+N22+N12
    q11 = R1*(N1r/P1 + N11*(gamma+m1)/(P1*(gamma+H1))
                + N21*(gamma+l2)/(P1*(gamma+H2)))
    q22 = R2*(N2r/P2 + N22*(gamma+m2)/(P2*(gamma+H2))
                + N12*(gamma+l1)/(P2*(gamma+H1)))
    q21 = R1*(N11*l1/(P1*(gamma+H1)) + N21*m2/(P1*(gamma+H2)))
    q12 = R2*(N12*m1/(P2*(gamma+H1)) + N22*l2/(P2*(gamma+H2)))
    return q11,q12,q21,q22


def reduced_q(N1, N2, x, y, l1, m1, l2, m2, gamma, R1, R2):
    e1,e2=l1/(l1+m1),l2/(l2+m2)
    k1=l1*m1/((l1+m1)*(gamma+l1+m1))
    k2=l2*m2/((l2+m2)*(gamma+l2+m2))
    S=k1*x+k2*y
    P1=N1-e1*x+e2*y
    P2=N2+e1*x-e2*y
    u,v=S/P1,S/P2
    return (R1*(1-u), R2*v, R1*u, R2*(1-v)), (S,P1,P2,u,v)


def char_at_one(q):
    q11,q12,q21,q22=q
    return (1-q11)*(1-q22)-q12*q21


def leading(q):
    q11,q12,q21,q22=map(float,q)
    return (q11+q22+sqrt((q11-q22)**2+4*q12*q21))/2


W=dict(N1=F(2), N2=F(1), l1=F(2), m1=F(2),
       l2=F(1,2), m2=F(1,2), gamma=F(2),
       R1=F(3,4), R2=F(6,5))


def test_witness():
    for x,expected in [(F(0),-F(1,200)), (F(3,4),F(4,595)),
                       (F(2),-F(1,120))]:
        qs=source_q(x=x,y=F(1),**W)
        qr,(S,P1,P2,u,v)=reduced_q(x=x,y=F(1),**W)
        assert qs==qr
        assert char_at_one(qs)==expected, (x,char_at_one(qs),expected)
        assert (leading(qs)<1)==(expected>0)
    # Denominator-cleared determinant is a degree-two polynomial.
    # At three rational arguments, it agrees with -(4*x*x-7*x+1)/160.
    # The degree bound comes from affine S, P1, P2; see RESULT.md.
    for x in (F(0),F(1),F(2)):
        q,(S,P1,P2,u,v)=reduced_q(x=x,y=F(1),**W)
        assert char_at_one(q)*P1*P2==-(4*x*x-7*x+1)/160
    rlow=(7-sqrt(33))/8
    rhigh=(7+sqrt(33))/8
    assert 0<rlow<.75<rhigh<2
    print('EXACT_WITNESS_OK')


def test_formula_and_signs():
    rng=Random(20261107)
    vals=[F(1,4),F(1,2),F(1),F(2),F(3),F(5),F(8)]
    for j in range(200):
        N1,N2=rng.choice(vals),rng.choice(vals)
        l1,m1,l2,m2,gamma=[rng.choice(vals) for _ in range(5)]
        R1,R2=F(1,2),F(3,2)
        # Fractions of each population are within the physical domain.
        f1=N1*F(rng.randrange(1,8),8)
        f2=N2*F(rng.randrange(1,8),8)
        inp=dict(N1=N1,N2=N2,l1=l1,m1=m1,l2=l2,m2=m2,
                 gamma=gamma,R1=R1,R2=R2)
        qs=source_q(x=f1,y=f2,**inp)
        qr,(S,P1,P2,u,v)=reduced_q(x=f1,y=f2,**inp)
        assert qs==qr
        assert P1>0 and P2>0 and S>0
        assert R1<leading(qr)<R2
        e1,e2=l1/(l1+m1),l2/(l2+m2)
        k1=l1*m1/((l1+m1)*(gamma+l1+m1))
        k2=l2*m2/((l2+m2)*(gamma+l2+m2))
        vy=(k2*P2+e2*S)/P2**2
        uy=(k2*P1-e2*S)/P1**2
        ux=(k1*P1+e1*S)/P1**2
        assert vy>0 and ux>0
        assert u*vy-v*uy==u*v*e2*(1/P1+1/P2)>0
        tiny=N2*F(1,4096)
        assert leading(reduced_q(x=f1,y=f2+tiny,**inp)[0])<leading(qr)
    print('RATIONAL_IDENTITIES_AND_NUMERICAL_STRESS_OK',200)


if __name__=='__main__':
    test_witness()
    test_formula_and_signs()
    print('VERIFY_OK')
