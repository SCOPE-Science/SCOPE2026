"""Exact arithmetic checks for a two-stratum serial-pool flux phase diagram.
Run: python3 verify.py. Requires only the Python standard library.
These checks supplement, and do not replace, the analytic proof.
"""
from fractions import Fraction as Q


def add(*polys):
    z = {}
    for p in polys:
        for key, value in p.items():
            z[key] = z.get(key, Q(0)) + value
    return {k: v for k, v in z.items() if v}


def neg(p):
    return {k: -v for k, v in p.items()}


def sub(p, q):
    return add(p, neg(q))


def mul(*polys):
    result = {(0, 0): Q(1)}
    for p in polys:
        nxt = {}
        for (i, j), a in result.items():
            for (k, l), b in p.items():
                key = (i + k, j + l)
                nxt[key] = nxt.get(key, Q(0)) + a * b
        result = {k: v for k, v in nxt.items() if v}
    return result


C = lambda n: {(0, 0): Q(n)}
V = {(1, 0): Q(1)}
R = {(0, 1): Q(1)}
# Exact numerator of the logarithmic derivative, times its positive denominator:
# -1/(R-v)+3/(v+1)-1/(v-1)-3/(v+R).
L = add(
    neg(mul(sub(V,C(1)),add(V,C(1)),add(V,R))),
    mul(C(3),sub(R,V),sub(V,C(1)),add(V,R)),
    neg(mul(sub(R,V),add(V,C(1)),add(V,R))),
    neg(mul(C(3),sub(R,V),sub(V,C(1)),add(V,C(1)))),
)
quad = add(mul(C(2),V,V),neg(mul(add(R,C(1)),V)),mul(C(2),R))
T = neg(mul(C(2),sub(R,C(1)),quad))
assert L == T, (L, T)


def deriv(x, r, w):
    x = Q(x)
    r = Q(r)
    w = Q(w)
    return w*(1-x)/(x+1)**3 + (1-w)*(r-x)/(x+r)**3


def flux(x, r, w):
    x, r, w = Q(x), Q(r), Q(w)
    return w*x/(x+1)**2 + (1-w)*x/(x+r)**2


def H(x, r):
    x, r = Q(x), Q(r)
    return (r-x)*(x+1)**3 / ((x-1)*(x+r)**3)


r = Q(20)
w = Q(1,20)
k = w/(1-w)
assert H(Q(5,2),r) == Q(2401,54675)
assert H(Q(8),r) == Q(2187,38416)
assert H(Q(5,2),r) < k < H(Q(8),r)
assert [(deriv(x,r,w)>0) for x in [Q(1),Q(2),Q(5),Q(8),Q(12),Q(20)]] == [True, False, False, True, False, False]
# Three certified disjoint intervals of derivative zero, with one peak in each outer interval.
for left,right in ((Q(1),Q(2)),(Q(5),Q(8)),(Q(8),Q(12))):
    assert deriv(left,r,w)*deriv(right,r,w)<0

# Exact stationarity algebra: F'(x)=0 if and only if w/(1-w)=H(x), 1<x<R.
for r0 in [Q(2),Q(8),Q(20),Q(100)]:
    for j in range(1,20):
        x = Q(1)+(r0-1)*Q(j,20)
        for w0 in [Q(1,20),Q(1,2),Q(19,20)]:
            lhs = deriv(x,r0,w0)
            rhs = (1-w0)*(x-1)/(x+1)**3*(H(x,r0)-w0/(1-w0))
            assert lhs == rhs

# Exactly conserved two-stage material flow, for realistic conversion <= total non-flushing loss.
for i, a, rate, intake, v in [(1,Q(1),Q(1,3),Q(3),Q(2)),
                             (2,Q(20),Q(4),Q(5),Q(7))]:
    substrate = intake/(a+v)
    methane = rate*substrate/(a+v)
    assert intake-(rate+(a-rate)+v)*substrate == 0
    assert rate*substrate-(a+v)*methane == 0
    assert v*methane == intake*rate*v/(a+v)**2

# Low- and high-flow limits are zero; positivity and stationary crossings are analytic.
assert all(flux(x,r,w)>0 for x in (Q(1,100),Q(1),Q(5),Q(20),Q(10000)))
print('PASS: exact bivariate logarithmic-derivative identity, witness window,')
print('stationarity equivalence, three separated sign changes, and pool balances')
