#!/usr/bin/env python3
"""Independent reconstruction using odd central-factor parity and a prefix."""
from collections import Counter
from itertools import product


def counts(word, k):
    result = {}
    for m in range(1, min(len(word), k)+1):
        result[m] = Counter(''.join(word[j:j+m]) for j in range(len(word)-m+1))
    return result


def recover(n, k, d):
    if n <= k:
        return next(x for x,v in d[n].items() if v == 1)
    symbols = set(d[1])
    if k == 1:
        prefix = ''
    else:
        prefix_set = []
        for u,c in d[k-1].items():
            followed = sum(d[k].get(a+u,0) for a in symbols)
            if c-followed == 1:
                prefix_set.append(u)
        assert len(prefix_set) == 1
        prefix = prefix_set[0]
    j = k if (n-k)%2 == 0 else k-1
    if j == 0:
        center = ''
    else:
        candidates = [x for x,v in d[j].items() if x == x[::-1] and v%2 == 1]
        assert len(candidates) == 1, (n,k,candidates)
        center = candidates[0]
    w = [None]*n
    def write(i,c):
        assert w[i] in (None,c)
        w[i] = c
    for i,c in enumerate(prefix):
        write(i,c)
        write(n-1-i,c)
    st = (n-j)//2
    for i,c in enumerate(center):
        write(st+i,c)
    holes = [i for i,x in enumerate(w) if x is None]
    assert len(holes) in (0,2), (n,k,holes)
    if holes:
        assert holes[0]+holes[1] == n-1
        known = Counter(x for x in w if x is not None)
        remaining = d[1] - known
        assert len(remaining) == 1 and list(remaining.values()) == [2]
        c = next(iter(remaining))
        for i in holes:
            write(i,c)
    assert None not in w
    return ''.join(w)


for q,maxk in ((2,7),(3,4),(4,3)):
    for k in range(1,maxk+1):
        for n in range(1,3*k+1):
            for half in product(map(str,range(q)),repeat=(n+1)//2):
                word = ''.join(half) + ''.join(half[-2::-1] if n%2 else half[::-1])
                assert recover(n,k,counts(word,k)) == word,(q,k,n,word)
        print(f'PASS q={q}, k={k}: decoder recovers every palindrome through {3*k}')
print('ALL DECODER TESTS PASSED')
