#!/usr/bin/env python3
"""Exact rational checks for the beta-binomial minimal thinning theorem."""
from fractions import Fraction as F
from math import comb


def rising(x, k):
    ans = F(1)
    for t in range(k):
        ans *= x + t
    return ans


def moment(a, b, k):
    return rising(a, k) / rising(a + b, k)


def check_case(n, a, b):
    assert n >= 1 and a > 0 and b > 0
    r = (a + n - 1) / (a + b + n - 1)
    assert F(0) < r < F(1)
    q = [F(0)] * (n + 1)
    q[n] = moment(a, b, n) / r**n
    if n > 1:
        q[n - 1] = F(0)
        for j in range(n - 2, -1, -1):
            q[j] = ((1-r)*(j+2)*(j+1)*q[j+2]
                    +(2-r)*(j+1)*(n-1-j)*q[j+1]) / ((n-j)*(a+j))
    assert all(v >= 0 for v in q)
    assert q[n] > 0
    assert q[n - 1] == 0
    assert all(q[j] > 0 for j in range(n + 1) if j != n - 1)
    assert sum(q) == 1

    # Original count distribution by the beta-binomial beta-moment formula.
    p = [F(comb(n,k))*rising(a,k)*rising(b,n-k)/rising(a+b,n)
         for k in range(n+1)]
    # Its r-thinned parent obtained from exact convolution.
    via_thinning = [sum(F(comb(j,k))*r**k*(1-r)**(j-k)*q[j]
                        for j in range(k,n+1)) for k in range(n+1)]
    assert via_thinning == p
    assert sum(p) == 1

    # Independently compute the inverse coefficients from the beta moments.
    via_moments = [F(comb(n,k)) * sum(F(comb(n-k,t))*(-1)**t
                                      *r**(n-k-t)*moment(a,b,k+t)
                                      for t in range(n-k+1)) /r**n
                   for k in range(n+1)]
    assert via_moments == q

    # Any smaller parameter produces a negative penultimate parent mass.
    u = r*F(9,10)
    negative = n * (u*moment(a,b,n-1)-moment(a,b,n)) /u**n
    assert negative < 0
    return r, q


cases = [(F(1),F(1)),(F(1,2),F(1,2)),(F(1,3),F(4)),
         (F(5),F(1,3)),(F(2),F(3)),(F(3,2),F(11,4)),
         (F(1,10),F(25)),(F(7),F(1,20)),(F(7,3),F(13,7))]
tested = 0
for a,b in cases:
    for n in range(1,19):
        check_case(n,a,b)
        tested += 1

r, q = check_case(4,F(2),F(3))
assert r == F(5,8)
assert q == [F(471,4375), F(704,4375), F(1152,4375), F(0), F(2048,4375)]
print(f"VERIFY_OK exact_cases={tested} beta23_n4_threshold={r.numerator}/{r.denominator} "
      f"hole={q[3]} support={sum(x>0 for x in q)}")
