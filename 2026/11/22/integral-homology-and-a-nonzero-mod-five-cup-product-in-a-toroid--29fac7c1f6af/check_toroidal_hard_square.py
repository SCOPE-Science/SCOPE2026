#!/usr/bin/env python3
"""Standalone exact checker for the C4 x C5 hard-square cyclic quotient.

Pure Python 3; uses no external files, data sets, or packages.
"""
from collections import Counter, defaultdict

M, N = 4, 5

def all_independent_faces():
    adj = [set() for _ in range(M*N)]
    for i in range(M):
        for j in range(N):
            v = i*N+j
            adj[v].update({((i+1)%M)*N+j, ((i-1)%M)*N+j,
                           i*N+(j+1)%N, i*N+(j-1)%N})
    out=defaultdict(list)
    def enumerate_from(face,allowed):
        if face: out[len(face)-1].append(face)
        for t,v in enumerate(allowed):
            enumerate_from(face+(v,), [w for w in allowed[t+1:] if w not in adj[v]])
    enumerate_from((), list(range(M*N)))
    assert all(all(not set(f[i:]) & adj[f[i]] for i in range(len(f))) for fs in out.values() for f in fs)
    return dict(out)

def rotated(face,s):
    return tuple((v//N)*N+(v%N+s)%N for v in face)

def canonical(face):
    return min(tuple(sorted(rotated(face,s))) for s in range(N))

def orient_to_canonical(face):
    target=canonical(face)
    for s in range(N):
        a=rotated(face,s)
        if tuple(sorted(a))==target:
            inv=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
            return (-1)**inv
    raise AssertionError

def boundaries(cells,cyclic):
    b={k: {f:i for i,f in enumerate(fs)} for k,fs in cells.items()}
    ds={}
    for k in range(1,8):
        d=defaultdict(int)
        for j,f in enumerate(cells[k]):
            for a in range(k+1):
                face=f[:a]+f[a+1:]
                base=canonical(face) if cyclic else face
                s=(-1)**a*(orient_to_canonical(face) if cyclic else 1)
                d[b[k-1][base],j]+=s
        ds[k]={ij:v for ij,v in d.items() if v}
    for k in range(2,8):
        # sparse multiplication d_{k-1} d_k
        first=defaultdict(list)
        for (i,j),v in ds[k-1].items():first[j].append((i,v))
        comp=defaultdict(int)
        for (j,l),v in ds[k].items():
            for i,w in first[j]: comp[i,l]+=w*v
        assert not any(comp.values()), ('boundary squared',k)
    return ds

def cancel_all(cells,ds):
    # Elementary integral chain contractions along unit incidences.
    remain={k:set(range(len(fs))) for k,fs in cells.items()}
    D={k:{i:{} for i in remain[k-1]} for k in ds}
    for k,d in ds.items():
        for (i,j),v in d.items():D[k][i][j]=v
    counts=0
    for k in range(1,8):
        d=D[k]
        while True:
            colcounts=Counter(j for row in d.values() for j in row)
            choices=[((len(row)-1)*(colcounts[j]-1),i,j,v)
                    for i,row in d.items() for j,v in row.items() if abs(v)==1]
            if not choices: break
            _,r,c,a=min(choices)
            pivotrow=d[r].copy()
            col={i:row[c] for i,row in d.items() if c in row}
            for i,u in col.items():
                if i==r:continue
                for j,v in pivotrow.items():
                    if j==c:continue
                    z=d[i].get(j,0)-a*u*v
                    if z:d[i][j]=z
                    else:d[i].pop(j,None)
            d.pop(r)
            for i in col:
                if i!=r:d[i].pop(c,None)
            remain[k].remove(c)
            remain[k-1].remove(r)
            if k+1 in D:D[k+1].pop(c)
            if k-1 in D:
                for row in D[k-1].values():row.pop(r,None)
            counts+=1
    out={k:{(i,j):v for i,row in d.items() for j,v in row.items()}
         for k,d in D.items()}
    # After all reductions, any nonunit entries must be handled by Smith form.
    return [len(remain[k]) for k in range(8)],out,counts

def mod_rank(d,p):
    cols=defaultdict(dict)
    for (i,j),a in d.items():
        if a%p:cols[j][i]=a%p
    pivots={}
    for j in sorted(cols):
        v=cols[j].copy()
        while v:
            row=min(v)
            if row not in pivots:
                inv=pow(v[row],-1,p)
                pivots[row]={i:(a*inv)%p for i,a in v.items()}
                break
            factor=v[row]
            for i,a in pivots[row].items():
                z=(v.get(i,0)-factor*a)%p
                if z:v[i]=z
                else:v.pop(i,None)
    return len(pivots)

def free_reduction(word):
    o=[]
    for x in word:
        if o and o[-1]==-x:o.pop()
        else:o.append(x)
    while len(o)>1 and o[0]==-o[-1]:o=o[1:-1]
    return o

def group_presentation(cells,cyclic):
    # An actual CW group presentation from the quotient 2-skeleton.
    def vertex(v):return v//N if cyclic else v
    num_vertices=M if cyclic else M*N
    parent=list(range(num_vertices))
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    tree=[]
    for j,(a,b) in enumerate(cells[1]):
        ra,rb=root(vertex(a)),root(vertex(b))
        if ra!=rb:parent[ra]=rb;tree.append(j)
    assert len(tree)==num_vertices-1
    edge_index={f:j+1 for j,f in enumerate(cells[1])}
    gens=set(range(1,len(cells[1])+1))-{j+1 for j in tree}
    def edge(a,b):
        f=(a,b)
        id=edge_index[canonical(f) if cyclic else f]
        if id-1 in tree:return []
        sign=orient_to_canonical(f) if cyclic else 1
        return [sign*id]
    rels=[]
    for a,b,c in cells[2]:
        rels.append(free_reduction(edge(a,b)+edge(b,c)+[-x for x in edge(a,c)[::-1]]))
    eliminations=0
    while True:
        rels=list(dict.fromkeys(tuple(free_reduction(w)) for w in rels))
        rels=[list(w) for w in rels if w]
        occurrences=Counter(abs(x) for w in rels for x in w)
        choices=[]
        for i,w in enumerate(rels):
            counts=Counter(abs(x) for x in w)
            choices += [(len(w),occurrences[g],i,g) for g,t in counts.items() if t==1]
        if not choices:break
        _,_,ri,g=min(choices)
        w=rels.pop(ri)
        pos=next(k for k,x in enumerate(w) if abs(x)==g)
        residual=w[pos+1:]+w[:pos]
        subst=[-x for x in residual[::-1]]
        if w[pos]==-g:subst=[-x for x in subst[::-1]]
        new=[]
        for w in rels:
            v=[]
            for x in w:
                if x==g:v.extend(subst)
                elif x==-g:v.extend([-y for y in subst[::-1]])
                else:v.append(x)
            new.append(free_reduction(v))
        rels=new
        gens.remove(g)
        eliminations+=1
    return gens,rels,eliminations

def verify():
    orig=all_independent_faces()
    assert [len(orig[k]) for k in range(8)]==[20,150,540,1010,1020,590,200,30]
    quot={k:sorted({canonical(f) for f in faces}) for k,faces in orig.items()}
    assert [len(quot[k]) for k in range(8)]==[4,30,108,202,204,118,40,6]
    # No face is invariant under a nonzero power of order-five translation:
    # the full five-point row orbit contains a graph edge.
    for faces in orig.values():
        assert all(rotated(f,s)!=f and set(rotated(f,s))!=set(f)
                   for f in faces for s in range(1,5))
    d_orig=boundaries(orig,False)
    d_quot=boundaries(quot,True)
    sizes0,m0,n0=cancel_all(orig,d_orig)
    sizes1,m1,n1=cancel_all(quot,d_quot)
    assert sizes0==[1,0,0,2,1,0,0,0] and all(not d for d in m0.values())
    assert sizes1==[1,1,1,2,1,0,0,0]
    assert len(m1[2])==1 and sorted(abs(v) for v in m1[2].values())==[5]
    assert all(not d for k,d in m1.items() if k!=2)
    # Field ranks are computed directly on the unreduced matrices, independently
    # of integral unit cancellations.
    expected0=[1,0,0,2,1,0,0,0]
    expected5=[1,1,1,2,1,0,0,0]
    for p in (2,3,5,7):
        for cells,ds,expect in ((orig,d_orig,expected0),
                                (quot,d_quot,expected5 if p==5 else expected0)):
            ranks={k:mod_rank(ds[k],p) for k in range(1,8)}
            bettis=[len(cells[k])-ranks.get(k,0)-ranks.get(k+1,0)
                    for k in range(8)]
            assert bettis==expect,(p,bettis,expect)
    go,ro,eo=group_presentation(orig,False)
    gq,rq,eq=group_presentation(quot,True)
    assert len(go)==0 and ro==[]
    assert len(gq)==1 and all(len(w)==5 and len({abs(x) for x in w})==1 for w in rq)
    assert all(w[0] in (next(iter(gq)),-next(iter(gq))) for w in rq)
    print('ORIGINAL_CELLS', [len(orig[k]) for k in range(8)])
    print('QUOTIENT_CELLS', [len(quot[k]) for k in range(8)])
    print('ORIGINAL_INTEGRAL_REDUCTION',sizes0,'unit_pairs',n0)
    print('QUOTIENT_INTEGRAL_REDUCTION',sizes1,'degree_two_entry',list(m1[2].values()),'unit_pairs',n1)
    print('ORIGINAL_PI1_REDUCTION',len(go),'generators;',len(ro),'relators;',eo,'Tietze eliminations')
    print('QUOTIENT_PI1_REDUCTION',len(gq),'generator;',rq,'relators;',eq,'Tietze eliminations')
    print('INDEPENDENT_MODULAR_RANK_CHECKS_PASSED', (2,3,5,7))
    print('TOROIDAL_HARD_SQUARE_C4_C5_ROTATION_CHECKS_OK')

if __name__=='__main__':verify()
