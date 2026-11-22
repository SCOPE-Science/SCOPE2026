#!/usr/bin/env python3
"""Direct finite-extension checks for height-two poset comparison deletion.
No external packages required. The finite checks are not an infinite proof.
"""
from itertools import combinations, product


def count_by_closure(a, b, deleted):
    """Independently add a vertex and test full transitive closure."""
    n = a+b
    old = {(i, a+j) for i in range(a) for j in range(b) if (i,j) not in deleted}
    count = 0
    for states in product((0, 1, 2), repeat=n):
        # 0 incomparable, 1 old < x, 2 x < old
        arcs = set(old)
        arcs.update((i, n) for i, s in enumerate(states) if s == 1)
        arcs.update((n, i) for i, s in enumerate(states) if s == 2)
        closure = set(arcs)
        for k in range(n+1):
            for i in range(n+1):
                if (i,k) not in closure:
                    continue
                for j in range(n+1):
                    if (k,j) in closure:
                        closure.add((i,j))
        if not any((i,i) in closure for i in range(n+1)) and closure == arcs:
            count += 1
    return count


def independent_sets(a, b, deleted):
    out = 0
    for left in range(1 << a):
        for right in range(1 << b):
            if all(not ((left>>i & 1) and (right>>j & 1)) for i,j in deleted):
                out += 1
    return out


def decomposition(a, b, deleted):
    D_left = 0
    D_right = 0
    for left in range(1, 1 << a):
        common = [j for j in range(b) if all((i,j) in deleted for i in range(a) if left>>i & 1)]
        D_left += (1 << len(common)) - 1
    for right in range(1, 1 << b):
        common = [i for i in range(a) if all((i,j) in deleted for j in range(b) if right>>j & 1)]
        D_right += (1 << len(common)) - 1
    return independent_sets(a, b, deleted)+(1 << a)+(1 << b)-2+D_left+D_right


def wedge_pairs(deleted):
    edges = list(deleted)
    return sum((i == ii or j == jj) for z,(i,j) in enumerate(edges)
               for ii,jj in edges[z+1:])


def bicliques(a,b,deleted):
    total = 0
    for I in range(1,1<<a):
        for J in range(1,1<<b):
            if all((i,j) in deleted for i in range(a) if I>>i&1
                   for j in range(b) if J>>j&1):
                total += 1
    return total


def is_matching(deleted):
    return len({i for i,j in deleted}) == len(deleted) and len({j for i,j in deleted}) == len(deleted)


def verify():
    tests = 0
    # Exhaustive missing-edge patterns of bounded size. Actual extension relations
    # are built directly, not by substituting into the claimed formula.
    for a in range(1,4):
        for b in range(1,4):
            universe = [(i,j) for i in range(a) for j in range(b)]
            for k in range(min(3,len(universe))+1):
                for edges in combinations(universe,k):
                    removed = frozenset(edges)
                    direct = count_by_closure(a,b,removed)
                    derived = decomposition(a,b,removed)
                    assert direct == derived, (a,b,removed,direct,derived)
                    assert direct == independent_sets(a,b,removed)+(1<<a)+(1<<b)-2+2*bicliques(a,b,removed)
                    if k <= min(a,b):
                        minimum = 3**k*2**(a+b-2*k)+2**a+2**b+2*k-2
                        assert direct >= minimum, (a,b,k,removed,direct,minimum)
                        assert (direct == minimum) == is_matching(removed), (a,b,k,removed)
                        if k >= 2 and not is_matching(removed):
                            second = minimum+2+3**(k-2)*2**(a+b-2*k)
                            assert direct >= second, (a,b,k,removed,direct,second)
                            assert (direct == second) == (wedge_pairs(removed) == 1), (a,b,k,removed)
                    tests += 1
    # At larger sizes, independently check the exact profile of every matching.
    for a in range(1,8):
        for b in range(1,8):
            for k in range(min(a,b)+1):
                removed = frozenset((i,i) for i in range(k))
                predicted = 3**k*2**(a+b-2*k)+2**a+2**b+2*k-2
                assert decomposition(a,b,removed) == predicted
    # Sharp second minimum also checked for all small nonmatching patterns.
    for a,b,k in [(2,2,2),(3,3,3),(3,4,3),(4,4,4)]:
        universe = [(i,j) for i in range(a) for j in range(b)]
        minimum = 3**k*2**(a+b-2*k)+2**a+2**b+2*k-2
        second = minimum+2+3**(k-2)*2**(a+b-2*k)
        outcomes = set()
        for choice in combinations(universe,k):
            removed=frozenset(choice)
            value = decomposition(a,b,removed)
            outcomes.add(value)
            assert value >= minimum
            if not is_matching(removed):
                assert value >= second
                assert (value == second) == (wedge_pairs(removed)==1)
        assert sorted(outcomes)[:2] == [minimum,second]
    # Strict FKG gap for two adjacent deletion edges, before all others.
    assert 5*16 > 9*8  # 5/8 > (3/4)^2
    print('ALL_HEIGHT_TWO_CHECKS_PASS',tests)


if __name__ == '__main__':
    verify()
