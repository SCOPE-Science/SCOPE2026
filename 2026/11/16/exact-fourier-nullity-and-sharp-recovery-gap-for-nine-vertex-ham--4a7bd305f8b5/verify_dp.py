"""Exact Held--Karp verification of selected signed Hamilton path multipliers.
No nonstandard modules are used. Vertex labels are 1 through 8.
"""
from itertools import combinations
from math import factorial


def signed_path_sum(n, negative_edges):
    neg = {tuple(sorted(edge)) for edge in negative_edges}
    assert all(1 <= a < b <= n for a, b in neg)
    dp = [[0] * n for _ in range(1 << n)]
    for u in range(n):
        dp[1 << u][u] = 1
    for mask in range(1, 1 << n):
        for end in range(n):
            count = dp[mask][end]
            if not count:
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                a, b = sorted((end + 1, nxt + 1))
                dp[mask | (1 << nxt)][nxt] += count * (-1 if (a, b) in neg else 1)
    total = sum(dp[-1])
    assert total % 2 == 0
    return total // 2


def run():
    for n in range(3, 9):
        assert signed_path_sum(n, ()) == factorial(n) // 2
    # A low-support K_9 spectral zero; all eight root-star edges are positive.
    support = {(1, 2), (1, 3), (1, 4), (5, 6)}
    assert signed_path_sum(8, support) == 0
    # K_9 single-negative-edge multiplier is also checked directly.
    assert signed_path_sum(8, {(1, 2)}) == 10080
    print("Held--Karp signed-path verification: PASS; K_9 four-edge zero confirmed")


if __name__ == "__main__":
    run()
