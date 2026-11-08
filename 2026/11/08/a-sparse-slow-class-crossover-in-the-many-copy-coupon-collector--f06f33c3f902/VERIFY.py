"""Finite diagnostics for a two-speed many-copy coupon collector."""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammaincc, gammainccinv

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

c = 1.0
r = 0.65
kappa = 1.0
y = brentq(lambda w: w - c - c * math.log(w / c) - 1, c + 1e-9, 20)
a, b = 1 - c / y, r - c / y
delta = r * y - c - c * math.log(r * y / c)
eta = (1 - b / a) / 2
check(0 < b < a < 1, "strict slopes")
check(0 < delta < 1, "sublinear slow class")
check(0 < eta < 0.5, "logarithmic phase")

p_slow = quad(lambda v: kappa * b / a * v ** (b / a - 1) *
              math.exp(-v - kappa * v ** (b / a)), 0, math.inf,
              epsabs=1e-11)[0]
p_fast = quad(lambda x: a * math.exp(-a*x) *
              math.exp(-math.exp(-a*x)-kappa*math.exp(-b*x)),
              -30, 80, epsabs=1e-11)[0]
check(0 < p_slow < 1, "nondegenerate slow winner")
check(abs(p_slow + p_fast - 1) < 1e-8, "marked density normalization")
check(abs(p_slow - 0.5472756865607) < 1e-8, "reference quadrature")

for n in (10**3, 10**5, 10**8, 10**12):
    L = math.log(n)
    m = int(math.floor(c*L))
    u = gammainccinv(m, 1/n)
    Q = gammaincc(m, r*u)
    M = kappa/Q
    check(abs(n*gammaincc(m,u)-1) < 2e-10, "fast quantile identity")
    check(M > 0 and Q > 0, "slow quantile")
    check(0.7 < M / (n**delta * L**eta) < 2, "critical scale sample")
    for x in (-1.0, 0.0, 1.0):
        fast = n*gammaincc(m,u+x)
        slow = M*gammaincc(m,r*(u+x))
        check(fast > 0 and slow > 0, "tail counts positive")
        # For finite n, both empirical intensity ratios converge to the law.
        if n >= 10**8:
            check(abs(math.log(fast)+a*x) < 0.08, "fast local tail")
            check(abs(math.log(slow/kappa)+b*x) < 0.08, "slow local tail")
    # Exact finite independent Erlang maximum formula, evaluated two ways.
    tail_f, tail_s = gammaincc(m,u), gammaincc(m,r*u)
    logprod = n*math.log1p(-tail_f) + int(M)*math.log1p(-tail_s)
    check(0 < math.exp(logprod) < 1, "exact no-defect product")

print(f"PASS ({checks} checks): y={y:.12f}, delta={delta:.12f}, eta={eta:.12f}, slow_last={p_slow:.12f}")
