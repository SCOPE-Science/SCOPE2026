"""Independent exhaustive small-block PAL2 spectrum checker (no external dependencies)."""
from itertools import product
from collections import Counter

def duplicate(w, i):
    assert 0 <= i <= len(w)-2
    return w[:i+2] + w[i:i+2][::-1] + w[i+2:]

def sphere(w):
    return {duplicate(duplicate(w, i), j)
            for i in range(len(w)-1) for j in range(len(w)+1)}

def defects(w):
    return [i for i in range(len(w)-1) if w[i] == w[i+1]]

def run():
    assert len(sphere('000')) == 1
    assert len(sphere('0110')) == 10
    for n in range(4, 13):
        sizes = Counter()
        maxima, runners = [], []
        M = (n*n + 5*n - 8)//2
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            c = len(sphere(w))
            sizes[c] += 1
            if c == M:
                maxima.append(w)
            elif c == M-3:
                runners.append(w)
            else:
                assert c <= M-4, (n, w, c, M)
        assert sizes[M] == 2 and sizes[M-3] == 4
        assert all(len(defects(w)) == 0 for w in maxima)
        assert all(len(defects(w)) == 1 and defects(w)[0] in (0, n-2) for w in runners)
        print(f'n={n}, maximum={M}, next={M-3}, maxima={len(maxima)}, runners={len(runners)}')

if __name__ == '__main__':
    run()
