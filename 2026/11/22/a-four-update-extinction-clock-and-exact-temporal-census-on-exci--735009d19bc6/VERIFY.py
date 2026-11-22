"""Reproduce exact three-color threshold-two extinction censuses on sunlet graphs.

Uses Python 3 standard library only. Run: python VERIFY.py
"""
from itertools import product


def zeros(d):
    return [[0] * d for _ in range(d)]


def matmul(a, b):
    n = len(a)
    c = zeros(n)
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    c[i][j] += a[i][k] * b[k][j]
    return c


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def eye(n):
    a = zeros(n)
    for i in range(n):
        a[i][i] = 1
    return a


def powers_and_charpoly(a, upto=12):
    d = len(a)
    p = eye(d)
    tr = [d]
    for k in range(1, max(upto, d) + 1):
        p = matmul(p, a)
        tr.append(trace(p))
    coef = [1]
    for k in range(1, d + 1):
        v = -sum(coef[k-j] * tr[j] for j in range(1, k + 1))
        assert v % k == 0
        coef.append(v // k)
    return tr, coef


def no_first_excitation_matrix():
    q = zeros(9)
    for left, center, right in product(range(3), repeat=3):
        n1 = (left == 1) + (right == 1)
        weight = 3 if center != 0 or n1 == 0 else 2 if n1 == 1 else 0
        q[3 * left + center][3 * center + right] += weight
    return q


def no_second_excitation_matrix():
    # Site letters A=(core 1, arbitrary pendant): weight 3;
    # B=(core 0, pendant 1): weight 1;
    # C=(all other core/pendant pairs): weight 5.
    # A newly excited core at t=2 exists exactly on a circular word
    # A B (B|C) B A. Reject the two possible completions below.
    banned = ('ABBBA', 'ABCBA')
    pre = sorted({''} | {p[:i] for p in banned for i in range(1, 5)},
                 key=lambda x: (len(x), x))
    a = zeros(len(pre))
    for k, s in enumerate(pre):
        for letter, weight in (('A', 3), ('B', 1), ('C', 5)):
            word = s + letter
            if any(word.endswith(p) for p in banned):
                continue
            dest = max((t for t in pre if word.endswith(t)), key=len)
            a[k][pre.index(dest)] += weight
    assert pre == ['', 'A', 'AB', 'ABB', 'ABC', 'ABBB', 'ABCB']
    return a


def direct_histogram(n):
    # Independent graph-neighbor evolution, no transfer or motif shortcuts.
    ans = [0] * 5
    nbrs = [[(i-1) % n, (i+1) % n, n+i] for i in range(n)] + [[i] for i in range(n)]
    for word in product(range(3), repeat=2*n):
        state = word
        for time in range(5):
            if not any(state):
                ans[time] += 1
                break
            if time == 4:
                raise AssertionError(('non-extinct', n, state))
            out = []
            for i in range(2*n):
                color = state[i]
                if color == 1:
                    out.append(2)
                elif color == 2:
                    out.append(0)
                else:
                    out.append(int(sum(state[j] == 1 for j in nbrs[i]) >= 2))
            state = tuple(out)
    return ans


def main():
    q = no_first_excitation_matrix()
    a = no_second_excitation_matrix()
    pq, cq = powers_and_charpoly(q, 20)
    pa, ca = powers_and_charpoly(a, 20)
    assert cq == [1, -9, 9, -21, 0, 0, 0, 0, 0, 0], cq
    assert ca == [1, -9, 0, 0, 18, -108, 0, 0], ca
    expected = {
        3: [1, 63, 485, 180, 0],
        4: [1, 255, 4307, 1926, 72],
        5: [1, 1023, 36425, 21330, 270],
        6: [1, 4095, 303407, 221022, 2916],
        7: [1, 16383, 2509925, 2226042, 30618],
        8: [1, 65535, 20690147, 21977406, 313632],
    }
    for n in range(3, 13):
        h = pq[n]
        t = 9**n - pa[n]
        hist = [1, 4**n-1, h-4**n, 9**n-h-t, t]
        assert sum(hist) == 9**n and min(hist) >= 0
        if n in expected:
            assert hist == expected[n], (n, hist, expected[n])
        if n <= 6:
            assert direct_histogram(n) == hist, (n, hist)
        print('n=%2d counts=%s' % (n, hist))
    print('characteristic polynomial Q: lambda^9 - 9 lambda^8 + 9 lambda^7 - 21 lambda^6')
    print('characteristic polynomial M: lambda^7 - 9 lambda^6 + 18 lambda^3 - 108 lambda^2')
    print('All independent enumeration and transfer checks passed.')

if __name__ == '__main__':
    main()
