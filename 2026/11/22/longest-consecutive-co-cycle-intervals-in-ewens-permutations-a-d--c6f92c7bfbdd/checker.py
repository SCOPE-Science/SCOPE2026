"""Independent finite enumerations for consecutive labels in equal permutation cycles.
Only finite identities are tested; asymptotic results require the accompanying proof.
"""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial


def longest_same_cycle_run(ids):
    best = cur = 1
    for a, b in zip(ids, ids[1:]):
        cur = cur + 1 if a == b else 1
        best = max(best, cur)
    return best


def permutation_cycle_ids(perm):
    n = len(perm)
    ids = [-1] * n
    for i in range(n):
        if ids[i] != -1: continue
        j = i
        while ids[j] == -1:
            ids[j] = i
            j = perm[j]
    return tuple(ids)


def partition_weights(n):
    # Independent restricted-growth-string partition enumerator.
    def rec(ids, counts):
        if len(ids) == n:
            weight = 1
            for size in counts: weight *= factorial(size-1)
            yield tuple(ids), weight
            return
        for c in range(len(counts)+1):
            if c == len(counts):
                yield from rec(ids+[c],counts+[1])
            else:
                cc = counts.copy(); cc[c] += 1
                yield from rec(ids+[c],cc)
    yield from rec([0],[1])


def main():
    tested = 0
    for n in range(2,9):
        by_perm = Counter()
        for p in permutations(range(n)):
            by_perm[longest_same_cycle_run(permutation_cycle_ids(p))] += 1
        by_parts = Counter()
        total=0
        for ids,w in partition_weights(n):
            by_parts[longest_same_cycle_run(ids)] += w
            total += w
        assert total == factorial(n)
        assert by_perm == by_parts, (n,by_perm,by_parts)
        assert sum(by_perm.values()) == factorial(n)
        assert sum((k-1)*v for k,v in by_perm.items()) >= 0
        tested += len(by_perm)+2
        print('n=',n,'exact longest-run probabilities=',{k: str(Fraction(v,factorial(n))) for k,v in sorted(by_perm.items())})
    print('PASS',tested,'exact assertions; no claim that finite checks prove asymptotics')

if __name__=='__main__':main()
