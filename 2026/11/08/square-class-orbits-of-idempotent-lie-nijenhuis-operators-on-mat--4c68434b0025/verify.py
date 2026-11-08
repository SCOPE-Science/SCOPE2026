#!/usr/bin/env python3
"""Direct finite-field verification of idempotent Lie-Nijenhuis operators on sl2.
No external dependencies. Results are exact in prime fields 3 and 5.
"""
from itertools import product, combinations
from collections import Counter


def inv(x,p):return pow(x%p,-1,p)

def rref(rows,p):
    a=[list(map(lambda x:x%p, row)) for row in rows]; n=len(a)
    if not n:return ()
    m=len(a[0]); rank=0
    for col in range(m):
        ix=next((j for j in range(rank,n) if a[j][col]),None)
        if ix is None:continue
        a[rank],a[ix]=a[ix],a[rank]
        z=inv(a[rank][col],p);a[rank]=[(v*z)%p for v in a[rank]]
        for j in range(n):
            if j==rank:continue
            c=a[j][col]
            if c:a[j]=[(x-c*y)%p for x,y in zip(a[j],a[rank])]
        rank+=1
        if rank==n:break
    return tuple(tuple(x) for x in a[:rank])

def all_subspaces(q,n,r):
    out=[]
    for piv in combinations(range(n),r):
        slots=[(i,j) for i in range(r) for j in range(piv[i]+1,n) if j not in piv]
        for vals in product(range(q),repeat=len(slots)):
            rows=[[0]*n for _ in range(r)]
            for i,c in enumerate(piv):rows[i][c]=1
            for (i,j),v in zip(slots,vals):rows[i][j]=v
            out.append(tuple(tuple(row) for row in rows))
    return out

def bracket(u,v,q):
    # x=(E,H,F); [H,E]=2E, [H,F]=-2F, [E,F]=H
    return ((2*(u[1]*v[0]-u[0]*v[1]))%q, (u[0]*v[2]-u[2]*v[0])%q, (2*(u[2]*v[1]-u[1]*v[2]))%q)

def is_lie_space(U,q):
    for a,b in combinations(U,2):
        if len(rref(U+(bracket(a,b,q),),q))>len(U):return False
    return True

def mat_prod(A,B,q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))%q for j in range(len(B[0]))) for i in range(len(A)))

def inverse(A,q):
    n=len(A); U=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        r=next((r for r in range(i,n) if U[r][i]%q),None)
        if r is None:return None
        U[i],U[r]=U[r],U[i]
        z=inv(U[i][i],q);U[i]=[v*z%q for v in U[i]]
        for j in range(n):
            if j!=i:
                z=U[j][i];U[j]=[(a-z*b)%q for a,b in zip(U[j],U[i])]
    return tuple(tuple(row[n:]) for row in U)

def projection_matrix(U,V,q):
    # U and V supplied as row-space bases; P=1 on U and 0 on V
    S=tuple(zip(*(U+V)))
    SI=inverse(S,q)
    assert SI is not None
    k=len(U);D=tuple(tuple(int(i==j and i<k) for j in range(3)) for i in range(3))
    return mat_prod(mat_prod(S,D,q),SI,q)

def mat_vec(A,u,q):return tuple(sum(a*b for a,b in zip(row,u))%q for row in A)

def nijenhuis(P,q):
    e=[(1,0,0),(0,1,0),(0,0,1)]
    for u,v in combinations(e,2):
        Nu=mat_vec(P,u,q);Nv=mat_vec(P,v,q)
        a=bracket(Nu,Nv,q)
        s=tuple((x+y)%q for x,y in zip(bracket(Nu,v,q),bracket(u,Nv,q)))
        b=mat_vec(P,tuple((x-y)%q for x,y in zip(s,mat_vec(P,bracket(u,v,q),q))),q)
        if a!=b:return False
    return True

def normal_class(U,V,q):
    # Rank-one image vector U, rank-two kernel Borel V.
    # For Borel with standard E,H basis, coefficient F=1 for U.
    if V == ((1,0,0),(0,1,0)):
        x=U[0]; assert x[2]!=0
        aa=x[1]*inv(x[2],q)%q;bb=x[0]*inv(x[2],q)%q
        d=(aa*aa+bb)%q
        return 0 if d==0 else (1 if pow(d,(q-1)//2,q)==1 else -1)
    return None

def run(q):
    sub={r:all_subspaces(q,3,r) for r in range(4)}
    assert [len(sub[r]) for r in range(4)]==[1,q*q+q+1,q*q+q+1,1]
    good2=[U for U in sub[2] if is_lie_space(U,q)]
    assert len(good2)==q+1
    rank_counts=Counter(); matrices=[]
    for r in range(4):
        for U in sub[r]:
            if not is_lie_space(U,q):continue
            for V in sub[3-r]:
                if not is_lie_space(V,q):continue
                if len(rref(U+V,q))!=3:continue
                P=projection_matrix(U,V,q)
                assert nijenhuis(P,q)
                matrices.append((r,P,U,V));rank_counts[r]+=1
    expect={0:1,1:q*q*(q+1),2:q*q*(q+1),3:1}
    assert dict(rank_counts)==expect,(rank_counts,expect)
    linecounts=Counter()
    for U in sub[1]:
        if len(rref(U+((1,0,0),(0,1,0)),q))!=3:continue
        linecounts[normal_class(U,((1,0,0),(0,1,0)),q)]+=1
    expectline={0:q,1:q*(q-1)//2,-1:q*(q-1)//2}
    assert dict(linecounts)==expectline,(linecounts,expectline)
    # All upper triangular projective transformations g=[[t,u],[0,1]]
    # act on non-Borel lines in sl2; test the classification by direct conjugation.
    orbits=[]; remaining=set(U for U in sub[1] if len(rref(U+((1,0,0),(0,1,0)),q))==3)
    def conj(g,x):
        a,b,c=x
        X=((b,a),(c,-b))
        G=((g[0],g[1]),(0,1));GI=inverse(G,q)
        Y=mat_prod(mat_prod(G,X,q),GI,q)
        return (Y[0][1]%q,Y[0][0]%q,Y[1][0]%q)
    while remaining:
        U=next(iter(remaining));out=set()
        for t in range(1,q):
            for u in range(q):out.add(rref((conj((t,u),U[0]),),q))
        assert out <= remaining
        orbits.append((len(out),normal_class(U,((1,0,0),(0,1,0)),q)))
        remaining.difference_update(out)
    assert sorted(sz for sz,_ in orbits)==sorted(expectline.values()),orbits
    # check square-class invariance and PGL2 orbit sizes via Borel times q+1.
    assert sorted((n*(q+1),c) for n,c in orbits)==sorted((n*(q+1),c) for c,n in expectline.items())
    print(f'q={q}: subspaces_2={len(sub[2])}, subalgebras_2={len(good2)}; ranks={dict(sorted(rank_counts.items()))}; total={len(matrices)}')
    print(f'q={q}: fixed-Borel square classes={dict(sorted(linecounts.items()))}; Borel-orbits={sorted(orbits)}; PGL2-rank1-orbits={sorted((n*(q+1),c) for n,c in orbits)}')

if __name__=='__main__':
    run(3);run(5)
    print('SL2_IDEMPOTENT_NIJENHUIS_DIRECT_PASS')

# Separate exhaustive 3^9 search, not relying on subalgebra enumeration.
def exhaustive_matrices_f3():
    q=3;I=((1,0,0),(0,1,0),(0,0,1));counts=Counter()
    for v in product(range(3),repeat=9):
        P=tuple(tuple(v[3*i:3*i+3]) for i in range(3))
        if mat_prod(P,P,q)!=P:continue
        if not nijenhuis(P,q):continue
        counts[len(rref(tuple(zip(*P)),q))]+=1
    assert dict(counts)=={0:1,1:36,2:36,3:1},counts
    print(f'q=3: exhaustive_3_pow_9_operator_matrices={dict(sorted(counts.items()))}')

if __name__=='__main__':
    exhaustive_matrices_f3()
