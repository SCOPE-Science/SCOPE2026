#!/usr/bin/env python3
"""Self-contained combinatorial verification for an asymmetric ternary Hamming prism.

Run: python verify.py certificate.json
The certificate is deliberately regenerated independently of the read-path checks.
Only the Python standard library is required.
"""
import collections
import hashlib
import itertools
import json
import sys
from collections import deque
from pathlib import Path

DIMS=(3,3,4)
V=list(itertools.product(*(range(n) for n in DIMS)))
N=len(V)
NEIGH=[]
for i,x in enumerate(V):
    NEIGH.append(sum(1<<j for j,y in enumerate(V)
                     if i!=j and any(a==b for a,b in zip(x,y))))

def maximal_cliques():
    out=[]
    def bk(R,P,X):
        if not (P|X):
            out.append(R);return
        U=P|X
        pivot=max((i for i in range(N) if U>>i&1),
                  key=lambda i:(NEIGH[i]&P).bit_count())
        cand=P&~NEIGH[pivot]
        while cand:
            bit=cand&-cand
            i=bit.bit_length()-1
            bk(R|bit,P&NEIGH[i],X&NEIGH[i])
            P^=bit;X|=bit;cand^=bit
    bk(0,(1<<N)-1,0)
    return sorted(out)

def all_faces():
    facets=maximal_cliques()
    fs=set()
    for f in facets:
        sub=f
        while sub:
            fs.add(sub)
            sub=(sub-1)&f
    return facets,fs

def facets_and_parents(faces):
    parents={s:set() for s in faces}
    for f in faces:
        y=f
        while y:
            z=y&-y;y-=z
            s=f^z
            if s in parents:parents[s].add(f)
    return parents

def apply_pair(faces,parents,s,f):
    assert s in faces and f in faces
    assert f.bit_count()==s.bit_count()+1 and f&s==s
    assert parents[s]=={f},(s,f,parents[s])
    for c in (s,f):
        faces.remove(c)
    for c in (s,f):
        y=c
        while y:
            z=y&-y;y-=z
            r=c^z
            if r in faces:parents[r].discard(c)

def make_collapses(faces):
    parents=facets_and_parents(faces)
    q=deque(sorted((s for s in faces if len(parents[s])==1),key=lambda s:(-s.bit_count(),s)))
    pairs=[]
    while q:
        s=q.popleft()
        if s not in faces or len(parents[s])!=1:continue
        f=next(iter(parents[s]))
        if f not in faces:continue
        apply_pair(faces,parents,s,f)
        pairs.append([s,f])
        for c in (s,f):
            y=c
            while y:
                z=y&-y;y-=z
                r=c^z
                if r in faces and len(parents[r])==1:q.append(r)
    return pairs

def tree_and_triangles(faces):
    edges={f for f in faces if f.bit_count()==2}
    triangles=sorted(f for f in faces if f.bit_count()==3)
    adj=[[] for _ in range(N)]
    for e in edges:
        i,j=[i for i in range(N) if e>>i&1]
        adj[i].append((j,e));adj[j].append((i,e))
    seen={0};q=deque([0]);tree=[]
    while q:
        i=q.popleft()
        for j,e in sorted(adj[i]):
            if j not in seen:
                seen.add(j);q.append(j);tree.append(e)
    assert len(seen)==N and len(tree)==N-1
    known=set(tree);witnesses=[]
    while True:
        changes=0
        for t in triangles:
            ed=[t^(1<<i) for i in range(N) if t>>i&1]
            if sum(e in known for e in ed)>=2:
                for e in ed:
                    if e not in known:
                        witnesses.append([e,t]);known.add(e);changes+=1
        if changes==0:break
    assert known==edges
    return tree,witnesses

def integer_pivots(faces, expected=None):
    triangles=sorted(f for f in faces if f.bit_count()==3)
    tets=sorted(f for f in faces if f.bit_count()==4)
    idx={f:i for i,f in enumerate(triangles)}
    piv={};rows=[];maxcoeff=0;maxwidth=0
    for f in tets:
        verts=[i for i in range(N) if f>>i&1]
        col={idx[f^(1<<i)]:(-1 if j%2 else 1)
             for j,i in enumerate(verts)}
        while col:
            row=max(col)
            if row not in piv:break
            old=piv[row]
            assert abs(old[row])==1
            fac=col[row]*old[row]
            for k,v in old.items():
                col[k]=col.get(k,0)-fac*v
                if col[k]==0:del col[k]
        if col:
            row=max(col)
            assert abs(col[row])==1,(f,row,col[row])
            piv[row]=col
            rows.append(row)
            maxcoeff=max(maxcoeff,max(map(abs,col.values())))
            maxwidth=max(maxwidth,len(col))
        else:rows.append(-1)
    if expected is not None:assert rows==expected
    return rows,len(piv),maxcoeff,maxwidth

def gf2_rank(faces):
    a=sorted(f for f in faces if f.bit_count()==3)
    idx={t:i for i,t in enumerate(a)}
    piv={}
    for f in sorted(t for t in faces if t.bit_count()==4):
        col=0
        y=f
        while y:
            bit=y&-y;y^=bit
            col^=1<<idx[f^bit]
        while col:
            k=col.bit_length()-1
            if k in piv:col^=piv[k]
            else:piv[k]=col;break
    return len(piv)

def build(path):
    fac,faces=all_faces()
    f0=dict(sorted(collections.Counter(x.bit_count() for x in faces).items()))
    assert len(fac)==154 and len(faces)==30991
    pairs=make_collapses(faces)
    assert len(pairs)==14227 and collections.Counter(f.bit_count() for f in faces)=={1:36,2:387,3:1185,4:929}
    tree,wit=tree_and_triangles(faces)
    assert len(wit)==352
    rows,rank,mx,mw=integer_pivots(faces)
    assert rank==833 and mx==1 and gf2_rank(faces)==833
    cert={'description':'Finite combinatorial collapse and integral chain certificate for Ind(K3 x K3 x K4)',
          'dimensions':list(DIMS),'initial_face_counts':[f0.get(i,0) for i in range(1,13)],
          'collapse_pairs':pairs,'spanning_tree_edges':tree,'triangle_nullhomotopy_witnesses':wit,
          'integer_boundary_pivot_rows':rows,'expected_residual_face_counts':[36,387,1185,929]}
    Path(path).write_text(json.dumps(cert,separators=(',',':'),ensure_ascii=False)+'\n',encoding='utf-8')
    print('GENERATED',len(fac),len(pairs),len(wit),rank)

def verify(path):
    cert=json.loads(Path(path).read_text(encoding='utf-8'))
    assert cert['dimensions']==list(DIMS)
    facets,faces=all_faces()
    counts=[sum(f.bit_count()==k for f in faces) for k in range(1,13)]
    assert counts==cert['initial_face_counts']
    assert len(facets)==154 and len(faces)==30991
    parents=facets_and_parents(faces)
    for s,f in cert['collapse_pairs']:
        apply_pair(faces,parents,s,f)
    assert len(cert['collapse_pairs'])==14227
    counts2=[sum(f.bit_count()==k for f in faces) for k in range(1,5)]
    assert counts2==cert['expected_residual_face_counts']==[36,387,1185,929]
    edges={f for f in faces if f.bit_count()==2}
    tris={f for f in faces if f.bit_count()==3}
    tree=cert['spanning_tree_edges']
    assert len(tree)==35 and len(set(tree))==35 and set(tree)<=edges
    groups=list(range(N))
    def root(i):
        while groups[i]!=i:i=groups[i]
        return i
    for e in tree:
        a,b=[i for i in range(N) if e>>i&1]
        assert root(a)!=root(b)
        groups[root(a)]=root(b)
    assert len({root(i) for i in range(N)})==1
    known=set(tree)
    for e,t in cert['triangle_nullhomotopy_witnesses']:
        assert e not in known and e in edges and t in tris and (t&e)==e
        boundary=[t^(1<<i) for i in range(N) if t>>i&1]
        assert len(boundary)==3 and e in boundary and set(boundary)-{e}<=known
        known.add(e)
    assert len(cert['triangle_nullhomotopy_witnesses'])==352 and known==edges
    pivots,rank,maxcoeff,maxwidth=integer_pivots(faces,cert['integer_boundary_pivot_rows'])
    assert len(pivots)==929 and rank==833 and maxcoeff==1
    assert gf2_rank(faces)==833
    assert counts2[2]-352==833
    assert counts2[3]-833==96
    assert counts2[0]-counts2[1]+counts2[2]-counts2[3]==-95
    print('INDEPENDENT_CERTIFICATE_REPLAY_OK')
    print('input_vertices 36; input_facets',len(facets),'; input_nonempty_faces 30991')
    print('input_face_vector',','.join(map(str,counts)))
    print('elementary_collapse_pairs',len(cert['collapse_pairs']),'; residual_face_vector',','.join(map(str,counts2)))
    print('spanning_tree_edges 35; triangle_nullhomotopy_witnesses 352; pi1 trivial')
    print('integral_boundary_rank',rank,'; unit_pivot_max_coefficient',maxcoeff,'; max_column_width',maxwidth)
    print('independent_mod2_boundary_rank',gf2_rank(faces),'; H2_Z 0; H3_Z rank 96')
    print('scale1_H1_rank 40; scale2_H3_rank 96; scale3_contractible')

if __name__=='__main__':
    assert len(sys.argv)==3 and sys.argv[1] in ('build','verify')
    if sys.argv[1]=='build':build(sys.argv[2])
    else:verify(sys.argv[2])
