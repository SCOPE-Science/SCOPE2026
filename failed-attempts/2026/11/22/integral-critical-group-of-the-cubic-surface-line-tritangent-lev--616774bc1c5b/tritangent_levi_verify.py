"""Exact arithmetic verification of the line--tritangent Levi graph of a smooth cubic surface.

Run: python3 tritangent_levi_verify.py. Requires only Python's standard library.
"""
from itertools import combinations
from collections import Counter


def build_graph():
    # Divisor coordinates (H,E_0,...,E_5) of the 27 (-1)-curves on Bl_6(P^2).
    curves = []
    for i in range(6):
        curves.append(("E", i, (0,) + tuple(int(j == i) for j in range(6))))
    for i in range(6):
        curves.append(("Q", i, (2,) + tuple(-int(j != i) for j in range(6))))
    for i, j in combinations(range(6), 2):
        curves.append(("L", (i, j), (1,) + tuple(-int(k in (i, j)) for k in range(6))))
    target = (3,) + (-1,) * 6  # The anticanonical divisor.
    planes = [tri for tri in combinations(range(27), 3)
              if tuple(sum(curves[i][2][j] for i in tri) for j in range(7)) == target]
    assert len(planes) == 45
    types = Counter(''.join(sorted(curves[i][0] for i in tri)) for tri in planes)
    assert types == {'ELQ': 30, 'LLL': 15}
    n = 27 + 45
    lap = [[0] * n for _ in range(n)]
    for t, tri in enumerate(planes):
        v = 27 + t
        for i in tri:
            lap[i][i] += 1
            lap[v][v] += 1
            lap[i][v] -= 1
            lap[v][i] -= 1
    assert all(lap[i][i] == 5 for i in range(27))
    assert all(lap[i][i] == 3 for i in range(27, 72))
    # Unique plane containing any two incident lines, and the SRG parameters.
    adjacency = [[sum(int((i in tri) and (j in tri)) for tri in planes)
                  if i != j else 0 for j in range(27)] for i in range(27)]
    assert all(adjacency[i][j] in (0, 1) for i in range(27) for j in range(27))
    assert all(sum(r) == 10 for r in adjacency)
    for i, j in combinations(range(27), 2):
        common = sum(adjacency[i][k] * adjacency[k][j] for k in range(27))
        assert common == (1 if adjacency[i][j] else 5)
    # Explicitly verify graph is connected.
    seen = {0}
    todo = [0]
    for v in todo:
        for w in range(n):
            if w not in seen and lap[v][w] < 0:
                seen.add(w)
                todo.append(w)
    assert len(seen) == 72
    return lap


def padic_smith_values(matrix, p, kmax, transpose_scan=False):
    """Elementary-divisor valuations via invertible local row/column operations.

    All computation takes place in Z/(p**kmax); pivot a unit times p**v,
    v<kmax, and annihilate row and column by exact modular operations.
    """
    order = len(matrix)
    mod = p ** kmax
    mat = [[entry % mod for entry in row] for row in matrix]
    out = []

    def valuation(x):
        if not x:
            return kmax
        v = 0
        while x % p == 0:
            v += 1
            x //= p
        return v

    for z in range(order):
        pivot_val, r, c = kmax, None, None
        indices = ((i, j) for j in range(z, order) for i in range(z, order)) if transpose_scan \
                  else ((i, j) for i in range(z, order) for j in range(z, order))
        for i, j in indices:
            v = valuation(mat[i][j])
            if v < pivot_val:
                pivot_val, r, c = v, i, j
        assert r is not None, 'precision too small for remaining elementary divisors'
        if r != z:
            mat[z], mat[r] = mat[r], mat[z]
        if c != z:
            for row in mat:
                row[z], row[c] = row[c], row[z]
        primepart = p ** pivot_val
        inv = pow(mat[z][z] // primepart, -1, mod // primepart)
        for i in range(z + 1, order):
            a = mat[i][z]
            if a:
                assert a % primepart == 0
                mult = (a // primepart * inv) % (mod // primepart)
                mat[i] = [(b - mult * t) % mod if j >= z else b
                          for j, (b, t) in enumerate(zip(mat[i], mat[z]))]
        for j in range(z + 1, order):
            a = mat[z][j]
            if a:
                assert a % primepart == 0
                mult = (a // primepart * inv) % (mod // primepart)
                for i in range(z, order):
                    mat[i][j] = (mat[i][j] - mult * mat[i][z]) % mod
        assert all(mat[i][z] == 0 for i in range(z + 1, order))
        assert all(mat[z][j] == 0 for j in range(z + 1, order))
        out.append(pivot_val)
    assert out == sorted(out)
    return dict(Counter(out))


def main():
    lap = build_graph()
    # Kirchhoff from N*N^T = 5I + A, A spectrum 10^1,1^20,(-5)^6.
    # Laplacian spectrum 0^1,8^1,(4 +/- sqrt(7))^20,5^6,3^24.
    tree_number = (8 * (16 - 7) ** 20 * 5 ** 6 * 3 ** 24) // 72
    assert 8 * 9 ** 20 * 5 ** 6 * 3 ** 24 == 72 * tree_number
    assert tree_number == 3 ** 62 * 5 ** 6
    targets = {3: {0: 42, 1: 10, 2: 5, 3: 14},
               5: {0: 65, 1: 6}, 2: {0: 71}}
    for sink in (71, 0):
        reduced = [[lap[i][j] for j in range(72) if j != sink]
                   for i in range(72) if i != sink]
        for p, precision in ((3, 65), (5, 10), (2, 5)):
            for reverse in (False, True):
                got = padic_smith_values(reduced, p, precision, reverse)
                assert got == targets[p], (sink, p, reverse, got)
    assert (3 ** (10 + 2*5 + 3*8 + 3*6) * 5 ** 6) == tree_number
    print('CUBIC_SURFACE_TRITANGENT_LEVI_CRITICAL_GROUP_VERIFIED_OK')
    print('27 lines; 45 tritangent planes; 135 flags; 72 vertices; 64 cycle rank')
    print('Tree count = 3^62 * 5^6')
    print('Critical group = (Z/3)^10 + (Z/9)^5 + (Z/27)^8 + (Z/135)^6')
    print('Two sink choices, two pivot-order choices, p=2,3,5 all agree')


if __name__ == '__main__':
    main()
