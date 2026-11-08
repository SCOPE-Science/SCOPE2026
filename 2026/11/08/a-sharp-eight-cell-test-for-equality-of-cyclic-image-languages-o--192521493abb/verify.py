#!/usr/bin/env python3
"""Exact finite-state verification for one-step cyclic ECA image-language classification.

Standard-library only.  All infinite-language equalities are checked by complete
reachability in finite deterministic relation-automaton products.
"""
from collections import Counter, defaultdict
from hashlib import sha256
import json


def local(rule, left, center, right):
    return (rule >> (4*left + 2*center + right)) & 1


def forward(rule, word):
    n = len(word)
    return tuple(local(rule, word[(i-1)%n], word[i], word[(i+1)%n]) for i in range(n))


def direct_images(rule, n):
    return {forward(rule, tuple((i >> j)&1 for j in range(n)))
            for i in range(1<<n)}


def matrices(rule):
    # Each matrix is four four-bit rows representing labeled arcs ab -> bc.
    mat = [[0]*4 for _ in (0,1)]
    for ab in range(4):
        for c in (0,1):
            bc = 2*(ab%2)+c
            bit = local(rule, ab//2, ab%2, c)
            mat[bit][ab] |= 1 << bc
    return mat


def mul(relation, matrix):
    result = 0
    for i in range(4):
        old_row = (relation >> (4*i)) & 15
        new_row = 0
        for j in range(4):
            if old_row & (1<<j):
                new_row |= matrix[j]
        result |= new_row << (4*i)
    return result


def accepts(relation):
    return any(relation & (1 << (5*i)) for i in range(4))


def automaton(rule):
    mats = matrices(rule)
    start = 0x8421
    states = [start]
    idx = {start: 0}
    transitions = []
    for state in states:
        row = []
        for mat in mats:
            nxt = mul(state, mat)
            if nxt not in idx:
                idx[nxt] = len(states)
                states.append(nxt)
            row.append(idx[nxt])
        transitions.append(tuple(row))
    outputs = [bool(accepts(state)) for state in states]
    return transitions, outputs


def same_all_lengths(a, b):
    da, fa = a
    db, fb = b
    seen = {(0, 0)}
    queue = [(0, 0)]
    for s, t in queue:
        if fa[s] != fb[t]:
            return False, len(queue)
        for bit in (0, 1):
            pair = (da[s][bit], db[t][bit])
            if pair not in seen:
                seen.add(pair)
                queue.append(pair)
    return True, len(queue)


def main():
    # True input brute force, independent of relation-automaton construction.
    image = [[None]*9 for _ in range(256)]
    for rule in range(256):
        for n in range(1, 9):
            image[rule][n] = direct_images(rule,n)

    for n in range(1,9):
        signatures = defaultdict(list)
        for rule in range(256):
            # Canonical key consists of ALL outputs, at ALL lengths <=n.
            signature = tuple(tuple(sorted(image[rule][k])) for k in range(1,n+1))
            signatures[signature].append(rule)
        print('DISTINCT_PREFIX_LANGUAGES',n,len(signatures))
        if n == 7:
            assert len(signatures) == 99
        if n == 8:
            assert len(signatures) == 100
            classes = sorted(signatures.values(),key=lambda g:g[0])

    assert Counter(map(len,classes)) == {1:8,2:75,4:10,6:3,10:4}
    from pathlib import Path
    table_path = Path(__file__).with_name('classes.json')
    assert json.loads(table_path.read_text(encoding='utf-8')) == classes
    assert all(sorted(g)==g for g in classes)
    assert image[57][8] != image[99][8]
    witness = tuple(map(int, '00010011'))
    assert witness in image[57][8] and witness not in image[99][8]
    assert all(image[57][n]==image[99][n] for n in range(1,8))
    predecessor = tuple(map(int,'11100101'))
    assert forward(57,predecessor)==witness

    automata = [automaton(rule) for rule in range(256)]
    # Cross-check the wholly different de Bruijn construction directly, at
    # every binary word of length at most 8 for each of the 256 rules.
    for rule in range(256):
        m = matrices(rule)
        for n in range(1,9):
            for i in range(1<<n):
                word = tuple((i>>j)&1 for j in range(n))
                relation = 0x8421
                for bit in word:
                    relation = mul(relation,m[bit])
                assert bool(accepts(relation)) == (word in image[rule][n]), (rule,word)

    # All 156 nonrepresentative rules are proved equivalent to their class
    # representative over *all* nonempty word lengths, not just <=8.
    checked = 0
    max_product = (0,None)
    for group in classes:
        rep = group[0]
        for other in group[1:]:
            equal, pairs = same_all_lengths(automata[rep],automata[other])
            assert equal,(rep,other)
            checked += 1
            if pairs > max_product[0]:
                max_product = (pairs,(rep,other))
    assert checked==156
    assert max_product == (2375,(22,104))

    print('NUMBER_CLASSES',len(classes))
    print('CLASS_SIZE_PROFILE',sorted(Counter(map(len,classes)).items()))
    print('EQUIVALENCE_BFS_CHECKS',checked)
    print('LARGEST_PRODUCT_BFS',max_product)
    print('SHARP_WITNESS_RULES',57,99,'WORD','00010011')
    print('CLASSES_JSON_SHA256',sha256((json.dumps(classes,separators=(',',':'))+'\n').encode()).hexdigest())
    print('VERIFY_OK')
    return classes

if __name__=='__main__':
    main()
