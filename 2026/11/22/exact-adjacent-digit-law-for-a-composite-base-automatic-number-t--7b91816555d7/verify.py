"""Exact rational checks and independent arithmetic tests for a base-15 digit law.

Run with Python 3: python3 verify.py
Only standard-library modules are needed.
"""
from collections import Counter
from fractions import Fraction

R = (3, 6, 9, 12)
E = (2, 5, 8, 11, 14)
DIGITS = R + E
q = {d: Fraction(3 if d in R else 5, 37) for d in DIGITS}


def valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def predicted_digit(n):
    t = 2*n - 1
    a = valuation(t, 3)
    b = valuation(t, 5)
    u = t // 5**b
    e = 2*a + 1
    if b > e:
        return 5
    y5 = (2*u*pow(pow(3,b,5), -1, 5)) % 5
    y3 = 0 if b < e else 2
    return next(d for d in range(15) if d%3==y3 and d%5==y5)


def independent_digit(n):
    value = (2*n-1)*(16**n-4)
    while value % 15 == 0:
        value //= 15
    return value % 15


def pair_distribution():
    out = Counter()
    for ij in ((12,6),(9,3),(3,12)):
        out[ij] += Fraction(1,5)
    for d in DIGITS:
        out[(6,d)] += q[d]/5
        out[(d,9)] += q[d]/5
    return dict(out)


def check():
    for n in range(1,301):
        assert predicted_digit(n) == independent_digit(n), n
    assert sum(q.values()) == 1
    assert sum(Fraction(2,3**(a+1))*Fraction(1,5**(2*a)) for a in range(12)) < Fraction(25,37)
    assert sum(pair_distribution().values()) == 1
    pairs = pair_distribution()
    assert len(pairs)==20, len(pairs)
    marginal = Counter()
    for (x,y), p in pairs.items():
        marginal[x] += p
    for d in DIGITS:
        assert marginal[d] == Fraction(8 if d in R else 1, 37), (d,marginal[d])
    assert all(p > 0 for p in pairs.values())
    counts = Counter()
    singleton = Counter()
    total = 200000
    prior = predicted_digit(1)
    for n in range(1,total+1):
        this = prior
        nxt = predicted_digit(n+1)
        counts[(this,nxt)] += 1
        singleton[this] += 1
        assert (this,nxt) in pairs, (n,this,nxt)
        prior = nxt
    assert set(counts)==set(pairs)
    max_error=max(abs(counts[key]-total*float(p)) for key,p in pairs.items())
    print('DIRECT_BIG_INTEGER_CHECKS=300')
    print('ADJACENT_PAIR_TESTS=',total)
    print('DISTINCT_PAIRS=',len(counts))
    print('MAX_ABSOLUTE_COUNT_ERROR=',round(max_error,4))
    print('CONDITIONAL_DIGIT_PROBABILITIES=',','.join(f'{d}:{q[d]}' for d in DIGITS))
    print('PAIR_PROBABILITIES=',','.join(f'{a}-{b}:{p}' for (a,b),p in sorted(pairs.items())))
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
