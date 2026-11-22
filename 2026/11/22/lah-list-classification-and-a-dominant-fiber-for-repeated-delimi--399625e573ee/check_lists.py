"""Construct observation representatives from sets of ordered lists.

The special token 0 is in one distinguished list. All other lists are unordered.
Usage: python3 check_lists.py
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial


def set_partitions(elements):
    """Yield each partition as a tuple of blocks, with blocks internally sorted."""
    if not elements:
        yield ()
        return
    first, *rest = elements
    for partition in set_partitions(rest):
        yield ((first,),) + partition
        for j in range(len(partition)):
            modified = list(partition)
            modified[j] = tuple(sorted((first,) + modified[j]))
            yield tuple(modified)


def set_of_lists(s):
    for partition in set_partitions(tuple(range(s+1))):
        orderings = [list(permutations(block)) for block in partition]
        from itertools import product
        for lists in product(*orderings):
            yield lists


def representative(lists, r):
    star = next(block for block in lists if 0 in block)
    other = [block for block in lists if 0 not in block]
    if len(other) > r-1:
        return None
    index = star.index(0)
    prefix, suffix = star[:index], star[index+1:]
    # Canonical choice: take all zero-length returns first, then
    # traverse the nonempty lists in lexicographic order.
    w = tuple(prefix) + (0,)*(r-len(other))
    for block in sorted(other):
        w += tuple(block) + (0,)
    return w + tuple(suffix)


def signature(w):
    return (tuple(sorted(Counter(w).items())),
            tuple(sorted(Counter(zip(w,w[1:])).items())))


def check(r,s):
    signatures = set()
    by_k = Counter()
    for lists in set_of_lists(s):
        word = representative(lists,r)
        if word is None:continue
        sig=signature(word)
        assert sig not in signatures, (r,s,'two list partitions with same profile')
        signatures.add(sig)
        by_k[len(lists)-1] += 1
    expected_k = {k: factorial(s)*comb(s+1,k+1)//factorial(k)
                  for k in range(min(s,r-1)+1)}
    assert dict(by_k) == expected_k, (r,s,by_k,expected_k)
    return len(signatures)


if __name__ == '__main__':
    cases=0
    for s in range(0,7):
        for r in range(1,9):
            check(r,s)
            cases+=1
    print('Set-of-lists bijection and finite-height counts: PASS')
    print('Parameter cases:', cases)
    print('Saturated profile counts for s=0,...,6:',
          [check(s+1,s) for s in range(7)])
