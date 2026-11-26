"""Independent finite checks for zero avoidance in dyadic Fibonacci recurrences.

Run with Python 3. No nonstandard dependencies; finite checks only.
"""

def gcd_depth(a, b, k):
    if a == 0 and b == 0:
        return k
    low = (a | b) & (-(a | b))
    return low.bit_length() - 1


def norm_test(a, b, k):
    j = gcd_depth(a, b, k)
    h = k - j
    if h < 3:
        return False
    a //= 1 << j
    b //= 1 << j
    return (a*a + a*b - b*b) % 8 in (3, 5)


def enumerate_modulus(k):
    modulus = 1 << k
    seen = bytearray(modulus * modulus)
    good_states = 0
    good_cycles = {}
    bad_cycles = {}
    for a in range(modulus):
        for b in range(modulus):
            ind = a * modulus + b
            if seen[ind]:
                continue
            x, y = a, b
            count = 0
            has_zero = False
            level = gcd_depth(a, b, k)
            while True:
                index = x * modulus + y
                if seen[index]:
                    assert (x, y) == (a, b)
                    break
                seen[index] = 1
                has_zero |= (x == 0)
                count += 1
                x, y = y, (x + y) % modulus
            predicted = norm_test(a, b, k)
            assert predicted == (not has_zero), (k, a, b, count)
            if predicted:
                good_states += count
                good_cycles[(level, count)] = good_cycles.get((level, count), 0) + 1
            else:
                bad_cycles[(level, count)] = bad_cycles.get((level, count), 0) + 1
    expected = 0 if k <= 2 else (1 << (2*k - 1)) - 8
    assert good_states == expected, (k, good_states, expected)
    for j in range(k):
        h = k - j
        period = 3 if h == 1 else 3 * (1 << (h - 1))
        expected_good = (1 << (h - 2)) if h >= 3 else 0
        assert good_cycles.get((j, period), 0) == expected_good, (k, j, period, good_cycles)
        expected_bad = (1 << (h - 2)) if h >= 3 else ((1 << (h - 1)) if h == 2 else 1)
        assert bad_cycles.get((j, period), 0) == expected_bad, (k, j, period, bad_cycles)
    return good_states, sum(good_cycles.values())


def main():
    for k in range(1, 10):
        good, cycles = enumerate_modulus(k)
        print(f'k={k} modulus={1<<k} zero_avoiding={good} zero_avoiding_cycles={cycles}')
    print('VERIFY_OK: complete modular orbit enumeration through 512, dyadic norm test, periods, and exact counts')


if __name__ == '__main__':
    main()
