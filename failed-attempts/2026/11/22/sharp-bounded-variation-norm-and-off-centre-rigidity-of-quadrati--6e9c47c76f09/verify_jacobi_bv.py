#!/usr/bin/env python3
"""Standalone checks for the quadratic symmetric Jacobi BV norm theorem.
Uses only the Python 3 standard library; finite checks complement the proof."""
from fractions import Fraction as F
from math import comb, sqrt, exp, lgamma, pi
from random import Random


def beta_half(p):
    return exp(lgamma(0.5)+lgamma(p)-lgamma(p+0.5))


def roots(p):
    c = 2*p+3
    b = c*c-c+4
    d = b*b-4*(c-2)*c*c
    return ((b-sqrt(d))/(2*(c-2)*c*c), (b+sqrt(d))/(2*(c-2)*c*c))


def A(p, a):
    return (2*p+1)/(2*p*beta_half(p))*(1-a*a)**p


def step_gain(p,a):
    c = 2*p+3
    t = abs(c*a)
    return A(p,a)*(2 if t <= 1 else t+1/t)


def sharp(p):
    u0,u1=roots(p)
    return step_gain(p,sqrt(u1))


def exact_integer_beta(p):
    return sum(((-1)**k)*F(2*comb(p-1,k),2*k+1) for k in range(p))


def exact_integral_monomial(k,a):
    return (F(1,1)-a**(k+1))/F(k+1)


def exact_weighted_moment(p,k,a):
    return sum((-1)**j*comb(p-1,j)*exact_integral_monomial(k+2*j,a) for j in range(p)) / exact_integer_beta(p)


def simpson_abs_affine(A_, B_, steps=40000):
    h=2.0/steps
    s=abs(A_-B_)+abs(A_+B_)
    for j in range(1,steps):
        t=-1+j*h
        s+=(4 if j%2 else 2)*abs(A_+B_*t)
    return s*h/3


def run():
    rng=Random(547401)
    # Separate exact rational moment computation proves the local derivative coefficients.
    for p in range(1,9):
        for aa in [F(-3,4),F(-1,3),F(1,5),F(2,3)]:
            v=F(1,2*p+1)
            v2=F(4*p,(2*p+1)**2*(2*p+3))
            m1=exact_weighted_moment(p,1,aa)
            m2=exact_weighted_moment(p,2,aa)-v*exact_weighted_moment(p,0,aa)
            alpha=m1/v
            beta=2*m2/v2
            expected=(F(2*p+1,2*p*1)* (1-aa*aa)**p)/exact_integer_beta(p)
            assert alpha==expected,(p,aa,alpha,expected)
            assert beta==expected*(2*p+3)*aa,(p,aa,beta)
    print('EXACT_JACOBI_MOMENTS_AND_STEP_DERIVATIVE_PASS')

    # Global optimization and the algebraic branch switch.
    for p in [.001,.02,.1,.3,.5,1,2,4,10,50,200]:
        c=2*p+3
        r0,r1=roots(p)
        assert 1/c**2<r0<1/c<r1<1,(p,r0,r1)
        best=sharp(p)
        assert best>step_gain(p,0)
        for j in range(3501):
            x=-1+2*j/3500
            assert step_gain(p,x)<=best*(1+2e-11),(p,x,best,step_gain(p,x))
    print('TWO_ROOT_GLOBAL_MAXIMUM_ALL_TEST_PARAMETERS_PASS')

    # Direct integration of projected step derivative, not the closed-form absolute integral.
    for p in [.5,1,2,3,8]:
        c=2*p+3
        for a in [.0,.04,.2,.5,.8]:
            val=simpson_abs_affine(A(p,a),A(p,a)*c*a)
            assert abs(val-step_gain(p,a))<5e-8,(p,a,val,step_gain(p,a))
    print('DIRECT_INDEPENDENT_VARIATION_INTEGRATION_PASS')

    # Random BV functions as signed sums of steps. Exact projection derivative is affine.
    for p in [.2,.5,1,2,10]:
        bound=sharp(p)
        for _ in range(1500):
            s0=s1=0.
            V=0.
            for k in range(rng.randrange(1,12)):
                x=rng.uniform(-.95,.95)
                jump=rng.uniform(-1,1)
                s0+=jump*A(p,x)
                s1+=jump*A(p,x)*(2*p+3)*x
                V+=abs(jump)
            assert simpson_abs_affine(s0,s1,steps=1000)<=bound*V*(1+1e-8)
    print('RANDOM_SIGNED_STIELTJES_BV_CONTRACTION_PASS 7500')

    # End regimes, each benchmark computed from the formula, not assumed exact.
    assert abs(sharp(.00001)-5/3)<3e-4
    for p in [500,2000,10000]:
        asympt=p*sqrt(2/(pi*exp(1)))
        assert abs(sharp(p)/asympt-1)<.025,(p,sharp(p)/asympt)
    assert abs(sharp(1)-1.63318)<.00005
    print('BETA_ENDPOINT_AND_GAUSSIAN_WEIGHT_LIMITS_PASS')
    print('ALL_QUADRATIC_JACOBI_BV_CHECKS_PASS')

if __name__ == '__main__':
    run()
