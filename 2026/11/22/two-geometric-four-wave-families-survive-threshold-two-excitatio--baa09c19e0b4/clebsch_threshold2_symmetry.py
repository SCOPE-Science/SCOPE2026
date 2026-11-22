"""Exact 1920-element Clebsch automorphism action on threshold-two four-cycles."""
from itertools import permutations
from collections import Counter
S=(1,2,4,8,15)
cycles={}
with open('clebsch_threshold2_a.log',encoding='utf8') as fd:
    for line in fd:
        a=line.split()
        if a and a[0]=='CYCLE': cycles[int(a[1])]=int(a[3])
assert len(cycles)==90
adj=[[v^s for s in S] for v in range(16)]
def next_state(c):
    E=c&65535;R=c>>16
    A=sum(1<<v for v in range(16) if sum(bool(E&(1<<u)) for u in adj[v])>=2)
    return ((A&~(E|R)&65535)|(E<<16))
def temporal(c):
    return [c,next_state(c),next_state(next_state(c)),next_state(next_state(next_state(c)))]
def canon(c):return min(temporal(c))
perms=[]
for p in permutations(S):
    L=[0]*16
    for v in range(1,16):
        bit=v&-v;k=bit.bit_length()-1
        L[v]=L[v^bit]^p[k]
    for t in range(16):
        mv=tuple(L[v]^t for v in range(16))
        assert all(set(mv[u] for u in adj[v])==set(mv[v]^s for s in S) for v in range(16))
        perms.append(mv)
assert len(set(perms))==1920

def transformmask(mask,perm):
    out=0
    while mask:
        bit=mask&-mask; mask-=bit
        out|=1<<perm[bit.bit_length()-1]
    return out

def tform(c,perm):
    E=c&65535;R=c>>16
    return canon(transformmask(E,perm)|(transformmask(R,perm)<<16))
classes=[]
seen=set()
for c in cycles:
    if c in seen:continue
    orb={tform(c,p) for p in perms}
    assert orb.issubset(cycles)
    seen.update(orb)
    classes.append((len(orb),cycles[c],c))
assert len(seen)==90
assert sorted(classes)==[(30,676,3932355),(60,644,3935235)]
print('AUTOMORPHISMS',len(perms))
print('SPATIAL_CLASSES',classes)

def flats(c):
    sets=[set(u for u in range(16) if (x&65535)&(1<<u)) for x in temporal(c)]
    assert all(len(x)==4 for x in sets)
    assert len(set.union(*sets))==16
    assert len(set(map(frozenset,sets)))==4
    assert all(__import__('functools').reduce(int.__xor__,v,0)==0 for v in sets)
    def direction(x):
        a=min(x);return frozenset(v^a for v in x)
    ds=[direction(x) for x in sets]
    return len(set(ds)), len(set(ds[::2])), len(set(ds[1::2]))
geo=Counter((cycles[c],flats(c)) for c in cycles)
print('PHASE_GEOMETRY',geo)
assert geo==Counter({(676,(1,1,1)):30,(644,(2,1,1)):60})
# Check sharp first-entry witness from ternary count encoding with explicit 8-step orbit
mask=54784
path=[mask]
for i in range(11):path.append(next_state(path[-1]))
print('WITNESS_BITS',path)
assert path[7]==0 and path[6]!=0
