"""Exact finite edge-identity checks supporting a separate infinite-dimensional proof."""
from fractions import Fraction

checks = 0

def run(A, B, G, L):
    global checks
    A, B = set(A), set(B)
    assert 0 in A and 0 in B and L in A and L in B
    for n in range(L - G + 1):
        assert any(n <= a <= n + G for a in A)
        assert any(n <= b <= n + G for b in B)
        checks += 2
    r = Fraction(1, 4)
    for forward in (True, False):
        edges = [(i, j) for i in A for j in B
                 if (0 <= j-i <= G if forward else 0 <= i-j <= G)]
        assert (0, 0) in edges
        assert all(any(i == a for i, j in edges) for a in A)
        assert all(any(j == b for i, j in edges) for b in B)
        checks += 3
        for i, j in edges:
            d = j-i if forward else i-j
            coeff = Fraction(1, 2) ** d
            assert Fraction(1, 2) ** G <= coeff <= 1
            assert (coeff ** 2 * r ** i == r ** j if forward
                    else coeff ** 2 * r ** j == r ** i)
            checks += 2

for L in (8, 16, 32, 64):
    evens = set(range(0, L + 1, 2))
    A = evens
    B = {0, L} | set(range(1, L, 2))
    run(A, B, 2, L)
    for pattern in range(16):
        A = evens | {2*k+1 for k in range(min(4, L//2)) if (pattern >> k) & 1}
        B = evens | {2*k+1 for k in range(min(4, L//2)) if ((pattern ^ 11) >> k) & 1}
        run(A, B, 2, L)
print(f"SYNDETIC_EXACT_EDGE_IDENTITY_OK {checks}")
