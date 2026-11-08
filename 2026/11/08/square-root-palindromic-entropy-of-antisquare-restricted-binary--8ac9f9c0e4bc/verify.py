"""Direct finite checks of palindrome entropy construction for antisquare-restricted binary words."""
from itertools import product

BAD_P = ('010', '101', '11111', '01110')
BAD_W = ('0011', '1100', '0110', '1001', '010101', '101010', '001011', '110100')
BLOCKS = ('0', '1100', '111100')

def code(w):
    return ''.join(str(int(a != b)) for a, b in zip(w, w[1:]))

def preimage(p, initial):
    w = [initial]
    for bit in p:
        w.append(str(int(w[-1]) ^ int(bit)))
    return ''.join(w)

def is_good(w):
    n = len(w)
    for k in range(2, n // 2 + 1):
        for i in range(n - 2 * k + 1):
            if all(w[i + j] != w[i + k + j] for j in range(k)):
                return False
    return True

def avoids(s, forbidden):
    return all(p not in s for p in forbidden)

def is_palindrome(w):
    return w == w[::-1]

def block_words(n):
    if n == 0:
        yield ''
    else:
        for b in BLOCKS:
            if len(b) <= n:
                for t in block_words(n - len(b)):
                    yield b + t

# All eight forbidden binary factors correspond to four Pansiot factors.
for p in BAD_P:
    images = {preimage(p, '0'), preimage(p, '1')}
    assert images <= set(BAD_W), (p, images)
assert set(BAD_W) == {preimage(p, s) for p in BAD_P for s in '01'}

# For every binary word through length 12, the finite-code avoidance equivalence is exact.
code_cases = 0
for n in range(1, 13):
    for t in product('01', repeat=n):
        w = ''.join(t)
        assert avoids(w, BAD_W) == avoids(code(w), BAD_P)
        if avoids(w, BAD_W):
            assert is_good(w)
        code_cases += 1

# Exhaustive palindromic good-word counts for small lengths.
pal_counts = []
for n in range(1, 25):
    count = 0
    for h in product('01', repeat=(n + 1) // 2):
        a = ''.join(h)
        w = a + (a[::-1] if n % 2 == 0 else a[:-1][::-1])
        if is_good(w):
            count += 1
    pal_counts.append(count)
assert pal_counts[:12] == [2, 2, 4, 2, 8, 4, 10, 6, 16, 10, 24, 14]

# The block prefix code gives a_n >= 2 T_h at lengths 2h+7 and 2h+8.
construction_cases = 0
rec = [0] * 16
rec[0] = 1
for h in range(1, len(rec)):
    rec[h] = sum(rec[h - m] for m in (1, 4, 6) if h >= m)
for h in range(0, 14):
    words = list(block_words(h))
    assert len(words) == rec[h]
    for r in (6, 7):
        seen = set()
        for v in words:
            p = v + '0' * r + v[::-1]
            assert avoids(p, BAD_P)
            assert is_palindrome(p)
            for initial in '01':
                w = preimage(p, initial)
                assert is_palindrome(w)
                assert is_good(w)
                seen.add(w)
                construction_cases += 1
        assert len(seen) == 2 * rec[h]
        n = 2 * h + r + 1
        if n <= len(pal_counts):
            assert len(seen) <= pal_counts[n - 1]

print('PASS: eight forbidden factors ↔ four Pansiot patterns')
print(f'PASS: {code_cases} exhaustive finite-code equivalences; forbidden-language implication')
print('PASS: 24 palindrome counts: ' + ', '.join(map(str, pal_counts)))
print(f'PASS: {construction_cases} generated palindromic good words, distinctness and recurrence')
print('PASS: all checked lower bounds for both parity classes')
