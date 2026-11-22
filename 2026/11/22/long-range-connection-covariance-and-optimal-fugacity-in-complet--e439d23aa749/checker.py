"""Exact, self-contained small-size checks for two disjoint connectivity events.

The complete all-size argument is the one-bridge decomposition in RESULT.md;
finite enumeration is an independent check, not the infinite proof.
"""
from fractions import Fraction
from itertools import product


def rhs(n, t):
    d = 1 + 2 * t
    return 4 * t**5 * (2*n*t**2 + n*t + 4*t + 4) / (d**4 * (n*t**2 + d)**2)


def brute(n, t):
    # Hubs 0 and 1, leaves 2 through n+1; four observed leaves 2,3,4,5.
    edges = [(h, 2 + j) for h in range(2) for j in range(n)]
    z = xa = xb = xab = Fraction(0)
    for mask in range(1 << len(edges)):
        parent = list(range(n + 2))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        cyclic = False
        count = 0
        for idx, (a, b) in enumerate(edges):
            if mask & (1 << idx):
                aa, bb = root(a), root(b)
                if aa == bb:
                    cyclic = True
                    break
                parent[aa] = bb
                count += 1
        if cyclic:
            continue
        roots = [root(j) for j in range(n + 2)]
        a = int(roots[2] == roots[3])
        b = int(roots[4] == roots[5])
        w = t**count
        z += w
        xa += w*a
        xb += w*b
        xab += w*a*b
    return xab/z - xa*xb/(z*z)


checks = 0
for n in range(4, 8):
    for t in (Fraction(1, 3), Fraction(1), Fraction(2)):
        assert brute(n, t) == rhs(n, t), (n, t)
        checks += 1

# Independent probability normalization and moment formulas for the exact
# one-bridge mixture; all arithmetic remains rational.
for n in (4, 5, 6, 10, 25, 100):
    for t in (Fraction(1, 7), Fraction(1), Fraction(5, 2)):
        d = 1 + 2*t
        p = t/d
        w0 = d/(d+n*t*t)
        w1 = t*t/(d+n*t*t)
        assert w0 + n*w1 == 1
        mean = w0*(2*p*p) + (n-2)*w1*(4*p*p) + 2*w1*(2*p)
        joint = w0*(4*p**4) + (n-4)*w1*(16*p**4) + 4*w1*(8*p**3)
        assert joint - mean**2 == rhs(n, t)
        checks += 2
print('FOREST_BRIDGE_EXACT_CHECKS_PASSED', checks)
