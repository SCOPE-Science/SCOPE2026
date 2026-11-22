"""Exact finite corroboration of the chain--antichain twinned-polytope inball theorem.

Usage: python verify_metric.py (requires SymPy). The unrestricted result uses
an analytic proof; this program checks instances and does not certify all d.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, S, sqrt, simplify, N


def sign_exact(expr):
    z = simplify(expr)
    if z == 0:
        return 0
    if z.is_positive:
        return 1
    if z.is_negative:
        return -1
    # SymPy's symbolic assumptions can be incomplete; use a high-precision
    # fallback only for clearly separated strict signs, never equality.
    w = N(z, 75)
    assert abs(w) > S(1) / 10**50, f"indeterminate expression {z}"
    return 1 if w > 0 else -1


def data(d):
    verts = []
    for i in range(d):
        v = [0] * d
        v[i] = 1
        verts.append(tuple(v))
    for k in range(1, d+1):
        for T in combinations(range(d), k):
            v = [0] * d
            for i in T:
                v[i] = -1
            verts.append(tuple(v))
    normals = [tuple([1] * d)]
    for j in range(d):
        for s in range(d):
            for U in combinations([i for i in range(d) if i != j], s):
                u = [0] * d
                for i in U:
                    u[i] = 1
                u[j] = -1
                normals.append(tuple(u))
    return verts, normals


def dot(u, v):
    return sum(i*j for i, j in zip(u, v))


def main():
    a_lo = sqrt(S(1)/2) - 1
    a_hi = 1 - sqrt(S(3)/2)
    assert sign_exact(a_hi - a_lo) == 1
    tested = 0
    for d in range(3, 8):
        verts, normals = data(d)
        assert len(verts) == d + 2**d - 1
        assert len(normals) == 1 + d*2**(d-1)
        assert len(set(verts)) == len(verts)
        assert len(set(normals)) == len(normals)
        tested += 4
        for u in normals:
            h = max(dot(u, v) for v in verts)
            assert h == 1, (d, u, h)
            tested += len(verts)
        # Every listed supporting plane really spans dimension d-1 for d<=5.
        if d <= 5:
            for u in normals:
                touching = [v for v in verts if dot(u, v) == 1]
                diff = [[v[i] - touching[0][i] for i in range(d)] for v in touching[1:]]
                assert Matrix(diff).rank() == d-1, (d, u)
                tested += 1
        for label, a in [('lower',a_lo),('upper',a_hi),('middle',(a_lo+a_hi)/2)]:
            tangencies = 0
            for u in normals:
                su = sum(u)
                norm2 = sum(k*k for k in u)
                slack = 1 - (su*a + sqrt(S(norm2)/2))
                sg = sign_exact(slack)
                assert sg >= 0, (d, label, u, slack)
                tangencies += (sg == 0)
                tested += 1
            pair_count = d*(d-1)
            expected = pair_count + (d if label=='lower' else 0) + (
                d*comb(d-1, 2) if label=='upper' else 0)
            assert tangencies == expected, (d, label, tangencies, expected)
            tested += 1
        # Strict dimension-independent monotonicity and all-ones barriers.
        assert sign_exact(1 - S(5)*sqrt(6)/12) == -1
        assert sign_exact(1 - (d*a_hi + sqrt(S(d)/2))) == 1
        tested += 2
        print(f'd={d}: {len(verts)} vertices, {len(normals)} facets, exact inball and contacts verified')
    print(f'PASS: {tested} finite exact/computational assertions; analytic theorem is all-dimensional.')

if __name__ == '__main__':
    main()
