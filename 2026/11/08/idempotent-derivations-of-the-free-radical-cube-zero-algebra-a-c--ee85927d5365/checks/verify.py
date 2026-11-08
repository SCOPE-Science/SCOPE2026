#!/usr/bin/env python3
"""Independent finite-field checks for idempotent derivations of the free length-three truncation.
Uses only Python's standard library; does not rely on formulas to test the GF(2) full enumeration.
"""
from itertools import product
from math import prod

def gf_mul(a,b,q):
    if q in (2,3,5):return a*b%q
    if q==4:
        aa=a; bb=b; z=0
        while bb:
            if bb&1:z^=aa
            bb>>=1; aa<<=1
            if aa&4:aa^=7
        return z
    raise ValueError(q)

def gf_add(a,b,q):return (a^b) if q==4 or q==2 else ((a+b)%q)
def gf_neg(a,q):return a if q in (2,4) else -a%q

def rank(rows,q):
    a=[list(r) for r in rows]; m=len(a); n=len(a[0]) if m else 0; t=0
    for j in range(n):
        pivot=next((i for i in range(t,m) if a[i][j]),None)
        if pivot is None:continue
        a[t],a[pivot]=a[pivot],a[t]
        if q==4:
            inv=next(i for i in (1,2,3) if gf_mul(a[t][j],i,q)==1)
        else:inv=pow(a[t][j],-1,q)
        a[t]=[gf_mul(v,inv,q) for v in a[t]]
        for i in range(m):
            if i!=t and a[i][j]:
                c=a[i][j]; a[i]=[gf_add(v,gf_neg(gf_mul(c,w,q),q),q) for v,w in zip(a[i],a[t])]
        t+=1
        if t==m:break
    return t

def gaussian(m,r,q):
    if r<0 or r>m:return 0
    # Exact integer quotient of products
    return prod(q**m-q**i for i in range(r))//prod(q**r-q**i for i in range(r))

def predicted(m,q):
    ans={}
    for r in range(m+1):
        s=m-r
        v=gaussian(m,r,q)*q**(r*s+r**3+3*r*s*s)
        ans[r]=v
    return ans

def lin_matrix_q(P,m,q):
    # Variables Q_{(ij),u}, written row-major, with rows ij, cols u.
    w=m*m; N=w*m
    L=[[gf_add(gf_mul(P[i][a],int(j==b),q),gf_mul(int(i==a),P[j][b],q),q) for a in range(m) for b in range(m)] for i in range(m) for j in range(m)]
    E=[[0]*N for _ in range(N)]
    for i in range(w):
        for j in range(m):
            row=i*m+j
            for h in range(w):E[row][h*m+j]=gf_add(E[row][h*m+j],L[i][h],q)
            for h in range(m):E[row][i*m+h]=gf_add(E[row][i*m+h],P[h][j],q)
            E[row][row]=gf_add(E[row][row],gf_neg(1,q),q)
    return E,L

def project(P,m,q):
    return all(gf_add(sum_field((gf_mul(P[i][a],P[a][j],q) for a in range(m)),q),gf_neg(P[i][j],q),q)==0 for i in range(m) for j in range(m))

def sum_field(iterable,q):
    v=0
    for x in iterable:v=gf_add(v,x,q)
    return v

def projection_fiber_check(m,q):
    rankcounts={r:0 for r in range(m+1)}
    projectioncounts={r:0 for r in range(m+1)}
    # GF(4) all P, GF(2) all P for m<=3, GF(3) m=2.
    for entries in product(range(q),repeat=m*m):
        P=[list(entries[i*m:(i+1)*m]) for i in range(m)]
        if not project(P,m,q):continue
        r=rank(P,q); s=m-r
        projectioncounts[r]+=1
        _,L=lin_matrix_q(P,m,q)
        if any(gf_add(sum_field((gf_mul(L[i][z],L[z][j],q) for z in range(m*m)),q),gf_neg(L[i][j],q),q) for i in range(m*m) for j in range(m*m)):
            continue
        E,_=lin_matrix_q(P,m,q)
        d=m*m*m-rank(E,q)
        expect=r**3+3*r*s*s
        assert d==expect,(m,q,r,d,expect)
        rankcounts[r]+=q**d
    expected=predicted(m,q) if q%2==0 else {r:(1 if r==0 else 0) for r in range(m+1)}
    assert rankcounts==expected,(m,q,rankcounts,expected)
    assert all(projectioncounts[r]==gaussian(m,r,q)*q**(r*(m-r)) for r in projectioncounts)
    return rankcounts

def full_gf2_m2():
    # 7-dimensional algebra, basis 1,x,y,xx,xy,yx,yy;
    # every choice of D(x),D(y) is tested, including possible constant terms.
    n=7
    idx={(1,1):3,(1,2):4,(2,1):5,(2,2):6}
    def mul(a,b):
        v=0
        for i in range(n):
            if (a>>i)&1:
                for j in range(n):
                    if (b>>j)&1:
                        if i==0: v^=1<<j
                        elif j==0:v^=1<<i
                        elif (i,j) in idx:v^=1<<idx[i,j]
        return v
    bases=[1<<i for i in range(n)]
    counts={0:0,1:0,2:0}; total_accepted=0
    for dx in range(1<<n):
        for dy in range(1<<n):
            D=[0,dx,dy]
            for i,j in [(1,1),(1,2),(2,1),(2,2)]:
                D.append(mul(D[i],bases[j]) ^ mul(bases[i],D[j]))
            def action(a):
                v=0
                for i in range(n):
                    if (a>>i)&1:v^=D[i]
                return v
            # Every derivation identity tested on all 49 ordered basis products.
            if any(action(mul(x,y)) != (mul(action(x),y)^mul(x,action(y))) for x in bases for y in bases):continue
            if any(action(v)!=v for v in D):continue
            total_accepted+=1
            r=rank([[(D[j]>>i)&1 for j in range(n)] for i in range(n)],2)
            # D's full rank values: r(P)=0->0; r(P)=1->3; r(P)=2->2
            inverse={0:0,3:1,2:2}
            assert r in inverse
            counts[inverse[r]]+=1
    assert total_accepted==353,(total_accepted,counts)
    assert counts==predicted(2,2),(counts,predicted(2,2))
    return counts

if __name__=='__main__':
    print('GF2_FULL_ALL_GENERATOR_IMAGES_M2',full_gf2_m2())
    for m,q in [(2,2),(2,3),(2,4),(3,2)]:
        res=projection_fiber_check(m,q)
        print('PROJECTION_AND_FIBER',f'm={m}',f'q={q}',res,'total',sum(res.values()))
    print('ALL_IDEMPOTENT_DERIVATION_CHECKS_PASS')
