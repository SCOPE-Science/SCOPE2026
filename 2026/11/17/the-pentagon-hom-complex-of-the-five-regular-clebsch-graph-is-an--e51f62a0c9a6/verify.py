"""Reproducible finite checks for Hom(C5, five-regular folded five-cube).
Only standard Python modules; assertions are active.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations, product

V = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
index = {x: i for i, x in enumerate(V)}
N = {x: {y for y in V if (x ^ y).bit_count() == 4} for x in V}
assert len(V) == 16 and all(len(N[x]) == 5 for x in V)
assert sum(len(N[x]) for x in V)//2 == 40
assert all(not (N[x] & N[y]) for x in V for y in N[x])
assert all(len(N[x]&N[y]) == 2 for x in V for y in V if x!=y and y not in N[x])

def is_hom(f):
    return all(f[(i+1)%5] in N[f[i]] for i in range(5))

def all_walks():
    for x0 in V:
        for x1 in N[x0]:
            for x2 in N[x1]:
                for x3 in N[x2]:
                    for x4 in N[x3] & N[x0]:
                        yield (x0,x1,x2,x3,x4)

walks = set(all_walks())
assert len(walks) == 1920
# Second description: five distinct Cayley generators in an arbitrary order.
gens=tuple(sum(1<<j for j in range(5) if j!=i) for i in range(5))
from_perm=set()
for x in V:
    for p in permutations(gens):
        path=[x]
        for g in p[:4]: path.append(path[-1]^g)
        assert path[-1]^p[4]==x
        from_perm.add(tuple(path))
assert from_perm == walks

def bitset(f):
    return tuple(1 << index[x] for x in f)

cells=set(bitset(w) for w in walks)
frontier=list(cells)
allbits=(1<<16)-1
nbits={x: sum(1<<index[y] for y in N[x]) for x in V}
cache={0:allbits}
def common(s):
    if s not in cache:
        b=s&-s
        cache[s]=common(s^b)&nbits[V[b.bit_length()-1]]
    return cache[s]
while frontier:
    future=[]
    for c in frontier:
        for i in range(5):
            options=common(c[(i-1)%5]|c[(i+1)%5]) & ~c[i]
            while options:
                b=options&-options
                options-=b
                d=c[:i]+(c[i]|b,)+c[i+1:]
                if d not in cells:
                    cells.add(d);future.append(d)
    frontier=future

def dim(c):
    return sum(s.bit_count()-1 for s in c)

def boundary(c):
    for i,s in enumerate(c):
        if s.bit_count()==1: continue
        x=s
        while x:
            b=x&-x
            x-=b
            yield c[:i]+(s^b,)+c[i+1:]

by_dim={i:{c for c in cells if dim(c)==i} for i in range(3)}
assert sum(map(len,by_dim.values()))==len(cells)==9120
assert tuple(len(by_dim[i]) for i in range(3))==(1920,4800,2400)
assert all(dim(c)<=2 for c in cells)
assert all(tuple(s.bit_count() for s in c).count(2)==2 for c in by_dim[2])

# Verify square attachment and local manifold conditions.
edge_squares=defaultdict(set)
vertex_edges=defaultdict(set)
vertex_squares=defaultdict(set)
for e in by_dim[1]:
    f=list(boundary(e))
    assert len(f)==2 and all(x in by_dim[0] for x in f)
    for v in f: vertex_edges[v].add(e)
for q in by_dim[2]:
    e=list(boundary(q))
    assert len(e)==4 and len(set(e))==4
    for x in e:
        assert x in by_dim[1]
        edge_squares[x].add(q)
    corners=set()
    for x in e:corners.update(boundary(x))
    assert len(corners)==4
    for v in corners: vertex_squares[v].add(q)
assert all(len(edge_squares[e])==2 for e in by_dim[1])
assert all(len(vertex_edges[v])==5 and len(vertex_squares[v])==5 for v in by_dim[0])
for v in by_dim[0]:
    link=defaultdict(set)
    for q in vertex_squares[v]:
        incident=[e for e in boundary(q) if v in set(boundary(e))]
        assert len(incident)==2
        a,b=incident
        link[a].add(b);link[b].add(a)
    assert len(link)==5 and all(len(neighbors)==2 for neighbors in link.values())
    seen={next(iter(link))}; queue=list(seen)
    while queue:
        for w in link[queue.pop()]:
            if w not in seen:seen.add(w);queue.append(w)
    assert len(seen)==5  # every vertex link is a 5-cycle

# 1-skeleton connectivity, independent union-find.
parent={v:v for v in by_dim[0]}
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x
for e in by_dim[1]:
    a,b=list(boundary(e));a=find(a);b=find(b)
    if a!=b:parent[a]=b
assert len({find(v) for v in by_dim[0]})==1

# Canonical cellular square-to-edge incidences, then orientation propagation.
def oriented_square_boundary(q):
    i,j=(i for i,s in enumerate(q) if s.bit_count()==2)
    assert i<j
    li=q[i]&-q[i];hi=q[i]^li
    lj=q[j]&-q[j];hj=q[j]^lj
    return {
        q[:i]+(hi,)+q[i+1:]:1,
        q[:i]+(li,)+q[i+1:]:-1,
        q[:j]+(hj,)+q[j+1:]:-1,
        q[:j]+(lj,)+q[j+1:]:1,
    }
orient={q:oriented_square_boundary(q) for q in by_dim[2]}
incidence=defaultdict(list)
for q,row in orient.items():
    for edge,sgn in row.items():incidence[edge].append((q,sgn))
assert all(len(incidence[e])==2 for e in by_dim[1])
fundamental={}
for start in by_dim[2]:
    if start in fundamental:continue
    fundamental[start]=1
    Q=deque([start])
    while Q:
        q=Q.popleft()
        for e,a in orient[q].items():
            for other,b in incidence[e]:
                if other==q:continue
                required=-fundamental[q]*a*b
                if other in fundamental:
                    assert fundamental[other]==required, 'nonorientable'
                else:
                    fundamental[other]=required
                    Q.append(other)
assert len(fundamental)==2400
assert all(sum(fundamental[q]*a for q,a in incidence[e])==0 for e in by_dim[1])

# A connected closed orientable surface of Euler characteristic -480 has genus 241.
chi=sum((-1)**i*len(by_dim[i]) for i in range(3))
assert chi==-480
assert (2-chi)//2==241
# Natural translation and coordinate-permutation action on the integral orientation line.
# A connected orientable surface has H_2=Z, so comparing one oriented square
# determines the scalar on its entire fundamental class.
base=next(iter(fundamental))
def target_map(t,p,x):
    y=t
    for i in range(5):
        if x&(1<<i):y^=1<<p[i]
    return y
def target_sign_on_top(t,p):
    mapped=[];local=1
    for s in base:
        old=[V[k] for k in range(16) if s>>k&1]
        new=[target_map(t,p,x) for x in old]
        if len(new)==2 and index[new[0]]>index[new[1]]:local=-local
        mapped.append(sum(1<<index[y] for y in new))
    mapped=tuple(mapped)
    assert mapped in fundamental
    return fundamental[base]*local*fundamental[mapped]
permutations_checked=0
for p in permutations(range(5)):
    sign=(-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
    for t in V:
        assert target_sign_on_top(t,p)==sign
        permutations_checked+=1
assert permutations_checked==1920
print('graph vertices=16 edges=40, strongly_regular=(16,5,0,2)')
print('hom_vertices=1920, equivalence_with_permutation_walks=PASS')
print('cell_f_vector=(1920,4800,2400), no_higher_cells=PASS')
print('edge_incidence_two=PASS, vertex_link_C5=PASS, connected=PASS')
print('orientable=PASS, signed_fundamental_cycle_squares=2400')
print('Euler=-480, orientable_genus=241')
print('target_affine_symmetries=1920, top_orientation_character=sgn(S5)')
print('H0=Z, H1=Z^482, H2=Z, other integral homology zero')
