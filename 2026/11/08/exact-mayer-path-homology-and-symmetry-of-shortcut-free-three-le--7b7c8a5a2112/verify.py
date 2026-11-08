#!/usr/bin/env python3
"""Exact finite-field check of Mayer chain formulas for three-level feedforward digraphs.
Only standard-library arithmetic is used. This test is corroborative, not an infinite proof.
"""
from itertools import product
P=2521
GEN=17  # a primitive root modulo the prime 2521


def rank(matrix,p=P):
    if not matrix:return 0
    m=[list(map(lambda x:x%p,row)) for row in matrix]
    h=len(m); w=len(m[0]); r=0
    for j in range(w):
        pivot=next((i for i in range(r,h) if m[i][j]),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r]
        z=pow(m[r][j],-1,p)
        m[r]=[(z*x)%p for x in m[r]]
        for i in range(r+1,h):
            z=m[i][j]
            if z:m[i]=[(u-z*v)%p for u,v in zip(m[i],m[r])]
        r+=1
        if r==h:break
    return r


def matmul(a,b):
    h=len(a); s=len(b); w=len(b[0]) if s else 0
    assert not s or len(a[0])==s
    return [[sum(a[i][k]*b[k][j] for k in range(s))%P for j in range(w)]for i in range(h)]


def check(a,b,c,N):
    assert 2520%N==0
    xi=pow(GEN,2520//N,P)
    assert pow(xi,N,P)==1 and all(pow(xi,j,P)!=1 for j in range(1,N))
    A=range(a);B=range(a,a+b);C=range(a+b,a+b+c)
    vs=list(A)+list(B)+list(C)
    edges=[(u,v) for u in A for v in B]+[(u,v) for u in B for v in C]
    tris=[(u,v,w) for u in A for v in B for w in C]
    forbidden=[(u,w) for u in A for w in C]
    di={v:i for i,v in enumerate(vs)}
    ei={e:i for i,e in enumerate(edges)}
    fi={f:i for i,f in enumerate(forbidden)}
    D1=[[0]*len(edges) for _ in vs]
    for j,(u,v) in enumerate(edges):
        D1[di[u]][j]=xi
        D1[di[v]][j]=1
    # D0 missing-chord matrix: check invariant basis via direct equality.
    F=[[0]*len(tris) for _ in forbidden]
    for j,(u,v,w) in enumerate(tris):F[fi[u,w]][j]=xi
    rF=rank(F)
    assert rF==a*c
    # Each vector e_{u,v,w} - e_{u,b0,w} is a genuine allowed 2-path combination.
    zbase=list(B)[0]
    columns=[]
    for u in A:
        for w in C:
            for v in B:
                if v==zbase:continue
                columns.append(((u,v,w),(u,zbase,w)))
    D2=[[0]*len(columns) for _ in edges]
    for col,(plus,minus) in enumerate(columns):
        for sg,tri in ((1,plus),(-1,minus)):
            u,v,w=tri
            assert (u,v) in ei and (v,w) in ei
            D2[ei[v,w]][col]=(D2[ei[v,w]][col]+sg)%P
            D2[ei[u,v]][col]=(D2[ei[u,v]][col]+sg*xi*xi)%P
    assert len(columns)==a*c*(b-1)==len(tris)-rF
    D20=matmul(D1,D2)
    r1=rank(D1);r2=rank(D2);r20=rank(D20)
    assert r1==a+b+c-1
    assert r2==(a+c-1)*(b-1)
    assert r20==(0 if N==2 else b-1)
    if N==2:assert all(not x for row in D20 for x in row)
    E=len(edges);V=len(vs);F2=len(columns)
    theoretical0={1:1,2:a+c+1}
    expected2={1:(a-1)*(b-1)*(c-1),2:(a*c-1)*(b-1)}
    for q in range(1,N):
        t=N-q
        b0=V-(r1 if t==1 else r20 if t==2 else 0)
        b1=E-(r1 if q==1 else 0)-(r2 if t==1 else 0)
        b2=F2-(r2 if q==1 else r20 if q==2 else 0)
        e0=theoretical0.get(t,V)
        if N==2:e1=0
        elif q==1:e1=(b-1)*(a+c-1)
        elif t==1:e1=V-1
        else:e1=E
        e2=expected2.get(q,F2)
        assert (b0,b1,b2)==(e0,e1,e2),(a,b,c,N,q,(b0,b1,b2),(e0,e1,e2))
    return r1,r2,r20,len(columns)


def characters(a,b,c,N,perms):
    xi=pow(GEN,2520//N,P)
    A=list(range(a)); B=list(range(a,a+b)); C=list(range(a+b,a+b+c))
    vs=A+B+C
    edges=[(u,v) for u in A for v in B]+[(u,v) for u in B for v in C]
    b0=B[0]
    basis=[(u,v,w) for u in A for w in C for v in B if v!=b0]
    ei={e:i for i,e in enumerate(edges)}
    bi={e:i for i,e in enumerate(basis)}
    V=len(vs); E=len(edges); F=len(basis)
    D1=[[0]*E for _ in range(V)]; D2=[[0]*F for _ in range(E)]
    for j,(u,v) in enumerate(edges):D1[u][j]=xi; D1[v][j]=1
    for j,(u,v,w) in enumerate(basis):
        D2[ei[v,w]][j]=(D2[ei[v,w]][j]+1)%P
        D2[ei[b0,w]][j]=(D2[ei[b0,w]][j]-1)%P
        D2[ei[u,v]][j]=(D2[ei[u,v]][j]+xi*xi)%P
        D2[ei[u,b0]][j]=(D2[ei[u,b0]][j]-xi*xi)%P
    D20=matmul(D1,D2)
    for pa,pb,pc in perms:
        perm=list(range(V))
        for part,flag in ((A,pa),(B,pb),(C,pc)):
            if flag:perm[part[0]],perm[part[1]]=perm[part[1]],perm[part[0]]
        assert all(perm[perm[i]]==i for i in range(V))
        T0=[[0]*V for _ in range(V)]
        T1=[[0]*E for _ in range(E)]
        T2=[[0]*F for _ in range(F)]
        for j in range(V):T0[perm[j]][j]=1
        for j,(u,v) in enumerate(edges):T1[ei[perm[u],perm[v]]][j]=1
        for j,(u,v,w) in enumerate(basis):
            u2,v2,w2=perm[u],perm[v],perm[w]
            b2=perm[b0]
            if v2!=b0:T2[bi[u2,v2,w2]][j]=(T2[bi[u2,v2,w2]][j]+1)%P
            if b2!=b0:T2[bi[u2,b2,w2]][j]=(T2[bi[u2,b2,w2]][j]-1)%P
        def tr(t):return sum(t[i][i] for i in range(len(t)))%P
        def image_trace(t,D):
            hh=len(t);ww=len(D[0]) if D else 0
            plus=[[(D[i][j]+sum(t[i][k]*D[k][j] for k in range(hh)))%P for j in range(ww)] for i in range(hh)]
            minus=[[(D[i][j]-sum(t[i][k]*D[k][j] for k in range(hh)))%P for j in range(ww)] for i in range(hh)]
            return (rank(plus)-rank(minus))%P
        ch0,ch1,ch2=tr(T0),tr(T1),tr(T2)
        im1,im2,im20=image_trace(T0,D1),image_trace(T1,D2),image_trace(T0,D20)
        fA=a-2*pa;fB=b-2*pb;fC=c-2*pc
        uA=fA-1;uB=fB-1;uC=fC-1
        for q in range(1,N):
            t=N-q
            h0=ch0-(im1 if t==1 else im20 if t==2 else 0)
            h1=ch1-(im1 if q==1 else 0)-(im2 if t==1 else 0)
            h2=ch2-(im2 if q==1 else im20 if q==2 else 0)
            e0={1:1,2:1+fA+fC}.get(t,fA+fB+fC)
            if N==2:e1=0
            elif q==1:e1=uB*(1+uA+uC)
            elif t==1:e1=fA+fB+fC-1
            else:e1=fA*fB+fB*fC
            e2={1:uA*uB*uC,2:uB*(fA*fC-1)}.get(q,fA*uB*fC)
            assert (h0%P,h1%P,h2%P)==(e0%P,e1%P,e2%P),(a,b,c,N,pa,pb,pc,q,(h0,h1,h2),(e0,e1,e2))


def main():
    examples=[(2,2,2),(2,3,2),(3,2,4),(2,4,3),(3,3,3),(1,4,2),(4,1,3),(4,4,4)]
    k=0
    for sizes in examples:
        for N in range(2,11):
            check(*sizes,N)
            k+=1
    for sizes in [(2,3,2),(3,3,3),(2,2,4)]:
        for N in [2,3,4,5,6]:
            characters(*sizes,N,list(product([0,1],repeat=3)))
    print(f'ALL_VERIFY_OK cases={k} primitive_orders=2..10 graph_sizes={len(examples)} exact_field={P} ranks_all_indices_and_symmetry_characters=verified')
if __name__=='__main__':main()
