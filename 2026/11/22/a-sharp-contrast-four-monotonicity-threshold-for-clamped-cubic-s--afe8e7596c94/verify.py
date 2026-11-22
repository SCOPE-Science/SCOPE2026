"""Exact-rational regression checks for a four-knot clamped cubic interpolant.
The analytic inequalities and minimax proof are given in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product


def hermite_derivative(y0, y1, d0, d1, length, t):
    t = Q(t)
    return ((6*t*t - 6*t)*y0 + (3*t*t-4*t+1)*length*d0
            + (-6*t*t+6*t)*y1 + (3*t*t-2*t)*length*d1) / length


def m_values(h, a, b, c):
    # Solve the two C2 continuity equations with flat endpoints.
    # h denotes both outer intervals; b is the central vertical increment.
    # Symmetry is not assumed for data.
    # Equations: 2(1+h)m1 + h*m2 = 3(a/h + h*b)
    #            h*m1 + 2(1+h)m2 = 3(h*b + c/h).
    A=2*(h+1); det=A*A-h*h
    r1=3*(a/h+h*b); r2=3*(h*b+c/h)
    return ((A*r1-h*r2)/det, (A*r2-h*r1)/det)


def monotonicity_derivative_min(h,a,b,c, sample_n=100):
    m1,m2=m_values(h,a,b,c)
    data=[(Q(0),a,Q(0),m1,h), (a,a+b,m1,m2,Q(1)),
          (a+b,a+b+c,m2,Q(0),h)]
    values=[]
    for y0,y1,d0,d1,L in data:
        for k in range(sample_n+1):
            values.append(hermite_derivative(y0,y1,d0,d1,L,Q(k,sample_n)))
    return min(values)


def main():
    checks=0
    for h in [Q(1,4), Q(1,2), Q(1), Q(2), Q(3)]:
        for a,b,c in product([Q(1),Q(2),Q(4)],repeat=3):
            m1,m2=m_values(h,a,b,c)
            # Both C2 join conditions verified directly.
            assert (4*m1-6*a/h)/h == 6*b-4*m1-2*m2
            assert (2*m1+4*m2-6*b) == (6*c/h-4*m2)/h
            checks+=2
    h=Q(1)
    for a,b,c in product([Q(1),Q(4)],repeat=3):
        assert monotonicity_derivative_min(h,a,b,c,80) >= 0
        checks+=1
    for R in [Q(401,100),Q(9,2),Q(5)]:
        m1,m2=m_values(Q(1),Q(1),R,Q(1))
        ee=m1-3
        tt=ee/(3*(1+ee))
        assert hermite_derivative(Q(0),Q(1),Q(0),m1,Q(1),tt)<0
        m1,m2=m_values(Q(1),R,Q(1),R)
        assert hermite_derivative(R,R+1,m1,m2,Q(1),Q(1,2))<0
        checks+=2
    for h in [Q(1,4),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(2)]:
        lower=h*h/(3*h+1); upper=2*h*(h+1)
        m=3*(lower/h+h)/(3*h+2)
        assert m==3*lower/h
        m=3*(upper/h+h)/(3*h+2)
        assert m==3
        assert min(upper,(3*h+1)/(h*h))<=4
        assert (min(upper,(3*h+1)/(h*h))==4)==(h==1)
        checks+=4
    # Exact middle and end-pocket formulas at rational witness points.
    for eps in [Q(1,1000),Q(1,100),Q(1,20),Q(1,10)]:
        r=Q(1,4)-eps
        q=3*(r+1)/(5*r)
        ee=q-3
        t=2*ee/(3*(1+ee))
        left=r*(-ee*t*t+(1+ee)*t*t*t)
        assert left == -4*r*ee**3/(27*(1+ee)**2)
        checks+=1
    print(f'PASS: {checks} exact symbolic-identity/endpoint/witness checks; finite derivative sampling supplements the proof')

if __name__=='__main__':
    main()
