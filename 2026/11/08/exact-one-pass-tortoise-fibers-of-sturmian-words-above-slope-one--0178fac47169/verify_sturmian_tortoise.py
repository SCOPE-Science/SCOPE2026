#!/usr/bin/env python3
"""Finite cross-checks for the exact Sturmian one-tortoise theorem.

Requires Python 3 standard library only. These finite checks supplement, and do not
replace, the infinite symbolic proof. Irrational slopes are evaluated at 72-digit
Decimal precision; this is an explicitly finite numerical cross-check.
"""
from collections import defaultdict
from decimal import Decimal, ROUND_FLOOR, getcontext

getcontext().prec = 72
D = Decimal
RT2 = D(2).sqrt()
RT5 = D(5).sqrt()
SLOPES = {
    "near_one_third": D(1)/3 + (RT2-1)/1000,
    "fibonacci": (D(3)-RT5)/2,
    "silver": RT2-1,
    "below_half": D(1)/2 - (RT2-1)/1000,
    "above_half": D(1)/2 + (RT2-1)/1000,
    "golden_conjugate": (RT5-1)/2,
    "one_over_sqrt_two": RT2/2,
    "near_one": D(1)-(RT2-1)/1000,
}


def flo(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def mechanical(alpha, x, n):
    """Binary mechanical coding at intercept x for indices 0,...,n-1."""
    return ''.join(str(flo(x+(i+1)*alpha)-flo(x+i*alpha))
                   for i in range(n))


def factors_via_intervals(alpha, n):
    """All n+1 coding cells cut by the first n+1 irrational-rotation endpoints."""
    cuts = sorted((-j*alpha) % 1 for j in range(n+1))
    assert len(set(cuts)) == n+1
    result = set()
    for i, x in enumerate(cuts):
        following = cuts[i+1] if i<n else cuts[0]+1
        result.add(mechanical(alpha, ((x+following)/2)%1, n))
    return result


def tortoise(word):
    k = word.find('1')
    return word if k<0 else word[:k]+word[k+1:]+'1'


def expected_classes(alpha, n, c):
    if n==1:
        return []
    if alpha > D('0.5'):
        return [frozenset(('10'+c[:n-2], '01'+c[:n-2]))]
    if n==2:
        return [frozenset(('01', '10'))]
    if n==3:
        return [frozenset(('001', '010', '100'))]
    return [frozenset(('10'+c[:n-2], '01'+c[:n-2])),
            frozenset(('001'+c[:n-3], '010'+c[:n-3]))]


def check_one(alpha, n):
    factors = factors_via_intervals(alpha, n)
    assert len(factors)==n+1, (alpha,n,'factor count',len(factors))
    fibers = defaultdict(set)
    for w in factors:
        fibers[tortoise(w)].add(w)
    observed = {frozenset(v) for v in fibers.values() if len(v)>1}
    c = mechanical(alpha, alpha, n)
    expected = set(expected_classes(alpha,n,c))
    assert observed == expected, (alpha,n,observed,expected)
    predicted = 2 if n==1 else (
        n if alpha>D('.5') else
        2 if n in (2,3) else n-1)
    assert len(fibers)==predicted, (alpha,n,len(fibers),predicted)


def direct_prefix_check(alpha, limit_n=27, length=28000):
    """Second factor enumeration not using intercept-cell sorting."""
    stream = mechanical(alpha,D(0),length)
    for n in range(1,limit_n+1):
        factors = {stream[i:i+n] for i in range(length-n+1)}
        assert factors==factors_via_intervals(alpha,n), (alpha,n,'scan versus rotation')


def main():
    runs=0
    for name,alpha in SLOPES.items():
        assert D(1)/3 < alpha < 1 and alpha != D('0.5'), (name,alpha)
        for n in range(1,82):
            check_one(alpha,n)
            runs += 1
        direct_prefix_check(alpha)
    print('STURMIAN_TORTOISE_VERIFY_OK',len(SLOPES),runs,
          'rotation_cell_census prefix_independent_scan n_le_81')


if __name__=='__main__':
    main()
