#!/usr/bin/env python3
"""Exact census of degree-graded one-vertex extensions of oriented paths."""
from collections import defaultdict, Counter
from itertools import product


def reverse_bits(s):
    return ''.join('1' if x == '0' else '0' for x in s)


def key(s):
    return min(s, s[::-1], reverse_bits(s), reverse_bits(s[::-1]))


def spectrum(s, bivariate=False):
    # status 0: new->old, status 1: old->new, status 2: no arc
    if bivariate:
        dp = {(1, 0, 0): 1, (0, 1, 1): 1, (0, 0, 2): 1}
    else:
        dp = {(1, 0): 1, (1, 1): 1, (0, 2): 1}
    for bit in s:
        nxt = defaultdict(int)
        for state, count in dp.items():
            prev = state[-1]
            for status in range(3):
                if bit == '0' and prev == 0 and status == 1:
                    continue
                if bit == '1' and prev == 1 and status == 0:
                    continue
                if bivariate:
                    target = (state[0] + (status == 0), state[1] + (status == 1), status)
                else:
                    target = (state[0] + (status != 2), status)
                nxt[target] += count
        dp = nxt
    if bivariate:
        ans = Counter()
        for (a, b, _), v in dp.items():
            ans[a, b] += v
        return ans
    ans = [0] * (len(s) + 2)
    for (k, _), v in dp.items():
        ans[k] += v
    return tuple(ans)


def direct(s, bivariate=False):
    # Independent enumeration of every ternary status word.
    d = Counter()
    for word in product(range(3), repeat=len(s) + 1):
        if any((bit == '0' and word[i:i+2] == (0, 1)) or
               (bit == '1' and word[i:i+2] == (1, 0))
               for i, bit in enumerate(s)):
            continue
        if bivariate:
            d[word.count(0), word.count(1)] += 1
        else:
            d[word.count(0) + word.count(1)] += 1
    if bivariate:
        return d
    return tuple(d[i] for i in range(len(s) + 2))


def run():
    for n in range(1, 9):
        fingerprints = defaultdict(set)
        for word in product('01', repeat=n - 1):
            s = ''.join(word)
            k = key(s)
            poly = spectrum(s)
            fingerprints[poly].add(k)
            assert poly == spectrum(s[::-1])
            assert poly == spectrum(reverse_bits(s))
            if n <= 6:
                assert poly == direct(s)
        sizes = sorted(len(v) for v in fingerprints.values())
        print(f'n={n}: orientation_classes={sum(sizes)}, distinct_polynomials={len(fingerprints)}, collision_fibres={sum(t>1 for t in sizes)}')
        if n < 8:
            assert all(size == 1 for size in sizes)
        else:
            assert sum(sizes) == 36 and len(fingerprints) == 35 and sizes.count(2) == 1
            common = next(poly for poly, v in fingerprints.items() if len(v) == 2)
            pair = sorted(fingerprints[common])
            assert pair == ['0010010', '0101110']
            assert common == (1, 16, 105, 368, 753, 923, 664, 257, 41)
            assert sum(common) == 3128
            print('collision_representatives=', pair)
            print('common_coefficients=', common)
            for s in pair:
                assert spectrum(s) == direct(s)
                v = spectrum(s, bivariate=True)
                assert v == direct(s, bivariate=True)
                print('bivariate_coefficient_u3v3', s, v[3,3])
            assert spectrum(pair[0], True)[3,3] == 163
            assert spectrum(pair[1], True)[3,3] == 164
    # Direct check of the two contrasting natural orientation families.
    for n in range(1, 13):
        chain = '0' * (n-1)
        fence = ''.join('0' if i%2==0 else '1' for i in range(n-1))
        c = sum(spectrum(chain))
        f = sum(spectrum(fence))
        expected_c = [3,8]
        while len(expected_c) < n:
            expected_c.append(3*expected_c[-1]-expected_c[-2])
        expected_f = [3,8]
        while len(expected_f) < n:
            expected_f.append(2*expected_f[-1]+2*expected_f[-2])
        assert c == expected_c[n-1] and f == expected_f[n-1]
    print('boundary_recursions_checked_through_n12')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
