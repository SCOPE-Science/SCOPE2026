"""Independent finite checks for optimal one-adjacent-swap detection codes.
Requires only the Python standard library.
"""
from itertools import product
from collections import Counter, defaultdict
from math import factorial, prod


def inversion_parity(word):
    return sum(a > b for i, a in enumerate(word) for b in word[i + 1:]) % 2


def adjacent(word):
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            yield word[:i] + (word[i + 1], word[i]) + word[i + 2:]


def predicted_by_content(counts):
    n = sum(counts)
    multinomial = factorial(n) // prod(factorial(c) for c in counts)
    odds = [i for i, c in enumerate(counts) if c % 2]
    m = n // 2
    if n % 2 == 0:
        fixed = factorial(m) // prod(factorial(c // 2) for c in counts) if not odds else 0
    else:
        if len(odds) != 1:
            fixed = 0
        else:
            j = odds[0]
            half = [c // 2 for c in counts]
            fixed = factorial(m) // prod(factorial(c) for c in half)
    return (multinomial + fixed) // 2


def max_matching(words):
    """Kuhn augmenting-path maximum bipartite matching, independently of pairing witness."""
    vertices = set(words)
    left = [w for w in words if inversion_parity(w) == 0]
    rights = {w: None for w in words if inversion_parity(w) == 1}

    def visit(u, seen):
        for v in adjacent(u):
            if v not in rights or v in seen:
                continue
            seen.add(v)
            if rights[v] is None or visit(rights[v], seen):
                rights[v] = u
                return True
        return False

    found = 0
    for u in left:
        found += visit(u, set())
    return found


def test(q, n):
    words = list(product(range(q), repeat=n))
    groups = defaultdict(list)
    for w in words:
        groups[tuple(w.count(a) for a in range(q))].append(w)
    for counts, group in groups.items():
        even = sum(inversion_parity(w) == 0 for w in group)
        predicted = predicted_by_content(counts)
        assert even == predicted, (q, n, counts, even, predicted)
        if n > 1:
            matching = max_matching(group)
            alpha = len(group) - matching
            assert alpha == predicted, (q, n, counts, alpha, predicted)
    predicted_total = (q**n + q**((n + 1) // 2)) // 2
    assert sum(predicted_by_content(c) for c in groups) == predicted_total
    assert sum(inversion_parity(w) == 0 for w in words) == predicted_total
    assert all(inversion_parity(v) == 1 for w in words if inversion_parity(w) == 0 for v in adjacent(w))
    print('q=%s n=%s types=%s exact_optimum=%s' % (q, n, len(groups), predicted_total))


if __name__ == '__main__':
    for q, maximum_n in ((2, 9), (3, 7), (4, 5)):
        for n in range(1, maximum_n + 1):
            test(q, n)
    print('ALL_ADJACENT_SWAP_CAPACITY_CHECKS_PASSED')
