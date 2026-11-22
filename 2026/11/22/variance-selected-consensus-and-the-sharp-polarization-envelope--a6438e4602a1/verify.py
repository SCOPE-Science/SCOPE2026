"""Reproduce algebraic and numerical tests for the neutral fast-assortative model.

Use Python 3.10+ standard library only. Numerical integration supplements,
not replaces, the analytic convergence proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def exact_moments(xs):
    n = len(xs)
    m = sum(xs, F(0))/n
    q = sum((x*x for x in xs), F(0))/n
    v = q - m*m
    if m == 0:
        assert all(x == 0 for x in xs) and q == 0 and v == 0
        return m, q, v
    velocities = [(q-x*x)/(2*(x+m)) for x in xs]
    mdot = sum(velocities, F(0))/n
    qdot = sum((2*x*z for x,z in zip(xs,velocities)), F(0))/n
    g = sum((1/(x+m) for x in xs), F(0))/n
    assert mdot == v*g/2
    assert qdot == -m*v*g
    assert qdot + 2*m*mdot == 0
    assert qdot - 2*m*mdot == -2*m*v*g
    assert v >= 0
    assert m*m <= q <= m
    return m,q,v


def velocity(xs):
    n=len(xs)
    m=sum(xs)/n
    q=sum(x*x for x in xs)/n
    return [(q-x*x)/(2*(x+m)) for x in xs]


def rk4_step(xs,h):
    a=velocity(xs)
    b=velocity([x+h*z/2 for x,z in zip(xs,a)])
    c=velocity([x+h*z/2 for x,z in zip(xs,b)])
    d=velocity([x+h*z for x,z in zip(xs,c)])
    return [x+h*(u+2*v+2*w+z)/6 for x,u,v,w,z in zip(xs,a,b,c,d)]


def numerical_case(xs,h=0.02,steps=3600):
    m0=sum(xs)/len(xs)
    q0=sum(x*x for x in xs)/len(xs)
    expected=sqrt((q0+m0*m0)/2)
    initial_inv=q0+m0*m0
    for k in range(steps):
        xs=rk4_step(xs,h)
        assert -1e-9 <= min(xs) <= max(xs) <= 1+1e-9
        if (k+1)%100==0:
            m=sum(xs)/len(xs)
            q=sum(x*x for x in xs)/len(xs)
            assert abs(q+m*m-initial_inv) < 2e-9
    m=sum(xs)/len(xs)
    assert abs(m-expected)<1e-7,(m,expected)
    assert max(xs)-min(xs)<3e-7


def main():
    rnd=Random(20261117)
    checks=0
    for n in range(1,15):
        for _ in range(100):
            xs=[F(rnd.randrange(0,13),12) for _ in range(n)]
            exact_moments(xs)
            checks+=1
    numerical_cases=[
        [0.0, 0.5, 1.0],
        [0.0, 0.0, 1.0, 1.0],
        [0.0, 0.2, 0.3, 0.7, 1.0],
        [0.1, 0.15, 0.4, 0.7, 0.95],
        [i/20 for i in range(21)],
        [0.25, 0.25, 0.25, 0.75, 0.75, 0.75],
        [0.5]*5,
        [0.0]*3+[1.0]*7,
    ]
    for xs in numerical_cases:
        numerical_case(xs)
    # Exact illustrations, including the sharp fixed-mean endpoint law.
    assert F(1,3)*(1+F(1,3))/2==F(2,9)
    print(f'PASS: {checks} exact-rational configurations and {len(numerical_cases)} RK4 trajectories')
    print('Uniform [0,1] law: limiting value sqrt(7/24) = %.12f' % sqrt(7/24))

if __name__=='__main__': main()
