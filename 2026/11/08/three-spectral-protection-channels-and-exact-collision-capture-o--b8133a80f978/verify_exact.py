"""Exact finite-field checks for the balanced multipartite two-boson loss theorem.

Only Python's standard library is needed.  Rank is computed modulo a prime;
the theorem's infinite-family proof is independent of this finite check.
"""


def rank_mod(rows, prime=1000003):
    A = [[v % prime for v in row] for row in rows]
    nrow = len(A)
    ncol = len(A[0]) if A else 0
    rank = 0
    for c in range(ncol):
        pivot = next((i for i in range(rank, nrow) if A[i][c]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][c], -1, prime)
        A[rank] = [(x * inv) % prime for x in A[rank]]
        for i in range(rank + 1, nrow):
            val = A[i][c]
            if val:
                A[i] = [(x - val * y) % prime for x, y in zip(A[i], A[rank])]
        rank += 1
    return rank


def finite_case(q, m):
    N = q * m
    pairs = [(i, j) for i in range(N) for j in range(i, N)]
    ix = {pair: k for k, pair in enumerate(pairs)}
    n = len(pairs)
    H = [[0] * n for _ in range(n)]
    for k, (i, j) in enumerate(pairs):
        if i == j:
            for v in range(N):
                if v // m != i // m:
                    H[ix[tuple(sorted((i, v)))]][k] += 1
        else:
            for v in range(N):
                if v // m != i // m:
                    H[ix[tuple(sorted((v, j)))]][k] += 2 if v == j else 1
                if v // m != j // m:
                    H[ix[tuple(sorted((i, v)))]][k] += 2 if v == i else 1
    D = [[0] * n for _ in range(N)]
    for v in range(N):
        D[v][ix[(v, v)]] = 1

    r = m if m >= 3 else 1
    t = q * (m - 1)
    expected = [t * (t + 1) // 2 - q * r,
                q * (q - 2) * (m - 1),
                q * (q - 3) // 2, 0, 0, 0]
    energies = [0, -m, -2*m, (q-1)*m, (q-2)*m, 2*(q-1)*m]
    found = []
    for energy in energies:
        K = [[H[i][j] - (energy if i == j else 0) for j in range(n)]
             for i in range(n)] + D
        found.append(n - rank_mod(K))
    assert found == expected, (q, m, expected, found)
    print(f'PASS exact modular rank: q={q}, m={m}; sector nullities={found}; total={sum(found)}')


if __name__ == '__main__':
    for q, m in [(3,2), (4,2), (3,3), (4,3), (5,2)]:
        finite_case(q, m)
