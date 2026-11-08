"""Independent finite checks for a five-run Abelian-square theorem.

Run: python3 verify_abelian_five_run.py
No external dependencies. All words are linear; the alphabet is {0,1}.
"""
from itertools import combinations, product


def abelian_squares(word):
    """Enumerate actual distinct nonempty Abelian-square factors."""
    out = set()
    n = len(word)
    for start in range(n):
        for half in range(1, (n - start) // 2 + 1):
            factor = word[start:start + 2 * half]
            if factor[:half].count('0') == factor[half:].count('0'):
                out.add(factor)
    return out


def runs(word):
    return 1 + sum(x != y for x, y in zip(word, word[1:]))


def predicted_five_run(a, b, c, d, e):
    if b == d:
        return sum(
            abs(i - j) <= c and (c + j - i) % 2 == 0
            for i in range(1, a + 1) for j in range(1, e + 1)
        )
    if (b + d) % 2:
        return 0
    if b > d:
        return max(0, min(e, a - c))
    return max(0, min(a, e - c))


def word5(a, b, c, d, e):
    return '0' * a + '1' * b + '0' * c + '1' * d + '0' * e


def compositions(n, k):
    for cuts in combinations(range(1, n), k - 1):
        points = (0,) + cuts + (n,)
        yield tuple(points[j + 1] - points[j] for j in range(k))


def main():
    observed = 0
    for n in range(5, 20):
        for a, b, c, d, e in compositions(n, 5):
            sq = abelian_squares(word5(a, b, c, d, e))
            five = sum(runs(factor) == 5 for factor in sq)
            expected = predicted_five_run(a, b, c, d, e)
            assert five == expected, (n, a, b, c, d, e, five, expected)
            assert len(sq) - five <= 8 * n
            observed += 1
    for a, b, c, d, e in product(range(1, 8), repeat=5):
        # Independently check the five-run word itself, using its two half counts.
        actual = 0
        for i in range(1, a + 1):
            for j in range(1, e + 1):
                f = '0' * i + '1' * b + '0' * c + '1' * d + '0' * j
                h = len(f) // 2
                actual += len(f) % 2 == 0 and f[:h].count('1') == f[h:].count('1')
        assert actual == predicted_five_run(a, b, c, d, e)
    for m in range(1, 51):
        a = e = 3 * m
        c = 2 * m
        assert predicted_five_run(a, 1, c, 1, e) == 4 * m * m + m
    for n in range(2, 19):
        for k in range(1, min(4, n) + 1):
            for lengths in compositions(n, k):
                word = ''.join('01'[j % 2] * lengths[j] for j in range(k))
                assert len(abelian_squares(word)) <= 5 * n
    print(f'VERIFY_OK five_run_words={observed} grid_cases={7**5} construction_cases=50')


if __name__ == '__main__':
    main()
