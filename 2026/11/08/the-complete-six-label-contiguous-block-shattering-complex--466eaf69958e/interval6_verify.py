#!/usr/bin/env python3
"""Exhaustive independent certificate checker for six-label contiguous-block shattering.

Usage: python interval6_verify.py [facet_orbits.json] [witnesses.json]
If paths absent, verify numerical theorem without certificates. No external packages.
"""
import itertools, json, math, sys, collections

N=6
LABELS=range(N)
QUERIES=tuple(sum(1<<x for x in a) for k in range(2,N) for a in itertools.combinations(LABELS,k))
QINDEX={q:i for i,q in enumerate(QUERIES)}
assert len(QUERIES)==56 and len(QINDEX)==56

# Independent incidence constructions: adjacent sliding windows and position span.
windows=set(); spans=set(); order_by_pattern={}
for p in itertools.permutations(LABELS):
    a=0
    for k in range(2,N):
        for j in range(N+1-k):
            q=sum(1<<x for x in p[j:j+k])
            a|=1<<QINDEX[q]
    loc={x:i for i,x in enumerate(p)}
    b=0
    for i,q in enumerate(QUERIES):
        pp=[loc[x] for x in LABELS if q>>x&1]
        if max(pp)-min(pp)+1==len(pp):b|=1<<i
    assert a==b, (p,a,b)
    windows.add(a);spans.add(b)
    order_by_pattern.setdefault(a,p)
assert windows==spans and len(windows)==360
PATS=tuple(sorted(windows))
FULL=(1<<len(PATS))-1
YES=tuple(sum(1<<j for j,v in enumerate(PATS) if (v>>i)&1) for i in range(len(QUERIES)))
NO=tuple(FULL^y for y in YES)

# Recursive splitting. The row population of each trace is an exact bitset.
# Every shattered k-support has a shattered (k-1)-prefix, proving exhaustivity.
levels=[{(): (FULL,)}]
while levels[-1]:
    next_level={}
    for support, groups in levels[-1].items():
        for i in range(support[-1]+1 if support else 0,len(QUERIES)):
            both=[]
            for g in groups:
                a=g & NO[i]; b=g & YES[i]
                if not a or not b:
                    break
                both.extend((a,b))
            else:
                next_level[support+(i,)]=tuple(both)
    levels.append(next_level)
    if len(levels)>9:raise AssertionError('unexpected depth')
counts=[len(level) for level in levels]
assert counts==[1,56,1540,17640,54810,20160,0],counts

# Independent spotwise direct signature witness check, for every top face.
for support in levels[5]:
    tr={sum(((x>>i)&1)<<j for j,i in enumerate(support)) for x in PATS}
    assert len(tr)==32

# All five adjacency edges of any six-label path form a shattered support.
# This witnesses the dimension and checks a natural extremal subfamily.
path_supports={tuple(sorted(QINDEX[(1<<p[i])|(1<<p[i+1])] for i in range(N-1))) for p in itertools.permutations(LABELS)}
assert len(path_supports)==360 and path_supports<=set(levels[5])

# A facet is a face belonging to no face in the immediately higher layer.
facets={}
for k in range(1,6):
    nonfacet=set()
    for face in levels[k+1]:
        for i in range(k+1):nonfacet.add(face[:i]+face[i+1:])
    facets[k]=set(levels[k])-nonfacet
assert {k:len(v) for k,v in facets.items()}=={1:0,2:0,3:0,4:25830,5:20160}

# Six-label symmetry acts on all subset queries.
perms=tuple(itertools.permutations(LABELS))
action=tuple(tuple(QINDEX[sum(1<<p[x] for x in LABELS if q>>x&1)] for q in QUERIES) for p in perms)
assert len(action)==math.factorial(N)

def orbit(face):
    return {tuple(sorted(mp[i] for i in face)) for mp in action}

# The disjoint-orbit partition is canonicalized by the lexicographically least support.
orbit_rows=[]
for k in [4,5]:
    remaining=set(facets[k])
    while remaining:
        representative=min(remaining)
        o=orbit(representative)
        assert o<=remaining and representative==min(o)
        remaining-=o
        orbit_rows.append({'size':k,'representative':list(representative),'orbit_size':len(o)})
assert sum(x['orbit_size'] for x in orbit_rows if x['size']==4)==25830
assert sum(x['orbit_size'] for x in orbit_rows if x['size']==5)==20160
assert [sum(x['size']==k for x in orbit_rows) for k in [4,5]]==[47,29]

# Intrinsic boundary-transition rank on five-query facets. For an all-positive
# ordering p, row j has a 1 at gap i iff query j changes its 0/1 membership
# between the two consecutive elements p[i],p[i+1]. Verify the rank is
# independent of the choice of all-positive ordering for every facet.
def gf2_rank(rows):
    pivots={}
    for v in rows:
        while v:
            b=v.bit_length()-1
            if b in pivots:v^=pivots[b]
            else:pivots[b]=v;break
    return len(pivots)

def boundary_rank(face,p):
    rows=[]
    for j in face:
        membership=[(QUERIES[j]>>v)&1 for v in p]
        rows.append(sum((membership[i]^membership[i+1])<<i for i in range(N-1)))
    return gf2_rank(rows)

ranks={}
for face,groups in levels[5].items():
    valid=groups[-1]  # all five answers positive
    seen=set()
    while valid:
        bit=valid&-valid
        ix=bit.bit_length()-1
        valid-=bit
        seen.add(boundary_rank(face,order_by_pattern[PATS[ix]]))
    assert len(seen)==1,(face,seen)
    ranks[face]=next(iter(seen))
assert collections.Counter(ranks.values())=={4:5040,5:15120}
for row in orbit_rows:
    if row['size']==5:
        row['boundary_rank']=ranks[tuple(row['representative'])]
assert collections.Counter((r['boundary_rank'],r['orbit_size']) for r in orbit_rows if r['size']==5)=={(4,360):2,(4,720):6,(5,720):21}

# Canonical representative and 32 witnessing orders for one five-query support.
support=min(levels[5]); witness_orders=[]
for bits in range(32):
    ps=[p for v,p in order_by_pattern.items() if sum(((v>>i)&1)<<j for j,i in enumerate(support))==bits]
    assert ps
    witness_orders.append(list(min(ps)))

if len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf-8') as f: stored=json.load(f)
    assert stored['query_masks']==list(QUERIES)
    assert stored['orbit_rows']==orbit_rows
    assert len(stored['orbit_rows'])==76
if len(sys.argv)>2:
    with open(sys.argv[2],encoding='utf-8') as f: cert=json.load(f)
    assert cert['support_indices']==list(support)
    assert cert['orders']==witness_orders
    for bits,p in enumerate(witness_orders):
        pos={v:i for i,v in enumerate(p)}
        observed=0
        for j,i in enumerate(support):
            t=[pos[v] for v in LABELS if QUERIES[i]>>v&1]
            if max(t)-min(t)+1==len(t):observed|=1<<j
        assert observed==bits

print('INTERVAL6_SHATTER_PASS concepts=360 queries=56 face_counts='+','.join(map(str,counts[:-1]))+' facets4=25830 facets5=20160 orbits4=47 orbits5=29 rank4=5040 rank5=15120')

