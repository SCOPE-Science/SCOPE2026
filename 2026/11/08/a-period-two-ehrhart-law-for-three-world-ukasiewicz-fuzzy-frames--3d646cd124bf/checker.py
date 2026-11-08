"""Reproduce the exact three-world Lukasiewicz preorder Ehrhart census.

Requires only Python 3 standard library. This is a finite, exact-arithmetic
certificate for the vertex denominators and interpolation sample counts;
the use of Ehrhart's theorem in the proof is mathematical, not empirical.
"""
from fractions import Fraction
from itertools import combinations, product

N = 6
INEQUALITIES = []
for j in range(N):
    lo = [0] * N; lo[j] = -1
    hi = [0] * N; hi[j] = 1
    INEQUALITIES.extend([(lo, 0), (hi, 1)])
# Coordinates: (d12, d21, d23, d32, d13, d31).
for i, j, k in [(4,0,2), (5,3,1), (0,4,3),
                (1,2,5), (2,1,4), (3,5,0)]:
    coeffs = [0] * N
    coeffs[i] = 1; coeffs[j] = -1; coeffs[k] = -1
    INEQUALITIES.append((coeffs, 0))
assert len(INEQUALITIES) == 18

def unique_solution(index_set):
    """Exact rational forward elimination and back substitution."""
    a = [[Fraction(c) for c in INEQUALITIES[i][0]] +
         [Fraction(INEQUALITIES[i][1])] for i in index_set]
    for i in range(N):
        pivot_row = next((j for j in range(i, N) if a[j][i]), None)
        if pivot_row is None:
            return None
        a[pivot_row], a[i] = a[i], a[pivot_row]
        pivot = a[i][i]
        for j in range(i+1, N):
            if not a[j][i]:
                continue
            factor = a[j][i] / pivot
            for col in range(i+1, N+1):
                a[j][col] -= factor * a[i][col]
            a[j][i] = 0
    x = [Fraction(0)] * N
    for i in range(N-1, -1, -1):
        x[i] = (a[i][N] - sum(a[i][j] * x[j] for j in range(i+1, N))) / a[i][i]
    return tuple(x)

def vertices():
    out = set()
    independent_bases = 0
    for active in combinations(range(len(INEQUALITIES)), N):
        x = unique_solution(active)
        if x is None:
            continue
        independent_bases += 1
        if all(sum(cj*xj for cj,xj in zip(coefs,x)) <= rhs
               for coefs,rhs in INEQUALITIES):
            out.add(x)
    return out, independent_bases

def finite_sum(m):
    total = 0
    for a,b,c,d in product(range(m+1), repeat=4):
        e_count = min(m, a+c) - max(0,a-d,c-b) + 1
        f_count = min(m, b+d) - max(0,b-c,d-a) + 1
        assert e_count >= 1 and f_count >= 1
        total += e_count*f_count
    return total

def polynomial(m):
    numerator = (54*m**6 + 324*m**5 + 875*m**4 +
                 1340*m**3 + 1236*m**2 + 656*m + 160)
    # At odd m subtract 1/32 from the polynomial for even m.
    numerator -= 5*(m % 2)
    assert numerator % 160 == 0
    return numerator // 160

def direct_count(m):
    out = 0
    for x in product(range(m+1), repeat=N):
        if all(sum(cj*xj for cj,xj in zip(coefs,x)) <= m*rhs
               for coefs,rhs in INEQUALITIES):
            out += 1
    return out

if __name__ == '__main__':
    vs, bases = vertices()
    fractional = {tuple(2*x for x in v) for v in vs
                  if any(z.denominator != 1 for z in v)}
    assert len(vs) == 31, len(vs)
    assert bases == 4704, bases
    assert fractional == {(1,2,1,2,2,1),(2,1,2,1,1,2)}, fractional
    assert len(vs) - len(fractional) == 29
    assert {x.denominator for v in vs for x in v} == {1, 2}
    samples = [finite_sum(m) for m in range(14)]
    assert samples == [1,29,281,1490,5533,16281,40693,90152,
                       182045,341585,603877,1016226,1640689,2556869]
    assert all(samples[m] == polynomial(m) for m in range(14))
    for m in range(4):
        assert direct_count(m) == samples[m]
    print('LUKASIEWICZ_THREE_WORLD_EXACT_CHECKS_OK',
          'vertices=', len(vs), 'independent_bases=', bases,
          'samples=', len(samples))
