#!/usr/bin/env python3
"""Check relative cellular chain ranks of the symmetric square of small finite graphs."""
from itertools import combinations_with_replacement, combinations
from sympy import Matrix

def rank_mod(A,p):
    m=[[(int(x)%p) for x in row] for row in A.tolist()]
    r=0
    for j in range(A.cols):
        pivot=next((i for i in range(r,A.rows) if m[i][j]),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r]
        inv=pow(m[r][j],-1,p)
        m[r]=[x*inv%p for x in m[r]]
        for i in range(A.rows):
            if i!=r and m[i][j]:
                a=m[i][j];m[i]=[(u-a*v)%p for u,v in zip(m[i],m[r])]
        r+=1
        if r==A.rows:break
    return r

def test(vs,edges, label):
    # Use arbitrary simple graph, edges oriented increasingly.
    edges=[tuple(sorted(e)) for e in edges]
    c0=list(combinations(vs,2))
    c1=[(v,k) for v in vs for k in range(len(edges))]
    c2=[('triangle',i) for i in range(len(edges))]+[('square',i,j) for i in range(len(edges)) for j in range(i+1,len(edges))]
    idx0={x:i for i,x in enumerate(c0)};idx1={x:i for i,x in enumerate(c1)}
    B1=Matrix.zeros(len(c0),len(c1));B2=Matrix.zeros(len(c1),len(c2))
    for (v,k),j in idx1.items():
        a,b=edges[k]
        for sign,z in [(-1,a),(1,b)]:
            if v!=z:B1[idx0[tuple(sorted((v,z)))],j]+=sign
    for j,(typ,*args) in enumerate(c2):
        if typ=='triangle':
            a,b=edges[args[0]]
            B2[idx1[(a,args[0])],j]+=1
            B2[idx1[(b,args[0])],j]+=1
        else:
            k,l=args;a,b=edges[k];c,d=edges[l]
            for v,el,sign in [(b,l,1),(a,l,-1),(d,k,-1),(c,k,1)]:
                B2[idx1[(v,el)],j]+=sign
    assert B1*B2==Matrix.zeros(len(c0),len(c2))
    n=len(vs); e=len(edges);r=e-n+1
    rq1=B1.rank();rq2=B2.rank()
    r2=len(c2)-rq2
    r1=len(c1)-rq1-rq2
    assert r1==0 and r2==r*(r-1)//2,(label,r1,r2,r)
    rp1=rank_mod(B1,2);rp2=rank_mod(B2,2)
    h1p=len(c1)-rp1-rp2
    assert h1p==r,(label,h1p,r)
    print(label, 'cycle rank',r,'chain dims',(len(c0),len(c1),len(c2)),'rational H2',r2,'mod2 H1',h1p)

if __name__=='__main__':
    test(list(range(4)),[(0,1),(1,2),(2,3)],'path4')
    test(list(range(3)),[(0,1),(1,2),(0,2)],'cycle3')
    test(list(range(4)),[(0,1),(1,2),(2,3),(0,3)],'cycle4')
    test(list(range(5)),[(0,1),(1,2),(0,2),(0,3),(3,4),(0,4)],'two triangles wedge')
    test(list(range(4)),list(combinations(range(4),2)),'complete K4')
    test(list(range(5)),list(combinations(range(5),2)),'complete K5')

def trace_test(vs,edges,perm,label):
    """Independent signed cellular Lefschetz test for a graph automorphism."""
    edges=[tuple(sorted(e)) for e in edges]
    index={e:i for i,e in enumerate(edges)}
    assert sorted(perm[v] for v in vs)==sorted(vs)
    def image_edge(k):
        a,b=edges[k]; x,y=perm[a],perm[b]
        e=tuple(sorted((x,y)))
        assert e in index
        return index[e],(1 if x<y else -1)
    # C0 diagonal removed: a two-element vertex subset is fixed by perm.
    c0=sum(1 for a,b in combinations(vs,2) if {perm[a],perm[b]}=={a,b})
    c1=0
    for v in vs:
        for k in range(len(edges)):
            t,s=image_edge(k)
            if perm[v]==v and t==k:c1+=s
    c2=0
    for k in range(len(edges)):
        t,s=image_edge(k)
        if t==k:c2+=s
    for k,l in combinations(range(len(edges)),2):
        t,st=image_edge(k);u,su=image_edge(l)
        if {t,u}=={k,l}:c2+=st*su*(1 if t<u else -1)
    lef=c0-c1+c2
    # Homological trace on H1 of the graph: L_graph = tr C0 - tr C1 = 1 - tr H1.
    vfixed=sum(perm[v]==v for v in vs)
    efix=sum(s for k in range(len(edges)) for j,s in [image_edge(k)] if j==k)
    a=1-(vfixed-efix)
    perm2={v:perm[perm[v]] for v in vs}
    efix2=sum((1 if perm2[x]<perm2[y] else -1) for x,y in edges if tuple(sorted((perm2[x],perm2[y]))) in index and tuple(sorted((perm2[x],perm2[y])))==(x,y))
    a2=1-(sum(perm2[v]==v for v in vs)-efix2)
    expect=(a*a-a2)//2
    assert lef==expect,(label,lef,expect,'trH1',a,a2,'chains',c0,c1,c2)
    print(label,'relative Lefschetz',lef,'exterior square trace',expect)

if __name__=='__main__':
    # Cycle reflection / rotations: second BM homology is absent.
    trace_test(list(range(5)),[(i,(i+1)%5) for i in range(5)],{i:(-i)%5 for i in range(5)},'pentagon reflection')
    trace_test(list(range(5)),[(i,(i+1)%5) for i in range(5)],{i:(i+1)%5 for i in range(5)},'pentagon rotation')
    # Two triangular petals swapped about their common point: determinant -1 on cycles.
    tt=[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]
    trace_test(list(range(5)),tt,{0:0,1:3,2:4,3:1,4:2},'two-petal swap')
    trace_test(list(range(5)),tt,{0:0,1:2,2:1,3:3,4:4},'single petal reflection')
    # Symmetric complete-graph examples.
    kk=list(combinations(range(4),2))
    trace_test(list(range(4)),kk,{0:1,1:0,2:2,3:3},'K4 transposition')
    trace_test(list(range(4)),kk,{0:1,1:2,2:0,3:3},'K4 3-cycle')

if __name__=='__main__':
    from sympy.matrices.normalforms import smith_normal_form
    from sympy.polys.domains import ZZ
    def torsion_test(vs,edges,label):
        edges=[tuple(sorted(e)) for e in edges]
        c1={(v,k):i for i,(v,k) in enumerate((v,k) for v in vs for k in range(len(edges)))}
        c2=[('triangle',k) for k in range(len(edges))]+[('square',k,l) for k,l in combinations(range(len(edges)),2)]
        B2=Matrix.zeros(len(c1),len(c2))
        for j,(typ,*p) in enumerate(c2):
            if typ=='triangle':
                a,b=edges[p[0]]
                B2[c1[(a,p[0])],j]+=1; B2[c1[(b,p[0])],j]+=1
            else:
                k,l=p;a,b=edges[k];c,d=edges[l]
                for v,ei,sign in [(b,l,1),(a,l,-1),(d,k,-1),(c,k,1)]:
                    B2[c1[(v,ei)],j]+=sign
        S=smith_normal_form(B2,domain=ZZ)
        nonunit=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if abs(int(S[i,i]))>1]
        rank1=len(edges)-len(vs)+1
        assert nonunit==[2]*rank1,(label,nonunit,rank1)
        print(label,'integral first-homology torsion Smith factors:',nonunit)
    torsion_test(list(range(4)),[(0,1),(1,2),(2,3),(0,3)],'C4')
    torsion_test(list(range(5)),[(0,1),(1,2),(0,2),(0,3),(3,4),(0,4)],'double triangle')
    torsion_test(list(range(4)),list(combinations(range(4),2)),'K4')
    torsion_test(list(range(5)),list(combinations(range(5),2)),'K5')
    print('VERIFY_OK')
