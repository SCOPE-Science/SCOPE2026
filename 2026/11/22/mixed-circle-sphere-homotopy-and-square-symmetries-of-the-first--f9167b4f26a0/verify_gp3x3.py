#!/usr/bin/env python3
"""Exact combinatorial and CW-presentation checks for a grid general-position complex."""
from itertools import combinations, product
from collections import Counter, deque

V = list(product(range(3), repeat=2))
n = len(V)
dist = lambda i,j: abs(V[i][0]-V[j][0])+abs(V[i][1]-V[j][1])
faces = []
for mask in range(1,1<<n):
    ids = [i for i in range(n) if mask >> i & 1]
    forbidden = any(dist(a,b)==dist(a,c)+dist(c,b)
                    for x,y,z in combinations(ids,3)
                    for a,b,c in ((x,y,z),(x,z,y),(y,z,x)))
    if not forbidden: faces.append(mask)
face_by_dim = {d:sorted(m for m in faces if m.bit_count()==d+1) for d in range(4)}
assert [len(face_by_dim[d]) for d in range(4)] == [9,36,16,1]
assert face_by_dim[3] == [sum(1<<i for i in (1,3,5,7))]
triples = sorted(tuple(i for i in range(n) if m>>i&1) for m in face_by_dim[2])
assert len(triples)==16
edges = sorted(combinations(range(n),2))
grid_edges = [e for e in edges if dist(*e)==1]
non_grid_edges = [e for e in edges if dist(*e)>1]
assert len(grid_edges)==12 and len(non_grid_edges)==24
assert all(dist(a,b)>1 and dist(a,c)>1 and dist(b,c)>1 for a,b,c in triples)
# The only 3-simplex can be collapsed across its free triangle (1,3,5).
free_tri = (1,3,5)
assert free_tri in triples
remaining_triangles = [t for t in triples if t!=free_tri]
# Choose a reproducible spanning tree in the non-grid graph.
neighbors = {i:[] for i in range(n)}
for a,b in non_grid_edges:
    neighbors[a].append(b);neighbors[b].append(a)
parent = {0:None}; q=deque([0]); tree=set()
while q:
    a=q.popleft()
    for b in sorted(neighbors[a]):
        if b not in parent:
            parent[b]=a;q.append(b);tree.add(tuple(sorted((a,b))))
assert len(parent)==9 and len(tree)==8
remaining_edges = [e for e in non_grid_edges if e not in tree]
generator = {e:i+1 for i,e in enumerate(remaining_edges)}
assert len(generator)==16

def reduce_word(word):
    result=[]
    for i in word:
        if result and result[-1] == -i: result.pop()
        else:result.append(i)
    return result

def edge_word(a,b):
    e=tuple(sorted((a,b)))
    if e in tree: return 0
    return generator[e] if a<b else -generator[e]

relators = [reduce_word([x for x in (edge_word(a,b),edge_word(b,c),edge_word(c,a)) if x])
            for a,b,c in remaining_triangles]
unused=set(generator.values()); cancellations=[]
while True:
    options=[]
    for j,r in enumerate(relators):
        for k,g in enumerate(r):
            if sum(abs(t)==abs(g) for t in r)==1:
                occurrences=sum(sum(abs(t)==abs(g) for t in rr) for rr in relators)
                options.append((len(r),occurrences,j,k,g))
    if not options:break
    _,_,j,k,g=min(options)
    word=relators[j]
    left,right=word[:k],word[k+1:]
    solution=reduce_word([-x for x in reversed(left)]+[-x for x in reversed(right)])
    replacement=solution if g>0 else [-x for x in reversed(solution)]
    G=abs(g)
    def substitute(w):
        result=[]
        for t in w:
            if abs(t)==G:
                result.extend(replacement if t>0 else [-x for x in reversed(replacement)])
            else:result.append(t)
        return reduce_word(result)
    relators=[substitute(w) for i,w in enumerate(relators) if i!=j]
    unused.remove(G)
    cancellations.append((G,word,replacement))
assert len(cancellations)==14 and len(unused)==2 and relators==[[]]
assert unused=={6,8}
# Fourteen free generators overall: 12 physical-grid edges plus 2 leftover.
# One zero-attaching 2-cell is left; this certifies the integral CW wedge type.

# An explicit primitive 2-cycle, represented in the original simplicial chains.
z_entries=[((0,2,4),-1),((0,4,6),-1),((0,5,6),1),
 ((1,5,6),-1),((0,2,7),1),((1,3,7),-1),
 ((2,3,7),1),((0,5,7),-1),((1,5,7),1),
 ((1,3,8),1),((2,3,8),-1),((2,4,8),1),
 ((1,6,8),-1),((4,6,8),1)]
z={tuple(t):sign for t,sign in z_entries}
assert len(z)==14 and all(t in remaining_triangles for t in z)
def chain_boundary_2(chain):
    b=Counter()
    for (a,c,d),val in chain.items():
        for edge,sign in (((c,d),1),((a,d),-1),((a,c),1)):
            b[edge]+=val*sign
    return {e:v for e,v in b.items() if v}
assert chain_boundary_2(z)=={}
# The 3-simplex boundary generates the only integral 3-boundaries.
tetra=(1,3,5,7)
b3={tuple(tetra[:i]+tetra[i+1:]):(-1)**i for i in range(4)}
assert chain_boundary_2(b3)=={}
assert any(t not in b3 and abs(v)==1 for t,v in z.items())

def orient_sign(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))

def sym_data(automorphism):
    p=[V.index(automorphism(*xy)) for xy in V]
    Lefschetz=0
    for f in faces:
        ids=[i for i in range(n) if f>>i&1]
        jds=[p[i] for i in ids]
        if set(ids)==set(jds):Lefschetz+=(-1)**(len(ids)-1)*orient_sign(jds)
    transformed=Counter()
    for t,val in z.items():
        y=[p[i] for i in t]
        transformed[tuple(sorted(y))]+=val*orient_sign(y)
    transformed={t:v for t,v in transformed.items() if v}
    orientation_sign=(-1)**int(automorphism(0,0) in ((0,2),(2,0))) # provisional; replaced below
    # identify the sign by comparing the coefficient of a 2-face absent from b3
    probe=next(t for t in z if t not in b3)
    orientation_sign=transformed.get(probe,0)//z[probe]
    assert orientation_sign in (-1,1)
    diff={t:transformed.get(t,0)-orientation_sign*z.get(t,0)
          for t in set(transformed)|set(z)|set(b3)}
    probe_b3=next(iter(b3))
    multiple=diff.get(probe_b3,0)//b3[probe_b3]
    assert all(diff.get(t,0)==multiple*b3.get(t,0) for t in diff)
    # H_0 trace=1, H_1 and H_2 are the only other homology groups.
    h1trace=1+orientation_sign-Lefschetz
    return h1trace,orientation_sign,Lefschetz

actions={
 'identity':lambda x,y:(x,y),
 'quarter_turn':lambda x,y:(y,2-x),
 'half_turn':lambda x,y:(2-x,2-y),
 'three_quarter_turn':lambda x,y:(2-y,x),
 'vertical_reflection':lambda x,y:(x,2-y),
 'horizontal_reflection':lambda x,y:(2-x,y),
 'diagonal_reflection':lambda x,y:(y,x),
 'other_diagonal':lambda x,y:(2-y,2-x),
}
expected={'identity':(14,1),'quarter_turn':(0,1),'half_turn':(-2,1),
          'three_quarter_turn':(0,1),'vertical_reflection':(2,-1),
          'horizontal_reflection':(2,-1),'diagonal_reflection':(0,-1),
          'other_diagonal':(0,-1)}
results={name:sym_data(fn) for name,fn in actions.items()}
assert all(results[name][:2]==expected[name] for name in expected),results
assert sum(t[0] for t in results.values())//8==2
assert sum(t[1] for t in results.values())==0
print('PASS: 9 vertices, 36 edges, 16 triangles, 1 tetrahedron')
print('PASS: 12 grid edges excluded from all triangles; non-grid graph connected')
print('PASS: tetrahedral free-face collapse, 14 CW generator/relator cancellations')
print('PASS: GP(P3 square P3) homotopy wedge of 14 circles and one 2-sphere')
print('PASS: explicit primitive 2-cycle and all 8 dihedral homology characters')
print('PASS: rational quotient ranks H1=2, H2=0')
print('dihedral traces:',results)
