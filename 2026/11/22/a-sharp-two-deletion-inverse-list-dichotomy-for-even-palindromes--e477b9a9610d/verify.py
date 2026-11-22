"""Independent direct/constructive checks of two-deletion inverse lists of even palindromes.
Run: python3 verify.py ; Python standard library only.
"""
from collections import defaultdict
from itertools import combinations, product


def is_subsequence(w, p):
    j = 0
    for v in p:
        if j < len(w) and v == w[j]:
            j += 1
    return j == len(w)


def palindrome_one_insertions(t):
    """Possible even palindromes one symbol longer than an odd word."""
    odd = {v for v in t if t.count(v) % 2}
    if len(odd) != 1:
        return set()
    a = next(iter(odd))
    return {p for k in range(len(t) + 1)
            for p in [t[:k] + (a,) + t[k:]] if p == p[::-1]}


def predicted_parents(z, alphabet):
    h = len(z) // 2
    if z == z[::-1]:
        half = z[:h]
        us = {half[:i] + (a,) + half[i:] for a in alphabet for i in range(h+1)}
        return {u + u[::-1] for u in us}
    left, right = 0, len(z)-1
    while left < right and z[left] == z[right]:
        left += 1
        right -= 1
    outer = z[:left]
    core = z[left:right+1]
    assert core[0] != core[-1]
    parents = set()
    for a, odd in [(core[0], core[1:]), (core[-1], core[:-1])]:
        for mid in palindrome_one_insertions(odd):
            p = outer + (a,) + mid + (a,) + outer[::-1]
            if is_subsequence(z, p):
                parents.add(p)
    return parents


def actual_parents(q, m):
    parents = defaultdict(set)
    for u in product(range(q), repeat=m):
        p = u + u[::-1]
        shadows = {tuple(c for idx, c in enumerate(p) if idx != i and idx != j)
                   for i, j in combinations(range(2*m), 2)}
        for z in shadows:
            parents[z].add(p)
    return parents


def check(q,m):
    alphabet = tuple(range(q))
    direct = actual_parents(q,m)
    predicted = 0
    observed_nonpal = 0
    for z in product(alphabet,repeat=2*m-2):
        pred = predicted_parents(z, alphabet)
        got = direct.get(z,set())
        assert pred == got, (q,m,z,pred,got)
        if z == z[::-1]:
            assert len(got) == (q-1)*m+1
            predicted += 1
        else:
            assert len(got) <= 2
            observed_nonpal += int(len(got)==2)
    assert predicted == q**(m-1)
    if m>=2:
        assert any(len(v)==2 for z,v in direct.items() if z!=z[::-1])
    return (q,m,q**m,len(direct),predicted,observed_nonpal)

if __name__=='__main__':
    cases = [(2,m) for m in range(1,10)] + [(3,m) for m in range(1,7)] + [(4,m) for m in range(1,5)] + [(5,m) for m in range(1,4)]
    results=[check(q,m) for q,m in cases]
    for row in results:
        print('PASS alphabet=%d semilength=%d parents=%d reachable=%d maximal_receivers=%d nonpal_list2=%d'%row)
    print('VERIFY_OK cases=%d total_source_words=%d'%(len(results),sum(q**m for q,m in cases)))
