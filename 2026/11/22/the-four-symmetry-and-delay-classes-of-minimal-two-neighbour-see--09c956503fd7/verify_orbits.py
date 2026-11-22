"""Independent symmetry/subcube check of inclusion-minimal two-neighbor seeds.

Run: python3 verify_orbits.py
Cube vertices are the integers 0,...,15 interpreted as bit vectors.
"""
import itertools
from collections import Counter

D=4
V=range(1<<D)
ALL=(1<<len(list(V)))-1
REPS=[(1,7,8),(3,4,8),(1,2,4,8),(0,3,7,8)]
EXPECT=[(3,4,48),(3,5,96),(4,3,16),(4,4,96)]

def permute_bits(v,p):
    out=0
    for old,new in enumerate(p):
        if (v>>old)&1:out|=1<<new
    return out

def group_orbit(rep):
    return {sum(1<<(permute_bits(v,p)^b) for v in rep)
        for p in itertools.permutations(range(D)) for b in V}

def percolates_by_subcubes(vertices):
    # A subcube is represented by (base, free) in four bits.
    # Adjacent/nearby subcubes are merged as in the subcube-hull theorem.
    cubes=[(v,0) for v in vertices]
    while True:
        found=False
        for i in range(len(cubes)):
            for j in range(i+1,len(cubes)):
                a,freea=cubes[i];b,freeb=cubes[j]
                fixed=15^(freea|freeb)
                if ((a^b)&fixed).bit_count()<=2:
                    free=freea|freeb|(a^b)
                    base=a&(~free&15)
                    cubes=cubes[:i]+cubes[i+1:j]+cubes[j+1:]+[(base,free)]
                    found=True
                    break
            if found:break
        if not found:break
    return len(cubes)==1 and cubes[0][1]==15

def time_by_rounds(seed):
    # Only representative verification uses round-time simulation,
    # whereas coverage/minimality is checked by independent subcube merging.
    active=set(seed)
    rounds=0
    while True:
        new=active|{v for v in V if sum((v^(1<<d)) in active for d in range(D))>=2}
        if new==active:break
        active=new; rounds+=1
    if active!=set(V):raise AssertionError('representative does not percolate')
    return rounds

union=set()
for rep,(size,rounds,count) in zip(REPS,EXPECT):
    o=group_orbit(rep)
    assert len(rep)==size and len(o)==count,(rep,len(o),count)
    assert all(s.bit_count()==size for s in o)
    assert time_by_rounds(rep)==rounds
    for s in o:
        ss=[v for v in V if (s>>v)&1]
        assert percolates_by_subcubes(ss)
        assert all(not percolates_by_subcubes([v for v in ss if v!=deleted]) for deleted in ss)
    assert not(o&union)
    union|=o
    print('orbit',rep,'size',size,'time',rounds,'count',len(o))

# An independent 2-to-4-site universe census; 2010 extremal theorem gives
# the 4-site upper bound, and the C++ checker independently handles all 2^16 sets.
small=set()
for size in range(5):
    for tup in itertools.combinations(V,size):
        if not percolates_by_subcubes(tup):continue
        if all(not percolates_by_subcubes([v for v in tup if v!=deleted]) for deleted in tup):
            small.add(sum(1<<v for v in tup))
assert small==union,(len(small),len(union))

def geometric_test(tup):
    n=len(tup)
    ds=tuple(sorted((a^b).bit_count() for a,b in itertools.combinations(tup,2)))
    if n==3:
        return ds in ((2,2,4),(2,3,3))
    if n==4 and ds==(2,2,2,2,2,2):
        xor=0
        for v in tup:xor^=v
        return xor!=0
    if n==4 and ds==(1,1,2,3,3,4):
        ed=[(a,b) for a,b in itertools.combinations(tup,2) if (a^b).bit_count()==1]
        return len(ed)==2 and len(set(ed[0]+ed[1]))==4
    return False

geometric={sum(1<<v for v in tup) for k in (3,4)
           for tup in itertools.combinations(V,k) if geometric_test(tup)}
assert geometric==union, (len(geometric),len(union))
assert len(union)==256

slow_triples={s for s in union if s.bit_count()==3 and time_by_rounds([v for v in V if s>>v&1])==5}
slow_extensions=[]
for s in slow_triples:
    opts=[s|(1<<v) for v in V if not(s>>v&1) and time_by_rounds([u for u in V if (s|(1<<v))>>u&1])==5]
    assert len(opts)==1
    slow_extensions.extend(opts)
assert len(slow_extensions)==96 and len(set(slow_extensions))==96
print('slow extensions',len(slow_extensions),'unique')
print('PASS')
