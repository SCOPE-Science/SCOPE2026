"""Independent finite checks of the crown graph locating-domination polynomial.

Run with Python 3.9+; uses only the standard library.  These finite checks
illustrate and stress-test, but do not replace the symbolic proof.
"""
from collections import Counter
from math import comb


def direct_profile(n, delete_matching=True):
    """Count all sets directly using open-neighborhood bit signatures."""
    neighbors = []
    for i in range(n):
        neighbors.append(sum(1 << (n + j) for j in range(n)
                             if not delete_matching or i != j))
    for j in range(n):
        neighbors.append(sum(1 << i for i in range(n)
                             if not delete_matching or i != j))
    counts = Counter()
    for mask in range(1 << (2*n)):
        signatures = []
        ok = True
        for v in range(2*n):
            if (mask >> v) & 1:
                continue
            s = mask & neighbors[v]
            if not s:
                ok = False
                break
            signatures.append(s)
        if ok and len(signatures) == len(set(signatures)):
            a = (mask & ((1 << n)-1)).bit_count()
            b = (mask >> n).bit_count()
            counts[a, b] += 1
    return counts


def polynomial_profile(n):
    """Evaluate the proved bivariate closed form by coefficient arithmetic."""
    # First term: no empty matched pairs, each pair A, B, or both.
    nonempty = Counter({(0, 0): 1})
    for _ in range(n):
        nxt = Counter()
        for (a, b), coefficient in nonempty.items():
            for state in ((1, 0), (0, 1), (1, 1)):
                nxt[a + state[0], b + state[1]] += coefficient
        nonempty = nxt
    poly = nonempty.copy()
    # Exactly one empty matched pair.
    for (a, b), coefficient in polynomial_profile_no_empty(n-1).items():
        poly[a, b] += n * coefficient
    # Non-dominating configurations with one entire color-side absent.
    poly[n-1, 0] -= n
    poly[0, n-1] -= n
    # Singleton side whose unique chosen vertex is unmatched on that pair.
    poly[n-1, 1] -= n
    poly[1, n-1] -= n
    poly[n-2, 1] -= n*(n-1)
    poly[1, n-2] -= n*(n-1)
    # At n=3, both singleton obstructions coincide in six assignments.
    if n == 3:
        poly[1, 1] += 6
    return Counter({k: v for k, v in poly.items() if v})


def polynomial_profile_no_empty(n):
    poly = Counter({(0, 0): 1})
    for _ in range(n):
        nxt = Counter()
        for (a, b), val in poly.items():
            nxt[a+1, b] += val
            nxt[a, b+1] += val
            nxt[a+1, b+1] += val
        poly = nxt
    return poly


def expected_minimum(n):
    if n in (3, 4):
        return n, (14 if n == 3 else 56)
    return n-1, n*(2**(n-1)-2*n)


def run():
    for n in range(3, 9):
        direct = direct_profile(n)
        formula = polynomial_profile(n)
        assert direct == formula, (n, direct-formula, formula-direct)
        min_size = min(a+b for (a, b) in direct)
        num_opt = sum(v for (a,b),v in direct.items() if a+b == min_size)
        assert (min_size, num_opt) == expected_minimum(n)
        assert sum(direct.values()) == 3**n+n*3**(n-1)-2*n*(n+1)+(6 if n==3 else 0)
        baseline = direct_profile(n, delete_matching=False)
        assert min(a+b for a,b in baseline) == 2*n-2
        print('n=%d: total=%d minimum=%d optimum_count=%d, K_nn_min=%d' %
              (n, sum(direct.values()), min_size, num_opt, 2*n-2))
    print('ALL EXACT BIVARIATE CHECKS PASS')


if __name__ == '__main__':
    run()
