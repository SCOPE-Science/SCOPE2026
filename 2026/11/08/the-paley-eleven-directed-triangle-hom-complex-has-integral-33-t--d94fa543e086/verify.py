#!/usr/bin/env python3
"""Integral cellular certificate for a directed 3-cycle Hom complex.
Only Python standard library; reproduce with `python verify.py`.
"""
from collections import Counter, defaultdict, deque

P=11
RES={pow(i,2,P) for i in range(1,P)}
FULL=(1<<P)-1
assert RES=={1,3,4,5,9}

def bits(mask): return [i for i in range(P) if mask & (1<<i)]
def subsets(mask):
    x=mask
    while x:
        yield x
        x=(x-1)&mask

def arc(x,y): return (y-x)%P in RES

# Independent exhaustive enumeration of the defining products of simplices.
cells=defaultdict(list)
for a in range(1,FULL+1):
    B=FULL
    for x in bits(a):
        B &= sum(1<<y for y in range(P) if arc(x,y))
    for b in subsets(B):
        C=FULL
        for x in bits(b):
            C &= sum(1<<y for y in range(P) if arc(x,y))
        for y in bits(a):
            C &= sum(1<<x for x in range(P) if arc(x,y))
        for c in subsets(C):
            t=(a,b,c)
            d=sum(x.bit_count() for x in t)-3
            assert d<=2
            cells[d].append(t)
for d in cells: cells[d].sort()
assert [len(cells[d]) for d in range(3)]==[165,495,330]
# Second, logically different enumeration: grow all multihomomorphisms
# from the directed 3-cycles by one allowed target vertex at a time.
seed=[]
for a in range(P):
    for b in range(P):
        for c in range(P):
            if arc(a,b) and arc(b,c) and arc(c,a):
                seed.append((1<<a,1<<b,1<<c))
assert len(seed)==165
seen=set(seed)
queue=deque(seed)
while queue:
    t=queue.popleft()
    for coordinate in range(3):
        for v in range(P):
            if t[coordinate]>>v&1:continue
            tt=list(t);tt[coordinate] |= 1<<v
            valid=True
            for j in range(3):
                if not all(arc(x,y) for x in bits(tt[j]) for y in bits(tt[(j+1)%3])):
                    valid=False;break
            if valid:
                new=tuple(tt)
                if new not in seen:seen.add(new);queue.append(new)
assert seen==set(sum((cells[d] for d in range(3)),[]))
assert Counter(tuple(x.bit_count() for x in t) for t in cells[2])==Counter({
    (3,1,1):55,(1,3,1):55,(1,1,3):55,
    (2,2,1):55,(2,1,2):55,(1,2,2):55})
index={d:{t:i for i,t in enumerate(cells[d])} for d in cells}

def boundary(cell):
    for j,mask in enumerate(cell):
        if mask.bit_count()==1:continue
        prefix=sum(cell[k].bit_count()-1 for k in range(j))
        for z,i in enumerate(bits(mask)):
            t=list(cell);t[j] ^= 1<<i
            yield tuple(t), (-1)**(prefix+z)

# Exact d_1 d_2 = 0, including all product-orientation signs.
for f in cells[2]:
    bb=Counter()
    for e,s in boundary(f):
        for v,t in boundary(e):bb[v]+=s*t
    assert all(v==0 for v in bb.values())

# Connectivity of the one-skeleton, without computing a homology matrix.
parent=list(range(len(cells[0])))
def root(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]];x=parent[x]
    return x
for e in cells[1]:
    vertices=[index[0][x] for x,_ in boundary(e)]
    assert len(vertices)==2
    parent[root(vertices[0])]=root(vertices[1])
assert len({root(i) for i in range(165)})==1

# The 495 one-cells are contained in two or three 2-cells; there are
# 330 double-incidence rows and 165 triple-incidence rows.
cofaces=defaultdict(list)
for i,t in enumerate(cells[2]):
    for e,sgn in boundary(t):
        cofaces[e].append((i,sgn))
assert len(cofaces)==495
assert Counter(len(v) for v in cofaces.values())=={2:330,3:165}

# Two-coface rows define a graph on the 330 oriented two-cells.
# A spanning forest supplies 325 integral unit pivots, leaving five
# component parameters. The residual 5x5 presentation has determinant 33
# and cyclic cokernel; this detects torsion rather than a unit minor.
adj=defaultdict(list)
for e,inc in cofaces.items():
    if len(inc)==2:
        (u,su),(v,sv)=inc
        transition=-su*sv
        adj[u].append((v,transition,e))
        adj[v].append((u,transition,e))
component=[-1]*330
orientation=[0]*330
chosen_tree=[]
component_sizes=[]
for start in range(330):
    if component[start]>=0:continue
    ci=len(component_sizes)
    orientation[start]=1;component[start]=ci
    queue=deque([start]);size=0
    while queue:
        u=queue.popleft();size+=1
        for v,transition,e in sorted(adj[u]):
            if component[v]<0:
                component[v]=ci
                orientation[v]=orientation[u]*transition
                chosen_tree.append(e)
                queue.append(v)
    component_sizes.append(size)
assert component_sizes==[66]*5
assert len(chosen_tree)==325 and len(set(chosen_tree))==325

# A triple-incidence row evaluated on a signed constant per component.
def projected_row(e):
    vec=[0]*5
    for u,s in cofaces[e]:vec[component[u]] += s*orientation[u]
    return tuple(vec)
# The five omitted double-incidence rows are dependent over Z.
remaining=[e for e in sorted(cofaces) if len(cofaces[e])==2 and e not in set(chosen_tree)]
assert len(remaining)==5
assert all(projected_row(e)==(0,0,0,0,0) for e in remaining)
# Triple rows reduce to five signed primitive two-coordinate relations.
relations=((1,0,0,0,2),(0,2,1,0,0),(0,0,2,0,1),
           (2,0,0,-1,0),(0,-1,0,2,0))
patterns={tuple(v) for v in relations}|{tuple(-x for x in v) for v in relations}
assert len(patterns)==10
triple=[e for e in sorted(cofaces) if len(cofaces[e])==3]
assert len(triple)==165
assert {projected_row(e) for e in triple}==patterns
chosen_relations=[]
for target in relations:
    chosen_relations.append(next(e for e in triple if projected_row(e)==target))
assert len(set(chosen_relations))==5
# Verify the exact 5-by-5 determinant and a unit 4-by-4 minor.
def det(mat):
    if len(mat)==1:return mat[0][0]
    return sum((-1)**j*mat[0][j]*det([r[:j]+r[j+1:] for r in mat[1:]])
               for j in range(len(mat)))
assert abs(det([list(v) for v in relations]))==33
assert any(abs(det([[relations[r][c] for c in range(5) if c!=col]
                    for r in range(5) if r!=row]))==1
           for row in range(5) for col in range(5))
# Four relations successively give x3=2*x0, x1=4*x0,
# x2=-8*x0, x4=16*x0; the fifth then gives 33*x0=0.
# Thus the five-dimensional presentation is Z/33; four residual
# relations are unit pivots and the fifth has coefficient 33.

# Rational and mod-two rank independently: bit elimination over F_2.
basis={}
for t in cells[2]:
    vector=0
    for e,_ in boundary(t):vector ^= 1<<index[1][e]
    while vector:
        lead=vector.bit_length()-1
        if lead not in basis:
            basis[lead]=vector
            break
        vector ^= basis[lead]
assert len(basis)==330

# Symmetry: 55 affine automorphisms and source coordinate 3-cycle are odd order,
# hence necessarily fix rank-one integral H1. A converse anti-automorphism
# paired with reflection of the source gives an involution.
for a in RES:
    for b in range(P):
        trans=lambda mask: sum(1<<((a*i+b)%P) for i in bits(mask))
        for t in cells[0]+cells[1]+cells[2]:
            assert tuple(trans(x) for x in t) in index[sum(x.bit_count() for x in t)-3]
for t in cells[0]+cells[1]+cells[2]:
    assert (t[1],t[2],t[0]) in index[sum(x.bit_count() for x in t)-3]

def negative(mask):return sum(1<<((-i)%P) for i in bits(mask))
def parity(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1
traces=[]
for d in range(3):
    trace=0
    for t in cells[d]:
        tnew=(negative(t[0]),negative(t[2]),negative(t[1]))
        assert tnew in index[d]
        if tnew!=t:continue
        s=(-1)**((t[1].bit_count()-1)*(t[2].bit_count()-1))
        for m in t:s*=parity([(-i)%P for i in bits(m)])
        trace+=s
    traces.append(trace)
assert traces==[5,-5,-10],traces
L=traces[0]-traces[1]+traces[2]
assert L==0
# H0 trace=1, H2=0; Lefschetz gives H1 trace=1, not -1.
print('PAL11_HOM_INTEGRAL_CERTIFICATE_OK')
print('cell_counts',tuple(len(cells[d]) for d in range(3)))
print('two_cells_triangles_squares',165,165)
print('edge_cofaces',dict(Counter(len(v) for v in cofaces.values())))
print('two_coface_components',component_sizes)
print('integral_presentation',len(chosen_tree),'tree',len(remaining),'redundant_double_rows',len(triple),'triple_rows')
print('relation_rows_masks',chosen_relations)
print('projected_relation_vectors',relations)
print('connectivity',1,'rank_mod2_d2',len(basis),'integral_h1','Z + Z/33')
print('converse_reflection_cellular_traces',traces,'H1_trace',1-L)

def modular_rank(p):
    pivot={}
    for t in cells[2]:
        vec={index[1][e]:s%p for e,s in boundary(t)}
        while vec:
            k=min(vec)
            if k not in pivot:
                inv=pow(vec[k],-1,p)
                pivot[k]={i:(v*inv)%p for i,v in vec.items()}
                break
            scale=vec[k]
            for i,v in pivot[k].items():
                new=(vec.get(i,0)-scale*v)%p
                if new:vec[i]=new
                elif i in vec:del vec[i]
    return len(pivot)
for p,rank in [(2,330),(3,329),(5,330),(11,329),(13,330)]:
    assert modular_rank(p)==rank,(p,modular_rank(p))
print('modular_d2_ranks',[(p,modular_rank(p)) for p in (2,3,5,11,13)])
