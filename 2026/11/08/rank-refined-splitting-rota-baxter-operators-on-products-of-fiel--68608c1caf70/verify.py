"""Independent small-case checks for splitting Rota--Baxter rank counts.

Run: python3 verify.py
No third-party dependencies. Finite tests corroborate but do not prove the theorem.
"""
from collections import Counter
from itertools import product
from math import comb


def expected(n):
    out = {}
    for k in range(n + 1):
        w = n - k
        tau = 1 if k in (0, n) else (n + 1) * (w + 1) ** (k - 1) * (k + 1) ** (w - 1)
        out[k] = comb(n, k) * tau
    return out


def brute_matrices(n, prime):
    """Enumerate all candidates constrained only by the diagonal RB equation.

    Each row has diagonal entry 0 or -1; its other entries lie in
    {0,1} or {0,-1}, respectively. This follows by substituting
    x=y=e_i into the defining identity. Test the full RB identity
    and split idempotency independently.
    """
    freq = Counter()
    total_rb = 0
    for bits in range(1 << (n * n)):
        row_bits = [[(bits >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        mat = [[(prime - 1) * row_bits[i][j] if i == j or row_bits[i][i] else row_bits[i][j]
                for j in range(n)] for i in range(n)]
        good = True
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    lhs = mat[i][k] * mat[j][k]
                    rhs = mat[i][j] * mat[j][k] + mat[j][i] * mat[i][k] + (i == j) * mat[i][k]
                    if (lhs - rhs) % prime:
                        good = False
                        break
                if not good:
                    break
            if not good:
                break
        if not good:
            continue
        total_rb += 1
        if all((sum(mat[i][h] * mat[h][j] for h in range(n)) + mat[i][j]) % prime == 0
               for i in range(n) for j in range(n)):
            # -R is an idempotent, so its rank equals its trace.
            freq[sum(mat[i][i] == prime - 1 for i in range(n))] += 1
    return total_rb, dict(freq)


def tree_edges_from_prufer(seq, nvertices):
    deg = [1] * nvertices
    for a in seq:
        deg[a] += 1
    edges = []
    for a in seq:
        leaf = next(i for i in range(nvertices) if deg[i] == 1)
        edges.append((leaf, a))
        deg[leaf] -= 1
        deg[a] -= 1
    left = [i for i in range(nvertices) if deg[i] == 1]
    edges.append((left[0], left[1]))
    return edges


def brute_trees(n):
    """Independently enumerate Cayley trees and proper colored rooted forests."""
    hist = Counter()
    for seq in product(range(n + 1), repeat=n - 1):
        edges = tree_edges_from_prufer(seq, n + 1)
        for color in product(range(2), repeat=n):
            if all(u == 0 or v == 0 or color[u - 1] != color[v - 1]
                   for u, v in edges):
                hist[sum(color)] += 1
    return dict(hist)


def main():
    for p, n in [(2, 1), (2, 2), (3, 2), (2, 3), (3, 3), (2, 4), (3, 4)]:
        total, hist = brute_matrices(n, p)
        wanted = expected(n)
        assert total == 2 ** n * (n + 1) ** (n - 1), (n, p, total)
        assert hist == wanted, (n, p, hist, wanted)
        print('MATRIX_OK', p, n, hist)
    for n in range(1, 6):
        hist = brute_trees(n)
        wanted = expected(n)
        assert hist == wanted, (n, hist, wanted)
        assert sum(hist.values()) == 2 * (n + 2) ** (n - 1)
        print('TREE_OK', n, hist)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
