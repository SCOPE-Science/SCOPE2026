"""Independent finite numerical checks of a spectral matrix certificate on spider powers.

Requires only Python 3 standard library. Not an infinite proof; see RESULT.md.
"""
import math


def matrix_test(m, ell, k):
    n = m * ell + 1
    neigh = [[] for _ in range(n)]
    for arm in range(m):
        start = 1 + arm * ell
        edges = [(0, start)] + [(start + t, start + t + 1) for t in range(ell - 1)]
        for a, b in edges:
            neigh[a].append(b)
            neigh[b].append(a)
    roots = [2.0 * math.cos(j * math.pi / (ell + 1)) for j in range(1, k + 1)]
    assert roots[-1] >= -1e-12
    # Columns of p(A) via successive multiplication by (A-lambda_j I).
    columns = []
    for source in range(n):
        v = [float(t == source) for t in range(n)]
        for root in roots:
            v = [sum(v[w] for w in neigh[u]) - root * v[u] for u in range(n)]
        columns.append(v)
    distances = []
    for source in range(n):
        d = [-1] * n
        d[source] = 0
        queue = [source]
        for u in queue:
            for w in neigh[u]:
                if d[w] < 0:
                    d[w] = d[u] + 1
                    queue.append(w)
        distances.append(d)
    for u in range(n):
        for v in range(u + 1, n):
            d = distances[u][v]
            x = columns[u][v]
            if d <= k:
                assert (-1) ** (k - d) * x > 1e-7, (m, ell, k, u, v, d, x)
            else:
                assert abs(x) < 1e-7, (m, ell, k, u, v, d, x)
            assert abs(columns[u][v] - columns[v][u]) < 1e-7
    # Check each of the k(m-1) explicitly independent eigenvectors in the kernel.
    for j, root in enumerate(roots, start=1):
        f = [math.sin(j * math.pi * t / (ell + 1)) for t in range(1, ell + 1)]
        for arm in range(m - 1):
            w = [0.0] * n
            for t in range(ell):
                w[1 + arm * ell + t] = f[t]
                w[1 + (m - 1) * ell + t] = -f[t]
            for u in range(n):
                assert abs(sum(columns[v][u] * w[v] for v in range(n))) < 1e-7
    return n


def main():
    tests = 0
    for k in range(3, 7):
        for ell in range(2 * k - 1, 2 * k + 2):
            for m in (3, 4):
                matrix_test(m, ell, k)
                tests += 1
    print('SPECTRAL_SUPPORT_AND_KERNEL_OK', tests)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
