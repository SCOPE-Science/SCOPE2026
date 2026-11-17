"""Independent exact-coefficient and finite quadrature diagnostics for the arctangent commutator.
Run with Python 3 standard library: python checker.py
The proof of the infinite-dimensional statement is in RESULT.md, not in this script.
"""
from fractions import Fraction
from math import atan, exp, log1p, pi, factorial, log


def F_over_t2(t):
    if t == 0:
        return 0.25
    if t < 0.05:
        # Alternating Taylor series for F(t)/t^2.
        return sum((-1)**k * t**(2*k) / ((2*k+1) * 2**(2*k+1) * (2*k+2)) for k in range(10))
    return (t*atan(t/2.0)-log1p(t*t/4.0))/(t*t)


def second_trace(s, N=24000):
    """Quadrature after v=2s^2 t, using composite Simpson on [0,48]."""
    end = 48.0
    h = end/N
    total = exp(0)*F_over_t2(0.0) + exp(-end)*F_over_t2(end/(2*s*s))
    for i in range(1,N):
        v=i*h
        total += (4 if i % 2 else 2)*exp(-v)*F_over_t2(v/(2*s*s))
    return pi/(2*s*s)*(h/3)*total


def coefficient(k):
    # F(t)=sum_k (-1)^k t^(2k+2) / [(2k+1) 2^(2k+1)(2k+2)].
    f = Fraction((-1)**k, (2*k+1)*2**(2*k+1)*(2*k+2))
    # integral of e^(-2s^2 t) t^(2k): (2k)! / (2s^2)^(2k+1)
    return f * Fraction(factorial(2*k),2**(2*k+1))


def main():
    checks = 0
    assert coefficient(0)==Fraction(1,8)
    assert coefficient(1)==Fraction(-1,384)
    assert coefficient(2)==Fraction(1,1280)
    checks+=3
    values={s:second_trace(s) for s in [0.125,0.25,0.5,1.0,2.0,3.0,4.0,8.0]}
    for s,v in values.items():
        lower = pi*(1/(8*s**2)-1/(384*s**6))
        upper = pi/(8*s*s)
        upper2=lower+pi/(1280*s**10)
        assert lower-1e-8 < v < upper+1e-8, (s,v,lower,upper)
        assert v <= upper2+1e-8, (s,v,upper2)
        checks+=3
    seq=list(values.values())
    assert all(x>y for x,y in zip(seq,seq[1:]))
    checks+=7
    assert abs(values[4.0]/(pi/(8*4**2))-1)<1e-4
    assert abs(values[8.0]/(pi/(8*8**2))-1)<1e-5
    checks+=2
    # Independent Cauchy-pair integral check for t=1 from numerical Simpson.
    # Direct exact expression I(t) = 2 pi (t atan(t/2) - log(1+t^2/4)).
    t=1.0
    # integrate the convolution on a second quadrature, independently
    n=20000
    h=t/n
    f=lambda x:(t-x)/(4+x*x)
    outer=f(0)+f(t)+sum((4 if i%2 else 2)*f(i*h) for i in range(1,n))
    I_direct=4*pi*(h/3)*outer
    I_exact=2*pi*(t*atan(t/2)-log1p(t*t/4))
    assert abs(I_exact-I_direct)<1e-9
    checks+=1
    print('PASS',checks,'diagnostic assertions; exact rational coefficients + finite quadratures')
    for s,v in values.items():
        print('s=',s,'Tr(C_s^2)~',format(v,'.12g'))


if __name__ == '__main__':
    main()
