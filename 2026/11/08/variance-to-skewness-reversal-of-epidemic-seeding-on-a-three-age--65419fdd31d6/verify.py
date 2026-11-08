"""Exact-algebra checks for a three-node pair-and-triangle SIS map.

Run with Python 3.10+; no third-party dependencies are required.
The analytic proof of global convergence and the invariant-manifold
expansion is given in RESULT.md; finite trajectories are diagnostic only.
"""
from fractions import Fraction as Q
from collections import defaultdict

DIM = 4  # three state coordinates and the recovery parameter
ZERO = (0,) * DIM

class Poly:
    def __init__(self, terms=None):
        self.d = {k: Q(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def c(v):
        return Poly({ZERO: Q(v)})

    @staticmethod
    def variable(i):
        powers = [0] * DIM
        powers[i] = 1
        return Poly({tuple(powers): Q(1)})

    def __add__(self, other):
        other = aspoly(other)
        d = defaultdict(Q)
        for k, v in self.d.items(): d[k] += v
        for k, v in other.d.items(): d[k] += v
        return Poly(d)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        return self + -aspoly(other)

    def __rsub__(self, other):
        return aspoly(other) - self

    def __mul__(self, other):
        other = aspoly(other)
        d = defaultdict(Q)
        for a, av in self.d.items():
            for b, bv in other.d.items():
                d[tuple(i + j for i, j in zip(a, b))] += av * bv
        return Poly(d)

    __rmul__ = __mul__

    def __pow__(self, k):
        assert isinstance(k, int) and k >= 0
        result = Poly.c(1)
        for _ in range(k): result = result * self
        return result

    def deriv(self, i):
        d = defaultdict(Q)
        for powr, v in self.d.items():
            if powr[i]:
                q = list(powr); q[i] -= 1
                d[tuple(q)] += v * powr[i]
        return Poly(d)

    def eval(self, args):
        return sum((v * __import__('math').prod(args[i] ** k for i,k in enumerate(p))
                    for p,v in self.d.items()), Q(0))

    def __eq__(self, other):
        return self.d == aspoly(other).d


def aspoly(x):
    return x if isinstance(x, Poly) else Poly.c(x)

x = [Poly.variable(i) for i in range(3)]
delta = Poly.variable(3)
h = Q(1, 2)
beta = Q(1, 20)


def Fpoly(i):
    j, k = [z for z in range(3) if z != i]
    return x[i] + h * (-delta*x[i] + (1-x[i])*(beta*(x[j]+x[k])+x[j]*x[k]))

F = [Fpoly(i) for i in range(3)]
m = sum(x, Poly.c(0)) * Q(1, 3)
y = [z-m for z in x]
V = sum((z**2 for z in y), Poly.c(0)) * Q(1, 3)
P = y[0]*y[1]*y[2]
f = m + h*m*(-delta + (1-m)*(Q(1, 10)+m))
k = (3*m-Q(9, 10))*Q(1, 4)

checks = 0
assert sum(F, Poly.c(0))*Q(1, 3) == f + k*V-Q(1, 2)*P
checks += 1
for i,j,third in [(0,1,2),(0,2,1),(1,2,0)]:
    fac = 1-h*(delta+beta*(1+x[third])+x[third])
    assert F[i]-F[j] == fac*(x[i]-x[j])
    checks += 1

cases = [
    (Q(9, 50), Q(1, 10), Q(4, 5), Q(8000, 18237)),
    (Q(7, 25), Q(3, 10), Q(3, 5), Q(0)),
    (Q(3, 10), Q(2, 5), Q(1, 2), Q(-1000, 8557)),
]
for d, low, high, wanted_a in cases:
    assert d > Q(1, 10) and d < Q(121, 400)
    assert h*(d+2*beta+1) < 1
    checks += 2
    for p in [Q(0),low,high]:
        args = [p,p,p,d]
        assert all(F[i].eval(args)==p for i in range(3))
        checks += 3
    lam = 1 + h*low*(Q(9, 10)-2*low)
    ell = 1-h*(d+beta*(1+low)+low)
    kk = (3*low-Q(9, 10))*Q(1, 4)
    a = kk/(ell*ell-lam)
    assert 0<ell<1<lam and a == wanted_a
    checks += 1
    args = [low,low,low,d]
    jac = [[F[i].deriv(j).eval(args) for j in range(3)] for i in range(3)]
    assert all(sum(row) == lam for row in jac)
    assert all(jac[i][i]-jac[i][j] == ell for i in range(3) for j in range(3) if j!=i)
    checks += 9

critical = Q(7,25)
low = Q(3,10)
lam = Q(209,200)
ell = Q(271,400)
coefficient = h/(lam-ell**3)
assert coefficient == Q(32000000,46977489)
checks += 1

# Diagnostic trajectories, not an infinite-time certificate.
def advance(initial,d,rounds=2500):
    v = list(map(float, initial))
    for _ in range(rounds):
        nxt=[]
        for i in range(3):
            j,kk=[a for a in range(3) if a!=i]
            nxt.append(v[i]+.5*(-float(d)*v[i]+(1-v[i])*(.05*(v[j]+v[kk])+v[j]*v[kk])))
        v=nxt
    return v

for d, p, expected in [
    (Q(9,50),Q(1,10),0.0),
    (Q(3,10),Q(2,5),.5)]:
    v=advance([float(p)+.02,float(p)-.02,float(p)],d)
    assert max(abs(z-expected) for z in v)<1e-9
    checks += 1

for sign, outcome in [(1,0.0),(-1,.6)]:
    t=.02
    v=advance([.3+sign*2*t,.3-sign*t,.3-sign*t],critical)
    assert max(abs(z-outcome) for z in v)<1e-9
    checks += 1

print(f'VERIFY_OK {checks} exact identities/certificates and finite trajectory diagnostics')
