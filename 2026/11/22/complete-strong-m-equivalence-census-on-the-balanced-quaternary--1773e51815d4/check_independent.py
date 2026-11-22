#!/usr/bin/env python3
"""Independent exact check via subsets of positions, not subsequence DP.

Compares all strong-scattered-profile fibers against components of the
local four-position exchange graph on balanced quaternary words.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

words=sorted({''.join(p) for p in permutations('00112233')})
assert len(words)==2520

patterns=tuple(''.join(p) for k in (2,3,4) for p in permutations('0123', k))
assert len(patterns)==60
positions=tuple(c for k in (2,3,4) for c in combinations(range(8), k))

def observation(word):
    counts=Counter()
    for pos in positions:
        pat=''.join(word[i] for i in pos)
        if len(set(pat))==len(pat):
            counts[pat]+=1
    return tuple(counts[p] for p in patterns)

fiber=defaultdict(set)
for word in words:
    fiber[observation(word)].add(word)

neighbors={}
for word in words:
    out=[]
    for j in range(5):
        z=word[j:j+4]
        if z[0]!=z[1] and z[0]==z[3] and z[1]==z[2]:
            out.append(word[:j] + z[1]+z[0]+z[0]+z[1] + word[j+4:])
    neighbors[word]=out

seen=set()
components=[]
for w in words:
    if w in seen:
        continue
    component={w}
    todo=[w]
    seen.add(w)
    while todo:
        u=todo.pop()
        for v in neighbors[u]:
            if v not in seen:
                seen.add(v); component.add(v); todo.append(v)
    components.append(component)

by_word={w:component for component in components for w in component}
assert len(by_word)==2520
assert all(by_word[w]==c for c in fiber.values() for w in c)
assert Counter(map(len,fiber.values()))=={1:2184,2:156,4:6}
print('independent_position_combination_check=PASS')
print('all_2346_scattered_fibers_equal_exactly_rewrite_components=PASS')
