"""Exact exhaustive tests for palindrome-source single-deletion confusability.
Runs with Python 3 standard library; finite tests supplement an infinite proof.
"""
from collections import defaultdict
from itertools import product


def palindrome(half, n):
    return half + (half[::-1] if n % 2 == 0 else half[-2::-1])


def descendants(word):
    return {word[:i] + word[i + 1:] for i in range(len(word))}


def graph(q, n):
    alphabet = tuple(range(q))
    halves = list(product(alphabet, repeat=(n + 1) // 2))
    words = [palindrome(h, n) for h in halves]
    sets = [descendants(w) for w in words]
    edges = {(i, j) for i in range(len(words)) for j in range(i + 1, len(words))
             if not sets[i].isdisjoint(sets[j])}
    return halves, words, edges


def check(q, n):
    halves, words, actual = graph(q, n)
    if n % 2 == 0:
        assert not actual, (q, n, 'even overlap')
    else:
        m = (n - 1) // 2
        assert len(actual) == q * (q ** (m + 1) - 1) // 2, (q, n, len(actual))
        # Complete recursive description of every edge, not merely the count.
        predicted = set()
        index = {h: i for i, h in enumerate(halves)}
        for i, h in enumerate(halves):
            for j in range(i + 1, len(halves)):
                k = halves[j]
                if h[0] == k[0]:
                    u, v = h[1:], k[1:]
                    if m == 0:
                        continue
                    pu = palindrome(u, n - 2)
                    pv = palindrome(v, n - 2)
                    if descendants(pu) & descendants(pv):
                        predicted.add((i, j))
                else:
                    a, b = h[0], k[0]
                    if (all(h[t] == (a if t % 2 == 0 else b) for t in range(m + 1))
                            and all(k[t] == (b if t % 2 == 0 else a) for t in range(m + 1))):
                        predicted.add((i, j))
        assert actual == predicted, (q, n, actual ^ predicted)
        # Every fixed-center family is independent and a full size clique partition exists.
        for c in range(q):
            same = [i for i, h in enumerate(halves) if h[-1] == c]
            assert len(same) == q ** m
            assert not any((min(i, j), max(i, j)) in actual
                           for s, i in enumerate(same) for j in same[s + 1:])
        for prefix in product(range(q), repeat=m):
            clique = [index[prefix + (c,)] for c in range(q)]
            assert all((min(i, j), max(i, j)) in actual
                       for s, i in enumerate(clique) for j in clique[s + 1:])
    return len(words)


def main():
    tests = [(2, n) for n in range(1, 18)] + [(3, n) for n in range(1, 10)] + [(4, n) for n in range(1, 8)]
    total = sum(check(q, n) for q, n in tests)
    print(f'VERIFY_OK tests={len(tests)} checked_palindromes={total}')


if __name__ == '__main__':
    main()
