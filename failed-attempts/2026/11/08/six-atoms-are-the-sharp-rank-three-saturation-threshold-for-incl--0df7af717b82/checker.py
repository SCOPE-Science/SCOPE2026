#!/usr/bin/env python3
"""Exact bounded-rank types of finite powerset posets in the relation-only language.

Run: python3 checker.py
Pure Python 3 standard library; no external data.
"""
from functools import lru_cache


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for head in range(total + 1):
            for rest in weak_compositions(total - head, parts - 1):
                yield (head,) + rest


def atomic_signature(cells, k):
    # Membership of a ground atom in chosen element i is bit i of its cell.
    # Equality is detected by mutual inclusion, so no separate relation needed.
    return tuple(
        all(cells[b] == 0 for b in range(1 << k)
            if (b >> i) & 1 and not ((b >> j) & 1))
        for i in range(k) for j in range(k)
    )


@lru_cache(None)
def all_types(n, k, remaining):
    """Return {(Venn-cell sizes): exact remaining-rank FO type}.

    The k chosen subsets cut the n atoms into 2**k cells. For each
    next element, a cell of size a splits in all a+1 ways. A rank-r
    type is its rank-zero diagram together with its set of all
    rank-(r-1) one-element extension types. Replacing that set by
    a frozenset is lossless because existential and universal formulas
    are Boolean combinations of those extension types.
    """
    out = {}
    if remaining == 0:
        for v in weak_compositions(n, 1 << k):
            out[v] = atomic_signature(v, k)
        return out
    nxt = all_types(n, k + 1, remaining - 1)
    stride = 1 << k
    for v in weak_compositions(n, stride):
        all_child_types = set()
        cells = [0] * (2 * stride)

        def split(j):
            if j == stride:
                all_child_types.add(nxt[tuple(cells)])
                return
            for upper in range(v[j] + 1):
                cells[j] = v[j] - upper
                cells[j + stride] = upper
                split(j + 1)
        split(0)
        # The atomic diagram is part of the type, even though it can
        # also be recovered from the nonempty set of child diagrams.
        out[v] = (atomic_signature(v, k), frozenset(all_child_types))
    return out


def root_type(n):
    return all_types(n, 0, 3)[(n,)]


def root_unary_count(n):
    return len({all_types(n, 1, 2)[(n-i, i)] for i in range(n+1)})


def direct_game_win(n, m, aa=(), bb=(), remaining=3):
    """Independent labelled-subset implementation of the 3-round game.

    Used solely for small cross-checks: no orbit/Venn compression.
    """
    if remaining == 0:
        return all(((aa[i] & aa[j]) == aa[i]) ==
                   ((bb[i] & bb[j]) == bb[i])
                   for i in range(len(aa)) for j in range(len(aa)))
    # Spoiler may choose from either side.
    for x in range(1 << n):
        if not any(direct_game_win(n, m, aa+(x,), bb+(y,), remaining-1)
                   for y in range(1 << m)):
            return False
    for y in range(1 << m):
        if not any(direct_game_win(n, m, aa+(x,), bb+(y,), remaining-1)
                   for x in range(1 << n)):
            return False
    return True


def main():
    signature = [root_type(n) for n in range(9)]
    # Exactly seven classes: n=0,1,2,3,4,5, and n>=6.
    for i in range(6):
        for j in range(i+1, 9):
            assert signature[i] != signature[j], (i,j)
    assert signature[6] == signature[7] == signature[8]
    assert [root_unary_count(n) for n in range(9)] == [1,2,3,4,5,6,7,7,7]
    # Independent direct game on the first three powerset sizes.
    for a in range(4):
        for b in range(a,4):
            assert direct_game_win(a,b) == (signature[a] == signature[b]), (a,b)
    # For n,m>=8 the universal 3-round strategy matching Venn cell
    # counts below 8,4,2,1 proves agreement: this part is mathematically
    # proved in the accompanying note and is not simulated here.
    print('BOOLEAN_INCLUSION_RANK3_OK',
          'unary_type_counts=1,2,3,4,5,6,7,7,7',
          'tail=6=7=8', 'direct_pairs=10')

if __name__ == '__main__':
    main()
