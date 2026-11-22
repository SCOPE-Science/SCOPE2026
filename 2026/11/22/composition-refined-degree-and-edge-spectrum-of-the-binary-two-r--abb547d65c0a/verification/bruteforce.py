"""Direct deletion-set verification of constant-composition ambiguity counts."""
from collections import Counter
from itertools import product
from math import comb


def descendants(word):
    return {word[:j] + word[j + 1:] for j in range(len(word))}


def expected_same(n, k):
    return sum((n - 2 * t + 1) * comb(n - 2 * t, k - t)
               for t in range(1, n // 2 + 1)
               if 0 <= k - t <= n - 2 * t)


def expected_cross(n, k):
    return sum((n - 2 * t) * comb(n - 2 * t - 1, k - t)
               for t in range(1, (n - 1) // 2 + 1)
               if 0 <= k - t <= n - 2 * t - 1)


def main():
    tested_pairs = 0
    for n in range(1, 11):
        words = list(product((0, 1), repeat=n))
        balls = [descendants(w) for w in words]
        weights = [sum(w) for w in words]
        degrees = [0] * len(words)
        edges = Counter()
        for i, x in enumerate(words):
            for j in range(i + 1, len(words)):
                tested_pairs += 1
                shared = len(balls[i] & balls[j])
                assert shared <= 2
                if shared != 2:
                    continue
                a, b = sorted((weights[i], weights[j]))
                assert b - a <= 1
                edges[(a, b)] += 1
                if a == b:
                    degrees[i] += 1
                    degrees[j] += 1
        for k in range(n + 1):
            assert edges[(k, k)] == expected_same(n, k), (n, k, 'same')
            assert edges[(k, k + 1)] == expected_cross(n, k), (n, k, 'cross')
            r, s = min(k, n - k), max(k, n - k)
            assert max(degrees[i] for i in range(len(words)) if weights[i] == k) == r * min(s, r + 1)
            for i, word in enumerate(words):
                if weights[i] != k:
                    continue
                alt_blocks = []
                start = 0
                for pos in range(1, n):
                    if word[pos] == word[pos - 1]:
                        alt_blocks.append(word[start:pos])
                        start = pos
                alt_blocks.append(word[start:])
                assert degrees[i] == sum(block.count(0) * block.count(1) for block in alt_blocks)
        print(f'n={n:2d} words={len(words):4d} same_weight_edges={sum(v for (a,b),v in edges.items() if a==b):5d} verified')
    print(f'PASS direct unordered-pair comparisons={tested_pairs}')


if __name__ == '__main__':
    main()
