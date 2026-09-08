"""Selberg Lambda^2 upper-bound certificate for the H-count below 1e9.

Sieve n in [1,X], X=1e9, by P = {2,3,5,7,11} (subset sieve: every H-hit
with all nine values > 11 survives, so the H-count is <= sifted count
plus the at most 11 values n <= 11). Density omega(p)=nu_p=#{-h mod p}.
Optimal Selberg weights at level D=1e5:
  rho(d) = prod_{p|d} nu_p/(p-nu_p),
  G = sum_{d|P, d<D} rho(d),
  f(d) = prod_{p|d} p/nu_p,
  lam_e = mu(e) f(e) G_e / G, G_e = sum_{m|P, m*e<D} rho(m).
Main term X/G; error sum_{d1,d2} |lam1 lam2| omega(lcm) using |r_d| <= omega(d).
U = main + err + 11 is a rigorous upper bound for ANY weights with lam_1=1
(Selberg, e.g. Friedlander-Iwaniec Thm 7.1); fp rounding covered by rounding U up.
Since prod(P)=2310 < D, support = all 32 squarefree divisors.
"""
import json, math

H = [0, 2, 6, 8, 30, 32, 36, 38, 42]
X = 1e9
D = 1e5
PRIMES = [2, 3, 5, 7, 11]
nu = {p: len({h % p for h in H}) for p in PRIMES}
assert all(nu[p] < p for p in PRIMES)

divs = [1]
for p in PRIMES:
    divs += [d*p for d in divs]
divs = sorted(d for d in divs if d < D)
assert len(divs) == 2**len(PRIMES) == 32  # full divisor support

def fac(d):
    return [p for p in PRIMES if d % p == 0]

def rho(d):
    r = 1.0
    for p in fac(d):
        r *= nu[p]/(p - nu[p])
    return r

def ffun(d):
    r = 1.0
    for p in fac(d):
        r *= p/nu[p]
    return r

def omega(d):
    r = 1
    for p in fac(d):
        r *= nu[p]
    return r

def mu(d):
    return -1 if len(fac(d)) % 2 else 1

G = sum(rho(d) for d in divs)
# closed form check: G = prod p/(p-nu)
G_closed = 1.0
for p in PRIMES:
    G_closed *= p/(p - nu[p])
assert abs(G - G_closed)/G < 1e-9, (G, G_closed)

lam = {}
for e in divs:
    Ge = sum(rho(m) for m in divs if m*e < D)
    lam[e] = mu(e)*ffun(e)*Ge/G
assert abs(lam[1] - 1.0) < 1e-9

main = X/G
err = 0.0
for d1 in divs:
    l1 = lam[d1]
    for d2 in divs:
        g = math.gcd(d1, d2)
        err += abs(l1*lam[d2])*omega(d1//g*d2)
U = main + err + 11
U_reported = U*(1 + 1e-9) + 1.0  # rounded up, safe direction

out = {
    "X": X, "level_D": D, "sifting_primes": PRIMES,
    "note": "subset sieve; H-hits with all values>11 survive; n<=11 adds<=11",
    "nu": {str(p): v for p, v in nu.items()},
    "n_support_divisors": len(divs),
    "G": G, "G_closed_form": G_closed,
    "lambda_1": lam[1],
    "max_abs_lambda": max(abs(v) for v in lam.values()),
    "main_term_X_over_G": main,
    "error_term": err,
    "small_n_correction": 11,
    "U": U, "U_reported_rounded_up": U_reported,
    "U_brackets_certified_count_1": bool(U_reported >= 1),
    "nontrivial_U_lt_X": bool(U_reported < X),
}
with open("output/artifacts/selberg.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
