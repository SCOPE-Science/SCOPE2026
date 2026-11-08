"""Finite, independent diagnostics for a theorem on the ternary Thue word.

This program tests finite instances; the all-length theorem follows from the
proof in RESULT.md, not from extrapolation of these checks.
"""

def tm(i):
    return i.bit_count() & 1


def transition_word(length):
    t = [tm(i) for i in range(length + 1)]
    return [0 if t[i:i + 2] == [0, 1] else
            2 if t[i:i + 2] == [1, 0] else 1
            for i in range(length)]


def morphic_word(length):
    w = '0'
    morphism = {'0': '012', '1': '02', '2': '1'}
    while len(w) < length:
        w = ''.join(morphism[c] for c in w)
    return [int(c) for c in w[:length]]


def full_signature(word):
    letters = [0] * 3
    pairs = [0] * 9
    for c in word:
        for a in range(3):
            pairs[3 * a + c] += letters[a]
        letters[c] += 1
    return tuple(letters + pairs)


def fingerprint(word):
    return (sum(c == 1 for c in word),
            sum(i for i, c in enumerate(word) if c == 1),
            sum(c == 0 for c in word),
            sum(i for i, c in enumerate(word) if c == 0))


def verify():
    for j in range(2, 11):
        n = 1 << j
        x = transition_word(4 * n)
        assert x == morphic_word(4 * n), ('substitution mismatch', j)
        words = [x[i:i+n] for i in range(3 * n)]
        sigs = [full_signature(w) for w in words]
        fps = [fingerprint(w) for w in words]
        assert len(set(map(tuple, words))) == 3 * n, ('factor collisions', j)
        assert len(set(sigs)) == 3 * n, ('binomial collisions', j)
        assert len(set(fps)) == 3 * n, ('fingerprint collisions', j)
        for f, s in zip(fps, sigs):
            assert f[0] == s[1] and f[2] == s[0]
            assert f[1] == s[4] + s[10] + f[0]*(f[0]-1)//2
            assert f[3] == s[6] + s[9] + f[2]*(f[2]-1)//2
        A = [fps[k * n][0] for k in range(3)]
        assert A[0] == A[2] and A[0] % 2 and A[1] % 4 == 2
        for k in range(3):
            for r in range(n):
                assert fps[k*n+r][0] == A[k]
                assert (fps[k*n+r][1] - fps[k*n][1] + r*A[k]) % n == 0
        for r in range(n):
            assert fps[r][1] == fps[2*n+r][1]
            assert fps[r][2] != fps[2*n+r][2]
        for r in range(n//2):
            assert fps[n+r][3] != fps[n+r+n//2][3]
        print('dyadic length', n, 'three-block factors', 3*n,
              'four-statistic signatures', len(set(fps)), 'binomial classes', len(set(sigs)))
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
