"""Bounded recovery/evidence script: Hilbert numerators (=reg) and BS-chain window sizes.
Run: python3 hilbert_check.py
"""
import math

def hilb(m, n, D):
    return [math.comb(m + d - 1, d) * math.comb(n + d - 1, d) for d in range(D + 1)]

def h_vector(m, n, terms=25):
    dim = m + n - 1
    H = hilb(m, n, terms)
    h = []
    for d in range(terms):
        s = 0
        for k in range(min(d, dim) + 1):
            s += ((-1) ** k) * math.comb(dim, k) * H[d - k]
        h.append(s)
    return h

def count_poset(m, n, reg):
    c = (m - 1) * (n - 1)
    def dp(pos, last):
        if pos > c:
            return 1
        return sum(dp(pos + 1, v) for v in range(last, reg + 1))
    return sum(dp(2, v) for v in range(1, reg + 1))

if __name__ == "__main__":
    for m, n in [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4)]:
        h = h_vector(m, n)
        nz = [i for i, v in enumerate(h) if v != 0]
        print(m, n, "h=", h[:12], "deg_h=", max(nz))
    print("poset sizes (reg=m-1):")
    for m, n in [(2, 2), (2, 3), (3, 3), (3, 4), (3, 5), (4, 4), (5, 5)]:
        print(m, n, "c=", (m - 1) * (n - 1), "count=", count_poset(m, n, m - 1))
