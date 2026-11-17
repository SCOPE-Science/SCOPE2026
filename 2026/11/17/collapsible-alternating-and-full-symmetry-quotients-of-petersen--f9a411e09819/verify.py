"""Exact barycentric orbit-complex collapse certificate for Petersen configurations."""
import itertools
from collections import defaultdict

LABELS=list(itertools.combinations(range(5),2)); li={p:i for i,p in enumerate(LABELS)}
EDGES=[e for e in itertools.combinations(range(10),2) if set(LABELS[e[0]]).isdisjoint(LABELS[e[1]])]
EL={frozenset(e):i for i,e in enumerate(EDGES)}
C0=list(itertools.combinations(range(10),2))
C1=[(e,v) for e,(a,b) in enumerate(EDGES) for v in range(10) if v not in (a,b)]
C2=[(a,b) for a,b in itertools.combinations(range(len(EDGES)),2) if len(set(EDGES[a]+EDGES[b]))==4]
C=[C0,C1,C2]; lut=[{x:i for i,x in enumerate(c)} for c in C]
FACE01={(lut[0][tuple(sorted((u,v)))],j) for j,(e,v) in enumerate(C1) for u in EDGES[e]}
FACE12={(lut[1][(e,v)],j) for j,(a,b) in enumerate(C2) for e,xx in ((a,EDGES[b]),(b,EDGES[a])) for v in xx}
FACE02={(lut[0][tuple(sorted((u,v)))],j) for j,(a,b) in enumerate(C2) for u in EDGES[a] for v in EDGES[b]}
INDEX01=defaultdict(list)
for i,j in FACE01:INDEX01[j].append(i)
TRI=sorted((i,j,k) for j,k in FACE12 for i in INDEX01[j])
assert (len(C0),len(C1),len(C2))==(45,120,75)
assert (len(FACE01),len(FACE12),len(FACE02),len(TRI))==(240,300,300,600)
VERT=[(d,i) for d in range(3) for i in range(len(C[d]))]
ONE=[((0,i),(1,j)) for i,j in sorted(FACE01)]+[((1,j),(2,k)) for j,k in sorted(FACE12)]+[((0,i),(2,k)) for i,k in sorted(FACE02)]
TWO=[((0,i),(1,j),(2,k)) for i,j,k in TRI]
ALL=[VERT,ONE,TWO]

def iso_action(p):
    v=[li[tuple(sorted(p[t] for t in pair))] for pair in LABELS]
    e=[EL[frozenset((v[a],v[b]))] for a,b in EDGES]
    return [lut[0][tuple(sorted((v[a],v[b])))] for a,b in C0], [lut[1][(e[a],v[b])] for a,b in C1], [lut[2][tuple(sorted((e[a],e[b])))] for a,b in C2]

def parity(p):return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2

def calc(name,group):
    maps=[iso_action(p) for p in group]
    orbitmaps=[];reps=[]
    for dd,simplices in enumerate(ALL):
        si={x:i for i,x in enumerate(simplices)};where={};rr=[]
        for i,x in enumerate(simplices):
            if i in where: continue
            oid=len(rr);rr.append(x)
            for f in maps:
                y=tuple((d,f[d][j]) for d,j in ((x,) if dd==0 else x))
                where[si[y[0] if dd==0 else y]]=oid
        assert len(where)==len(simplices)
        orbitmaps.append(where);reps.append(rr)
    adj=defaultdict(list)
    for eid,(v,w) in enumerate(reps[1]):
        # find representative endpoints and orbit vertex IDs
        a=orbitmaps[0][ALL[0].index(v)];b=orbitmaps[0][ALL[0].index(w)]
        adj[eid]=[a,b]
    e_lookup={e:i for i,e in enumerate(ALL[1])}
    tris={}
    for tid,t in enumerate(reps[2]):
        sides=[(t[0],t[1]),(t[0],t[2]),(t[1],t[2])]
        ee=[orbitmaps[1][e_lookup[s]] for s in sides]
        assert len(set(ee))==3,(name,tid,ee)
        tris[tid]=ee
    remaining=set(tris); active_edges=set(range(len(reps[1]))); certificate=[]
    while remaining:
        deg=defaultdict(int)
        for t in remaining:
            for e in tris[t]: deg[e]+=1
        opts=[(t,e) for t in sorted(remaining) for e in tris[t] if deg[e]==1]
        if not opts:break
        t,e=opts[0];certificate.append((t,e));remaining.remove(t);active_edges.remove(e)
    # graph connectivity and acyclic check after 2-cell collapse
    verts=set(range(len(reps[0]))); p={v:v for v in verts}
    def find(a):
        while p[a]!=a:a=p[a]
        return a
    cycles=0
    for e in active_edges:
        a,b=adj[e]
        if find(a)==find(b):cycles+=1
        else:p[find(a)]=find(b)
    comps=len({find(a) for a in verts})
    print(name, 'group_size',len(group),'original_barycentric',(len(VERT),len(ONE),len(TWO)), 'orbits',tuple(map(len,reps)),'triangle_edge_pairs',certificate,'remaining_tris',sorted(remaining),'remaining_graph_edges',sorted(active_edges),'components',comps,'cycle_rank',cycles)
    assert not remaining and comps==1 and cycles==0 and len(active_edges)==len(verts)-1
    return tuple(map(len,reps)),certificate,sorted(active_edges)

if __name__=='__main__':
    perms=list(itertools.permutations(range(5)))
    calc('A5',[p for p in perms if parity(p)==0]);calc('S5',perms)
    print('PETERSEN_TWO_PARTICLE_A5_S5_COLLAPSES_PASS')
