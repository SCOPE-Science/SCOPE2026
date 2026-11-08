#!/usr/bin/env python3
"""Independent finite checks of a twofold Beatty range-test theorem.

Uses only Python's standard library. Decimal precision is ample for the reported
finite comparisons; no finite computation certifies the infinite assertions.
"""
from decimal import Decimal, localcontext


def atan_series(z):
    total = Decimal(0)
    power = z
    for k in range(400):
        term = power / (2*k + 1)
        total += term if k % 2 == 0 else -term
        if abs(term) < Decimal('1e-85'):
            break
        power *= z*z
    return total


def cube_root(n):
    x = Decimal(str(n ** (1/3)))
    n = Decimal(n)
    for _ in range(25):
        x = (2*x + n/(x*x))/3
    return x


def check(alpha, n, label, square=None):
    a2 = square if square is not None else alpha*alpha
    phi = (Decimal(1)+Decimal(5).sqrt())/2
    lo = 1-1/alpha
    predicted = ((1-alpha+1/alpha)**2/(2*alpha)) if alpha<phi else Decimal(0)
    f = lambda y: int((alpha*y).to_integral_value(rounding='ROUND_FLOOR'))
    images = {f(f(k)) for k in range(1,n+1)}
    false_positive = false_negative = missing_region = 0
    first = None
    for x in range(1,n+1):
        u = (Decimal(x)/alpha) % 1
        v = (Decimal(x)/a2) % 1
        sufficient = (lo < u and 1-2/alpha < v-u/alpha < lo)
        exceptional = (lo < u < 2-alpha and v>2-2/alpha+u/alpha)
        actual = x in images
        if sufficient and not actual: false_positive += 1
        if actual and not sufficient:
            false_negative += 1
            if first is None: first=x
        if exceptional: missing_region += 1
        assert actual == (sufficient or exceptional), (label,x,actual,sufficient,exceptional)
    assert false_positive == 0
    assert missing_region == false_negative
    if alpha>=phi: assert false_negative == 0
    if label=='sqrt2': assert false_negative == 0
    if label=='cuberoot3':
        assert first==2
        assert false_negative>0
    print('DIRECT_RANGE_EQUIVALENCE_OK',label,'N=',n,'false_negatives=',false_negative,
          'false_positives=',false_positive,'density=',f'{false_negative/n:.8f}',
          'torus_prediction_if_independent=',f'{predicted:.8f}')


def main():
    with localcontext() as c:
        c.prec=95
        a2=Decimal(2).sqrt(); a6=Decimal(6).sqrt()
        pi=16*atan_series(Decimal(1)/5)-4*atan_series(Decimal(1)/239)
        check(a2,6000,'sqrt2',square=Decimal(2))
        check(a6,6000,'sqrt6',square=Decimal(6))
        check(cube_root(3),16000,'cuberoot3')
        check(pi/2,20000,'pi_over_2')
        check((1+Decimal(5).sqrt())/2,6000,'phi')
    print('VERIFY_OK','finite_only=True','analytic_equidistribution_not_computationally_certified=True')

if __name__=='__main__': main()
