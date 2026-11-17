"""Finite checks for the 2-adic value-image theorem for derangement numbers.

This script is supporting evidence, not a substitute for the infinite proof.
Run: python3 verify_derangement_image.py
"""

def v2(z):
    if z == 0:
        raise ValueError('valuation of zero')
    z = abs(z)
    return (z & -z).bit_length()-1


def derangements_mod(m, count):
    value = 1 % m
    result = [value]
    for n in range(1, count):
        value = (n * value + (1 if n % 2 == 0 else -1)) % m
        result.append(value)
    return result


def expected(k):
    mod = 1 << k
    return {x for x in range(mod) if x % 2 == 0 or x % 8 == 1}


def check():
    counts = []
    for k in range(1, 13):
        mod = 1 << k
        vals = derangements_mod(mod, mod)
        got = set(vals)
        exp = expected(k)
        assert got == exp, (k, sorted(exp-got), sorted(got-exp))
        if k >= 3:
            assert len(got) == 5 * (1 << (k-3))
        counts.append(len(got))
    mod = 1 << 16
    vals = derangements_mod(mod, 512)
    odd_pairs = 0
    even_pairs = 0
    for x in range(1, 256, 2):
        for y in range(x + 2, 256, 2):
            assert v2(vals[x] - vals[y]) == v2(x-y)
            odd_pairs += 1
    for x in range(0, 256, 4):
        for y in range(x + 4, 256, 4):
            assert v2(vals[x] - vals[y]) == v2(x-y)+1
            even_pairs += 1
    print('VERIFY_OK levels=12 image_sizes=' + ','.join(map(str, counts))
          + ' odd_pairs=' + str(odd_pairs) + ' mod4_pairs=' + str(even_pairs))

if __name__ == '__main__':
    check()
