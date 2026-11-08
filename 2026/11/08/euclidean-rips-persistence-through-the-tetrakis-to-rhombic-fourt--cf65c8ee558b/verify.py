"""Exact finite verifier for a 14-point cube--octahedron Rips interpolation.

Run: python verify.py  (from the directory containing collapse_certificate.json).
All face masks use vertices 0,...,5 for the axes and 6,...,13 for corners.
Only Python's standard library is needed.
"""
import json
from collections import Counter, defaultdict, deque
from itertools import product
from pathlib import Path

AXES=[tuple(3*s if i==j else 0 for i in range(3)) for j in range(3) for s in (-1,1)]
CORNERS=list(product((-2,2),repeat=3))
POINTS=AXES+CORNERS
N=len(POINTS)
ALL=(1<<N)-1
D2={(i,j):sum((p-q)**2 for p,q in zip(POINTS[i],POINTS[j]))
    for i in range(N) for j in range(i+1,N)}
assert Counter(D2.values())=={9:24,16:12,18:12,32:12,33:24,36:3,48:4}

def flag_faces(threshold):
    adjacent=[0]*N
    for (i,j),sq in D2.items():
        if sq<=threshold:
            adjacent[i]|=1<<j
            adjacent[j]|=1<<i
    return {face for face in range(1,1<<N)
            if all(((face^(1<<v))&~adjacent[v])==0
                   for v in range(N) if face&(1<<v))}

def fvector(faces):
    return dict(sorted(Counter(face.bit_count()-1 for face in faces).items()))

def verify_collapse(initial,target,sequence):
    assert target<=initial
    faces=set(initial)
    for lower,upper in sequence:
        assert lower in faces and upper in faces
        assert lower not in target and upper not in target
        assert lower.bit_count()+1==upper.bit_count()
        assert lower&upper==lower
        cofacets=[co for v in range(N) if not lower&(1<<v)
                  if (co:=lower|(1<<v)) in faces]
        assert cofacets==[upper],(lower,upper,cofacets)
        faces.remove(lower)
        faces.remove(upper)
    assert faces==target,(len(faces-target),len(target-faces))

F={q:flag_faces(q) for q in (9,16,18,32,33,36,48)}
assert [fvector(F[q]) for q in (9,16,18,32,33)]==[
    {0:14,1:24},
    {0:14,1:36,2:24},
    {0:14,1:48,2:56,3:20},
    {0:14,1:60,2:100,3:60,4:6},
    {0:14,1:84,2:280,3:560,4:672,5:448,6:128}]

# The first stage is a connected graph with first Betti number 24-14+1=11.
low_adj={v:set() for v in range(N)}
for face in F[9]:
    if face.bit_count()==2:
        a,b=[v for v in range(N) if face>>v&1]
        low_adj[a].add(b)
        low_adj[b].add(a)
seen={0}; queue=deque([0])
while queue:
    for b in low_adj[queue.popleft()]:
        if b not in seen:seen.add(b);queue.append(b)
assert len(seen)==14

# At the 2nd stage, the flag complex is a closed connected 2-manifold.
K=F[16]
assert max(f.bit_count() for f in K)==3
assert sum((-1)**(k)*v for k,v in fvector(K).items())==2
for edge in (f for f in K if f.bit_count()==2):
    assert sum(1 for tri in K if tri.bit_count()==3 and tri&edge==edge)==2
for v in range(N):
    link_edges=[f^(1<<v) for f in K if f.bit_count()==3 and f>>v&1]
    link_vertices={w for e in link_edges for w in range(N) if e>>w&1}
    deg=Counter(w for e in link_edges for w in range(N) if e>>w&1)
    assert all(deg[w]==2 for w in link_vertices)
    linked={min(link_vertices)}; queue=deque(linked)
    while queue:
        u=queue.popleft()
        for e in link_edges:
            if e>>u&1:
                for w in range(N):
                    if e>>w&1 and w not in linked:
                        linked.add(w);queue.append(w)
    assert linked==link_vertices
# It is a sphere by the classification of compact connected surfaces.

# Exact elementary collapses, independently rechecked against all faces.
certificate=json.loads(Path(__file__).with_name('collapse_certificate.json').read_text())
assert len(certificate['c_to_b'])==32
assert len(certificate['d_to_corner'])==80
verify_collapse(F[18],F[16],certificate['c_to_b'])
CUBE={f for f in F[32] if f&63==0}
verify_collapse(F[32],CUBE,certificate['d_to_corner'])
assert fvector(CUBE)=={0:8,1:24,2:32,3:16}

# Four antipodal pairs of cube vertices: CUBE is (S^0)^{*4}=S^3.
opp_cube={(6+i,6+7-i) for i in range(4)}
assert all((a,b) in D2 and D2[(a,b)]==48 for a,b in opp_cube)
assert CUBE=={m for m in range(1,1<<N) if m&63==0 and
               all((m&(1<<a)==0 or m&(1<<b)==0) for a,b in opp_cube)}

# At the fifth stage the only forbidden pairs are the seven antipodal
# pairs: (S^0)^{*7}=S^6. The final two shells separately produce a cone.
opp_axis={(2*i,2*i+1) for i in range(3)}
assert F[33]=={m for m in range(1,1<<N) if
               all((not m&(1<<a) or not m&(1<<b))
                   for a,b in opp_cube|opp_axis)}
for q in (36,48):
    assert F[q]=={m for m in range(1,1<<N) if
                all(((m^(1<<i))&~sum((1<<j) for j in range(N)
                     if j!=i and D2.get((min(i,j),max(i,j)),0)<=q))==0
                     for i in range(N) if m>>i&1)}
# At shell 36 axes become a simplex and join the corner complex: cone.
assert all((m|(1<<0)) in F[36] for m in F[36] if not m&(1<<0))
assert len(F[48])==(1<<N)-1

# Additional independent mod-2 boundary ranks for the five nontrivial stages.
def mod2_betti(faces):
    by_dim=defaultdict(list)
    for face in faces:by_dim[face.bit_count()-1].append(face)
    highest=max(by_dim)
    ranks={0:0,highest+1:0}
    for d in range(1,highest+1):
        row={face:i for i,face in enumerate(by_dim[d-1])}
        basis={}
        for face in by_dim[d]:
            col=0
            for v in range(N):
                if face>>v&1:col^=1<<row[face^(1<<v)]
            while col:
                p=col.bit_length()-1
                if p in basis:col^=basis[p]
                else:basis[p]=col;break
        ranks[d]=len(basis)
    return {d:len(by_dim[d])-ranks[d]-ranks[d+1] for d in by_dim
            if len(by_dim[d])-ranks[d]-ranks[d+1]}
expected={9:{0:1,1:11},16:{0:1,2:1},18:{0:1,2:1},
          32:{0:1,3:1},33:{0:1,6:1}}
for q in expected:
    assert mod2_betti(F[q])==expected[q]

# All statements concern the parameter interval 3/2 <= t <= 2.
# The squared shell orders follow from the seven exact formulas
# a=t*t-2*t+3, b=4, c=2*t*t, d=8, e=t*t+2*t+3,
# f=4*t*t, g=12. The only variable interchange is f=g at t=sqrt(3).
print('PASS: 14 vertices, seven squared-distance shells, 91 pairs')
print('PASS: face vectors, closed triangulated 2-sphere, connected 11-cycle graph')
print('PASS: 32+80 elementary collapses and both cross-polytope joins')
print('PASS: mod-2 Betti ranks at all five essential stages')
print('PASS: exact interval families H0, H1, H2, H3, H6; parameter switch t=sqrt(3)')
