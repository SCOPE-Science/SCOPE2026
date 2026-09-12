"""Bounded recovery/verification tests for theta=(1/9,2/9,4/9,1/3) genus-2 Picard-Fuchs origin question."""
import itertools, random
from fractions import Fraction
from sympy import (Rational, cos, pi, symbols, minimal_polynomial,
                   QQ, Poly, simplify)
from sympy.ntheory import totient as euler_phi

theta = [Rational(1,9), Rational(2,9), Rational(4,9), Rational(1,3)]
print("theta =", theta)
print("sum =", sum(theta))
print("denominators =", [int(t.q) for t in theta])
print("PVI (alpha,beta,gamma,delta) =",
      ((theta[3]-1)**2/2, -theta[0]**2/2, theta[1]**2/2, (1-theta[2]**2)/2))

# --- 1. Okamoto denominator invariance under random words ---
def apply_word(th, word):
    th = list(th)
    for g in word:
        if g[0] == 'perm':
            th = [th[i] for i in g[1]]
        elif g[0] == 'sign':
            th = [ -x if s else x for x, s in zip(th, g[1])]
        elif g[0] == 'trans':
            th = [ x+n for x, n in zip(th, g[1])]
    return th

def denoms(th):
    return sorted(Fraction(int(x.p), int(x.q)).denominator for x in th)

random.seed(1227)
base_den = denoms(theta)
perms = list(itertools.permutations([0,1,2,3]))
ok = True
for trial in range(3000):
    w = []
    for _ in range(random.randint(1,6)):
        c = random.random()
        if c < 0.4:
            w.append(('perm', random.choice(perms)))
        elif c < 0.8:
            w.append(('sign', [random.random()<0.5 for _ in range(4)]))
        else:
            # even-sum integer translation (QD4 root lattice translation)
            n = [random.randint(-3,3) for _ in range(4)]
            if sum(n) % 2: n[0] += 1
            w.append(('trans', n))
    if denoms(apply_word(theta, w)) != base_den:
        ok = False; print("COUNTEREXAMPLE", w); break
print("denominator multiset invariant over 3000 random Okamoto words:", ok, base_den)

# alcove check: entries already in [0,1)?
print("alcove-minimal (all in [0,1)):", all(0 <= t < 1 for t in theta))

# elliptic-list comparison: k/9 in (1/6)Z ?
for t in theta:
    print(f"  {t}: in (1/6)Z ? {(t*6).q == 1}")

# --- 2. eigenvalue orders (Jimbo-Miwa: tr M_i = 2cos(pi*theta_i)) ---
def order_exp_pi_theta(t):
    # order of e^{i*pi*t}, t = a/b reduced
    a, b = int(t.p), int(t.q)
    from math import gcd
    return 2*b // gcd(a, 2*b)
ords = [order_exp_pi_theta(t) for t in theta]
print("orders of e^{i pi th_i} =", ords)
# doubled convention e^{2 i pi th}:
def order_2(t):
    a, b = int(t.p), int(t.q)
    from math import gcd
    return b // gcd(a, b)
print("orders of e^{2 i pi th_i} =", [order_2(t) for t in theta])

# --- 3. allowed Sp(4,Z) eigenvalue orders: phi(n)<=4 ---
allowed = [n for n in range(1, 61) if euler_phi(n) <= 4]
print("allowed orders (phi<=4):", allowed)
print("9 present?", 9 in allowed, "| 18 present?", 18 in allowed)
# divisibility lemma: 9|n -> 6|phi(n), check n<=2000
bad = [n for n in range(9, 2001, 1) if n % 9 == 0 and int(euler_phi(n)) % 6 != 0]
print("multiples of 9 with 6 not dividing phi(n) [must be empty]:", bad)
print("phi(9),phi(18) =", euler_phi(9), euler_phi(18))

# --- 4. trace-field degrees ---
x = symbols('x')
for label, expr in [("2cos(pi/9)", 2*cos(pi/9)), ("2cos(2pi/9)", 2*cos(2*pi/9)),
                    ("2cos(4pi/9)", 2*cos(4*pi/9)), ("2cos(pi/3)", 2*cos(pi/3))]:
    mp = minimal_polynomial(expr, x)
    print(label, "minpoly =", mp, "degree =", Poly(mp, x).degree())
# allowed traces have degree <= 2
maxdeg = 0
for n in allowed:
    for k in range(n):
        mp = minimal_polynomial(2*cos(2*pi*k/n), x)
        d = Poly(mp, x).degree()
        maxdeg = max(maxdeg, d)
print("max trace-field degree over allowed orders:", maxdeg)

# --- 5. signed-sum resonance scan (reducible/Riccati locus honesty check) ---
res = []
for s in itertools.product([1,-1],[1,-1],[1,-1],[1,-1]):
    v = sum(si*ti for si, ti in zip(s, theta))
    if v.q == 1 and int(v) % 2 == 0:
        res.append((s, v))
print("signed sums in 2Z:", [(s, str(v)) for s, v in res])
