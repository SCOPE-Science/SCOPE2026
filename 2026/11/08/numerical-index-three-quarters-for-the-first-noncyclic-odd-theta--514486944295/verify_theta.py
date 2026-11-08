"""Exact, dependency-free certificate verification for a theta-graph numerical index."""
from fractions import Fraction as Q
from itertools import product
from collections import deque
from pathlib import Path
import json

EDGES=((0,2),(2,1),(0,3),(3,1),(0,4),(4,5),(5,1))
N=6

def connected(edges):
    seen={0}
    while True:
        nxt=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
        if nxt==seen:break
        seen=nxt
    return len(seen)==N

def dual_vertices():
    adj={j:[] for j in range(N)}
    for a,b in EDGES:adj[a].append(b);adj[b].append(a)
    d=[None]*N;d[0]=0;q=deque([0])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if d[w] is None:d[w]=d[v]+1;q.append(w)
    assert all(x is not None for x in d)
    F=[]
    for vals in product(*(range(-d[i],d[i]+1) for i in range(1,N))):
        f=(0,)+vals
        if any(abs(f[a]-f[b])>1 for a,b in EDGES):continue
        tight=[(a,b) for a,b in EDGES if abs(f[a]-f[b])==1]
        if connected(tight):F.append(f)
    return F

def dot(f,y):return sum(Q(f[i])*y[i-1] for i in range(1,N))

def main(path):
    cert=json.loads(Path(path).read_text(encoding='utf-8'))
    F=dual_vertices()
    assert len(F)==54==cert['expected_dual_vertices']
    assert tuple(map(tuple,cert['edges']))==EDGES
    assert cert['scale_numerator']==3 and cert['scale_denominator']==4
    grouped={(d['edge_id'],d['vertex_id']):d for d in cert['decompositions']}
    expected={(ei,fi) for ei,(a,b) in enumerate(EDGES) for fi,f in enumerate(F) if f[a]==f[b]}
    assert set(grouped)==expected and len(grouped)==78
    faces=[];checks=0
    for ei,(a,b) in enumerate(EDGES):
        F_e=[f for f in F if f[a]-f[b]==1]
        faces.append(len(F_e))
        assert len(F_e) in (21,22)
        for fi,f in enumerate(F):
            if f[a]!=f[b]:continue
            ent=grouped[ei,fi];weights=[];sumf=[Q(0) for _ in range(N)]
            for vi,sg,num,den in ent['terms']:
                assert 0<=vi<len(F) and sg in (-1,1)
                assert isinstance(num,int) and isinstance(den,int) and num>0 and den>0
                assert abs(sg*(F[vi][a]-F[vi][b]))==1
                w=Q(num,den);weights.append(w)
                for j in range(N):sumf[j]+=w*sg*F[vi][j]
                checks+=1
            assert sum(weights)==1
            assert tuple(sumf)==tuple(Q(3,4)*x for x in f)
    # Rank-one witness T:x -> ell(x)y. The first coordinate corresponds to vertex 1.
    y=tuple(map(Q,(0,1,0,0,-2)))
    ell=(Q(-1,4),Q(-1),Q(-3,4),Q(3,4),Q(0))
    ey=[]
    for a,b in EDGES:
        va=ell[a-1] if a else Q(0)
        vb=ell[b-1] if b else Q(0)
        ey.append(va-vb)
    assert max(map(abs,ey))==1
    norm_y=max(abs(dot(f,y)) for f in F)
    assert norm_y==4
    gs=[]
    for a,b in EDGES:
        face=[f for f in F if f[a]-f[b]==1]
        gs.append(max(abs(dot(f,y)) for f in face))
    assert gs==[3,4,4,4,4,4,4],gs
    numerical_radius=max(abs(u)*g for u,g in zip(ey,gs))
    assert numerical_radius==3
    assert norm_y*max(abs(x) for x in ey)==4
    print('THETA_INDEX_EXACT_OK', 'dual_extremes',len(F),'convex_certificates',len(grouped),'rational_terms',checks,'faces',faces,'norm',norm_y,'radius',numerical_radius,'index',Q(3,4))

if __name__=='__main__':
    import sys
    main(sys.argv[1] if len(sys.argv)>1 else str(Path(__file__).with_name('theta_certificate.json')))
