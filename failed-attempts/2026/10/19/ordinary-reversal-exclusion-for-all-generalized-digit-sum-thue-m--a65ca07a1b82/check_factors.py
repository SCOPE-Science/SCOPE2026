#!/usr/bin/env python3
"""Independent finite checks of reversal exclusion in digit-sum words.
This is a computational test; the proof in RESULT.md covers all parameters.
"""

def factors_from_block_pairs(base, modulus, length):
    # Only used for base >= 3, where each length-4 window meets <=2 blocks.
    pairs = {(a, (a + 1) % modulus) for a in range(modulus)}
    while True:
        new = set(pairs)
        for a, c in pairs:
            t = [((a + i) % modulus) for i in range(base)] + [((c + i) % modulus) for i in range(base)]
            new.update(zip(t, t[1:]))
        if new == pairs:
            break
        pairs = new
    factors = set()
    for a, c in pairs:
        t = tuple((a + i) % modulus for i in range(base)) + tuple((c + i) % modulus for i in range(base))
        factors.update(t[i:i + length] for i in range(len(t) - length + 1))
    return factors

def digit_sum_mod(number, base, modulus):
    s = 0
    while number:
        number, d = divmod(number, base)
        s += d
    return s % modulus

def run():
    for base in range(3, 17):
        for mod in range(3, 20):
            fs = factors_from_block_pairs(base, mod, 4)
            assert all(f[::-1] not in fs for f in fs), (base, mod)
    for mod in range(3, 30):
        seq = [digit_sum_mod(n, 2, mod) for n in range(65536)]
        f3 = {tuple(seq[i:i+3]) for i in range(len(seq)-2)}
        f4 = {tuple(seq[i:i+4]) for i in range(len(seq)-3)}
        assert all(f[::-1] not in f4 for f in f4), mod
        assert all((f == f[::-1]) or (f[::-1] not in f3) for f in f3), mod
    print('VERIFY_OK: base 3..16 modulus 3..19 exact block-pair cover; base 2 modulus 3..29 finite prefix 65536')

if __name__ == '__main__':
    run()
