#!/usr/bin/env python3
"""Finite, exact verification of the eight-agent shortest averaging topology theorem.

Requires Python 3 standard library only. The mathematical proof of the
entropy-saturation lemma is in RESULT.md; this script verifies the remaining
finite classification and two explicit averaging certificates.
"""
from itertools import permutations

V = tuple(range(8))
FIRST = ((0, 1), (2, 3), (4, 5), (6, 7))


def matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rest = vertices[1:j] + vertices[j + 1:]
        for tail in matchings(rest):
            yield ((a, b),) + tail


def neighbors(edges):
    adj = [set() for _ in V]
    for a, b in edges:
        assert a != b and b not in adj[a]
        adj[a].add(b)
        adj[b].add(a)
    return adj


def isomorphic(edges_a, edges_b):
    a, b = neighbors(edges_a), neighbors(edges_b)
    assert all(len(x) == 3 for x in a + b)
    mapped = {}
    used = set()

    def walk():
        if len(mapped) == 8:
            return True
        remaining = [u for u in V if u not in mapped]
        u = max(remaining, key=lambda x: sum(int(z in mapped) for z in a[x]))
        for v in V:
            if v in used:
                continue
            if all(((w in a[u]) == (mapped[w] in b[v])) for w in mapped):
                mapped[u] = v
                used.add(v)
                if walk():
                    return True
                del mapped[u]
                used.remove(v)
        return False

    return walk()


def cube_edges():
    return tuple((u, u ^ (1 << j)) for u in V for j in range(3)
                 if u < (u ^ (1 << j)))


def wagner_edges():
    return tuple((u, (u + 1) % 8) for u in V) + tuple(
        (u, u + 4) for u in range(4))


def apply_exact_word(word):
    # Rows multiplied by 8: all arithmetic throughout is integral.
    rows = [[8 * int(i == j) for j in V] for i in V]
    for a, b in word:
        sm = [rows[a][j] + rows[b][j] for j in V]
        assert all(k % 2 == 0 for k in sm)
        rows[a] = [k // 2 for k in sm]
        rows[b] = rows[a].copy()
    return rows


def main():
    all_matchings = tuple(matchings(V))
    assert len(all_matchings) == 105
    q3, w8 = cube_edges(), wagner_edges()
    assert not isomorphic(q3, w8)
    first_masks = [0] * 8
    for a, b in FIRST:
        first_masks[a] = first_masks[b] = (1 << a) | (1 << b)

    counts = {'cube': 0, 'wagner': 0, 'other': 0}
    step2_counts = {'two-four-cycles': 0, 'eight-cycle': 0}
    for second in all_matchings:
        if any(first_masks[a] & first_masks[b] for a, b in second):
            continue
        second_masks = first_masks[:]
        for a, b in second:
            second_masks[a] = second_masks[b] = first_masks[a] | first_masks[b]
        # If first+second have two components, they are two C4's;
        # otherwise their union is one C8.
        combined = neighbors(FIRST + second)
        reachable = {0}
        stack = [0]
        while stack:
            z = stack.pop()
            for v in combined[z]:
                if v not in reachable:
                    reachable.add(v)
                    stack.append(v)
        typ = 'eight-cycle' if len(reachable) == 8 else 'two-four-cycles'
        assert len(reachable) in (4, 8)
        step2_counts[typ] += 1
        for third in all_matchings:
            if any(second_masks[a] & second_masks[b] for a, b in third):
                continue
            edges = FIRST + second + third
            adj = neighbors(edges)
            assert all(len(x) == 3 for x in adj)
            assert apply_exact_word(edges) == [[1] * 8 for _ in V]
            kind = ('cube' if isomorphic(edges, q3) else
                    'wagner' if isomorphic(edges, w8) else 'other')
            counts[kind] += 1
            assert kind != 'other', edges

    assert step2_counts == {'two-four-cycles': 12, 'eight-cycle': 48}
    assert counts == {'cube': 144, 'wagner': 336, 'other': 0}

    cube_word = (
        FIRST + ((0, 2), (1, 3), (4, 6), (5, 7)) +
        ((0, 4), (1, 5), (2, 6), (3, 7))
    )
    wagner_word = (
        ((0, 4), (1, 5), (2, 6), (3, 7)) +
        ((0, 1), (2, 3), (4, 5), (6, 7)) +
        ((0, 7), (1, 2), (3, 4), (5, 6))
    )
    for name, word, prototype in (
        ('cube', cube_word, q3), ('wagner', wagner_word, w8)
    ):
        assert set(map(frozenset, word)) == set(map(frozenset, prototype))
        assert apply_exact_word(word) == [[1] * 8 for _ in V]
        print(name + ': exact 12-contact identity 1*1^T/8 verified')
    # A 5-cycle (0,1,2,3,4,0) certifies Wagner nonbipartiteness.
    wset = {frozenset(x) for x in w8}
    assert all(frozenset(x) in wset for x in
               ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0)))
    print('step-two matching types:', step2_counts)
    print('admissible third matchings / graph types:', counts)
    print('all exact-rational and finite-isomorphism assertions passed')


if __name__ == '__main__':
    main()
