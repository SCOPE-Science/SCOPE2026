"""Independent base-three encoding for the exact wheel rule and constructive waves."""
from itertools import product

def successor_integer(code, n):
    digits = []
    temp = code
    for _ in range(n + 1):
        digits.append(temp % 3)
        temp //= 3
    output = []
    for i in range(n + 1):
        v = digits[i]
        if i == 0:
            vote = sum(digits[j] == (v + 1) % 3 for j in range(1, n + 1))
        else:
            vote = sum(digits[j] == (v + 1) % 3 for j in (0, 1 + (i - 2) % n, 1 + i % n))
        output.append((v + 1) % 3 if vote >= 2 else v)
    return sum(v * 3 ** i for i, v in enumerate(output))


def encode(xs):
    return sum(v * 3 ** i for i, v in enumerate(xs))


def wave(n):
    return (1,) + (0,) * (n - 4) + (1, 1, 2, 2)


def floyd_period(seed, n):
    f = lambda x: successor_integer(x, n)
    tortoise, hare = f(seed), f(f(seed))
    while tortoise != hare:
        tortoise, hare = f(tortoise), f(f(hare))
    period = 1
    hare = f(tortoise)
    while hare != tortoise:
        period += 1
        hare = f(hare)
    return period


if __name__ == '__main__':
    from collections import Counter
    for n in range(3, 8):
        basins = Counter(floyd_period(seed, n) for seed in range(3 ** (n + 1)))
        expected = ({1: 3 ** (n + 1)} if n <= 6 else {1: 6393, 21: 168})
        assert dict(basins) == expected, (n, basins)
        print('independent_basins(%d)=%s' % (n, sorted(basins.items())))

    for n in range(3, 10):
        fixed = sum(successor_integer(x, n) == x for x in range(3 ** (n + 1)))
        assert fixed == 3 * (n + 2), (n, fixed)
        print('fixed(%d)=%d' % (n, fixed))
    for n in range(7, 121):
        seed = encode(wave(n))
        first = seed
        for j in range(1, 4):
            first = successor_integer(first, n)
        word = wave(n)
        expected = encode((1,) + word[2:] + word[1:2])
        assert first == expected, ('bad three-step shift', n)
        if n <= 20:
            z = seed
            for t in range(1, 3 * n + 1):
                z = successor_integer(z, n)
                if t < 3 * n:
                    assert z != seed, ('short period', n, t)
            assert z == seed, ('bad return', n)
    print('CONSTRUCTION_OK 7..120; direct minimal-return tests 7..20')
