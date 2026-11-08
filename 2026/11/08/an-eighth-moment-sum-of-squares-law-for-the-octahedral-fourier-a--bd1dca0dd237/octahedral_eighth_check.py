"""Exact finite Fourier-coefficient proof check; Python 3, standard library only.

No floating-point approximation, randomized test, or external data is used.
"""
from collections import defaultdict
from math import factorial


def mul(x, y):
    z = defaultdict(int)
    for a, c in x.items():
        for b, d in y.items():
            z[(a[0] + b[0], a[1] + b[1])] += c * d
    return {k: v for k, v in z.items() if v}


def plus(*polys):
    z = defaultdict(int)
    for p in polys:
        for k, v in p.items():
            z[k] += v
    return {k: v for k, v in z.items() if v}


def scale(p, t):
    return {k: t*v for k, v in p.items() if t*v}


def conjugate(p):
    return {(-a, -b): v for (a, b), v in p.items()}


def absolute_square(p):
    return mul(p, conjugate(p))


one = {(0, 0): 1}
V = {(1, 0): 1}
W = {(0, 1): 1}
q1, q2, q3 = one, mul(V, V), mul(W, W)
S = plus(q1, q2, q3)
T = plus(mul(q1, q1), mul(q2, q2), mul(q3, q3))
Q = plus(mul(q1, q2), mul(q1, q3), mul(q2, q3))

# A coefficient of P^m is a Laurent polynomial in v and w.
chars = [((1,0,0),one), ((-1,0,0),one),
         ((0,1,0),V), ((0,-1,0),V),
         ((0,0,1),W), ((0,0,-1),W)]

def moment(m):
    coeff = {(0,0,0): one}
    for _ in range(m):
        new = defaultdict(dict)
        for freq, poly in coeff.items():
            for step, phase in chars:
                target = tuple(freq[i]+step[i] for i in range(3))
                new[target] = plus(new[target], mul(poly,phase))
        coeff = dict(new)
    out = {}
    for phase_poly in coeff.values():
        out = plus(out, absolute_square(phase_poly))
    return out, len(coeff)

formulas = {
    2: plus(scale(one,54), scale(absolute_square(S),4)),
    3: plus(scale(one,564), scale(absolute_square(S),144)),
    4: plus(scale(one,6390), scale(absolute_square(S),3360),
            scale(absolute_square(plus(T,scale(Q,4))),36))
}
for m in (2,3,4):
    lhs, count = moment(m)
    assert lhs == formulas[m], (m, plus(lhs,scale(formulas[m],-1)))
    value_at_one = sum(lhs.values())
    assert value_at_one == {2:90,3:1860,4:44730}[m]
    print('order',2*m,'frequency_sums',count,'all_equal_moment',value_at_one,
          'exact_laurent_identity_PASS')

# Explicit finite-alphabet minimizer count using the mandatory cubic-root multiset.
for q in (3,6,9):
    root_multisets = sum(1 for i in range(q) for j in range(q) for k in range(q)
         if len({(j-i)%q, (k-i)%q}) == 2
         and {(j-i)%q,(k-i)%q} == {q//3,2*q//3})
    assert root_multisets == 2*q
    assert root_multisets*q**3 == 2*q**4
print('OCTAHEDRAL_EIGHTH_EXACT_PASS')
