"""Independent cyclic difference-set test of the ternary plane, standard library only."""
from itertools import combinations
from collections import Counter
base=(0,1,3,9)
lines=tuple(sum(1<<((i+d)%13) for d in base) for i in range(13))
assert all(L.bit_count()==4 for L in lines)
assert len({((a&b).bit_count()) for a,b in combinations(lines,2)})==1
assert all((a&b).bit_count()==1 for a,b in combinations(lines,2))
F=(1<<13)-1
hypotheses={a|b|c for a,b,c in combinations(lines,3)}
assert len(hypotheses)==286
shattered=set()
for size in range(14):
    for indices in combinations(range(13),size):
        s=sum(1<<i for i in indices)
        traces={s&h for h in hypotheses}
        if len(traces)==1<<size:
            shattered.add(s)
expected={s for s in range(1<<13) if s.bit_count()<=3 or
          (s.bit_count()==4 and all((s&L).bit_count()<3 for L in lines))}
assert shattered==expected
assert Counter(x.bit_count() for x in shattered)=={0:1,1:13,2:78,3:286,4:234}
facets={s for s in shattered if not any(t!=s and s&t==s for t in shattered)}
assert Counter(s.bit_count() for s in facets)=={3:52,4:234}
assert {F^h for h in hypotheses}==facets
print('CYCLIC_PROJECTIVE_TRIPLE_LINES_PASS',
      'lines=13 concepts=286 supports=8192 faces=(1,13,78,286,234)',
      'facet_complement_duality=286')
