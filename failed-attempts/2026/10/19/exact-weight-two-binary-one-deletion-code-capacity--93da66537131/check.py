"""Finite reproducibility tests of the weight-two one-deletion formula.

Run: python3 check.py. Only Python's standard library is required.
"""
from itertools import combinations


def words(n):
    for i, j in combinations(range(n), 2):
        yield ''.join('1' if k in (i, j) else '0' for k in range(n))


def deletion_ball(w):
    return {w[:k] + w[k + 1:] for k in range(len(w))}


def constructed(n):
    m = n - 1
    pairs = [(t, t + 1) for t in range(1, m + 1, 2)]
    pairs.extend((a, a + 3) for a in range(2, m - 1, 4))
    return [''.join('1' if k in (i, j) else '0'
                    for k in range(1, n + 1)) for i, j in pairs]


def check_code(c):
    seen = {}
    for w in c:
        for d in deletion_ball(w):
            if d in seen and seen[d] != w:
                return False, (seen[d], w, d)
            seen[d] = w
    return True, None


def maximum_clique(compat):
    """Exact branch-and-bound maximum clique for small compatibility graphs."""
    size = len(compat)
    best = 0

    def search(candidate, found):
        nonlocal best
        if not candidate:
            best = max(best, found)
            return
        if found + candidate.bit_count() <= best:
            return
        while candidate:
            if found + candidate.bit_count() <= best:
                break
            low = candidate & -candidate
            i = low.bit_length() - 1
            candidate ^= low
            search(candidate & compat[i], found + 1)

    search((1 << size) - 1, 0)
    return best


def brute_optimum(n):
    ws = list(words(n))
    ds = [deletion_ball(w) for w in ws]
    compatibility = []
    for i in range(len(ws)):
        mask = 0
        for j in range(len(ws)):
            if i != j and ds[i].isdisjoint(ds[j]):
                mask |= 1 << j
        compatibility.append(mask)
    return maximum_clique(compatibility)


def main():
    for n in range(2, 81):
        c = constructed(n)
        bound = (3*n - 2)//4
        assert len(c) == bound and len(c) == len(set(c)), n
        assert all(len(w) == n and w.count('1') == 2 for w in c), n
        ok, witness = check_code(c)
        assert ok, (n, witness)
        if n <= 9:
            opt = brute_optimum(n)
            assert opt == bound, (n, opt, bound)
            print(f'n={n}: exhaustive optimum={opt}; construction={len(c)}')
    print('PASS: construction and deletion-ball disjointness at every n=2,...,80')
    print('PASS: exhaustive optimum through n=9')


if __name__ == '__main__':
    main()
