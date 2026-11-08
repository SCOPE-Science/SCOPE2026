"""Exact finite certificate for cyclic seven-piece rotated odometers."""
from fractions import Fraction

Q = 7
B = 8
M = Q * B

def rotate(k):
    return tuple((i + k) % Q for i in range(Q))

def graph(pi):
    assert sorted(pi) == list(range(Q))
    edges = []
    for j in range(M):
        m = B * pi[j // B] + j % B
        if m < 28:
            edges.append(('rigid', m + 28))
        elif m < 42:
            edges.append(('rigid', m - 14))
        elif m < 49:
            edges.append(('rigid', m - 35))
        else:
            edges.append(('tail', m - 49))
    return edges

def induction(pi):
    edges = graph(pi)
    h, nxt, used = [], [], []
    for i in range(Q):
        j = i
        path = []
        while True:
            assert j not in path and len(path) < M
            if path:
                assert j >= Q, ('premature return to section', pi, i)
            path.append(j)
            tag, dest = edges[j]
            if tag == 'tail':
                nxt.append(dest)
                h.append(len(path))
                used.extend(path)
                break
            j = dest
    assert sorted(nxt) == list(range(Q))
    assert len(set(used)) == len(used)
    return tuple(nxt), tuple(h), tuple(used)

def rigid_cycles(pi):
    edges = graph(pi)
    found = set()
    cycles = []
    for j in range(M):
        if j in found:
            continue
        path = []
        order = {}
        cur = j
        while cur not in found and cur not in order:
            order[cur] = len(path)
            path.append(cur)
            kind, target = edges[cur]
            if kind == 'tail':
                break
            cur = target
        if cur in order and edges[path[-1]][0] == 'rigid':
            cycles.append(tuple(path[order[cur]:]))
        found.update(path)
    return cycles

EXPECT = {
    0: [((0, 1, 2, 3, 4, 5, 6), (8, 8, 8, 8, 8, 8, 8))],
    1: [((4, 5, 6, 2, 3, 0, 1), (4, 4, 4, 20, 20, 2, 2)), ((1, 2, 3, 4, 5, 6, 0), (2, 2, 2, 2, 2, 2, 44))],
    2: [((6, 0, 1, 2, 3, 4, 5), (38, 3, 3, 3, 3, 3, 3)), ((6, 0, 1, 2, 3, 4, 5), (8, 1, 1, 1, 1, 1, 1))],
    3: [((3, 4, 5, 6, 2, 0, 1), (8, 8, 8, 8, 18, 3, 3)), ((3, 4, 5, 6, 2, 0, 1), (4, 4, 4, 4, 18, 3, 3))],
    4: [((1, 2, 3, 4, 5, 6, 0), (2, 2, 2, 2, 2, 2, 44)), ((4, 5, 6, 2, 3, 0, 1), (4, 4, 4, 20, 20, 2, 2))],
    5: [((5, 6, 3, 4, 0, 1, 2), (8, 8, 3, 3, 2, 2, 2)), ((5, 6, 3, 4, 0, 1, 2), (4, 4, 3, 3, 2, 2, 2))],
    6: [((6, 0, 1, 2, 3, 4, 5), (8, 1, 1, 1, 1, 1, 1))],
}

if __name__ == '__main__':
    for k in range(Q):
        pi = rotate(k)
        for expected_next, expected_heights in EXPECT[k]:
            next_pi, h, cells = induction(pi)
            assert (next_pi, h) == (expected_next, expected_heights), (k, pi, next_pi, h)
            assert (len(set(cells)) == M) == (sum(h) == M)
            pi = next_pi
        if k in (0, 1, 4):
            assert not rigid_cycles(pi)
        else:
            if k in (2, 3):
                assert rigid_cycles(pi)
            else:
                assert rigid_cycles(rotate(k))
    # Exact affine-branch identity on all macrocell images away from the tail.
    for k in range(Q):
        for j in range(M):
            left, right = Fraction(j, M), Fraction(j + 1, M)
            middle = (left + right) / 2
            shifted = (middle + Fraction(k, Q)) % 1
            n = 1
            while shifted >= 1 - Fraction(1, 2 ** n):
                n += 1
            image = shifted - 1 + Fraction(3, 2 ** n)
            typ, dest = graph(rotate(k))[j]
            if typ == 'rigid':
                assert image >= Fraction(dest, M) and image < Fraction(dest + 1, M)
            else:
                assert image >= 0 and image < Fraction(1, B)
    print('SEVEN_ROTATIONS_EXACT_GRAPH_OK')
