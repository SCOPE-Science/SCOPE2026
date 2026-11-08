"""Standalone tests for affine occurrence laws of generalized period-doubling words.
Run: python3 verify.py
"""
from collections import Counter

def valuation(n, base):
    v = 0
    while n % base == 0:
        n //= base
        v += 1
    return v

def word_at(i, base):
    return valuation(i + 1, base) % 2

def substitution(word, base):
    return ''.join('0' * (base - 1) + ('1' if a == '0' else '0') for a in word)

def data(n, base):
    # Base n=1 is a virtual seed, not a classification of length-one factors.
    if n == 1:
        return ('0', '0', 0, 0, 0)
    m = (n + base - 1) // base
    d = base * m - n
    plus_old, minus_old, h, plus_r, minus_r = data(m, base)
    plus = substitution(minus_old, base)[base - 1:] + '0' * (base - 1 - d)
    minus = substitution(plus_old, base)[d:]
    return (plus, minus, h + 1, base * minus_r + base - 1, base * plus_r + d)

def is_unbordered(w):
    return all(w[:l] != w[-l:] for l in range(1, len(w)))

def run():
    tested = 0
    classified = 0
    for b in range(2, 8):
        limit = 12000
        w = ''.join(str(word_at(i, b)) for i in range(limit + 120))
        zero = {i for i in range(limit) if w[i] == '0'}
        for n in range(2, 97):
            plus, minus, h, rp, rm = data(n, b)
            assert len(plus) == len(minus) == n, (b,n)
            assert plus[0] == minus[-1] == '1'
            assert plus[-1] == minus[0] == '0'
            assert plus == minus[::-1], (b,n)
            assert is_unbordered(plus) and is_unbordered(minus), (b,n)
            assert 0 <= rp < b**h and 0 <= rm < b**h
            period = b**h
            for label, pattern, residue in ((1,plus,rp), (0,minus,rm)):
                actual = {i for i in range(limit) if w[i:i+n] == pattern}
                expected = {period*j+residue for j in zero if period*j+residue < limit}
                assert actual == expected, (b,n,label, actual^expected)
                tested += len(actual) + len(expected)
            if n <= 15 and b <= 5:
                all_u = {w[i:i+n] for i in range(limit) if is_unbordered(w[i:i+n])}
                assert all_u == {plus,minus}, (b,n, all_u)
                classified += 1
    print('VERIFY_OK', 'occurrence_comparisons=', tested,
          'complete_unbordered_classifications=', classified,
          'bases=2..7', 'lengths=2..96', 'positions=0..11999')

if __name__ == '__main__':
    run()
