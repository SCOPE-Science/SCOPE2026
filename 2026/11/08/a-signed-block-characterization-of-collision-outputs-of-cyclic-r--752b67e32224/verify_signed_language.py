#!/usr/bin/env python3
"""Check a signed block normal form for multiple Rule-30 ancestors on a ring.
Standard-library Python 3. Run: python3 verify_signed_language.py.
Checks the pair-automaton reduction and exhaustive short-ring equivalence.
"""

E = (("A", 1, "D", 0),
     ("D", 1, "B", 1), ("D", 1, "C", 1),
     ("B", 0, "A", 0), ("B", 1, "A", 1),
     ("C", 0, "B", 0), ("C", 0, "C", 0))
V = "ABCD"


def local(a, b, c):
    return a ^ (b | c)


def full_pair_graph():
    """States are ordered (a,b;c,d) in four binary digits."""
    edges = {}
    for s in range(16):
        a, b, c, d = ((s >> j) & 1 for j in (3, 2, 1, 0))
        if (a, b) == (c, d):
            continue
        out = []
        for e in (0, 1):
            for f in (0, 1):
                if local(a, b, e) == local(c, d, f):
                    t = (b << 3) | (e << 2) | (d << 1) | f
                    out.append((local(a, b, e), t))
        edges[s] = out
    return edges


def graph_reaches(s, target, edges):
    stack = [t for _, t in edges[s]]
    seen = set()
    while stack:
        v = stack.pop()
        if v == target:
            return True
        if v not in seen:
            seen.add(v)
            stack.extend(t for _, t in edges.get(v, ()))
    return False


def certify_pair_quotient():
    edges = full_pair_graph()
    recurrent = {s for s in edges if graph_reaches(s, s, edges)}
    # Recurrent off-diagonal states; other four cannot occur in a cyclic collision.
    loc = {1: ('A', 0), 4: ('A', 1),
           2: ('B', 0), 8: ('B', 1),
           3: ('C', 0), 12: ('C', 1),
           6: ('D', 0), 9: ('D', 1)}
    assert recurrent == set(loc), (recurrent, set(loc))
    assert len(edges) == 12
    expected = sorted(E)
    assert sorted((loc[t][0], bit, loc[u][0], loc[t][1] ^ loc[u][1])
                  for t, out in edges.items() if t in recurrent
                  for bit, u in out if u in recurrent) == sorted(E + E), \
           'Each signed quotient transition should lift in two orientations'
    assert sorted((loc[u][0], bit, loc[v][0], loc[u][1] ^ loc[v][1])
                  for u in (1, 2, 3, 6)
                  for bit, v in edges[u] if v in recurrent) == expected
    print('INDEPENDENT_PAIR_GRAPH_REDUCTION_OK 12 offdiagonal, 8 recurrent')


def graph_ambiguity(word):
    for start in V:
        states = {(start, 0)}
        for char in word:
            states = {(b, p ^ q) for a, t, b, q in E
                      for v, p in states if v == a and t == int(char)}
            if not states:
                break
        if (start, 0) in states:
            return True
    return False


def parses_blocks(word):
    n = len(word)
    if set(word) == {'0'}:
        return True
    for r in range(n):
        w = word[r:] + word[:r]
        dp = {(0, 0)}
        for _ in range(n):
            ndp = set(dp)
            for i, p in dp:
                if i + 3 > n or w[i:i+2] != '11':
                    continue
                for j in range(i+2, n):
                    if j > i+2 and w[j-1] != '0':
                        break
                    ndp.add((j+1, p ^ (w[j] == '0')))
            if ndp == dp:
                break
            dp = ndp
        if (n, 0) in dp:
            return True
    return False


def image(x, n):
    y = 0
    for i in range(n):
        a, b, c = ((x >> (j % n)) & 1 for j in (i-1, i, i+1))
        y |= local(a, b, c) << i
    return y


def exhaustive():
    total = 0
    for n in range(3, 17):
        counts = [0] * (1 << n)
        for x in range(1 << n):
            counts[image(x, n)] += 1
        for y, k in enumerate(counts):
            s = ''.join(str((y >> i) & 1) for i in range(n))
            graph = graph_ambiguity(s)
            blocks = parses_blocks(s)
            assert graph == blocks == (k >= 2), (n, s, k, graph, blocks)
            assert k <= 3
            assert (k == 3) == (n % 3 == 0 and y == (1 << n) - 1)
        total += 1 << n
    print('SIGNED_BLOCK_LANGUAGE_EQUIVALENCE_OK 3..16', total, 'targets')


if __name__ == '__main__':
    certify_pair_quotient()
    exhaustive()
