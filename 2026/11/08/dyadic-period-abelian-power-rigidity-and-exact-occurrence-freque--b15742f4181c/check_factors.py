"""Independent exhaustive factor check for dyadic Abelian powers.

Theorem implementation is intentionally separated from the direct test.
"""

def period_doubling(length):
    w = '1'
    while len(w) < length:
        w = ''.join('10' if x == '1' else '11' for x in w)
    return w[:length]


def factors_of_exponent(w, period, exponent):
    width = period * exponent
    result = set()
    for i in range(len(w) - width + 1):
        factor = w[i:i+width]
        blocks = [factor[j*period:(j+1)*period] for j in range(exponent)]
        if len({b.count('1') for b in blocks}) == 1:
            assert len(set(blocks)) == 1, (period, exponent, i)
            result.add(factor)
    return result


def rotations(t):
    return {t[i:] + t[:i] for i in range(len(t))}


def template(period):
    k = period.bit_length() - 1
    def a(i):
        v = 0
        x = i + 1
        while x % 2 == 0:
            x //= 2
            v += 1
        return str(1 - v % 2)
    return ''.join(a(i) for i in range(period - 1)) + str(1 - k % 2)


def check():
    w = period_doubling(1 << 15)
    for k in range(9):
        m = 1 << k
        t = template(m)
        for exponent in (2, 3, 4, 5):
            actual = factors_of_exponent(w, m, exponent)
            expected = {r * exponent for r in rotations(t)} if exponent <= 3 else set()
            assert actual == expected, (k, exponent, len(actual), len(expected), sorted(expected-actual)[:1])
            print(f'period={m:3d} exponent={exponent}: {len(actual)} distinct factors')
    w12 = '101110101011'
    assert w12 in w
    assert len({w12[i:i+3].count('1') for i in (0, 3, 6, 9)}) == 1
    assert len({w12[i:i+3] for i in (0, 3, 6, 9)}) > 1
    print('non-dyadic counterexample at period 3 verified')

if __name__ == '__main__':
    check()
