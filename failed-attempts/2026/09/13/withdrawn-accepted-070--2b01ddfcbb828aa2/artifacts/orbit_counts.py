"""Reproducible orbit-count check for Schanuel vs DLO ledger.

S_inf = Sym(N) orbits on N^n <-> set partitions (equality patterns) -> Bell numbers.
Aut(Q,<) orbits on Q^n <-> weak total orders / preferential arrangements
  (order patterns x_i < x_j /=/ >) -> ordered Bell (Fubini) numbers.

We verify by brute-force enumeration for small n and by closed recurrences,
with the key separation already at n=2: 2 vs 3.
"""
import itertools
from functools import lru_cache


def bell_via_recurrence(n):
    # Bell triangle / Dobinski recurrence B_{n+1} = sum_k C(n,k) B_k
    B = [1]
    from math import comb
    for m in range(n):
        B.append(sum(comb(m, k) * B[k] for k in range(m + 1)))
    return B[n]


def ordered_bell_via_recurrence(n):
    # OB_n = sum_{k=0..n} k! S(n,k); recurrence via S
    # Stirling numbers of the second kind
    S = [[0] * (n + 1) for _ in range(n + 1)]
    S[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            S[i][k] = k * S[i - 1][k] + S[i - 1][k - 1]
    from math import factorial
    return sum(factorial(k) * S[n][k] for k in range(n + 1))


def partitions_bruteforce(n):
    """Enumerate set partitions of {0..n-1} via restricted growth strings."""
    if n == 0:
        yield []
        return

    def rec(i, maxv, cur):
        if i == n:
            yield list(cur)
            return
        for v in range(maxv + 1):
            cur.append(v)
            yield from rec(i + 1, max(maxv, v + 1), cur)
            cur.pop()

    yield from rec(1, 1, [0])


def weak_orders_bruteforce(n):
    """Enumerate weak total orders (total preorders) on n labeled items.

    Represent as rank functions r: [n] -> {0..k-1} surjective (ordered Bell).
    Two rank functions define the same preorder iff they differ by a strictly
    increasing relabeling of ranks; canonical rep = restricted-growth-like with
    gaps forbidden and order matters. Brute force: all maps [n]->[n], quotient
    by order-isomorphism of image.
    """
    if n == 0:
        yield []
        return
    seen = set()
    for f in itertools.product(range(n), repeat=n):
        # canonicalize: replace values by their rank order
        vals = sorted(set(f))
        canon = tuple(vals.index(v) for v in f)
        if canon not in seen:
            # check surjectivity onto 0..k-1 (automatic) and keep
            seen.add(canon)
    yield from (list(s) for s in sorted(seen))


def main():
    print("n | Bell(enum) Bell(rec) | OrdBell(enum) OrdBell(rec)")
    for n in range(0, 6):
        b_enum = sum(1 for _ in partitions_bruteforce(n))
        b_rec = bell_via_recurrence(n)
        ob_enum = sum(1 for _ in weak_orders_bruteforce(n))
        ob_rec = ordered_bell_via_recurrence(n)
        print(f"{n} | {b_enum} {b_rec} | {ob_enum} {ob_rec}")
        assert b_enum == b_rec, (n, b_enum, b_rec)
        assert ob_enum == ob_rec, (n, ob_enum, ob_rec)
    # Key ledger separation at n=2
    assert bell_via_recurrence(2) == 2, "S_inf orbits on N^2 must be 2"
    assert ordered_bell_via_recurrence(2) == 3, "Aut(Q) orbits on Q^2 must be 3"
    # Further values for the table
    assert [bell_via_recurrence(n) for n in range(5)] == [1, 1, 2, 5, 15]
    assert [ordered_bell_via_recurrence(n) for n in range(5)] == [1, 1, 3, 13, 75]
    print("OK: Bell = [1,1,2,5,15,...], OrderedBell = [1,1,3,13,75,...]; separation at n=2 (2 vs 3).")


if __name__ == "__main__":
    main()
