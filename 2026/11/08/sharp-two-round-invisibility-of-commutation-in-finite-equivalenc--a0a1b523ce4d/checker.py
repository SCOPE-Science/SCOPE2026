"""Exhaustive finite search for the least rank-two invisibility of equivalence-relation commutation.
Python 3 standard library only. Relational signature: equality, E, F.
"""
from itertools import product


def rgs_partitions(n):
    """All set partitions via restricted-growth words, exactly once each."""
    if n == 0:
        yield ()
        return
    def rec(t, maximum):
        if len(t) == n:
            yield tuple(t)
            return
        for a in range(maximum + 2):
            t.append(a)
            yield from rec(t, max(maximum, a))
            t.pop()
    yield from rec([0], 0)


def one_round_pointed_signature(E, F, x):
    # Four possible ordered-pair patterns for y distinct from x;
    # the self-pair is a fifth type, encoded as bit 3.
    mask = 0
    for y in range(len(E)):
        typ = (int(x != y) << 2) | (int(E[x] == E[y]) << 1) | int(F[x] == F[y])
        mask |= 1 << typ
    return mask


def two_round_sentence_signature(E, F):
    # Two-round EF equivalence from the empty tuple is equality of these sets.
    return tuple(sorted({one_round_pointed_signature(E, F, x) for x in range(len(E))}))


def commutes(E, F):
    n = len(E)
    for x in range(n):
        for y in range(n):
            EF = any(E[x] == E[z] and F[z] == F[y] for z in range(n))
            FE = any(F[x] == F[z] and E[z] == E[y] for z in range(n))
            if EF != FE:
                return False
    return True


def ef_two_round_wins(A, B):
    E, F = A
    G, H = B
    def atomic(x, y, xp, yp):
        return ((x == y) == (xp == yp) and (E[x] == E[y]) == (G[xp] == G[yp])
                and (F[x] == F[y]) == (H[xp] == H[yp]))
    def second(x, xp):
        return (all(any(atomic(x, y, xp, yp) for yp in range(len(G))) for y in range(len(E)))
                and all(any(atomic(x, y, xp, yp) for y in range(len(E))) for yp in range(len(G))))
    return (all(any(second(x, xp) for xp in range(len(G))) for x in range(len(E)))
            and all(any(second(x, xp) for x in range(len(E))) for xp in range(len(G))))


def check():
    per_size = {}
    evaluated = 0
    for n in range(1, 7):
        Ps = list(rgs_partitions(n))
        C, N = {}, {}
        for E, F in product(Ps, repeat=2):
            evaluated += 1
            s = two_round_sentence_signature(E, F)
            (C if commutes(E, F) else N).setdefault(s, (E, F))
        per_size[n] = C, N
    assert evaluated == 44168, evaluated
    # For n<=2, any frame has <=1 nontrivial pair-type. A same-signature
    # frame then has E,F each either equality or universal, hence commuting.
    # A 3-point noncommuting pair contains a V with x's E-only and F-only
    # neighbors but no point outside both classes. A commuting frame cannot
    # realize that pointed two-round pattern (rectangular-intersection lemma).
    # These facts exclude all unenumerated size pairs whose total <=10.
    for total in range(2, 10):
        for c in range(3, 7):
            n = total-c
            if 3 <= n <= 6:
                assert not (set(per_size[c][0]) & set(per_size[n][1]))
    optimal = {}
    for c,n in [(4,6), (5,5), (6,4)]:
        joint = set(per_size[c][0]) & set(per_size[n][1])
        optimal[(c,n)] = joint
    assert optimal[(4,6)] == {(120,)}
    assert optimal[(5,5)] == set()
    assert optimal[(6,4)] == {(56,120), (88,120)}
    grid = ((0,0,1,1),(0,1,0,1))
    cycle = ((0,0,1,1,2,2),(0,1,0,2,1,2))
    assert commutes(*grid) and not commutes(*cycle)
    assert two_round_sentence_signature(*grid) == two_round_sentence_signature(*cycle) == (120,)
    assert ef_two_round_wins(grid,cycle)
    assert not ef_two_round_wins(((0,0),(0,1)),((0,0,1),(0,1,0)))
    print('RANK_TWO_COMMUTATION_SHARP_OK', 'partition_pairs',evaluated, 'optimal_signatures',3)


if __name__ == '__main__':
    check()
