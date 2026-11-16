"""Exact integer checks for Fourier coefficients of wheel spanning-tree indicators.

Uses only the Python standard library. Run: python verify_wheel.py
"""
from itertools import combinations, product


def edges(n):
    return ([(i, (i + 1) % n) for i in range(n)]
            + [(i, n) for i in range(n)])


def all_tree_transform(n):
    es = edges(n)
    signal = [0] * (1 << (2 * n))
    for subset in combinations(range(2 * n), n):
        parent = list(range(n + 1))
        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v
        ok = True
        for j in subset:
            a, b = es[j]
            a, b = root(a), root(b)
            if a == b:
                ok = False
                break
            parent[a] = b
        if ok:
            signal[sum(1 << j for j in subset)] = 1
    count = sum(signal)
    # In-place exact Walsh-Hadamard transform.
    step = 1
    length = len(signal)
    while step < length:
        for start in range(0, length, 2 * step):
            for j in range(start, start + step):
                a, b = signal[j], signal[j + step]
                signal[j], signal[j + step] = a + b, a - b
        step *= 2
    return count, signal


def lucas(m):
    if m == 0:
        return 2
    a, b = 2, 1
    for _ in range(m):
        a, b = b, a + b
    return a


def witness_signs(n, inner, corner):
    """A family of 4^(n/3) distinct singular signings for n divisible by 3."""
    assert n % 3 == 0
    k = n // 3
    assert len(inner) == len(corner) == k
    rim = [0] * n
    spoke = [0] * n
    for j in range(k):
        rim[3*j] = inner[j]
        rim[3*j+1] = corner[j]
        rim[3*j+2] = corner[j]
    for j in range(k):
        spoke[3*j] = corner[j-1]
        spoke[3*j+1] = corner[j]
        spoke[3*j+2] = -corner[j]
    return rim, spoke


def wheel_signed_minor(n, rim, spoke):
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        r = rim[i]
        M[i][i] += r
        M[j][j] += r
        M[i][j] -= r
        M[j][i] -= r
        M[i][i] += spoke[i]
    return M


def bareiss_det(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    div = 1
    for j in range(n-1):
        if a[j][j] == 0:
            for i in range(j+1,n):
                if a[i][j]:
                    a[j],a[i] = a[i],a[j]
                    sign = -sign
                    break
            else:
                return 0
        pivot = a[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                z = a[i][k] * pivot - a[i][j] * a[j][k]
                assert z % div == 0
                a[i][k] = z // div
        for i in range(j+1,n):
            a[i][j] = 0
        div = pivot
    return sign * a[-1][-1]


def main():
    totals = []
    for n in range(3, 10):
        count, spectrum = all_tree_transform(n)
        target_count = lucas(2 * n) - 2
        assert count == target_count, (n,count,target_count)
        zeros = sum(z == 0 for z in spectrum)
        assert (zeros == 0) == (n % 3 != 0), (n,zeros)
        if n % 3 == 0:
            assert all(z % 4 == 0 for z in spectrum)
        else:
            assert all(z & 1 for z in spectrum)
        # Direct check against signed Kirchhoff determinant for selected masks.
        for mask in {0, (1 << (2*n)) - 1, ((1 << (2*n)) - 1) // 3}:
            rim = [-1 if mask & (1 << j) else 1 for j in range(n)]
            spoke = [-1 if mask & (1 << (n+j)) else 1 for j in range(n)]
            assert spectrum[mask] == bareiss_det(wheel_signed_minor(n,rim,spoke))
        totals.append((n,count,zeros))
    print('Exact exhaustive Walsh transform results (n, trees, zeros):',totals)

    for n in [3,6,9,12]:
        k = n//3
        signings = set()
        for row in product((-1,1),repeat=2*k):
            rim,spoke = witness_signs(n,row[:k],row[k:])
            signings.add(tuple(rim + spoke))
            M = wheel_signed_minor(n,rim,spoke)
            x = [1,1,2]*k
            assert all(sum(M[i][j] * x[j] for j in range(n)) == 0
                       for i in range(n))
            if n <= 9:
                assert bareiss_det(M) == 0
        assert len(signings) == 4**k
        print('n=%d: %d distinct explicitly null signed Laplacians verified'
              % (n,len(signings)))
    print('WHEEL_TREE_WALSH_MOD3_EXACT_CHECKS_PASS')


if __name__ == '__main__':
    main()
