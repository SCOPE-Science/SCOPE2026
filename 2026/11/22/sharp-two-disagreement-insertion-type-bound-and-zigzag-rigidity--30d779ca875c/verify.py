#!/usr/bin/env python3
"""Two finite diagnostic checks for two-disagreement insertion types.

Standard Python only; a finite diagnostic, not the infinite proof.
"""
import itertools
from collections import Counter


def type_disagreement(perm):
    n = len(perm)
    first = [(1 << i) - 1 for i in range(n + 1)]
    second = [0]
    for value in perm:
        second.append(second[-1] | (1 << (value-1)))
    return sum((a ^ b).bit_count() == 2 for a in first for b in second)


def direct_disagreement(perm):
    n = len(perm)
    positions = [0] * (n+1)
    for i, p in enumerate(perm):
        positions[p] = i
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            disagreements = sum((v<=i) != (positions[v]<j) for v in range(1,n+1))
            ans += disagreements == 2
    return ans


def reference_zigzag(n):
    # Unique Hamilton cycle in the path square, rooted at vertex 1.
    path = [1] + list(range(2,n+1,2)) + list(range(n if n%2 else n-1,2,-2))
    assert len(path)==n and set(path)==set(range(1,n+1))
    def to_perm(cycle):
        p = [0]*n
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):p[a-1]=b
        return tuple(p)
    return {to_perm(path),to_perm([path[0]]+path[:0:-1])}


def main():
    tot = 0
    for n in range(2,10):
        best = -1
        maxima = set()
        count = 0
        for p in itertools.permutations(range(1,n+1)):
            v=type_disagreement(p)
            assert v<=3*(n-1)
            if n<=6:
                assert v==direct_disagreement(p), (n,p)
            if v>best:
                best=v;maxima={p}
            elif v==best:
                maxima.add(p)
            count += 1
        expected = ({(2,1)} if n==2 else
                    {(2,3,1),(3,1,2),(3,2,1)} if n==3 else
                    reference_zigzag(n))
        assert best == 3*(n-1), (n,best)
        assert maxima == expected, (n,maxima,expected)
        print(f'n={n} permutations={count} maximum={best} maximizers={len(maxima)}')
        tot +=count
    for n in range(3,11):
        # Compute Hamilton cycles by fixing initial vertex 1, reversing symmetry.
        canonical=set()
        for pathTail in itertools.permutations(range(2,n+1)):
            cycle=(1,)+pathTail
            if all(abs(cycle[i]-cycle[(i+1)%n])<=2 for i in range(n)):
                canonical.add(cycle)
        assert len(canonical)==2,(n,canonical)
        print(f'P_{n}^2 oriented Hamiltonian cycles=2')
    print(f'PASS independent enumeration; total={tot} permutations')
    print('FINITE_ENUMERATION_DOES_NOT_PROVE_ALL_N')

if __name__=='__main__':main()
