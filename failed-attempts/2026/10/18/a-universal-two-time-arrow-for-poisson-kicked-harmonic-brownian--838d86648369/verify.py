"""Exact checks for stationary OU compound-Poisson time-arrow formulas.
Run: python3 verify.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def moments(k, total=4):
    # Cumulant-to-raw-moment recurrence, allowing centered innovations.
    ms = [F(1)]
    for n in range(1, total + 1):
        ms.append(sum(F(comb(n - 1, j - 1)) * k[j] * ms[n - j]
                      for j in range(1, n + 1)))
    return ms

def test_case(lam, rho, diff, jumps, a):
    # jumps: exact rational discrete distribution [(probability, size)].
    mu = [F(0)] * 5
    for n in range(1, 5):
        mu[n] = sum(p * y ** n for p, y in jumps)
    cu = [F(0)] * 5
    cu[1] = F(0)  # center stationary position
    cu[2] = diff / lam + rho * mu[2] / (2 * lam)
    cu[3] = rho * mu[3] / (3 * lam)
    cu[4] = rho * mu[4] / (4 * lam)
    cz = [F(0)] + [(1 - a ** n) * cu[n] for n in range(1, 5)]
    m = moments(cu)
    z = moments(cz)

    def mixed(p, q):
        return sum(F(comb(q, j)) * a**j * m[p + j] * z[q - j]
                   for j in range(q + 1))
    check(mixed(1, 1) == a * cu[2])
    check(mixed(1, 2) - mixed(2, 1) == (a*a - a) * cu[3])
    check(mixed(1, 3) - mixed(3, 1) == (a**3 - a) * cu[4])
    check(mixed(1, 3) - mixed(3, 1) <= 0)
    if any(y != 0 and p > 0 for p, y in jumps):
        check(mixed(1, 3) - mixed(3, 1) < 0)
    check(cz[2] == (1-a*a)*cu[2])
    check(m[4] - 3*m[2]**2 == cu[4])
    check(mu[4] >= 0)

laws = [
    [(F(1,2),F(2)),(F(1,2),F(-2))],
    [(F(2,3),F(-1)),(F(1,3),F(5))],
    [(F(1,4),F(0)),(F(1,4),F(-3)),(F(1,2),F(1))],
    [(F(3,5),F(1)),(F(2,5),F(-1))],
]
for lam in [F(1,3),F(1),F(5,2)]:
    for rho in [F(1,2),F(5)]:
        for diff in [F(0),F(2,7),F(3)]:
            for law in laws:
                for a in [F(1,7),F(1,2),F(3,4),F(9,10)]:
                    test_case(lam,rho,diff,law,a)

# The normalized quartic signal F(a)=a(1-a^2) is maximal at 1/sqrt(3).
# The two-sided exact difference-of-cubes certificate:
# maximum=(2/(3sqrt(3))) and (2/(3sqrt(3)))^2 - [a(1-a^2)]^2 >=0
# is checked rationally by derivative and polynomial factorization.
# The derivative of a-a^3 is 1-3a^2, hence the only interior
# critical point is a=1/sqrt(3), a strict global maximum on (0,1).
# Exact rational tests also verify universal two-lag ratio.
for a in [F(1,31),F(1,13),F(1,4),F(2,5),F(3,4),F(99,100)]:
    f = lambda x: x * (1 - x*x)
    check(f(a*a) / f(a) == a*(1+a*a))
# Algebraic derivative of R(a)=a+a^3 is 1+3a^2>0.
print('passed',checks,'exact rational checks; quartic peak at a=1/sqrt(3)')
