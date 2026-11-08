"""Verify a complete simplicial collapse certificate for a truncated-icosahedral graph-metric Rips complex."""
import json
import itertools
import collections
import sys
from pathlib import Path

certificate_path = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name('certificate.json'))
cert = json.loads(certificate_path.read_text(encoding='utf-8'))
E = set()
def edge(a,b):
    E.add(tuple(sorted((a,b))))
for i in range(5):
    u,v=2+i,7+i
    for a,b in ((0,u),(1,v),(u,2+(i+1)%5),(v,7+(i+1)%5),(u,v),(u,7+(i-1)%5)):
        edge(a,b)
assert len(E)==30
N=[set() for _ in range(12)]
for u,v in E:
    N[u].add(v);N[v].add(u)
assert all(len(n)==5 for n in N)
T = [t for t in itertools.combinations(range(12),3) if all(tuple(sorted(z)) in E for z in itertools.combinations(t,2))]
assert len(T)==20
half=sorted((u,v) for u in range(12) for v in N[u])
assert [list(x) for x in half]==cert['halved_edges']
index={p:i for i,p in enumerate(half)}
H=[set() for _ in range(60)]
def hed(a,b):
    a,b=index[a],index[b]
    assert a!=b
    H[a].add(b);H[b].add(a)
for u,v in E:
    hed((u,v),(v,u))
for u in range(12):
    for v,w in itertools.combinations(sorted(N[u]),2):
        if tuple(sorted((v,w))) in E:
            hed((u,v),(u,w))
assert all(len(n)==3 for n in H)
assert sum(map(len,H))//2==90
R=[set(neighbors) for neighbors in H]
for u in range(60):
    for v in H[u]: R[u].update(H[v])
    R[u].discard(u)
assert all(len(neighbors)==9 for neighbors in R)
# Independent complete clique enumeration of the graph square.
faces=set()
def enumerate_cliques(face,allowed):
    for i,v in enumerate(allowed):
        newface=face+(v,)
        faces.add(newface)
        enumerate_cliques(newface,[w for w in allowed[i+1:] if w in R[v]])
enumerate_cliques((),list(range(60)))
assert len(faces)==802
assert [sum(len(f)==k for f in faces) for k in range(1,6)]==cert['expected_initial_f_vector']==[60,270,340,120,12]
remaining=set(faces)
for j,(small,big) in enumerate(cert['collapse_pairs']):
    small,big=tuple(small),tuple(big)
    assert small in remaining and big in remaining,('missing face',j)
    assert len(big)==len(small)+1 and set(small)<set(big),('codimension',j)
    cofaces=[f for f in remaining if set(small).issubset(f) and f!=small]
    assert cofaces==[big],('not free',j,cofaces)
    remaining.remove(small);remaining.remove(big)
assert len(cert['collapse_pairs'])==120
assert max(map(len,remaining))==3
assert [sum(len(f)==k for f in remaining) for k in range(1,4)]==cert['expected_residual_f_vector']==[60,270,232]
# An explicit face system for the original polyhedral sphere.
poly=[]
for u in range(12):
    neighbors=sorted(N[u])
    rim={v:sorted(w for w in N[u] if w!=v and tuple(sorted((v,w))) in E) for v in neighbors}
    assert all(len(x)==2 for x in rim.values())
    seq=[neighbors[0],rim[neighbors[0]][0]]
    while len(seq)<5:
        opts=[w for w in rim[seq[-1]] if w!=seq[-2]]
        assert len(opts)==1
        seq.append(opts[0])
    assert len(set(seq))==5 and seq[0] in rim[seq[-1]]
    poly.append([index[u,v] for v in seq])
for a,b,c in T:
    poly.append([index[a,b],index[b,a],index[b,c],index[c,b],index[c,a],index[a,c]])
assert collections.Counter(map(len,poly))=={5:12,6:20}
edgefaces=collections.Counter()
vertex_faces=[[] for _ in range(60)]
for j,p in enumerate(poly):
    assert len(p)==len(set(p))
    for x in p:vertex_faces[x].append(j)
    for a,b in zip(p,p[1:]+p[:1]):
        assert b in H[a]
        edgefaces[tuple(sorted((a,b)))]+=1
assert len(edgefaces)==90 and set(edgefaces.values())=={2}
# The polygonal face system is the combinatorial sphere: every vertex link is 3-cycle.
assert all(len(f)==3 for f in vertex_faces)
for v in range(60):
    star_edges=set()
    for j in vertex_faces[v]:
        cyc=poly[j]; i=cyc.index(v)
        star_edges.add(tuple(sorted((cyc[(i-1)%len(cyc)],cyc[(i+1)%len(cyc)]))))
    neighbors=H[v]
    assert len(star_edges)==3 and set(itertools.chain.from_iterable(star_edges))==neighbors
assert len(H)-sum(map(len,H))//2+len(poly)==2
# Every face boundary bounds explicit 2-chains in the graph-metric Rips complex.
for p in poly:
    if len(p)==5:
        assert all(b in R[a] for a,b in itertools.combinations(p,2))
    else:
        for i,j,k in ((0,1,2),(2,3,4),(4,5,0),(0,2,4)):
            assert tuple(sorted((p[i],p[j],p[k]))) in faces
chi=sum((-1)**(len(f)-1) for f in faces)
assert chi==22
# Connected 2D collapse, pi_1=0 via facial relators; rank H_2 = chi-1 = 21.
print('BUCKMINSTERFULLERENE_RIPS2_WEDGE21_OK')
print('vertices=60 edges=90 flag_faces=802 initial_f_vector=60,270,340,120,12')
print('free_face_pairs=120 residual_f_vector=60,270,232')
print('polyhedral_faces=12_pentagons+20_hexagons edge_incidence=2 vertex_links=triangles')
print('all_32_facial_loops_bound_simplicial_2_chains; pi_1=0 chi=22')
