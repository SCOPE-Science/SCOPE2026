"""Standalone independent verification using forbidden 2x2 matrices and edge-bit flips."""
from collections import Counter


def is_acyclic_matrix(mask, m, n):
    """In a complete bipartite orientation, a directed cycle entails a directed 4-cycle."""
    for i in range(m):
        for k in range(i + 1, m):
            for j in range(n):
                for ell in range(j + 1, n):
                    a = (mask >> (i * n + j)) & 1
                    b = (mask >> (i * n + ell)) & 1
                    c = (mask >> (k * n + j)) & 1
                    d = (mask >> (k * n + ell)) & 1
                    if a == d and b == c and a != b:
                        return False
    return True


def observed(m, n):
    f = is_acyclic_matrix
    ans = Counter()
    for mask in range(1 << (m * n)):
        if f(mask, m, n):
            ans[sum(f(mask ^ (1 << bit), m, n)
                    for bit in range(m * n))] += 1
    return ans


def main():
    target = {
        (2, 2): [0, 0, 0, 8, 6],
        (2, 3): [0, 0, 0, 0, 24, 12, 10],
        (3, 3): [0, 0, 0, 0, 0, 90, 72, 36, 18, 14],
        (3, 4): [0, 0, 0, 0, 0, 0, 312, 360, 192, 96, 60, 24, 22],
        (4, 4): [0] * 7 + [1472, 2304, 1056, 1248, 192, 408, 64, 96, 32, 30],
    }
    for (m, n), seq in target.items():
        h = observed(m, n)
        actual = [h[i] for i in range(len(seq))]
        assert actual == seq, (m, n, actual)
        assert sum(h.values()) == sum(seq)
        print(f'K_{m},{n}: {sum(h.values())} orientations; exact degree profile verified')
    print('LONESUM_MATRIX_CERTIFICATE_PASS')


if __name__ == '__main__':
    main()
