"""Direct checks for three-zero circular Abelian-square type formula.
Run with Python 3, no dependencies. Positions and half-lengths are integers.
This is finite testing, not a proof of the unbounded theorem.
"""
from itertools import combinations
from random import Random


def predicted_from_gaps(gaps):
    n = sum(gaps)
    assert n % 2 == 1 and n >= 3 and all(x >= 1 for x in gaps)
    kmax = (n - 1) // 2
    predicted = set()
    for m in range(1, min(kmax, (max(gaps) - 1) // 2) + 1):
        predicted.add((m, 0))
    for i, x in enumerate(gaps):
        y, z = gaps[(i + 1) % 3], gaps[(i + 2) % 3]
        low = x // 2 + 1
        high = min(kmax, x + min(y, z) - 1)
        for m in range(low, high + 1):
            predicted.add((m, 1))
    a, b, c = sorted(gaps)
    formula = kmax - (1 if c % 2 == 0 else 0) + max(
        0, min(kmax, a + b - 1, c // 2) - a // 2
    )
    assert len(predicted) == formula
    return predicted


def observed_from_word(word):
    n = len(word)
    # Count all circular intervals from scratch using doubled-prefix counts.
    doubled = word + word
    prefix = [0]
    for symbol in doubled:
        prefix.append(prefix[-1] + (symbol == '0'))
    observed = set()
    for m in range(1, (n - 1) // 2 + 1):
        for start in range(n):
            zleft = prefix[start + m] - prefix[start]
            zright = prefix[start + 2 * m] - prefix[start + m]
            if zleft == zright:
                observed.add((m, zleft))
    return observed


def cyclic_gaps(word):
    positions = [i for i, v in enumerate(word) if v == '0']
    assert len(positions) == 3
    return (positions[1] - positions[0], positions[2] - positions[1],
            len(word) + positions[0] - positions[2])


def main():
    tested = 0
    for n in range(3, 30, 2):
        for positions in combinations(range(n), 3):
            arr = ['1'] * n
            for position in positions:
                arr[position] = '0'
            word = ''.join(arr)
            predicted = predicted_from_gaps(cyclic_gaps(word))
            observed = observed_from_word(word)
            assert predicted == observed, (n, word, predicted, observed)
            for k in range(1, (n - 1) // 2 + 1):
                assert sum(1 for half, _ in predicted if half <= k) >= k
            tested += 1
    print('EXHAUSTIVE_WORDS_PASS', tested, 'odd lengths 3..29')
    rng = Random(20261102)
    extra = 0
    for _ in range(250):
        gaps = [rng.randint(1, 130) for _ in range(3)]
        if sum(gaps) % 2 == 0:
            gaps[0] += 1
        word = ''.join('0' + '1' * (gap - 1) for gap in gaps)
        assert predicted_from_gaps(gaps) == observed_from_word(word), gaps
        extra += 1
    print('RANDOM_GAPS_PASS', extra, 'max length', 391)
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
