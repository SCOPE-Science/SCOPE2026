"""Finite consistency checks for two-speed threshold-reset renewal formulas.

Run with Python >= 3.9: python checker.py
This is a numerical and exact-arithmetic consistency checker; the
infinite-time statements require the analytical proofs in RESULT.md.
"""
from fractions import Fraction
import cmath
import math

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def renewal_mass(kmax, m, n, p):
    q = 1 - p
    u = [Fraction(1)]
    for k in range(1, kmax + 1):
        u.append((p * u[k-m] if k >= m else 0)
                 + (q * u[k-n] if k >= n else 0))
    return u


def finite_phase_law(k, s, m, n, p, u):
    q = 1-p
    distribution = {}
    for duration, chance in ((m, p), (n, q)):
        for j in range(min(k + 1, duration)):
            x = 1 - (s + j)/duration
            weight = chance * u[k-j]
            distribution[x] = distribution.get(x, Fraction(0)) + weight
    return distribution


def limiting_phase_law(s, m, n, p):
    q = 1 - p
    mu = p*m + q*n
    distribution = {}
    for duration, chance in ((m,p),(n,q)):
        for j in range(duration):
            x = 1 - (s+j)/duration
            weight = chance/mu
            distribution[x] = distribution.get(x, Fraction(0)) + weight
    return distribution

for m, n in ((1,2), (2,3), (2,5), (3,7), (5,8)):
    for p in (Fraction(1,4), Fraction(2,5), Fraction(1,2), Fraction(3,4)):
        mu = p*m + (1-p)*n
        u = renewal_mass(2500, m, n, p)
        verify(abs(float(u[-1]-1/mu)) < 2e-5, 'lattice renewal limit')
        for s in (Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(3,4)):
            nu = limiting_phase_law(s,m,n,p)
            verify(sum(nu.values()) == 1, 'limit normalization')
            verify(all(0 <= x <= 1 and mass > 0 for x,mass in nu.items()), 'limit support')
            mean = sum(x*w for x,w in nu.items())
            verify(mean == Fraction(1,2) + (Fraction(1,2)-s)/mu, 'phase-sawtooth mean')
            for k in range(0, 120):
                P = finite_phase_law(k,s,m,n,p,u)
                verify(sum(P.values()) == 1, 'finite law normalization')
                verify(all(0 <= x <= 1 and w >= 0 for x,w in P.items()), 'finite support')
            P = finite_phase_law(2500,s,m,n,p,u)
            total_variation = sum(abs(P.get(x,0)-nu.get(x,0)) for x in set(P)|set(nu))/2
            verify(float(total_variation) < 3e-5, 'finite phase total variation limit')

# Fully rational illustrated phase distribution.
p = Fraction(2,5)
s = Fraction(1,4)
u = renewal_mass(800, 1, 2, p)
nu_limit = limiting_phase_law(s, 1, 2, p)
verify(nu_limit == {Fraction(3,4):Fraction(1,4), Fraction(7,8):Fraction(3,8),
                    Fraction(3,8):Fraction(3,8)}, 'illustrated atomic law')
verify(sum(x*w for x,w in nu_limit.items()) == Fraction(21,32), 'illustrated mean')

# Incommensurate travel times: continued-fraction near-resonant zeros.
a = 1.
b = math.sqrt(2)
p = .4
q = 1-p
mu = p*a+q*b
for K, M in ((29,41), (70,99), (169,239), (408,577), (985,1393), (2378,3363)):
    delta = 2*math.pi*(K*b/a-M)
    verify(0 < abs(delta) < .1, 'approximant mismatch')
    w = -1j*q/mu*delta - (p*q*a*a/(2*mu**3))*delta**2
    for _ in range(12):
        ea = cmath.exp(-a*w)
        eb = cmath.exp(-b*w-1j*delta)
        f = 1-p*ea-q*eb
        fp = p*a*ea+q*b*eb
        w -= f/fp
    F = 1-p*cmath.exp(-a*w)-q*cmath.exp(-b*w-1j*delta)
    verify(abs(F)<1e-12, 'root residual')
    verify(w.real < 0, 'root left of imaginary axis')
    approximation = -1j*q/mu*delta - (p*q*a*a/(2*mu**3))*delta**2
    verify(abs(w-approximation) < .03*abs(delta)**3, 'quadratic expansion')
    z = 1j*(2*math.pi*K/a)+w
    B = 1/z-(p*(1-cmath.exp(-a*z))/a+q*(1-cmath.exp(-b*z))/b)/z**2
    verify(abs(B)>0.5/abs(z), 'noncancelling observable pole')
    verify(abs(p*a*cmath.exp(-a*z)+q*b*cmath.exp(-b*z))>.7*mu,
           'simple resonance root')

print(f'PASS: {checks} finite exact-arithmetic and complex-root assertions.')
print('All infinite-time conclusions still require the separate analytic proof.')
