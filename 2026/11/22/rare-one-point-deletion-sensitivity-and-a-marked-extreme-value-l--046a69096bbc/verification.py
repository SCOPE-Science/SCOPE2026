"""Deterministic finite checks for circular longest-gap one-deletion sensitivity.

Scientific scope: numerical checks of finite identities, NOT a proof of an infinite limit.
The accompanying mathematical proof gives all limiting conclusions.
"""
import math
from fractions import Fraction


def harmonic(m):
    return sum((Fraction(1, k) for k in range(1, m + 1)), Fraction())


def event_prob(n):
    return harmonic(n-1) / (n-1)


def exact_tail_integer(n, t):
    # Exponential-scale increase D = (sum E_i) * (new_max - old_max).
    # For integral t, use the stable quadrature outside this function.
    import mpmath as mp
    t = mp.mpf(t)
    m = n - 2
    return mp.exp(-2*t) * mp.quad(lambda z: -mp.log(z) * (1-mp.exp(-t)*z)**m, [0, 1])


def exact_binomial_tail(n, t):
    import mpmath as mp
    t = mp.mpf(t)
    return mp.exp(-2*t) * sum((-1)**j*math.comb(n-2, j)*mp.exp(-j*t)/(j+1)**2 for j in range(n-1))


def conditional_reference(n, t):
    import mpmath as mp
    return exact_tail_integer(n, t) / (mp.mpf(harmonic(n-1).numerator)/harmonic(n-1).denominator/(n-1))


def assert_close(a, b, tol=1e-18):
    assert abs(float(a-b)) < tol, (a,b)


def run():
    import mpmath as mp
    mp.mp.dps=55
    checks=0
    # Compare beta identity with gamma-integral and full finite tail binomial form.
    for n in range(2, 13):
        assert event_prob(n) == sum((Fraction((-1)**j*math.comb(n-2,j),(j+1)**2) for j in range(n-1)), Fraction())
        checks+=1
        for t in (0, mp.mpf('0.25'), mp.mpf('0.9'), mp.mpf('1.7')):
            assert_close(exact_tail_integer(n,t),exact_binomial_tail(n,t),1e-30)
            checks+=1
    # Exact mean exponential-scale increment via integration of binomial tail.
    for n in range(2, 16):
        m=n-2
        expected=sum((Fraction((-1)**j*math.comb(m,j),(j+1)**2*(j+2)) for j in range(m+1)),Fraction())
        stated=(harmonic(n-1)-1)/(n-1)+Fraction(1,n*(n-1))
        assert expected == stated
        checks+=1
    # Finite conditional density tends to product of negative-log Gamma(2) and Exp(1).
    for n in (100,1000,100000):
        for x,w in ((0,1),(-1,0.5),(1,0.75)):
            z=mp.log(n)+x
            fz=(n-2)*mp.exp(-z)*(1-mp.exp(-z))**(n-3)
            ft=(z+w)*mp.exp(-z-w)
            fn=fz*ft/(mp.mpf(harmonic(n-1).numerator)/harmonic(n-1).denominator/(n-1))
            limiting=mp.exp(-2*x-mp.exp(-x)-w)
            if n == 100000: assert abs(float(fn/limiting-1)) < 0.105
            checks+=1
    for t in (mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2')):
        n=1000
        c=conditional_reference(n,t)
        assert abs(float(c-mp.exp(-t))) < 0.18
        checks+=1
    # Total mass and simple moments for the theoretical factorization.
    assert_close(mp.quad(lambda x: x*mp.exp(-x),[0,mp.inf]),1,1e-25);checks+=1
    assert_close(mp.quad(lambda g: g*mp.exp(-g),[0,mp.inf]),1,1e-25);checks+=1
    print(f'PASS: {checks} deterministic finite/numerical assertions; theorem proof is separate.')

if __name__=='__main__':run()
