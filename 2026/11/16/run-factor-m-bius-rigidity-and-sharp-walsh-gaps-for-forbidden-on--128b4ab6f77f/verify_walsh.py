"""Exact full Walsh-transform checks for binary strings forbidding k consecutive ones.
Run: python3 verify_walsh.py (standard library only)."""
from math import gcd


def allowed(mask, n, k):
    run = 0
    for j in range(n):
        if mask >> j & 1:
            run += 1
            if run >= k:
                return False
        else:
            run = 0
    return True


def walsh(values):
    a = values[:]
    stride = 1
    while stride < len(a):
        for i in range(0, len(a), 2 * stride):
            for j in range(i, i + stride):
                x, y = a[j], a[j + stride]
                a[j], a[j + stride] = x + y, x - y
        stride *= 2
    return a


def expected_min(n, k):
    r = n % (k + 1)
    return 1 if r in (0, k) else 1 << r


def witness_mask(n, k):
    r = n % (k + 1)
    return (1 << n) - 1 if r in (0, k) else (1 << (n - r)) - 1


def main():
    checked = 0
    samples = {}
    for k in range(2, 8):
        for n in range(1, 16):
            a = [int(allowed(x, n, k)) for x in range(1 << n)]
            spectrum = walsh(a)
            nonzero = [abs(v) for v in spectrum if v]
            delta = expected_min(n, k)
            assert min(nonzero) == delta, (n, k, 'minimum', min(nonzero), delta)
            assert gcd(*nonzero) == delta, (n, k, 'gcd')
            witness = witness_mask(n, k)
            assert abs(spectrum[witness]) == delta, (n, k, 'witness', witness, spectrum[witness])
            assert max(abs(v) for v in spectrum) == sum(a)
            assert sum(v * v for v in spectrum) == (1 << n) * sum(a)
            if n % (k + 1) in (0, k):
                assert all(v & 1 for v in spectrum)
            if k in (3, 4, 5) and n in (k, k + 2, k + 3):
                samples[f'k={k},n={n}'] = {
                    'valid_strings': sum(a),
                    'zero_characters': spectrum.count(0),
                    'sharp_gap': delta,
                    'witness_mask': witness,
                    'witness_value': spectrum[witness],
                }
            checked += 1
    print('WALSH_FULL_ENUMERATION_PASS', checked, samples)


if __name__ == '__main__':
    main()
