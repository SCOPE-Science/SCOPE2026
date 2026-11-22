"""Exact finite census for spanning-tree edge-query shattering on KG(5,2).
Each possible edge-support mask is tested by forest and connectivity predicates.
"""
from itertools import combinations,permutations
from collections import Counter
V=list(combinations(range(5),2))
E=[(i,j) for i in range(10) for j in range(i+1,10) if set(V[i]).isdisjoint(V[j])]
assert len(E)==15

def graph_parts(mask):
    p=list(range(10));sz=[1]*10;cyclic=False
    def root(i):
        while p[i]!=i:
            i=p[i]
        return i
    for j,(u,v) in enumerate(E):
        if not (mask>>j)&1:continue
        a,b=root(u),root(v)
        if a==b:cyclic=True
        else:p[a]=b
    return len({root(i) for i in range(10)}),cyclic

ok=[]
for s in range(1<<15):
    nc,bad=graph_parts(s)
    if not bad and graph_parts(((1<<15)-1)^s)[0]==1:ok.append(s)
O=set(ok)
poly=Counter(s.bit_count() for s in ok)
assert [poly[i] for i in range(7)]==[1,15,105,445,1230,2160,1930] and sum(poly.values())==5886
facets={s for s in O if all(s|(1<<i) not in O for i in range(15) if not s>>i&1)}
assert len(facets)==1930 and all(s.bit_count()==6 for s in facets)
assert sum(graph_parts(s)[1] for s in range(1<<15) if s.bit_count()==6 and graph_parts(((1<<15)-1)^s)[0]==1)==70
vnum={v:i for i,v in enumerate(V)}; enum={e:i for i,e in enumerate(E)}
perms=[]
for a in permutations(range(5)):
    induced=[vnum[tuple(sorted(a[i] for i in v))] for v in V]
    perms.append([enum[tuple(sorted((induced[u],induced[v])))] for u,v in E])

def act(s,a):
    r=0
    for i in range(15):
        if s>>i&1:r|=1<<a[i]
    return r
rem=set(facets);orbits=[]
while rem:
    s=min(rem);orb={act(s,a) for a in perms}; assert orb<=rem
    orbits.append((s,len(orb)));rem-=orb
assert sorted(Counter(n for _,n in orbits).items())==[(30,1),(40,1),(60,3),(120,14)]
assert set(orbits)=={
    (4501,30),(235,40),(222,60),(245,60),(669,60),
    (219,120),(238,120),(246,120),(667,120),(683,120),
    (685,120),(686,120),(691,120),(693,120),(694,120),
    (746,120),(754,120),(4330,120),(4491,120)}
# Exact cycle-type classification of the coforest bases excluded by cycles.
cycles={5:[],6:[]}
for s in range(1<<15):
    k=s.bit_count()
    if k not in (5,6):continue
    deg=[0]*10
    for i,(u,v) in enumerate(E):
        if s>>i&1:deg[u]+=1;deg[v]+=1
    if sum(x>0 for x in deg)==k and all(x in (0,2) for x in deg):
        # With Petersen girth five, a 5- or 6-edge 2-regular subgraph is one cycle.
        cycles[k].append(s)
assert (len(cycles[5]),len(cycles[6]))==(12,10)
cyclic_cotrees={s for s in range(1<<15) if s.bit_count()==6
                 and graph_parts(((1<<15)-1)^s)[0]==1 and graph_parts(s)[1]}
from_fives=set()
for c in cycles[5]:
    choices={c|(1<<j) for j in range(15) if not c>>j&1
             and graph_parts(((1<<15)-1)^(c|(1<<j)))[0]==1}
    assert len(choices)==5
    from_fives.update(choices)
assert len(from_fives)==60
assert len(cyclic_cotrees)==70
assert set(cycles[6])<=cyclic_cotrees
assert cyclic_cotrees==from_fives|set(cycles[6])

# Explicit basis-exchange failure.
a,b,e=238,8283,7
assert a in facets and b in facets and (a>>e&1) and not(b>>e&1)
assert all((a^(1<<e))|(1<<j) not in facets for j in range(15) if b>>j&1 and not(a>>j&1))
print('PETERSEN_DIRECT_PASS faces=5886 facets=1930 facet_orbits=19 bad_cotrees=70')
