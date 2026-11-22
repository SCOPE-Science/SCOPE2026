"""Exact shattering census for unions of three distinct projective lines in PG(2,3).
All operations are integral; Python standard library only.
"""
from itertools import product, combinations
from collections import Counter

Q=3

def canonical(x):
    for v in x:
        if v:
            return tuple(y*pow(v,-1,Q)%Q for y in x)
    raise ValueError('zero vector')

P=sorted({canonical(v) for v in product(range(Q),repeat=3) if any(v)})
lines=sorted({sum(1<<i for i,p in enumerate(P) if sum(a*b for a,b in zip(h,p))%Q==0)
              for h in P})
assert len(P)==len(lines)==13
assert len(set(lines))==13 and all(x.bit_count()==4 for x in lines)
assert all((a&b).bit_count()==1 for a,b in combinations(lines,2))
assert all(sum(bool(L&(1<<i)) for L in lines)==4 for i in range(13))
full=(1<<13)-1
family={a|b|c for a,b,c in combinations(lines,3)}
assert len(family)==286
assert Counter(x.bit_count() for x in family)=={9:234,10:52}
complement_family={full^x for x in family}
collinear_triples={s for s in range(1<<13) if s.bit_count()==3 and any(s&L==s for L in lines)}
arcs={s for s in range(1<<13) if s.bit_count()==4 and all((s&L).bit_count()<=2 for L in lines)}
assert len(collinear_triples)==52 and len(arcs)==234
assert complement_family==arcs|collinear_triples

def faces_for(concepts):
    return {s for s in range(1<<13) if len({c&s for c in concepts})==1<<s.bit_count()}

faces=faces_for(family)
expected={s for s in range(1<<13) if s.bit_count()<=3}|arcs
assert faces==expected
assert Counter(s.bit_count() for s in faces)=={0:1,1:13,2:78,3:286,4:234}
facets={s for s in faces if not any(t!=s and s&t==s for t in faces)}
assert facets==arcs|collinear_triples

# Control family is exactly TWO distinct projective lines, not the 2-line family allowing a repeat.
exact_two={a|b for a,b in combinations(lines,2)}
faces_two=faces_for(exact_two)
assert Counter(s.bit_count() for s in faces_two)=={0:1,1:13,2:78,3:286,4:702}
assert arcs<=faces_two
print('COORDINATE_PROJECTIVE_TRIPLE_LINES_PASS',
      'lines=13 concepts=286 supports=8192',
      'faces=(1,13,78,286,234)', 'facets=(52,234)',
      'two_distinct_four_faces=702')
