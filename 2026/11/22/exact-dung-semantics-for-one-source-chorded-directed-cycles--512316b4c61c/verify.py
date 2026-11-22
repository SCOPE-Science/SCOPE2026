"""Independent exhaustive check of chord-source directed-cycle Dung semantics.
This file is a finite sanity check, not the proof of the all-order theorem.
Run: python verify.py
"""
from itertools import combinations


def predicted(n, extra):
    extra = frozenset(extra)
    last = max(extra | {1})
    seed = [0] * n
    seed[0] = 1
    for j in range(1, n):
        seed[j] = 0 if j == 1 or j in extra else 1 - seed[j-1]
    with_zero = last % 2 == (n - 1) % 2
    if with_zero:
        assert seed[n-1] == 0
    else:
        assert seed[n-1] == 1
    common = {frozenset()}
    stab = set()
    if n % 2 == 0:
        odd = frozenset(range(1, n, 2))
        common.add(odd)
        stab.add(odd)
    if with_zero:
        a = frozenset(j for j in range(n) if seed[j])
        common.add(a)
        stab.add(a)
    preferred = set(stab) if stab else {frozenset()}
    return common, preferred, stab


def direct(n, extra):
    successors = [(1 << ((j+1)%n)) for j in range(n)]
    for j in extra: successors[0] |= 1 << j
    preds = [0]*n
    for u, out in enumerate(successors):
        for v in range(n):
            if out & (1 << v): preds[v] |= 1 << u
    full = (1 << n)-1
    admissible, complete, stable = [], set(), set()
    for s in range(1<<n):
        attacked = 0
        for u in range(n):
            if s & (1 << u): attacked |= successors[u]
        if attacked & s: continue
        defended = 0
        for v in range(n):
            if preds[v] & ~attacked == 0: defended |= 1<<v
        if s & ~defended: continue
        admissible.append(s)
        if s == defended: complete.add(s)
        if (s|attacked) == full: stable.add(s)
    preferred = {s for s in admissible if not any((t != s and s&t == s) for t in admissible)}
    convert = lambda fam: {frozenset(j for j in range(n) if s>>j & 1) for s in fam}
    return convert(complete), convert(preferred), convert(stable)


def main():
    cases = 0
    for n in range(4, 13):
        candidates = tuple(range(2, n-1))
        for mask in range(1 << len(candidates)):
            extra = frozenset(j for j in candidates if mask >> (j-2) & 1)
            a = direct(n, extra)
            b = predicted(n, extra)
            assert a == b, (n, extra, a, b)
            cases += 1
    for n in range(4, 25):
        potential = range(2, n-1)
        even_expected = odd_expected = 0
        for mask in range(1<<(n-3)):
            k = max({1} | {j for j in potential if mask>>(j-2)&1})
            if k % 2 == (n-1)%2:
                even_expected += 1
            else:
                odd_expected += 1
        if n & 1:
            r = (n-1)//2
            assert even_expected == (4**(r-1)-1)//3
            assert even_expected+odd_expected == 4**(r-1)
        else:
            r = n//2
            assert even_expected == (2*4**(r-2)+1)//3
            assert even_expected+odd_expected == 2*4**(r-2)
    print('VERIFY_OK', cases, 'complete/preferred/stable cases; enumerator census through n=24')

if __name__ == '__main__':main()
