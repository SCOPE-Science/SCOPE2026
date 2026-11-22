"""Reproducible arithmetic checks for a cubic plane-map inverse theorem.

All universal statements require the accompanying analytic proof; tests are finite.
Python 3 standard library only.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt

rng=Random(730461)
checks=0
for k in range(2400):
    u=Q(rng.randint(-9,9),rng.randint(1,9))
    b=Q(rng.randint(-9,9),rng.randint(1,9))
    w=Q(rng.randint(-9,9),rng.randint(1,9))
    x=Q(rng.randint(-9,9),rng.randint(1,9))
    p=u*u*x*x*x+(b-3*u*u)*x-w
    dp=3*u*u*x*x+b-3*u*u
    # The prescribed Jacobian has determinant -dp.
    assert dp == b+3*u*u*(x*x-1)
    # Cubic discriminant from polynomial coefficients.
    disc=u*u*(4*(3*u*u-b)**3-27*u*u*w*w)
    direct=-(4*u*u*(b-3*u*u)**3+27*u**4*w*w)
    assert disc == direct
    if u and 3*u*u>b:
        h=1-b/(3*u*u)
        # Cusp/fold height squared, keeping all data rational.
        e2=4*u**4*h**3
        assert (disc>0)==(w*w<e2)
        assert (disc==0)==(w*w==e2)
    elif u:
        assert disc <= 0
    # A rational critical point: choose b from u and x to force dp=0.
    if u:
        bc=3*u*u*(1-x*x)
        Pc=u*u*x**3+(bc-3*u*u)*x
        assert Pc==-2*u*u*x**3
    checks+=1

# Repeated-root and triple-root boundary examples.
for u in [Q(1,3),Q(-1,3),Q(2,5)]:
    b=3*u*u
    assert 3*u*u-b==0
    assert u*u*0**3+(b-3*u*u)*0==0
    # Fold x = 1/2 has a double root and x=-1 a simple root.
    b=3*u*u*Q(3,4)
    w=-u*u*Q(1,4)
    p=lambda x:u*u*x**3+(b-3*u*u)*x-w
    dp=lambda x:3*u*u*x*x+b-3*u*u
    assert p(Q(1,2))==dp(Q(1,2))==p(Q(-1))==0
    assert dp(Q(-1))!=0

# Three exact roots at a negative-b target: as u decreases two diverge.
for u in [Q(1,2),Q(1,4),Q(1,8),Q(1,16)]:
    b=-u*u
    p=lambda x:u*u*x**3+(b-3*u*u)*x
    assert all(p(x)==0 for x in (Q(-2),Q(0),Q(2)))

# Uniform compact-target asymptotic of the two escaping branches via Newton.
for b in [-0.5,-1.25,-3.0]:
    for w in [-2.0,0.0,2.0]:
        for u in [1e-3,1e-4]:
            for sign in [-1,1]:
                x=sign*sqrt(-b)/u+w/(-2*b)
                for j in range(9):
                    fun=u*u*x**3+(b-3*u*u)*x-w
                    der=3*u*u*x*x+b-3*u*u
                    x-=fun/der
                assert abs(x-(sign*sqrt(-b)/u+w/(-2*b))) < 10.0*u*(1+w*w)*(1+abs(b))
print(f"PASS: {checks} exact-rational discriminant, derivative and fold cases; boundary roots and compact-target inverse-escape asymptotics")
