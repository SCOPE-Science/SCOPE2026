"""Exact rational verification of a four-cell paired tent map."""
import sympy as sp

z = sp.symbols('z')
I = [(sp.Integer(-1), -sp.Rational(1, 2)),
     (-sp.Rational(1, 2), sp.Integer(0)),
     (sp.Integer(0), sp.Rational(1, 2)),
     (sp.Rational(1, 2), sp.Integer(1))]
slopes = [3, -3, -3, 3]
intercepts = [2, -1, 1, -2]
image_ranges = []
for j, (low, high) in enumerate(I):
    endpoints = [slopes[j] * w + intercepts[j] for w in (low, high)]
    image_ranges.append((min(endpoints), max(endpoints)))
cover = [[j for j, (low, high) in enumerate(image_ranges)
          if low <= I[i][0] and I[i][1] <= high] for i in range(4)]
assert cover == [[0, 1], [0, 1, 2, 3], [0, 1, 2, 3], [2, 3]]

# The 4-state transition matrix acts on the stationary cell itinerary.
P = sp.Matrix([[sp.Rational(1, 3) if j in cover[i] else 0
                for i in range(4)] for j in range(4)])
assert P == sp.Matrix([[1, 1, 1, 0], [1, 1, 1, 0],
                      [0, 1, 1, 1], [0, 1, 1, 1]]) / 3
pi = sp.Matrix([[sp.Rational(1, 6), sp.Rational(1, 3),
                 sp.Rational(1, 3), sp.Rational(1, 6)]])
assert pi * P == pi and all(v > 0 for v in P ** 2)
Q = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)],
               [sp.Rational(1, 3), sp.Rational(2, 3)]])
for j in range(4):
    assert sum(P[j, i] for i in range(2)) == Q[j // 2, 0]
    assert sum(P[j, i] for i in range(2, 4)) == Q[j // 2, 1]

rho = [sp.Rational(1, 3), sp.Rational(2, 3),
       sp.Rational(2, 3), sp.Rational(1, 3)]
assert sum((b - a) * rho[j] for j, (a, b) in enumerate(I)) == 1
assert [sp.Rational(1, 2) * rho[j] for j in range(4)] == list(pi)

# For density a_j+b_j*x on each source cell, the PF image is affine on
# each target cell, with coefficients computed by exact inverse branches.
L = sp.zeros(8)
for i, sources in enumerate(cover):
    for j in sources:
        L[2 * i, 2 * j] += sp.Rational(1, 3)
        L[2 * i, 2 * j + 1] += -sp.Rational(intercepts[j], 3 * slopes[j])
        L[2 * i + 1, 2 * j + 1] += sp.Rational(1, 3 * slopes[j])

h0 = sp.zeros(8, 1)
hS = sp.zeros(8, 1)
wX = sp.zeros(1, 8)
wS = sp.zeros(1, 8)
for j, (a, b) in enumerate(I):
    sg = -1 if j < 2 else 1
    h0[2 * j] = rho[j]
    hS[2 * j] = rho[j] * sg
    wX[0, 2 * j] = (b ** 2 - a ** 2) / 2
    wX[0, 2 * j + 1] = (b ** 3 - a ** 3) / 3
    wS[0, 2 * j] = sg * (b - a)
    wS[0, 2 * j + 1] = sg * (b ** 2 - a ** 2) / 2
assert L * h0 == h0
assert wX * h0 == sp.zeros(1, 1)
assert wS * h0 == sp.zeros(1, 1)
assert (wX * L ** 0 * h0)[0] == 0

hX = sp.zeros(8, 1)
for j in range(4):
    hX[2 * j + 1] = rho[j]

B = (sp.eye(8) - z * L).inv()
G = {'XX': (wX * B * hX)[0],
     'SS': (wS * B * hS)[0],
     'S0_Xn': (wX * B * hS)[0],
     'X0_Sn': (wS * B * hX)[0]}

expected = {'XX': 3 / (4 * (3 - z)),
            'SS': 3 / (3 - z),
            'S0_Xn': (4 * z + 15) / (12 * (3 - z)),
            'X0_Sn': (z + 45) / (4 * (3 - z) * (z + 9))}
for name, form in expected.items():
    assert sp.cancel(G[name] - form) == 0, name

for n in range(16):
    xx = sp.Rational(1, 4 * 3 ** n)
    ss = sp.Rational(1, 3 ** n)
    sx = sp.Rational(5, 12) if n == 0 else sp.Rational(3, 4 * 3 ** n)
    xs = sp.Rational(1, 3 ** (n + 1)) + sp.Rational((-1) ** n, 12 * 9 ** n)
    assert (wX * L ** n * hX)[0] == xx
    assert (wS * L ** n * hS)[0] == ss
    assert (wX * L ** n * hS)[0] == sx
    assert (wS * L ** n * hX)[0] == xs
    if n:
        assert sx - xs > 0

assert sp.cancel(2 * sp.cancel(G['XX']).subs(z, 1) - sp.Rational(3, 4)) == 0
assert sp.cancel(2 * sp.cancel(G['SS']).subs(z, 1) - 3) == 0
assert sp.factor(L.charpoly(z).as_expr()) == z**4*(z-1)*(3*z-1)*(9*z-1)*(9*z+1)/243
for n in range(1, 11):
    Vx = n * sp.Rational(1, 4) + sum(
        2 * (n - k) * sp.Rational(1, 4 * 3**k) for k in range(1, n))
    Vs = n + sum(2 * (n - k) * sp.Rational(1, 3**k) for k in range(1, n))
    assert Vx == sp.Rational(n, 2) - sp.Rational(3, 8) * (1 - sp.Rational(1, 3**n))
    assert Vs == 2 * n - sp.Rational(3, 2) * (1 - sp.Rational(1, 3**n))
print('PASS: exact four-cell Markov law, stationary density, four generating functions, 16 lags, time direction and finite variance.')
