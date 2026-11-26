"""Finite checks for commutator-fiber counts on graph Lie algebras of forests.

Run with Python 3 (standard library only). Exhaustive checks are finite
examples, not proof of the quantified theorem.
"""
from itertools import combinations, product


def add(a, b, q):
    return (a ^ b) if q == 4 else (a + b) % q


def sub(a, b, q):
    return (a ^ b) if q == 4 else (a - b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    out = 0
    aa = a
    bb = b
    while bb:
        if bb & 1:
            out ^= aa
        bb >>= 1
        aa <<= 1
        if aa & 4:
            aa ^= 7  # x^2 + x + 1
    return out


def is_forest(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


def predicted(n, edges, w, q):
    """Independent closed vertex-zero-set expression."""
    forced = set()
    positive_edges = sum(bool(t) for t in w)
    for (a, b), t in zip(edges, w):
        if t:
            forced.update((a, b))
    total = 0
    for mask in range(1 << n):
        zeros = {i for i in range(n) if mask & (1 << i)}
        if zeros & forced:
            continue
        keep = set(range(n)) - zeros
        internal_edges = sum(a in keep and b in keep for a, b in edges)
        components = len(keep) - internal_edges
        total += (q + 1) ** components * q ** positive_edges * (q - 1) ** (len(keep) - positive_edges)
    return total


def direct_counts(n, edges, q):
    """Independent complete enumeration of paired vertex vectors."""
    out = {}
    for x in product(range(q), repeat=n):
        for y in product(range(q), repeat=n):
            w = tuple(sub(mul(x[a], y[b], q), mul(x[b], y[a], q), q) for a,b in edges)
            out[w] = out.get(w, 0) + 1
    return out


def verify(n, edges, q):
    assert is_forest(n, edges)
    actual = direct_counts(n, edges, q)
    for w in product(range(q), repeat=len(edges)):
        want = predicted(n, edges, w, q)
        got = actual.get(w, 0)
        assert got == want, (n, edges, q, w, got, want)
        assert want > 0
    assert sum(actual.values()) == q ** (2*n)


def main():
    checks = 0
    for n in range(1, 5):
        choices = list(combinations(range(n), 2))
        for mask in range(1 << len(choices)):
            edges = tuple(e for i,e in enumerate(choices) if (mask >> i) & 1)
            if not is_forest(n, edges):
                continue
            for q in (2, 3):
                verify(n, edges, q)
                checks += 1
    for n, edges, q in (
        (4, ((0,1),(1,2),(2,3)), 4),
        (4, ((0,1),(0,2),(0,3)), 4),
        (4, ((0,1),(1,2),(2,3)), 5),
        (5, ((0,1),(1,2),(2,3),(3,4)), 2),
        (5, ((0,1),(0,2),(0,3),(0,4)), 2),
    ):
        verify(n, edges, q)
        checks += 1
    print(f'ALL_FOREST_FIBER_CHECKS_PASSED {checks}')
    p4 = ((0,1),(1,2),(2,3))
    print('P4_BINARY_PROFILE', {str(w):predicted(4,p4,w,2) for w in product(range(2),repeat=3)})
    print('FULL_SUPPORT',[(q,predicted(4,p4,(1,1,1),q)) for q in (2,3,4,5)])


if __name__ == '__main__':
    main()
