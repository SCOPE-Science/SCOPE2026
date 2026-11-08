#!/usr/bin/env python3
"""Exact orbit quotient of the three-variable finite Brandt-matrix game.

For B_n={0} U ([n]x[n]), the only automorphisms needed here are
simultaneous permutations of the two matrix indices. A triple of semigroup
elements is classified by its zero positions and equality pattern among at
most six row/column endpoints. For each n, all permitted orbits and all
one-coordinate substitutions are enumerated, not sampled.
"""
from itertools import product


def canonical(seq):
    names = {}
    out = []
    for element in seq:
        if element is None:
            out.append(None)
        else:
            pair = []
            for x in element:
                if x not in names:
                    names[x] = len(names)
                pair.append(names[x])
            out.append(tuple(pair))
    return tuple(out)


def restricted_growth(length):
    if length == 0:
        yield ()
        return
    for previous in restricted_growth(length-1):
        for x in range(max(previous, default=-1)+2):
            yield previous + (x,)


def patterns(k=3):
    found = []
    for occupied in product((False, True), repeat=k):
        positions = [i for i, yes in enumerate(occupied) if yes]
        for labels in restricted_growth(2*len(positions)):
            seq = [None]*k
            for j, i in enumerate(positions):
                seq[i] = (labels[2*j], labels[2*j+1])
            seq = tuple(seq)
            assert seq == canonical(seq)
            found.append(seq)
    assert len(set(found)) == len(found)
    return found


def used(state):
    return len({index for pair in state if pair is not None for index in pair})


def product_of(a, b):
    if a is None or b is None or a[1] != b[0]:
        return None
    return (a[0],b[1])


def atomic(state):
    vals = (None,) + state  # None is the named absorbing zero
    return (tuple(a == b for a in vals for b in vals),
            tuple(product_of(a,b)==c for a in vals for b in vals for c in vals))


def successors(state, variable, n):
    remaining = list(state)
    remaining[variable] = None
    remaining = canonical(remaining)
    m = used(remaining)
    result = {remaining}
    # Every replacement has 0, 1 or 2 new index labels. The codes m and m+1
    # represent genuinely new labels, which require available base indices.
    for a in range(m+2):
        for b in range(m+2):
            updated = list(remaining)
            updated[variable] = (a,b)
            updated = canonical(updated)
            if used(updated) <= n:
                result.add(updated)
    return frozenset(result)


def normalize(signatures):
    keys = sorted(set(signatures.values()))
    code = {v:i for i,v in enumerate(keys)}
    return {key:code[v] for key,v in signatures.items()}


def calculation():
    all_states = patterns()
    assert len(all_states)==255 # 1+3*B_2+3*B_4+B_6 = 1+6+45+203
    sizes = range(1,9)
    states = {n:tuple(s for s in all_states if used(s)<=n) for n in sizes}
    edges = {(n,s,j): successors(s,j,n)
             for n in sizes for s in states[n] for j in range(3)}
    for (n,s,j),targets in edges.items():
        assert targets <= set(states[n])
    # Rigorous tail check: an orbit and all of its one-variable extensions
    # involve at most six endpoints, so these entire finite orbit-game
    # transition systems are identical for n=6,7,8. It follows by the same
    # coordinate argument that they are identical for every n>=6.
    assert states[6] == states[7] == states[8]
    for s in states[6]:
        for j in range(3):
            assert edges[6,s,j] == edges[7,s,j] == edges[8,s,j]
    color = normalize({(n,s):atomic(s) for n in sizes for s in states[n]})
    root = (None,None,None)
    table = []
    for rank in range(12):
        class_keys = [color[n,root] for n in sizes]
        # No use is made of the numerical labels, only their equality classes.
        number = len(set(class_keys))
        table.append((rank, number, class_keys))
        print(f"rank={rank} distinct_sentence_theories={number} "
              f"type_classes={len(set(color.values()))} "
              f"root_colors={','.join(map(str,class_keys))}")
        next_color = normalize({(n,s):(
             color[n,s],
             tuple(tuple(sorted({color[n,t] for t in edges[n,s,j]}))
                   for j in range(3)))
             for n in sizes for s in states[n]})
        if len(set(next_color.values()))==len(set(color.values())):
            assert all((color[x]==color[y])==(next_color[x]==next_color[y])
                   for x in color for y in color if x[0]==6 and y[0]==7)
            print(f"stable_rank={rank}")
            break
        color = next_color
    assert [i[1] for i in table] == [1,2,3,5,6]
    assert [i[2] for i in table][-1][-3:] == [table[-1][2][-3]]*3
    for rank,_,keys in table:
        for n in range(1,8):
            if keys[n-1] != keys[n]:
                assert rank >= {1:1,2:2,3:3,4:3,5:4}.get(n,0)
    print('ORBIT_CHECK_PASS')

if __name__=='__main__':
    calculation()
