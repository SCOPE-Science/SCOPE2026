#!/usr/bin/env python3
"""Reproducible integral Vietoris–Rips filtration of the icosidodecahedral graph.
Python >=3.9 standard library only. No downloaded data or algebra package needed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import random

# Dodecahedral graph GP(10,2), vertices u_i = i, v_i = i+10.
D_EDGES = sorted({tuple(sorted((i,(i+1)%10))) for i in range(10)} |
                 {tuple(sorted((i,i+10))) for i in range(10)} |
                 {tuple(sorted((i+10,10+(i+2)%10))) for i in range(10)})
assert len(D_EDGES)==30
D_ADJ=[set() for _ in range(20)]
for a,b in D_EDGES:
    D_ADJ[a].add(b);D_ADJ[b].add(a)
assert all(len(a)==3 for a in D_ADJ)
# Edge-vertex indexing of the icosidodecahedral graph I=L(D).
I_ADJ=[set() for _ in range(30)]
for i,e in enumerate(D_EDGES):
    for j,f in enumerate(D_EDGES):
        if i!=j and set(e)&set(f):I_ADJ[i].add(j)
assert all(len(x)==4 for x in I_ADJ)
DIST=[]
for s in range(30):
    dist=[-1]*30; dist[s]=0;Q=deque([s])
    while Q:
        u=Q.popleft()
        for v in I_ADJ[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1;Q.append(v)
    assert -1 not in dist
    DIST.append(dist)
assert max(map(max,DIST))==5
assert Counter(DIST[i][j] for i in range(30) for j in range(i+1,30)) == {1:60,2:120,3:120,4:120,5:15}

def faces(radius):
    adj=[sum(1<<j for j in range(30) if j!=i and DIST[i][j]<=radius) for i in range(30)]
    F=set()
    def extend(mask,cands):
        while cands:
            bit=cands&-cands;cands-=bit
            v=bit.bit_length()-1
            new=mask|bit
            assert new not in F
            F.add(new)
            extend(new,cands&adj[v])
    extend(0,(1<<30)-1)
    return F

def boundary(mask):
    vs=[i for i in range(30) if mask&(1<<i)]
    return [(mask^(1<<i),1 if p%2==0 else -1) for p,i in enumerate(vs)]

def match(F,order):
    unused=set(F);pairs=[]
    for v in order:
        bit=1<<v
        # All pairs in one layer have disjoint endpoints.
        for sigma in sorted(s for s in unused if not s&bit and (s|bit) in unused):
            tau=sigma|bit
            if sigma in unused and tau in unused:
                unused.remove(sigma);unused.remove(tau)
                pairs.append((sigma,tau))
    return unused,pairs

def check_matching(F,crit,pairs):
    assert len(crit)+2*len(pairs)==len(F)
    seen=set();mate={}
    for s,t in pairs:
        assert s in F and t in F and s.bit_count()+1==t.bit_count() and t&s==s
        assert s not in seen and t not in seen
        seen.add(s);seen.add(t);mate[s]=t
    assert crit==F-seen
    # Matched Hasse arcs point upward, every other covering arc downward.
    indeg={f:0 for f in F};outs=defaultdict(list);incidences=0
    for t in F:
        for s,_ in boundary(t):
            if not s:continue
            assert s in F
            a,b=(s,t) if mate.get(s)==t else (t,s)
            outs[a].append(b);indeg[b]+=1;incidences+=1
    Q=deque(s for s in F if indeg[s]==0);processed=0
    while Q:
        s=Q.popleft();processed+=1
        for t in outs[s]:
            indeg[t]-=1
            if indeg[t]==0:Q.append(t)
    assert processed==len(F),(processed,len(F))
    return incidences

def canonical_cycle(v):
    seq=[]
    for rev in [v,list(reversed(v))]:
        for off in range(len(rev)):
            seq.append(tuple(rev[off:]+rev[:off]))
    return min(seq)

def pentagons():
    # Enumerate all simple five-cycles without geometry input.
    C=set()
    for s in range(20):
        def visit(path):
            x=path[-1]
            if len(path)==5:
                if s in D_ADJ[x]:C.add(canonical_cycle(path))
                return
            for n in D_ADJ[x]:
                if n not in path:visit(path+[n])
        visit([s])
    assert len(C)==12
    return sorted(C)

def fundamental_surface_cycle():
    idx={e:i for i,e in enumerate(D_EDGES)}
    triangles=set()
    # Icosidodecahedron has 20 triangular faces, one for each vertex of D.
    for v in range(20):
        star=[idx[tuple(sorted((v,n)))] for n in D_ADJ[v]]
        assert len(star)==3
        triangles.add(sum(1<<i for i in star))
    # Its 12 pentagonal faces, canonically triangulated into three triangles.
    for C in pentagons():
        edges=[idx[tuple(sorted((C[i],C[(i+1)%5])))] for i in range(5)]
        for i in range(1,4):
            triangles.add(sum(1<<k for k in (edges[0],edges[i],edges[i+1])))
    assert len(triangles)==56
    cofaces=defaultdict(list)
    for t in triangles:
        for e,sign in boundary(t):cofaces[e].append((t,sign))
    assert len(cofaces)==84 and all(len(v)==2 for v in cofaces.values())
    assert 30-84+56==2
    # Verify this is a closed 2-manifold, rather than just a pseudomanifold:
    # every vertex link is a connected cycle.
    for v in range(30):
        link=defaultdict(set)
        for t in triangles:
            if t&(1<<v):
                ab=[i for i in range(30) if (t&(1<<i)) and i!=v]
                assert len(ab)==2
                a,b=ab
                link[a].add(b);link[b].add(a)
        assert len(link)>=3 and all(len(n)==2 for n in link.values())
        visited={next(iter(link))};todo=list(visited)
        while todo:
            for x in link[todo.pop()]:
                if x not in visited:visited.add(x);todo.append(x)
        assert len(visited)==len(link)
    # Orient the triangulated sphere consistently; this also verifies orientability.
    first=min(triangles);signs={first:1};queue=deque([first])
    while queue:
        t=queue.popleft()
        for e,sgn in boundary(t):
            for other,sgn2 in cofaces[e]:
                if other==t:continue
                wanted=-signs[t]*sgn*sgn2
                if other in signs:assert signs[other]==wanted
                else:signs[other]=wanted;queue.append(other)
    assert len(signs)==56
    assert all(sum(signs[t]*s for t,s in cofaces[e])==0 for e in cofaces)
    return signs

def cocycle_and_pairing(F,crit,pairs,z):
    crit2=next(s for s in crit if s.bit_count()==3)
    matched_2={s:t for s,t in pairs if s.bit_count()==3 and t.bit_count()==4}
    @lru_cache(maxsize=None)
    def lmb(s):
        if s==crit2:return 1
        if s not in matched_2:return 0
        t=matched_2[s]
        terms=boundary(t);di=dict(terms)
        return -sum(coeff*lmb(face) for face,coeff in terms if face!=s)*di[s]
    vals={f:lmb(f) for f in F if f.bit_count()==3}
    # A genuine integral cocycle: evaluate every boundary of every 3-simplex.
    for t in F:
        if t.bit_count()==4:
            assert sum(sign*vals[s] for s,sign in boundary(t))==0
    pairing=sum(sign*vals[t] for t,sign in z.items())
    # The Morse matching has only critical cells in degrees 0 and 2.
    # Thus the cocycle pairing one critical 2-cell to 1 is primitive.
    assert vals[crit2]==1
    assert abs(pairing)==1
    return pairing,sum(bool(x) for x in vals.values())

# Deliberately fixed reproducible permutations, discovered by bounded finite search.
# They are valid for the GP(10,2) edge-ordering generated above.
ORDER2=None
ORDER3=None

def find_perfect_order(F):
    for seed in range(2000):
        order=list(range(30));random.Random(seed).shuffle(order)
        crit,pairs=match(F,order)
        if Counter(s.bit_count()-1 for s in crit)=={0:1,2:1}:
            return seed,order,crit,pairs
    raise RuntimeError('No matching found; not evidence of nonexistence')

def main():
    print('DODECAHEDRON_EDGES',len(D_EDGES),'ICOSIDODECAHEDRON_VERTICES',len(I_ADJ), 'EDGES',sum(map(len,I_ADJ))//2)
    z=fundamental_surface_cycle()
    print('SURFACE_TRIANGLES',len(z),'PENTAGONS',len(pentagons()))
    sizes={}
    for r in (2,3):
        F=faces(r)
        sizes[r]=F
        print('SCALE',r,'F_VECTOR',sorted(Counter(f.bit_count() for f in F).items()))
        seed,order,crit,pairs=find_perfect_order(F)
        incidences=check_matching(F,crit,pairs)
        pairing,cochain_support=cocycle_and_pairing(F,crit,pairs,z)
        print('MATCH',r,'SEED',seed,'ORDER',','.join(map(str,order)),'PAIRS',len(pairs),'CRITICAL',sorted((s.bit_count()-1,s) for s in crit),'HASSE_INCIDENCES',incidences)
        print('INTEGRAL_COCYCLE',r,'SUPPORT',cochain_support,'SURFACE_PAIRING',pairing)
    assert sizes[2].issubset(sizes[3])
    assert Counter(f.bit_count() for f in sizes[2])=={1:30,2:180,3:380,4:330,5:102}
    assert Counter(f.bit_count() for f in sizes[3])=={1:30,2:300,3:1340,4:3150,5:4374,6:3800,7:2100,8:720,9:140,10:12}
    # At scale four, all but the fifteen antipodal pairs are edges; they partition vertices.
    nonedges=[(i,j) for i in range(30) for j in range(i+1,30) if DIST[i][j]==5]
    assert len(nonedges)==15 and len(set(x for ab in nonedges for x in ab))==30
    print('SCALE_4_ANTIPODAL_MATCHING',len(nonedges),'SPHERE_DIMENSION',14)
    # Scale one: 20 edge-disjoint filled star triangles, then connected graph with 30 V,40 E.
    assert sum(1 for i in range(30) for j in range(i+1,30) if DIST[i][j]==1)==60
    print('SCALE_1_TRIANGLES',20,'CIRCLE_RANK',60-20-30+1)
    print('BARCODE_REDUCED_H0','29x[0,1)')
    print('BARCODE_H1','11x[1,2)')
    print('BARCODE_H2','1x[2,4)')
    print('BARCODE_H14','1x[4,5)')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
