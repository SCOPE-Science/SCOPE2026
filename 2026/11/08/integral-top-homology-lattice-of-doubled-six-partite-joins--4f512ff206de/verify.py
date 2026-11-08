#!/usr/bin/env python3
"""Independently reconstructs colored-pair doublings and exact top cycles.
No external dependencies; standard library only.
"""
import itertools
from collections import defaultdict
from math import prod

COLORS=range(6)
PAIRS=list(itertools.combinations(COLORS,2))
MATCHINGS=[]
for p in PAIRS:
    remaining=[i for i in COLORS if i not in p]
    for q in itertools.combinations(remaining,2):
        r=tuple(i for i in remaining if i not in q)
        M=tuple(sorted((p,q,r)))
        if M not in MATCHINGS:MATCHINGS.append(M)
MATCHINGS=sorted(MATCHINGS)
assert len(MATCHINGS)==15

def modrank(columns,p):
    """Sparse modular Gaussian elimination on column boundaries."""
    basis={}
    for col in columns:
        vec={i:(val%p) for i,val in col.items() if val%p}
        while vec:
            k=min(vec)
            if k not in basis:
                scale=pow(vec[k],-1,p)
                basis[k]={i:(a*scale)%p for i,a in vec.items() if a%p}
                break
            factor=vec[k]
            for i,a in basis[k].items():
                x=(vec.get(i,0)-factor*a)%p
                if x:vec[i]=x
                else:vec.pop(i,None)
    return len(basis)

def build(ns,check_rank=True):
    sets=[tuple(range(n)) for n in ns]
    vertices=sorted([(p,choice) for p in PAIRS for choice in itertools.product(*(sets[i] for i in p))])
    index={v:j for j,v in enumerate(vertices)}
    faces1=set(); faces2=set()
    for M in MATCHINGS:
        pools=[[index[(pair,choice)] for choice in itertools.product(*(sets[i] for i in pair))] for pair in M]
        for a,b,c in itertools.product(*pools):
            tri=tuple(sorted((a,b,c)));faces2.add(tri)
            faces1.update(itertools.combinations(tri,2))
    faces1=sorted(faces1);faces2=sorted(faces2)
    eidx={e:j for j,e in enumerate(faces1)}
    cols=[{eidx[(b,c)]:1,eidx[(a,c)]:-1,eidx[(a,b)]:1} for a,b,c in faces2]
    f0=len(vertices);f1=len(faces1);f2=len(faces2)
    w={pair:ns[pair[0]]*ns[pair[1]] for pair in PAIRS}
    b1=2*sum(w.values())-14
    b2=sum(prod(w[p]-1 for p in M) for M in MATCHINGS)
    assert f0==sum(w.values())
    assert f1==sum(sum(w[p]*w[q] for p,q in itertools.combinations(M,2)) for M in MATCHINGS)
    assert f2==sum(prod(w[p] for p in M) for M in MATCHINGS)
    assert f0-f1+f2==1-b1+b2
    for p in (2,3) if check_rank else ():
        rank=modrank(cols,p)
        assert rank==f2-b2,(ns,p,rank,f2-b2)
        assert f1-(f0-1)-rank==b1
    print('sizes',ns,'faces',(f0,f1,f2),'betti',(b1,b2),'rank_d2',f2-b2)
    return vertices,index,eidx,faces2,cols,b1,b2

def top_cycle_basis_check(ns):
    vertices,vid,edge_index,faces2,cols,b1,b2=build(ns)
    tidx={f:i for i,f in enumerate(faces2)}
    basis_count=0; pivots=set()
    for M in MATCHINGS:
        groups=[]
        for pair in M:
            labels=[vid[(pair,x)] for x in itertools.product(*(range(ns[i]) for i in pair))]
            groups.append(labels)
        for a,b,c in itertools.product(*(G[1:] for G in groups)):
            terms=defaultdict(int)
            for bits in itertools.product((0,1),repeat=3):
                chosen=[ [groups[0][0],a][bits[0]], [groups[1][0],b][bits[1]], [groups[2][0],c][bits[2]] ]
                terms[tidx[tuple(sorted(chosen))]]+=(-1)**(3-sum(bits))
            boundary=defaultdict(int)
            for t,coef in terms.items():
                for e,sgn in cols[t].items():boundary[e]+=coef*sgn
            assert all(not x for x in boundary.values()),(M,a,b,c)
            pivot=tidx[tuple(sorted((a,b,c)))]
            assert terms[pivot]==1 and pivot not in pivots
            pivots.add(pivot);basis_count+=1
    assert basis_count==b2
    print('TOP_CYCLE_BASIS',ns,'integral_cycles',basis_count,'distinct_unit_pivots',len(pivots))

def fixed_trace(ns,fs):
    w={p:ns[p[0]]*ns[p[1]] for p in PAIRS}
    z={p:fs[p[0]]*fs[p[1]] for p in PAIRS}
    t1=16+2*sum(z[p]-1 for p in PAIRS)
    t2=sum(prod(z[p]-1 for p in M) for M in MATCHINGS)
    e0=sum(z.values());e1=sum(sum(z[p]*z[q] for p,q in itertools.combinations(M,2)) for M in MATCHINGS)
    e2=sum(prod(z[p] for p in M) for M in MATCHINGS)
    assert e0-e1+e2-1 ==-t1+t2
    print('TRACE_TEST',ns,fs,'H1',t1,'H2',t2)

if __name__=='__main__':
    cases=[(1,1,1,1,1,1),(2,1,1,1,1,1),(2,2,1,1,1,1),(2,2,2,1,1,1),(2,2,2,2,1,1),(2,2,2,2,2,2),(2,3,2,2,2,2)]
    for ns in cases:
        small=prod(ns)<=64
        build(ns,check_rank=small)
    for ns in [(2,1,1,1,1,1),(2,2,2,2,2,2),(2,3,2,2,2,2)]:top_cycle_basis_check(ns)
    for ns in [(2,2,2,2,2,2),(2,3,2,2,2,2)]:
        fixed_trace(ns,ns)
        for i,n in enumerate(ns):
            if n>=2:
                fs=list(ns);fs[i]-=2;fixed_trace(ns,fs)
    print('ALL_VERIFY_OK')

def sign_of_reordering(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def actual_action_check(ns, permutations):
    vertices,vid,eidx,faces2,cols,b1,b2=build(ns,check_rank=False)
    edges=sorted(eidx,key=eidx.get)
    tidx={t:i for i,t in enumerate(faces2)}
    assert len(permutations)==6
    vertex_map=[]
    for pair,choice in vertices:
        x=(permutations[pair[0]][choice[0]], permutations[pair[1]][choice[1]])
        vertex_map.append(vid[(pair,x)])
    def trchain(faces):
        total=0
        for face in faces:
            img=tuple(vertex_map[i] for i in face)
            if tuple(sorted(img))==face:total+=sign_of_reordering(img)
        return total
    t0=trchain([(i,) for i in range(len(vertices))]);t1=trchain(edges);t2=trchain(faces2)
    # Project each transformed eight-term integral cycle onto its own unit-pivot face.
    actual_H2=0
    for M in MATCHINGS:
        groups=[]
        for p in M:
            groups.append([vid[(p,x)] for x in itertools.product(*(range(ns[i]) for i in p))])
        for a,b,c in itertools.product(*(G[1:] for G in groups)):
            pivot=tuple(sorted((a,b,c)))
            coeff=0
            for bits in itertools.product((0,1), repeat=3):
                f=tuple(sorted(([groups[0][0],a][bits[0]], [groups[1][0],b][bits[1]], [groups[2][0],c][bits[2]])))
                img=tuple(vertex_map[i] for i in f)
                if tuple(sorted(img))==pivot:
                    coeff+=(-1)**(3-sum(bits))*sign_of_reordering(img)
            actual_H2+=coeff
    fixed=[sum(permutations[i][j]==j for j in range(ns[i])) for i in range(6)]
    expected_H2=sum(prod(fixed[i]*fixed[j]-1 for i,j in M) for M in MATCHINGS)
    expected_H1=2*sum(fixed[i]*fixed[j] for i,j in PAIRS)-14
    actual_H1=1+actual_H2-(t0-t1+t2)
    assert actual_H2==expected_H2,(ns,actual_H2,expected_H2)
    assert actual_H1==expected_H1,(ns,actual_H1,expected_H1)
    print('ACTUAL_ACTION',ns,'fixed',fixed,'chain_traces',(t0,t1,t2),'H1',actual_H1,'H2',actual_H2)

if __name__=='__main__':
    for ns in ((2,2,2,2,2,2),(2,3,2,2,2,2)):
        idperms=[tuple(range(n)) for n in ns]
        actual_action_check(ns,idperms)
        for i,n in enumerate(ns):
            perm=[list(range(k)) for k in ns]
            perm[i][0],perm[i][1]=perm[i][1],perm[i][0]
            actual_action_check(ns,perm)
        if ns[1]==3:
            perm=[list(range(k)) for k in ns]
            perm[1]=[1,2,0]
            actual_action_check(ns,perm)
    print('ALL_ACTIONS_OK')
