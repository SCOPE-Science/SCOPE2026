from fractions import Fraction as F

# Abstract variance identity.
EA = F(7, 5)
EB = EA
EB2 = F(19, 6)
EAB = EB2
EA2 = F(23, 5)

lhs = EA2 - 2 * EAB + EB2
rhs = (EA2 - EA * EA) - (EB2 - EB * EB)
assert lhs == rhs

# Classical Mackey-Glass slope thresholds.
n = 9.65

def fp(u):
    v = u ** n
    return (1.0 + (1.0 - n) * v) / ((1.0 + v) ** 2)

def g(u):
    return abs(fp(u)) - 0.5

def bisect(a, b, steps=100):
    fa, fb = g(a), g(b)
    assert fa == 0.0 or fb == 0.0 or fa * fb < 0.0
    for _ in range(steps):
        m = 0.5 * (a + b)
        fm = g(m)
        if fa == 0.0:
            return a
        if fm == 0.0:
            return m
        if fa * fm <= 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)

roots = [
    bisect(0.70, 0.77),
    bisect(0.82, 0.88),
    bisect(1.25, 1.40),
]
targets = [0.7356331448588916, 0.8457944676553084, 1.3248837608752877]

for r, t in zip(roots, targets):
    assert abs(r - t) < 1e-9
    assert abs(g(r)) < 1e-10

# Sign structure of the slope-subcritical windows.
assert g(0.80) < 0.0
assert g(1.00) > 0.0
assert g(1.50) < 0.0

print("VERIFY_OK")
