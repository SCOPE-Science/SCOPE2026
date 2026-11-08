"""Finite-step consistency checks for a reset quantum walk.

Run: python3 verify.py
Uses only the Python standard library. These diagnostics do not replace the proof.
"""

import math
import random
from fractions import Fraction

checks = 0


def check(test, message):
    global checks
    assert test, message
    checks += 1


def quantum_returns(ell):
    """Evolve a normalized localized three-state Grover walker, retaining all sites."""
    root = math.sqrt(ell)
    s = [1.0, root, 1.0]
    norm = math.sqrt(ell + 2.0)
    s = [v / norm for v in s]
    coin = [[2.0 * s[i] * s[j] - float(i == j) for j in range(3)] for i in range(3)]
    state = {0: s}
    returns = []
    for t in range(4):
        origin = state.get(0, [0.0, 0.0, 0.0])
        returns.append(sum(v * v for v in origin))
        mass = sum(v * v for pos in state.values() for v in pos)
        check(abs(mass - 1.0) < 2e-12, 'unitarity')
        out = {}
        for x, vec in state.items():
            rotated = [sum(coin[i][j] * vec[j] for j in range(3)) for i in range(3)]
            for i, jump in enumerate((-1, 0, 1)):
                dest = out.setdefault(x + jump, [0.0, 0.0, 0.0])
                dest[i] += rotated[i]
        state = out
    return returns


def quantum_formula(ell):
    x = ell
    return [1.0, x / (x + 2),
            (x**3 - 4*x**2 + 4*x + 8) / (x + 2)**3,
            x*(x**4 - 8*x**3 + 40*x**2 + 32*x + 144) / (x + 2)**5]


def classical_returns(ell):
    q = ell / (ell + 2)
    r = 1 / (ell + 2)
    dist = {0: 1.0}
    vals = []
    for t in range(4):
        vals.append(dist.get(0, 0.0))
        nxt = {}
        for x, a in dist.items():
            for move, prob in [(-1, r), (0, q), (1, r)]:
                nxt[x+move] = nxt.get(x+move, 0.0) + a*prob
        dist = nxt
    return vals


def classical_formula(ell):
    x = ell
    return [1.0, x/(x+2), (x*x+2)/(x+2)**2,
            (x**3+6*x)/(x+2)**3]


def rewards(vals):
    f1 = vals[0]
    f2 = f1 + vals[1]
    f3 = f2 + vals[2]
    f4 = f3 + vals[3]
    a = f3 / 3.0
    b = (f1 / 3.0 + 2.0*f4 / 3.0) / 3.0
    c = (f2 + f4) / 6.0
    return a,b,c


def polynomial_p(x):
    return 3*x**4 - 8*x**3 - 3*x**2 - 28*x + 4


def polynomial_q(x):
    return 3*x**4 + 2*x**3 + 3*x**2 - 20*x - 4


def bisect(f, lo, hi):
    assert f(lo) * f(hi) < 0
    for _ in range(100):
        mid = (lo+hi)/2
        if f(mid)*f(lo) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


alpha = bisect(polynomial_p, .14, .141)
beta = bisect(polynomial_q, 1.608, 1.609)
gamma = (7.0 + math.sqrt(41.0)) / 2.0
p_second = bisect(polynomial_p, 3.624, 3.626)
check(0 < alpha < (7-math.sqrt(41))/2 < beta < p_second < gamma, 'threshold order')

for ell in [1e-4, .01, .14, alpha, .2, .3, .5, 1., beta, 2., 3.6, p_second, 5., gamma, 8., 20., 200.]:
    direct = quantum_returns(ell)
    theoretical = quantum_formula(ell)
    for j in range(4):
        check(abs(direct[j]-theoretical[j]) < 1e-11, 'quantum return formula')
    actual_classical = classical_returns(ell)
    predicted_classical = classical_formula(ell)
    for j in range(4):
        check(abs(actual_classical[j]-predicted_classical[j]) < 1e-12, 'classical return formula')
    q0,q1,q2,q3=theoretical
    d = (ell+2)**5
    check(abs((2*q3-q1-q2) + 8*polynomial_p(ell)/d) < 1e-10, 'first polynomial identity')
    check(abs((q2+q3-2*q1) + 8*polynomial_q(ell)/d) < 1e-10, 'second polynomial identity')
    check(abs((q3-q2) + 8*(ell**2-7*ell+2)*(ell**2+ell+2)/d) < 1e-10, 'third polynomial identity')
    a,b,c = rewards(theoretical)
    expected = ['A' if ell < alpha else 'B' if ell < beta else 'C' if ell < gamma else 'A'][0]
    best = 'ABC'[max(range(3), key=lambda j: (a,b,c)[j])]
    if min(abs(ell-t) for t in (alpha,beta,gamma)) > 1e-8:
        check(best == expected, 'phase regime')
    ca,cb,cc = rewards(predicted_classical)
    check(ca > cb-1e-11 and ca > cc-1e-11, 'classical always deterministic')

rgen = random.Random(43620)
for i in range(2000):
    ell = math.exp(rgen.uniform(-7, 7))
    a,b,c = rewards(quantum_formula(ell))
    v = [rgen.random() for _ in range(3)]
    v = [z/sum(v) for z in v]
    objective = sum(z*w for z,w in zip(v,(a,b,c)))
    check(objective <= max(a,b,c) + 2e-14, 'all constrained laws bounded by a vertex')
    p = [v[1]/3, v[2]/2, v[0], 2*v[1]/3+v[2]/2]
    check(abs(sum(p)-1) < 1e-13, 'law normalized')
    check(abs(sum(j*p[j-1] for j in range(1,5))-3) < 1e-13, 'mean fixed')
    f1=1
    vals=quantum_formula(ell)
    f=[0.0] + [sum(vals[:j]) for j in range(1,5)]
    check(abs(sum(p[j-1]*f[j] for j in range(1,5))/3 - objective) < 2e-13,
          'renewal reward agreement')

for x in [Fraction(1, 7), Fraction(1), Fraction(2), Fraction(5), Fraction(17)]:
    p0=Fraction(1)
    p1=x/(x+2)
    p2=(x**3-4*x*x+4*x+8)/(x+2)**3
    p3=x*(x**4-8*x**3+40*x*x+32*x+144)/(x+2)**5
    P=3*x**4-8*x**3-3*x*x-28*x+4
    Q=3*x**4+2*x**3+3*x*x-20*x-4
    check(2*p3-p1-p2 == -8*P/(x+2)**5, 'rational P identity')
    check(p2+p3-2*p1 == -8*Q/(x+2)**5, 'rational Q identity')
    check(p3-p2 == -8*(x*x-7*x+2)*(x*x+x+2)/(x+2)**5, 'rational third identity')

q = quantum_formula(1.0)
a,b,c = rewards(q)
check(abs(a-5/9)<1e-14, 'example deterministic')
check(abs(b-1471/2187)<1e-14, 'example quantum randomized')
check(abs(c-469/729)<1e-14, 'example other protocol')
ca,cb,cc=rewards(classical_formula(1.0))
check(abs(ca-5/9)<1e-14, 'example classical optimum')
check(ca > cb and ca > cc, 'classical strict advantage')

print(f'PASS: {checks} bounded checks; switch points {alpha:.12f}, {beta:.12f}, {gamma:.12f}')
