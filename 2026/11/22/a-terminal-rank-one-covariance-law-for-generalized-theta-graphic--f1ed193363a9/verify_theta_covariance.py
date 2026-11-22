"""Exact integer checks for the theta-path graphical zonotope covariance formula.
Run with Python 3; no third-party packages required.
"""
from itertools import combinations, product


def check(lengths):
    r = len(lengths)
    assert r >= 3 and all(ell >= 2 for ell in lengths)
    n = 2 + sum(ell - 1 for ell in lengths)
    m = sum(lengths)
    columns = []
    edges = []
    next_vertex = 2
    for ell in lengths:
        path = [0] + list(range(next_vertex, next_vertex + ell - 1)) + [1]
        next_vertex += ell - 1
        block = []
        for a, b in zip(path, path[1:]):
            e = [0] * n
            e[a], e[b] = 1, -1
            block.append(e)
            edges.append(e)
        columns.append(block)
    q = [1 << ell for ell in lengths]
    A = [v - 1 for v in q]
    D = [v - 2 for v in q]

    def prod(items):
        p = 1
        for item in items:
            p *= item
        return p

    N = 2 * prod(A) - prod(D)
    alphaN = [2 * (prod(D[j] for j in range(r) if j != i)
                    - prod(A[j] for j in range(r) if j != i))
              for i in range(r)]
    betaN = {(i,j): 2 * prod(A[k] for k in range(r) if k != i and k != j)
             for i, j in combinations(range(r), 2)}
    gammaN = sum(alphaN) + 2 * sum(betaN.values())
    # N times 4 Cov(V) = sum_i (N-alphaN_i) L_i + gammaN vv^T.
    expectation_numer = [[0] * n for _ in range(n)]
    for i, block in enumerate(columns):
        for e in block:
            for a in range(n):
                for b in range(n):
                    expectation_numer[a][b] += (N - alphaN[i]) * e[a] * e[b]
    v = [1, -1] + [0] * (n-2)
    for a in range(n):
        for b in range(n):
            expectation_numer[a][b] += gammaN*v[a]*v[b]

    obs = [[0]*n for _ in range(n)]
    count = 0
    edges_per_arm = []
    st = 0
    for ell in lengths:
        edges_per_arm.append((st, st+ell))
        st += ell
    for bits in product((-1, 1), repeat=m):
        coherent = set()
        for start, end in edges_per_arm:
            if all(bits[i] == bits[start] for i in range(start, end)):
                coherent.add(bits[start])
        if len(coherent) == 2:
            continue
        count += 1
        u = [sum(bits[j]*edges[j][a] for j in range(m)) for a in range(n)]
        for a in range(n):
            for b in range(n):
                obs[a][b] += u[a]*u[b]
    assert count == N, (lengths, count, N)
    assert obs == expectation_numer, (lengths, obs, expectation_numer)
    print(f"PASS paths={tuple(lengths)}; vertices={count}; coordinates={n}; trace_num={sum(obs[i][i] for i in range(n))}")


if __name__ == '__main__':
    for args in ((2,2,2), (2,2,3), (2,3,4), (3,3,3), (2,2,2,2),
                 (2,2,2,3), (2,2,2,2,2), (2,2,2,2,2,2)):
        check(args)
    print('THETA_MULTIARM_COVARIANCE_EXACT_PASS')
