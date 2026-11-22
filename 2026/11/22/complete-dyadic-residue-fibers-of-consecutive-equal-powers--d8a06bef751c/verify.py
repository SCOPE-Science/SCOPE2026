"""Independent finite checks for consecutive-power dyadic residue fibers."""
from collections import Counter


def h(k):
    if k & 1:
        return 1
    return 2 if k == 2 else (k & -k).bit_length() + 1


def v2(z):
    assert z != 0
    return (abs(z) & -abs(z)).bit_length() - 1


def f(k, x, mod):
    return (pow(x, k, mod) + pow(x + 1, k, mod)) % mod


checks = 0
for k in range(1, 41):
    hk = h(k)
    for n in range(1, 12):
        mod = 1 << n
        fibers = Counter(f(k, x, mod) for x in range(mod))
        target_mod = 1 << min(n, hk)
        target = {a: target_mod for a in range(mod) if a % target_mod == 1 % target_mod}
        assert fibers == target, (k, n, fibers, target)
        assert sum(fibers.values()) == mod
        checks += 1

# Compare raw differences, without relying on the finite fiber formula.
for k in (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 31, 40):
    b = 0 if k == 1 else (2 if k % 2 == 0 and k >= 4 else 1)
    t = 0 if k < 4 or k % 2 else v2(k)
    for x in range(64):
        for y in range(x + 1, 64):
            if b and (x - y) % (1 << b):
                continue
            if k == 1:
                expected = v2(x - y) + 1
            elif k == 2:
                expected = v2(x - y) + 1
            elif k & 1:
                expected = v2(x - y)
            else:
                expected = v2(x - y) + t
            # Direct integer powers, no modulo arithmetic or previous formulas.
            actual = v2(x**k + (x + 1)**k - y**k - (y + 1)**k)
            assert actual == expected, (k, x, y, actual, expected)
            checks += 1

print(f"PASS: {checks} complete-fiber and valuation-difference checks")
