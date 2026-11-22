"""Finite diagnostic checks for the swapped-axis ellipse-gauge theorem.

The proof for all real parameters is mathematical, not inferred from sampling.
"""
from fractions import Fraction
from math import hypot, sqrt, isclose
from random import Random


def q(v, a, b):
    x, y = v
    return min(hypot(x / a, y / b), hypot(x / b, y / a))


def pc(v, a, b):
    M, m = sorted((abs(v[0]), abs(v[1])), reverse=True)
    if a == b or m <= (b*b/(a*a))*M:
        return hypot(M/a, m/b)
    return (M+m)/sqrt(a*a+b*b)


def q2_fraction(v, a, b):
    x, y = v
    return min(x*x/(a*a)+y*y/(b*b), x*x/(b*b)+y*y/(a*a))


def check():
    counter = 0
    # Exact-rational witnesses from Pythagorean triples.
    for a0,b0,L0 in [(5,12,13),(8,15,17),(7,24,25),(20,21,29)]:
        a,b,L = map(Fraction,(max(a0,b0),min(a0,b0),L0))
        e=(a*a/L,b*b/L); f=(b*b/L,a*a/L)
        m=((e[0]+f[0])/2,(e[1]+f[1])/2)
        K=(a*a+b*b)/(2*a*b)
        assert q2_fraction(e,a,b)==1
        assert q2_fraction(f,a,b)==1
        assert q2_fraction(m,a,b)==K*K
        counter+=3
        for sg1 in (-1,1):
            for sg2 in (-1,1):
                ee=(sg1*e[0],sg2*e[1]);ff=(sg1*f[0],sg2*f[1])
                mm=((ee[0]+ff[0])/2,(ee[1]+ff[1])/2)
                assert q2_fraction(mm,a,b)==K*K
                counter+=1

    # Deterministic finite stress tests; never a substitute for the proof.
    rng=Random(20261120)
    for a,b in [(1.0,1.0),(1.01,1.0),(1.1,1.0),(1.5,1.0),
                (2.0,1.0),(3.0,1.0),(5.0,2.0),(10.0,1.0)]:
        K=(a*a+b*b)/(2*a*b)
        L=sqrt(a*a+b*b)
        e=(a*a/L,b*b/L);f=(b*b/L,a*a/L)
        assert isclose(q(e,a,b),1.0,abs_tol=1e-12)
        assert isclose(q(f,a,b),1.0,abs_tol=1e-12)
        assert isclose(q(((e[0]+f[0])/2,(e[1]+f[1])/2),a,b),K,abs_tol=1e-12)
        counter+=3
        for _ in range(7000):
            x=(rng.randint(-100,100)/37,rng.randint(-100,100)/37)
            y=(rng.randint(-100,100)/41,rng.randint(-100,100)/41)
            lhs=q((x[0]+y[0],x[1]+y[1]),a,b)
            rhs=K*(q(x,a,b)+q(y,a,b))
            assert lhs <= rhs+1e-10, (a,b,x,y,lhs,rhs)
            counter+=1
            p_sum=pc((x[0]+y[0],x[1]+y[1]),a,b)
            p_x=pc(x,a,b);p_y=pc(y,a,b)
            assert p_sum<=p_x+p_y+1e-10
            assert p_sum<=lhs+1e-10
            assert lhs<=K*p_sum+1e-10
            counter+=3
        # Contact segments: no sampled point beats the asserted midpoint.
        for j in range(401):
            t=j/400
            z=(t*e[0]+(1-t)*f[0],t*e[1]+(1-t)*f[1])
            assert q(z,a,b)<=K+1e-12
            counter+=1
    print(f"ELLIPSE_GAUGE_DIAGNOSTIC_OK {counter}")


if __name__=='__main__':
    check()
