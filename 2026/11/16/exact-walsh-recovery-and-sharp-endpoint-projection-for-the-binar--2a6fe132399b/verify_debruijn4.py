"""Independent Python exact-integer verification of the order-four de Bruijn word-codebook spectrum.

Run with Python 3 and no third-party packages.
"""
from collections import Counter
from fractions import Fraction

M = 1 << 16

def rooted_words():
    result = []
    for word in range(M):
        windows = {
            sum(((word >> ((i + j) % 16)) & 1) << j for j in range(4))
            for i in range(16)
        }
        if len(windows) == 16:
            result.append(word)
    return result

def transform(values):
    values = list(values)
    span = 1
    while span < M:
        for base in range(0, M, 2 * span):
            for j in range(span):
                left = values[base + j]
                right = values[base + span + j]
                values[base + j] = left + right
                values[base + span + j] = left - right
        span *= 2
    return values

def main():
    words = rooted_words()
    assert len(words) == 256 and len(set(words)) == 256
    f = [0] * M
    for word in words:
        f[word] = 1
    w = transform(f)
    hist = Counter(w)
    target = {
        -96: 64, -80: 32, -64: 96, -48: 1088, -32: 2640,
        -16: 7872, 0: 42022, 16: 7744, 32: 2576,
        48: 1184, 64: 216, 256: 2,
    }
    assert hist == target
    assert sum(z*z for z in w) == M * len(words)
    assert min(abs(z) for z in w if z) == 16
    assert all(z % 16 == 0 for z in w)
    assert all(w[k] == 0 for k in range(M) if k.bit_count() % 2)
    lags = {1:0, 2:0, 3:0, 4:-96, 5:16, 6:-16, 7:-48, 8:32}
    assert all(w[(1 << i) | (1 << j)] == lags[min(j-i, 16-j+i)]
               for i in range(16) for j in range(i+1, 16))
    supported = transform([int(z != 0) for z in w])
    assert supported[0] == 23514
    assert sum(supported) == M
    assert sum(abs(z) for z in supported) == 2520272
    assert Fraction(sum(abs(z) for z in supported), M) == Fraction(157517, 4096)
    print('DEBRUIJN4_PY_PASS support=256 zero=42022 rank=23514 '
          'projection=157517/4096 signed_levels=12')

if __name__ == '__main__':
    main()
