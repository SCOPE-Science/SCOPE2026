"""Exact finite checks for the vertex inertia of biclique nonempty-bond polytopes.
Only the finite cases stated here are tested; the theorem is proved analytically.
"""
from fractions import Fraction
from itertools import product
from math import floor


def moments(p, q):
    P, Q = 1 << p, 1 << q
    C = (P - 2) * (Q - 2) + 2 * (p + q)
    alpha = Fraction(2 * (p + q - 4), C)
    beta_l = Fraction(2 * (p + q - Q - 2), C)
    beta_r = Fraction(2 * (p + q - P - 2), C)
    gamma = Fraction(2 * (p + q - 6), C)
    return C, alpha, beta_l, beta_r, gamma


def predicted(p, q):
    C, a, bl, br, g = moments(p, q)
    interaction = (1 - bl - br + g) / 4
    left = (1 - bl + (q - 1) * (br - g)) / 4
    right = (1 - br + (p - 1) * (bl - g)) / 4
    total = (1 + (q - 1) * br + (p - 1) * bl
             + (p - 1) * (q - 1) * g - p * q * a * a) / 4
    return [total, left, right, interaction]


def enumerate_bonds(p, q):
    # Orientation of the cut is immaterial, so fix the first L spin to 0.
    result = []
    for remaining in product((0, 1), repeat=p + q - 1):
        bits = (0,) + remaining
        a, b = bits[:p], bits[p:]
        ones_l, ones_r = sum(a), sum(b)
        mixed = 0 < ones_l < p and 0 < ones_r < q
        singleton = ones_l + ones_r in (1, p + q - 1)
        if mixed or singleton:
            result.append(tuple(int(a[i] != b[j])
                                for i in range(p) for j in range(q)))
    assert len(result) == len(set(result))
    return result


def verify_covariance(p, q):
    cuts = enumerate_bonds(p, q)
    C, a, bl, br, g = moments(p, q)
    assert len(cuts) * 2 == C
    n = len(cuts)
    m = p * q
    means = [Fraction(sum(v[e] for v in cuts), n) for e in range(m)]
    assert all(x == (1 - a) / 2 for x in means)
    checks = 0
    for e in range(m):
        i, j = divmod(e, q)
        for f in range(m):
            k, h = divmod(f, q)
            empirical = Fraction(sum(v[e] * v[f] for v in cuts), n) - means[e] * means[f]
            if e == f:
                theoretical = (1 - a * a) / 4
            elif i == k:
                theoretical = (br - a * a) / 4
            elif j == h:
                theoretical = (bl - a * a) / 4
            else:
                theoretical = (g - a * a) / 4
            assert empirical == theoretical, (p, q, e, f, empirical, theoretical)
            checks += 1
    # Independently test four invariant subspaces by matrix multiplication.
    d = (1 - a*a)/4; u = (br-a*a)/4; v = (bl-a*a)/4; w = (g-a*a)/4
    mat = [[d if e == f else u if e//q == f//q else v if e%q == f%q else w
            for f in range(m)] for e in range(m)]
    spectral = predicted(p, q)
    vectors = [([1] * m, 0)]
    if p > 1:
        vectors.append(([1 if e//q == 0 else -1 if e//q == 1 else 0 for e in range(m)], 1))
    if q > 1:
        vectors.append(([1 if e%q == 0 else -1 if e%q == 1 else 0 for e in range(m)], 2))
    if p > 1 and q > 1:
        vectors.append(([(1 if e//q == 0 else -1 if e//q == 1 else 0) *
                         (1 if e%q == 0 else -1 if e%q == 1 else 0) for e in range(m)], 3))
    for vec, typ in vectors:
        assert [sum(mat[e][f]*vec[f] for f in range(m)) for e in range(m)] == [spectral[typ]*z for z in vec]
    return len(cuts), checks


def threshold(p):
    # floor[(2^p-4)/p -p +6] +1, using exact integer division.
    return (2**p - 4)//p - p + 7


def delta_numerator(p, q):
    C = (2**p-2)*(2**q-2)+2*(p+q)
    A = p*(p+q-6)-2**p+4
    return A*C-2*p*(p+q-4)**2


def check():
    case_count=vertex_count=entry_count=0
    for p in range(2, 6):
        for q in range(p, 9):
            if p+q > 11:
                continue
            vertices, checks = verify_covariance(p, q)
            case_count += 1; vertex_count += vertices; entry_count += checks
            t = threshold(p)
            a, l, r, z = predicted(p, q)
            assert z >= l >= r and a < l
            assert (a < r) == (q < t), (p,q,t,a,r)
            assert (a > r) == (q >= t)
            assert z > 0 and l > 0 and r > 0
            assert (a == 0) == (p == q == 2)
    phase_count = 0
    for p in range(2, 19):
        t = threshold(p)
        assert t > p
        for q in (p, max(p,t-2), t-1, t, t+1, 2*t):
            H=delta_numerator(p, q)
            assert (H<0) == (q<t)
            assert (H>0) == (q>=t)
            phase_count += 1
    print(f'BICLIQUE_BOND_INERTIA_CHECKS_PASSED cases={case_count} vertices={vertex_count} entries={entry_count} phases={phase_count}')

if __name__ == '__main__':
    check()
