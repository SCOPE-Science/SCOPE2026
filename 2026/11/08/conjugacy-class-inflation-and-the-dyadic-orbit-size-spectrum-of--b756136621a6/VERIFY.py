"""Finite cross-checks of conjugacy-class inflation in Thue--Morse.

Run: python VERIFY.py. Only Python 3 standard library is required.
This is a finite consistency test; the infinitary statement uses the proof.
"""
from collections import Counter, defaultdict


def morph(w):
    return ''.join('01' if a == '0' else '10' for a in w)


def factor_set(word, n):
    return {word[i:i + n] for i in range(len(word) - n + 1)}


def rotation_key(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def class_map(factors):
    ans = defaultdict(set)
    for w in factors:
        ans[rotation_key(w)].add(w)
    return ans


word = '0'
for _ in range(15):
    word = morph(word)
word2 = morph(word)

for n in range(4, 65):
    F_n = factor_set(word, n)
    F_next = factor_set(word, n + 1)
    F_2n = factor_set(word, 2 * n)
    assert F_n == factor_set(word2, n), f'prefix insufficient at {n}'
    assert F_2n == factor_set(word2, 2 * n), f'prefix insufficient at 2*{n}'
    C_n, C_2n = class_map(F_n), class_map(F_2n)
    closing = {w for w in F_n if w + w[0] in F_next}
    predicted = Counter(len(members) + len(members & closing)
                        for members in C_n.values())
    predicted[1] += len(F_next) - len(closing)
    actual = Counter(map(len, C_2n.values()))
    assert predicted == actual, f'multiset formula at {n}: {predicted}, {actual}'
    assert len(C_2n) == len(C_n) + len(F_next) - len(closing)
    # Directly compare the *individual* inherited and newly isolated classes.
    A = {morph(u) for u in F_n}
    def odd_word(v):
        return ''.join(('1' if v[i] == '0' else '0') + v[i + 1]
                       for i in range(n))
    B = {odd_word(v) for v in F_next}
    assert not (A & B) and A | B == F_2n
    for members in C_n.values():
        image = {morph(u) for u in members}
        attach = {odd_word(u + u[0]) for u in members if u in closing}
        assert len(image) == len(members)
        assert len(attach) == len(members & closing)
        assert C_2n[rotation_key(next(iter(image)))] == image | attach
    for v in F_next:
        if v[0] != v[-1]:
            w = odd_word(v)
            assert C_2n[rotation_key(w)] == {w}

for k in range(2, 8):
    n = 2 ** k
    F = factor_set(word, n)
    C = class_map(F)
    actual = Counter(map(len, C.values()))
    target = Counter({1: 2 * n - 8, 2: 3, n: 1})
    if target[1] == 0:
        del target[1]
    assert actual == target, (n, actual, target)
    block = '0'
    for _ in range(k):
        block = morph(block)
    rot = {block[i:] + block[:i] for i in range(n)}
    assert len(rot) == n and rot in C.values(), n
    closing = {w for w in F if w + w[0] in factor_set(word, n + 1)}
    assert closing == rot, (n, closing, rot)
    assert len(F) == 3 * n - 2 and len(C) == 2 * n - 4

# Structural forbidden factors used in the proof.
for q in ('000', '111', '01010', '10101'):
    assert q not in factor_set(word, len(q)), q

print('VERIFY_OK: multiset n=4..64; dyadic n=4..128; forbidden blocks')
