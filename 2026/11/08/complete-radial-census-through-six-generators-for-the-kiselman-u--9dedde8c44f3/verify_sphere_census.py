#!/usr/bin/env python3
"""Standalone exhaustive certificate for exact Kiselman semigroup metric levels n<=6.

Canonical word theorem used: each repeated letter must have both a lower
and a higher letter between consecutive occurrences (Kudryavtseva--Mazorchuk).
The validation has two distinct generation algorithms and two level tests.
"""
from collections import Counter, deque
from functools import lru_cache
import hashlib

@lru_cache(None)
def reduce_word(word):
    """Normalize by deleting duplicate i if its intervening letters are all <i or >i."""
    w = list(word)
    while True:
        changed = False
        for a in range(len(w)):
            for b in range(a + 1, len(w)):
                if w[a] != w[b]:
                    continue
                mid = w[a + 1:b]
                if all(v < w[a] for v in mid):
                    del w[b]
                    changed = True
                    break
                if all(v > w[a] for v in mid):
                    del w[a]
                    changed = True
                    break
            if changed:
                break
        if not changed:
            return tuple(w)

def extend_is_canonical(w, x):
    # All old pairs already satisfy canonicality. Only the last new x pair matters.
    try:
        index = len(w) - 1 - w[::-1].index(x)
    except ValueError:
        return True
    middle = w[index + 1:]
    return any(a < x for a in middle) and any(a > x for a in middle)

def enumerate_canonical(n):
    """Directly enumerate the canonical language without performing reductions."""
    todo = [()]
    seen = {()}
    for w in todo:
        for x in range(1, n + 1):
            if extend_is_canonical(w, x):
                v = w + (x,)
                assert v not in seen
                seen.add(v)
                todo.append(v)
    return seen

def enumerate_by_products(n):
    """Independently generate the closure of 1 under right-multiplication."""
    seen = {()}
    todo = deque([()])
    while todo:
        w = todo.popleft()
        for x in range(1, n + 1):
            v = reduce_word(w + (x,))
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return seen

def greedy_level(w, n):
    level = n
    for x in w:
        if x == level:
            level -= 1
    return level

def deleted_level(w, n):
    # Independently check equality in the K_n quotient via canonical reductions.
    for r in range(n + 1):
        deleted = tuple(x for x in w if x > r)
        reduced = reduce_word(deleted)
        target = tuple(range(n, r, -1))
        if reduced == target:
            return r
    raise AssertionError('missing radius')

def main():
    expected_orders = (1, 2, 5, 18, 115, 1710, 83973)
    summaries = []
    for n in range(1, 7):
        words = enumerate_canonical(n)
        assert len(words) == expected_orders[n], (n, len(words))
        from_products = enumerate_by_products(n)
        assert words == from_products, ('normal-form mismatch', n)
        levels = Counter()
        for w in words:
            l1 = greedy_level(w, n)
            l2 = deleted_level(w, n)
            assert l1 == l2, ('level mismatch', n, w, l1, l2)
            levels[l1] += 1
        counts = tuple(levels[r] for r in range(n+1))
        assert counts[0] == 1
        assert sum(counts) == len(words)
        assert counts[1] == counts[-1] == expected_orders[n-1]
        assert counts[1:] == counts[:0:-1], ('finite palindrome fails',n,counts)
        h = hashlib.sha256()
        for w in sorted(words):
            h.update(bytes((len(w),)) + bytes(w))
        digest = h.hexdigest()
        print('n=%d order=%d spheres=%s canonical_sha256=%s' % (n,len(words),counts,digest),flush=True)
        summaries.append((n, counts, digest))
    print('VERIFY_OK cases=6 complete_words=%d two_generators=matched two_level_rules=matched' %
          sum(len(enumerate_canonical(n)) for n in range(1,7)),flush=True)
if __name__ == '__main__':
    main()
