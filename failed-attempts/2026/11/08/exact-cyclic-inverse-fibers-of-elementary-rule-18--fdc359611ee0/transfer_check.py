"""Independent adjacency-matrix verification of Rule 18 cyclic fibers."""
from random import Random


def fib(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def formula(bits):
    n = len(bits)
    indices = [i for i, v in enumerate(bits) if v]
    if not indices:
        a, b = 2, 1
        for _ in range(n):
            a, b = b, a + b
        return a + 1
    if len(indices) % 2:
        return 0
    t = len(indices)
    gaps = [(indices[(i + 1) % t] - indices[i] - 1) % n for i in range(t)]
    ans = 0
    for k in (0, 1):
        p = 1
        for j in range(k, t, 2):
            p *= fib(gaps[j])
        ans += p
    return ans


def matrices():
    A = [[[0] * 4 for _ in range(4)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                output = int((a, b, c) in ((0, 0, 1), (1, 0, 0)))
                A[output][2 * a + b][2 * b + c] = 1
    return A


def transfer(bits, A):
    M = [[int(i == j) for j in range(4)] for i in range(4)]
    for v in bits:
        B = A[v]
        M = [[sum(M[i][k] * B[k][j] for k in range(4)) for j in range(4)]
             for i in range(4)]
    return sum(M[i][i] for i in range(4))


def main():
    A = matrices()
    for n in range(1, 13):
        for mask in range(1 << n):
            bits = [(mask >> i) & 1 for i in range(n)]
            assert formula(bits) == transfer(bits, A), (n, mask)
    rng = Random(271828)
    for n in (13, 20, 35, 60, 100, 180):
        patterns = [[0] * n, [1] * n,
                    [i % 2 for i in range(n)],
                    [int(i % 3 == 0) for i in range(n)]]
        patterns += [[rng.getrandbits(1) for _ in range(n)] for _ in range(200)]
        for bits in patterns:
            assert formula(bits) == transfer(bits, A), (n, bits)
    print('TRANSFER_OK: exact trace equality for all n<=12 and 1224 length 13..180 test words')


if __name__ == '__main__':
    main()
