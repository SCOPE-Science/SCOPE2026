#!/usr/bin/env python3
"""Independent integer checks for seven-point binary Walsh magnitude profiles."""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from math import comb

N=7
EVEN=[v for v in range(1,1<<N) if v.bit_count()%2==0 and v.bit_count()>=4]

def rref_basis(words):
    piv={}
    for x in words:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv: y ^= piv[p]
            else:
                piv[p]=y
                break
    return tuple(piv[p] for p in sorted(piv,reverse=True))

def space(words):
    s={0}
    for x in words: s|={v^x for v in s}
    return frozenset(s)

def relation_profile(R):
    cnt=Counter(x.bit_count() for x in R if x)
    return tuple(cnt[i] for i in (4,6))

def wprofile_from_relation(R):
    dual=[x for x in range(1<<N) if all((x&v).bit_count()%2==0 for v in R)]
    counts=Counter(abs(N-2*x.bit_count()) for x in dual)
    size=len(dual)
    return tuple((counts[a],size) for a in (1,3,5,7))

def normalized_profile(R):
    cnt=wprofile_from_relation(R)
    from fractions import Fraction
    return tuple(Fraction(a,b) for a,b in cnt)

all_spaces={1:{frozenset([0])}}
for size in (2,4,8,16):
    prev=all_spaces[size//2]
    cur=set()
    for V in prev:
        for x in EVEN:
            if x not in V:
                T=frozenset(v for v in V)|frozenset(v^x for v in V)
                if all(v==0 or v.bit_count()>=4 for v in T):cur.add(T)
    all_spaces[size]=cur
assert [len(all_spaces[k]) for k in (1,2,4,8,16)]==[1,42,175,30,0]

expected={
 (0,0,0): (35,21,7,1,64),
 (1,1,0): (19,9,3,1,32),
 (1,0,1): (15,15,1,1,32),
 (2,3,0): (11,3,1,1,16),
 (2,2,1): (9,6,0,1,16),
 (3,7,0): (7,0,0,1,8),
}
# Validate all relation spaces, not only representatives.
for size in (1,2,4,8):
    for R in all_spaces[size]:
        t=size.bit_length()-1
        key=(t,)+relation_profile(R)
        assert key in expected, (key,R)
        expected_row=expected[key]
        assert normalized_profile(R)==tuple(__import__('fractions').Fraction(k,expected_row[-1]) for k in expected_row[:-1]),(R,key)

# Also independent affine-orbit test by coordinate permutations.
def permute(x,p):
    return sum(1<<p[j] for j in range(N) if x>>j&1)
for size in (1,2,4,8):
    unseen=set(all_spaces[size]); orbits=[]
    while unseen:
        R=next(iter(unseen))
        orbit={frozenset(permute(v,p) for v in R) for p in permutations(range(N))}
        assert orbit<=all_spaces[size]
        orbits.append(len(orbit));unseen-=orbit
    assert len(orbits)==(1 if size in (1,8) else 2),orbits

# Build relation space directly from each 7-subset in F2^4 and compare raw Walsh.
def nullspace_relation(points):
    n=len(points)
    return frozenset(v for v in range(1<<n) if v.bit_count()%2==0 and
       __import__('functools').reduce(int.__xor__,(points[i] for i in range(n) if v>>i&1),0)==0)

four_counts=Counter()
for E in combinations(range(16),7):
    R=nullspace_relation(E)
    key=(len(R).bit_length()-1,)+relation_profile(R)
    p=normalized_profile(R)
    actual=Counter(abs(sum(1 if (u&x).bit_count()%2==0 else -1 for x in E)) for u in range(16))
    assert tuple(__import__('fractions').Fraction(actual[a],16) for a in (1,3,5,7))==p,(E,key)
    four_counts[key]+=1
assert sum(four_counts.values())==comb(16,7)==11440
assert set(four_counts)=={(3,7,0),(2,3,0),(2,2,1)}

# Compare MacWilliams Krawtchouk formula independently for every relation orbit.
for size in (1,2,4,8):
    R=next(iter(all_spaces[size]))
    for j in range(8):
        val=0
        for v in R:
            w=v.bit_count()
            val+=sum((-1)**s*comb(w,s)*comb(7-w,j-s)
                     for s in range(max(0,j-(7-w)), min(w,j)+1))
        direct=sum(1 for u in range(128) if u.bit_count()==j and
                   all((u&v).bit_count()%2==0 for v in R))
        assert val==size*direct
print('CHECK_OK relation_spaces_1_2_4_8=1_42_175_30 all_7_subsets_F2_4=11440 affine_orbits=6')
print('F2^4 types:',dict(sorted(four_counts.items())))
for key in sorted(expected): print(key,expected[key])
