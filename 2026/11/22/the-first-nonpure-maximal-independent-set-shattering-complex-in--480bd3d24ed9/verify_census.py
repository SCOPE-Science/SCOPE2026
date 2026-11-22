"""Exhaustive support and facet census for maximal independent sets of Q_d, d<=4.
No external dependencies. Run: python3 verify_census.py
"""
from collections import Counter
from itertools import combinations

def all_mis(d):
    n = 1 << d
    neighborhoods = [sum(1 << (v ^ (1 << j)) for j in range(d)) for v in range(n)]
    closed = [(1 << v) | neighborhoods[v] for v in range(n)]
    result=[]
    for h in range(1 << n):
        if any((h & (1<<v)) and (h & neighborhoods[v]) for v in range(n)):
            continue
        if all(h & closed[v] for v in range(n)):
            result.append(h)
    return result

def shattered(mis,d):
    n=1<<d
    return {s for s in range(1<<n)
            if (1<<s.bit_count()) <= len(mis) and
            len({m&s for m in mis}) == (1 << s.bit_count())}

def facets(sh,d):
    n=1<<d
    return {s for s in sh if all((s|(1<<v)) not in sh for v in range(n) if not(s>>v)&1)}

def histogram(sets):
    c=Counter(s.bit_count() for s in sets)
    return [c[i] for i in range(max(c,default=0)+1)]

expect = {
    1: ([1,2], [1]),
    2: ([1,4], [1]),
    3: ([1,8,16], [2]),
    4: ([1,16,88,160,104], [2,4]),
}
for d in range(1,5):
    mis=all_mis(d)
    sh=shattered(mis,d)
    ft=facets(sh,d)
    print('Q',d,'MIS',len(mis),'size_counts',sorted(Counter(m.bit_count() for m in mis).items()),
          'shattering',histogram(sh),'facets',sorted(Counter(f.bit_count() for f in ft).items()))
    assert histogram(sh)==expect[d][0]
    assert sorted({f.bit_count() for f in ft})==expect[d][1]
    assert all((1 << s.bit_count()) == len({m&s for m in mis}) for s in sh)
    if d==4:
        assert Counter(m.bit_count() for m in mis)=={4:24,5:16,8:2}
        assert Counter(f.bit_count() for f in ft)=={2:8,4:104}
        antipodes={((1<<v)|(1<<(v^15))) for v in range(16)}
        assert {f for f in ft if f.bit_count()==2}==antipodes
print('Q4_MIS_SHATTER_CENSUS_PASS')
