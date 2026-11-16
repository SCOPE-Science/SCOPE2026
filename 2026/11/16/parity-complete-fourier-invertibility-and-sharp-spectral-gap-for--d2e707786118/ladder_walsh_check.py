"""Independent exact checks for spanning-tree Walsh kernels on 2-by-n ladders.

Run: python3 check.py
Dependencies: Python standard library only.
"""
from itertools import combinations, product
from math import comb


def edges(n):
    assert n >= 1
    # Vertices 0..n-1 (upper rail), n..2n-1 (lower rail).
    return ([(i, i + 1) for i in range(n - 1)]
            + [(n + i, n + i + 1) for i in range(n - 1)]
            + [(i, n + i) for i in range(n)])


def is_tree(n, es, mask):
    parent = list(range(2*n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for j, (u, v) in enumerate(es):
        if mask >> j & 1:
            a, b = find(u), find(v)
            if a == b:
                return False
            parent[a] = b
    return len({find(i) for i in range(2*n)}) == 1


def spanning_masks(n):
    es = edges(n)
    for ij in combinations(range(len(es)), 2*n - 1):
        mask = sum(1 << i for i in ij)
        if is_tree(n, es, mask):
            yield mask


def fwht(data):
    a = list(data)
    d = 1
    while d < len(a):
        step = d * 2
        for base in range(0, len(a), step):
            for j in range(base, base+d):
                x, y = a[j], a[j+d]
                a[j], a[j+d] = x+y, x-y
        d *= 2
    return a


def spanning_count_recurrence(n):
    if n == 1:
        return 1
    x, y = 1, 4
    for _ in range(3, n+1):
        x, y = y, 4*y-x
    return y


def sign_mask(n, lower_edge_signs=None):
    # All rungs -1, both rails share the same sign on each column edge.
    lower_edge_signs = lower_edge_signs or (1,)*(n-1)
    assert len(lower_edge_signs) == n-1
    result = sum(1 << j for j in range(2*n-2, 3*n-2))
    for j, a in enumerate(lower_edge_signs):
        if a == -1:
            result |= (1 << j) | (1 << (j+n-1))
    return result


def signed_path_laplacian_action(n, weights, vec):
    out = [0]*n
    for i, a in enumerate(weights):
        out[i] += a*(vec[i] - vec[i+1])
        out[i+1] += a*(vec[i+1] - vec[i])
    return out


def bareiss_det(mat):
    a = [list(r) for r in mat]
    nn = len(a)
    if nn == 0:
        return 1
    sign, prev = 1, 1
    for k in range(nn-1):
        if a[k][k] == 0:
            for i in range(k+1, nn):
                if a[i][k]:
                    a[i], a[k] = a[k], a[i]
                    sign *= -1
                    break
            else:
                return 0
        pivot = a[k][k]
        for i in range(k+1, nn):
            for j in range(k+1, nn):
                num = a[i][j]*pivot - a[i][k]*a[k][j]
                assert num % prev == 0
                a[i][j] = num//prev
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]


def signed_tree_cofactor(n, freq):
    ee = edges(n)
    s = 2*n
    l = [[0]*s for _ in range(s)]
    for j, (u, v) in enumerate(ee):
        w = -1 if (freq >> j) & 1 else 1
        l[u][u] += w
        l[v][v] += w
        l[u][v] -= w
        l[v][u] -= w
    return bareiss_det([row[:-1] for row in l[:-1]])


def run():
    for n in range(1, 8):
        masks = list(spanning_masks(n))
        total = spanning_count_recurrence(n)
        assert len(masks) == total, (n, len(masks), total)
        data = [0]*(1 << (3*n-2))
        for m in masks:
            data[m] = 1
        vals = fwht(data)
        assert vals[0] == total and max(map(abs, vals)) == total
        assert all((v-total) % 2 == 0 for v in vals)
        w = vals[sign_mask(n)]
        if n%2:
            assert all(v != 0 for v in vals)
            assert min(map(abs, vals)) == 1
            assert w == (-1)**((n+1)//2)
        else:
            assert w == 0
            assert any(v == 0 for v in vals)
            for a in product((-1,1), repeat=n//2-1):
                rail = []
                for j in range(n-1):
                    rail.append(1 if j%2 == 0 else a[(j-1)//2])
                assert vals[sign_mask(n, rail)] == 0
        print(f'n={n}, trees={len(masks)}, frequencies={len(vals)}, zeros={vals.count(0)}, special={w}')
    for n in range(2, 24, 2):
        m = n//2
        u = [1 if i%4 in (0,3) else -1 for i in range(n)]
        for q in range(1 << (m-1)):
            a = [1 if j%2 == 0 else (-1 if q >> ((j-1)//2)&1 else 1) for j in range(n-1)]
            assert signed_path_laplacian_action(n, a, u) == [2*t for t in u]
    for n in range(1, 14):
        assert signed_tree_cofactor(n, sign_mask(n)) == (0 if n%2 == 0 else (-1)**((n+1)//2))
    print('LADDER_SPANNING_TREE_WALSH_EXACT_CHECKS_PASS')


if __name__ == '__main__':
    run()
