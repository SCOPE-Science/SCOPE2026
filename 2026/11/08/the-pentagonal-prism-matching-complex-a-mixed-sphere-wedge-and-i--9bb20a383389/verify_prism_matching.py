#!/usr/bin/env python3
"""Exact integral discrete-Morse and symmetry checks for the pentagonal-prism matching complex.
Run with Python 3.9+; no external dependencies. All masks refer to the edge order printed below.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 5
E = [tuple(sorted((5*a+i,5*a+(i+1)%N))) for a in range(2) for i in range(N)]
E += [(i,5+i) for i in range(N)]
edge_ends = [(1<<a)|(1<<b) for a,b in E]

def dim(mask):
    return mask.bit_count()-1

def bdry(mask):
    i_list = [i for i in range(len(E)) if mask>>i&1]
    return {mask^(1<<i): (-1 if j%2 else 1) for j,i in enumerate(i_list)}

# Independent face enumerations: incremental endpoint DP and entire power-set scan.
F={0}; occ={0:0}
for i,V in enumerate(edge_ends):
    for mask in sorted(F):
        if occ[mask]&V == 0:
            new=mask|(1<<i)
            F.add(new)
            occ[new]=occ[mask]|V

F2=set()
for mask in range(1<<len(E)):
    seen=0
    for i,V in enumerate(edge_ends):
        if mask>>i&1:
            if seen&V:break
            seen|=V
    else:F2.add(mask)
assert F==F2
assert len(F)==342 and len(E)==15
assert [sum(dim(mask)==d for mask in F) for d in range(5)]==[15,75,145,95,11]

# The matching is formed by toggling the least available edge (respectively greatest),
# while keeping the empty face out of the ordinary face poset.
def matching(order):
    unmatched=set(F)-{0}
    pairs=[]
    for i in order:
        for low in sorted(unmatched):
            if low>>i&1:continue
            up=low|(1<<i)
            if up in unmatched:
                unmatched.remove(low)
                unmatched.remove(up)
                pairs.append((low,up))
    assert len(pairs)==168 and len(unmatched)==5
    assert Counter(dim(mask) for mask in unmatched)=={0:1,2:2,3:2}
    assert len({x for pair in pairs for x in pair})==336
    return pairs,unmatched

# Every codimension-one edge of the Hasse diagram is directed lower -> upper,
# with matched edges reversed; Kahn's algorithm verifies *all* directed arrows.
def check_acyclic(pairs):
    reversed_edges={(low,up) for low,up in pairs}
    verts=F-{0}
    indeg={mask:0 for mask in verts}
    links=defaultdict(list)
    total=0
    for up in verts:
        if dim(up)==0:continue
        for low in bdry(up):
            if (low,up) in reversed_edges:source,target=up,low
            else:source,target=low,up
            links[source].append(target)
            indeg[target]+=1
            total+=1
    assert total==1020
    Q=deque(x for x,n in indeg.items() if n==0)
    processed=0
    while Q:
        x=Q.popleft();processed+=1
        for y in links[x]:
            indeg[y]-=1
            if indeg[y]==0:Q.append(y)
    assert processed==len(verts)
    return total

p1,c1=matching(range(len(E)))
p2,c2=matching(reversed(range(len(E))))
check_acyclic(p1)
check_acyclic(p2)
assert sorted(c1)==[1,660,8258,11264,12816]

# Integer chains are dicts simplex-mask -> coefficient.
def clean(c):return {s:a for s,a in c.items() if a}

def plus(a,b):
    out=defaultdict(int,a)
    for s,v in b.items():out[s]+=v
    return clean(out)

def boundary_chain(c):
    out=defaultdict(int)
    for s,coeff in c.items():
        for t,epsilon in bdry(s).items():out[t]+=coeff*epsilon
    return clean(out)

# Two Morse boundary methods: first eliminate lower-matched faces algebraically.
def lower_reduce(c,pairs):
    match=dict(pairs)
    out=defaultdict(int,c)
    for _ in range(30000):
        lowers=[s for s,v in out.items() if v and s in match]
        if not lowers:return clean(out)
        s=lowers[0];v=out[s]
        t=match[s]
        epsilon=bdry(t)[s]
        for u,b in bdry(t).items():out[u]-=(v//epsilon)*b
    raise AssertionError('gradient reduction did not terminate')

for pairs,crits in [(p1,c1),(p2,c2)]:
    two=sorted(s for s in crits if dim(s)==2)
    three=sorted(s for s in crits if dim(s)==3)
    for s in three:
        red=lower_reduce(bdry(s),pairs)
        assert all(red.get(c,0)==0 for c in two)
        assert not red

# Forman chain flow Phi = 1 + dV + Vd, with V(low)=-epsilon^{-1} high.
# The stabilized critical coefficient maps are the integral Morse projection.
def vector_field(c,pairs):
    match=dict(pairs)
    out=defaultdict(int)
    for low,a in c.items():
        if low in match:
            up=match[low]
            eps=bdry(up)[low]
            out[up]-=a//eps
    return clean(out)

def one_flow(c,pairs):
    return plus(plus(c,boundary_chain(vector_field(c,pairs))),vector_field(boundary_chain(c),pairs))

def stabilize(c,pairs):
    for _ in range(200):
        nxt=one_flow(c,pairs)
        if nxt==c:return c
        c=nxt
    raise AssertionError('Morse flow failed to stabilize')

for pairs,crits in [(p1,c1),(p2,c2)]:
    for d in (2,3):
        for s in sorted(x for x in crits if dim(x)==d):
            z=stabilize({s:1},pairs)
            assert boundary_chain(z)=={}
            assert {x:a for x,a in z.items() if x in crits}=={s:1}

# An independent simplicial boundary computation over F_2.
def binary_rank(vectors):
    pivots={}
    for x in vectors:
        while x:
            i=x.bit_length()-1
            if i not in pivots:
                pivots[i]=x
                break
            x^=pivots[i]
    return len(pivots)

ranks=[]
for d in (1,2,3,4):
    lower=sorted(s for s in F if dim(s)==d-1)
    pos={s:i for i,s in enumerate(lower)}
    upper=sorted(s for s in F if dim(s)==d)
    col=[sum(1<<pos[t] for t in bdry(s)) for s in upper]
    ranks.append(binary_rank(col))
assert ranks==[14,61,82,11]

# Signed edge permutation action and integral Morse chain representation.
edge_ids={e:i for i,e in enumerate(E)}
def act(chain,perm):
    edge_perm=[edge_ids[tuple(sorted((perm[a],perm[b])))] for a,b in E]
    out=defaultdict(int)
    for face,coeff in chain.items():
        p=[edge_perm[i] for i in range(len(E)) if face>>i&1]
        inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        transformed=sum(1<<i for i in p)
        out[transformed]+=(-1 if inversions%2 else 1)*coeff
    return clean(out)

def representation(degree,perm,pairs,critical):
    basis=sorted(s for s in critical if dim(s)==degree)
    rows=[]
    for s in basis:
        z=stabilize({s:1},pairs)
        image=stabilize(act(z,perm),pairs)
        assert boundary_chain(image)=={}
        rows.append([image.get(c,0) for c in basis])
    return [list(x) for x in zip(*rows)]

rot=[(v+1)%5 if v<5 else 5+(v-5+1)%5 for v in range(10)]
ref=[(-v)%5 if v<5 else 5+(-(v-5))%5 for v in range(10)]
swap=[(v+5)%10 for v in range(10)]
compose=lambda a,b: [a[b[i]] for i in range(10)]
EYE=[[1,0],[0,1]]
prod=lambda a,b:[[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
matrices={}
for d in (2,3):
    A=representation(d,rot,p1,c1)
    B=representation(d,ref,p1,c1)
    C=representation(d,swap,p1,c1)
    assert A==EYE
    assert prod(B,B)==EYE and prod(C,C)==EYE and prod(B,C)==prod(C,B)
    matrices[d]=(A,B,C)
assert matrices[2][1]==[[1,1],[0,-1]] and matrices[2][2]==[[-1,-1],[0,1]]
assert matrices[3][1]==[[1,-1],[0,-1]] and matrices[3][2]==[[1,-1],[0,-1]]

# Independently recompute each representation with the reverse-order Morse matching:
# traces are basis-independent and must agree with the first chain model.
for d in (2,3):
    for perm,expected in zip((rot,ref,swap),matrices[d]):
        other=representation(d,perm,p2,c2)
        assert sum(other[i][i] for i in range(2))==sum(expected[i][i] for i in range(2))

# Exact signed simplicial Lefschetz trace validates the difference of degree-2/3 traces.
def reduced_lefschetz(perm):
    value=-1
    for face in F-{0}:
        value+=(-1)**dim(face)*act({face:1},perm).get(face,0)
    return value
for perm in (rot,ref,swap,compose(ref,swap)):
    predicted=sum((-1)**d*sum(representation(d,perm,p1,c1)[i][i] for i in range(2)) for d in (2,3))
    assert reduced_lefschetz(perm)==predicted

# Compare ordinary and perfect matching subcomplexes, counting their relative cells.
P=[s for s in F if dim(s)==4]
PF={s for p in P for s in F if s&~p==0}
assert len(P)==11 and len(PF)==242
assert Counter(dim(s) for s in F-PF)=={1:10,2:50,3:40}

print('PENTAGONAL_PRISM_ORDINARY_MATCHING_VERIFIED')
print('edges=15 ordinary_faces=341 f_vector=(15,75,145,95,11)')
print('complete_Hasse_incidences=1020 forward_Morse_pairs=168 reverse_Morse_pairs=168')
print('forward_critical=(1,0,2,2,0) in degrees (0,1,2,3,4); Morse_d3_zero=True')
print('integral_homotopy=2*S^2 wedge 2*S^3')
print('F2_simplicial_boundary_ranks=(14,61,82,11)')
print('r_rotation_on_H2_H3=identity; H2=reflection_sign + layer_sign; H3=trivial + product_sign')
print('perfect_matching_facets=11 perfect_subcomplex_faces=241 nonextendible_relative_cells=100')
