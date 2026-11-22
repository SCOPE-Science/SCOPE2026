"""Exact-rational spot checks for the Poisson-xgamma thinning theorem.

Proof of all-parameter statements is in RESULT.md; these finite checks
verify the algebraic certificates and independent parameter examples.
Run: python3 checker.py
"""
from fractions import Fraction as F
from math import comb

checks = 0

def expect(flag, label):
    global checks
    assert flag, label
    checks += 1


def P(q):
    return 3*q**4 - 6*q**3 - 5*q**2 + 4*q + 1


def H(q):
    return 9*(1-q)*(1+q*(1-q))**3


def canonical_b(q, N):
    """Exact b_n = n [z^n] log G(z), n >= 1."""
    d = q*(1-q)
    t0 = F(2)
    t1 = F(2)/(1+d)
    out = []
    for n in range(1,N+1):
        out.append(q**n*(3-t1))
        t0, t1 = t1, F(2)*t1/(1+d) - t0/(1+d)
    return out


def pmf_mixture(q, n):
    return q**n*((1-q)**2 + q*(1-q)**3*comb(n+2,2))


def pmf_original(theta, n):
    return (theta**2 * (2*(1+theta)**2 + theta*(n+1)*(n+2))
            / (2*(1+theta)**(n+4)))

expect(P(F(7,10)) == F(123,10000), 'P(7/10)')
expect(P(F(71,100)) == F(-6561557,100000000), 'P(71/100)')
expect(H(F(71,100))-4 == F(57693129079919,100000000000000), 'endpoint modulus certificate')
expect(H(F(0))==9, 'other endpoint')
q=F(5,7)
bs=canonical_b(q,3)
expect(bs[0]-bs[1] == F(-2390,170569), 'strictly decreasing but non-thinning witness')
for n in range(40):
    expect(pmf_mixture(q,n+1) < pmf_mixture(q,n), 'decreasing-mass witness finite spot check')

for q in (F(1,10),F(1,4),F(1,2),F(7,10),F(3,4),F(9,10)):
    theta = (1-q)/q
    bs = canonical_b(q,32)
    for n in range(16):
        expect(pmf_mixture(q,n) == pmf_original(theta,n), 'mixture pmf equality')
    for n in range(1,31):
        expect(bs[n-1] > 0, 'positive Levy coefficient')
        # identity b_n-b_(n+1) for n=1 is (1-q)P(q)/(1+d)^2 times q
    d=q*(1-q)
    expect((bs[0]-bs[1]) == q*(1-q)*P(q)/(1+d)**2, 'first canonical difference')
    if q <= F(7,10):
        for n in range(31):
            expect(bs[n]>=bs[n+1], 'monotone canonical b')
    else:
        expect(bs[0]<bs[1], 'non-self-decomposable first obstruction')

# Independent PGF coefficient check: expansion through n=15.
# Numerator (1-q)^2 [(1-qz)^2+q(1-q)] and denominator (1-qz)^3.
for q in (F(2,7),F(7,10),F(3,4)):
    g0 = (1-q)**2
    a0 = g0*(1+q*(1-q))
    a1 = -2*q*g0
    a2 = q*q*g0
    for n in range(16):
        rhs = (a0*comb(n+2,2)*q**n
               + (a1*comb(n+1,2)*q**(n-1) if n>=1 else 0)
               + (a2*comb(n,2)*q**(n-2) if n>=2 else 0))
        expect(rhs==pmf_mixture(q,n), 'PGF expansion')

print('PASS:',checks,'exact-rational assertions; finite tests support, not replace, the proof')
