"""Check small finite commuting-permutation quotients and the flat-loop separation law.

Run: python verify.py
The general theorem is proved mathematically; these tests are finite checks only.
"""
from itertools import combinations


def hnf_lattices(bound):
    for index in range(1, bound + 1):
        for a in range(1, index + 1):
            if index % a:
                continue
            c = index // a
            for b in range(a):
                yield index, a, b, c


def member(hnf, u, v):
    _, a, b, c = hnf
    return v % c == 0 and (u - (v // c) * b) % a == 0


def move(hnf, state, u, v):
    _, a, b, c = hnf
    x, y = state
    q, r = divmod(y + v, c)
    return (x + u - q * b) % a, r


def words_of_length(length):
    for u in range(-length, length + 1):
        v = length - abs(u)
        yield u, v
        if v:
            yield u, -v


def first_separating_length(a, b, bound):
    for length in range(1, bound + 1):
        if any(member(a, u, v) != member(b, u, v)
               for u, v in words_of_length(length)):
            return length
    return None


def check(bound=20):
    # Independent action evaluation agrees with the subgroup-membership test.
    simulated = 0
    for h in hnf_lattices(bound):
        index, a, b, c = h
        assert index == a * c
        for length in range(1, min(index, 8) + 1):
            for u, v in words_of_length(length):
                wanted = member(h, u, v)
                for x in range(a):
                    for y in range(c):
                        observed = move(h, (x, y), u, v) == (x, y)
                        assert observed == wanted, (h, (x, y), (u, v))
                        simulated += 1
    assert simulated > 100000

    last_count = 0
    checked_pairs = 0
    for n in range(2, bound + 1):
        lattices = list(hnf_lattices(n))
        # Hermite normal forms must realize the known divisor-sum count.
        assert len(lattices) == sum(sum(d for d in range(1, k + 1) if k % d == 0)
                                    for k in range(1, n + 1))
        # The short-loop fingerprint, not merely a list of HNF entries,
        # is injective across all models with at most n states.
        word_vectors = [vec for length in range(1, n)
                        for vec in words_of_length(length)]
        fingerprints = []
        for h in lattices:
            f = 0
            for j, (u, v) in enumerate(word_vectors):
                if member(h, u, v):
                    f |= 1 << j
            fingerprints.append(f)
        assert len(set(fingerprints)) == len(lattices), n
        checked_pairs += len(lattices) * (len(lattices) - 1) // 2
        last_count = len(lattices)
        if n <= 10:
            # Independent least-witness computation also tests sharpness.
            farthest = max(first_separating_length(x, y, n - 1)
                           for x, y in combinations(lattices, 2))
            assert farthest == n - 1, (n, farthest)
        # Sharp pair: x coordinate has period n versus n-1.
        left = (n, n, 0, 1)
        right = (n-1, n-1, 0, 1)
        assert first_separating_length(left, right, n - 1) == n - 1
    print(f'VERIFY_OK: {simulated} independent orbit/loop checks; '
          f'{checked_pairs} distinct lattice pairs covered by injective fingerprints; '
          f'{last_count} types at size bound {bound}.')


if __name__ == '__main__':
    check()
