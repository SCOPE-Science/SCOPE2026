#!/usr/bin/env python3
"""Exact integer polynomial certificate and independent isolated-word census."""
from itertools import product

FORBIDDEN = ('010', '110111', '111011')
PREFIXES = ('', '0', '1', '01', '11', '110', '111', '1101', '1110', '11011', '11101')
# Coefficients of the vector X(z) in (I-zT)X(z)=D(z)b.
X = (
    (1,1,2,2,1,1),
    (1,1,1,1),
    (1,1,2,0,2,1,1),
    (1,0,1,-1,1,1,1),
    (1,1,0,1,2,2,1),
    (1,0,1,1,1),
    (1,0,1,1,2,2,1),
    (0,0,1,0,1,1,1),
    (0,1,1,1,1),
    (0,1,0,1,1,1),
    (0,),
)
D = (1,-1,0,-1,0,-1,-1,-1)
N = (1,1,0,1,2,2,1)


def nxt(state, letter):
    word = state + letter
    if any(p in word for p in FORBIDDEN):
        return None
    return max((p for p in PREFIXES if word.endswith(p)), key=len)


def after(state, suffix):
    for char in suffix:
        state = nxt(state, char)
        if state is None:
            return None
    return state


def main():
    edges = {(i, PREFIXES.index(nxt(state, letter))) for i, state in enumerate(PREFIXES)
             for letter in '01' if nxt(state, letter) is not None}
    b = tuple(int(after(p, '11') is not None) for p in PREFIXES)
    for i in range(len(PREFIXES)):
        for deg in range(9):
            lhs = (X[i][deg] if deg < len(X[i]) else 0)
            lhs -= sum(X[j][deg-1] if deg and deg-1 < len(X[j]) else 0
                       for k, j in edges if k == i)
            rhs = b[i] * (D[deg] if deg < len(D) else 0)
            assert lhs == rhs, (i, deg, lhs, rhs)
    initial = after('', '11')
    assert initial == '11' and tuple(X[PREFIXES.index(initial)]) == N

    # A finite word is isolated precisely when its 11-padded form avoids
    # all three forbidden factors. Count independently by swap testing.
    counts = []
    for n in range(15):
        isolated = 0
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            if '010' in w:
                continue
            neighbors = []
            for j in range(n-1):
                if w[j] != w[j+1]:
                    v = w[:j] + w[j+1] + w[j] + w[j+2:]
                    if '010' not in v:
                        neighbors.append(v)
            pad = '11' + w + '11'
            direct = not neighbors
            regular = not any(f in pad for f in FORBIDDEN)
            assert regular == direct, (n, w, neighbors)
            isolated += direct
        counts.append(isolated)
        expected = (N[n] if n < len(N) else 0)
        expected += sum(counts[n-k] for k in (1,3,5,6,7) if n >= k)
        assert isolated == expected, (n, isolated, expected)
        print('isolated', n, isolated)
    print('VERIFY_ISOLATED_OK')


if __name__ == '__main__':
    main()
