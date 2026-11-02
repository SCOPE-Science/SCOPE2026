#!/usr/bin/env python3
from collections import defaultdict

def inv_mod(a,p):
    return pow(a%p,-1,p)

def rank_mod(M,p):
    A=[[(x%p) for x in row] for row in M]
    if not A: return 0
    r=0; ncol=len(A[0])
    for c in range(ncol):
        piv=next((i for i in range(r,len(A)) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        s=inv_mod(A[r][c],p)
        A[r]=[(x*s)%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]%p:
                q=A[i][c]%p
                A[i]=[(x-q*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==len(A): break
    return r

def nullspace_mod(M,p,ncols):
    if not M:
        return [[1 if i==j else 0 for i in range(ncols)] for j in range(ncols)]
    A=[[(x%p) for x in row] for row in M]
    r=0; piv=[]
    for c in range(ncols):
        q=next((i for i in range(r,len(A)) if A[i][c]%p),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        s=inv_mod(A[r][c],p); A[r]=[(x*s)%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]%p:
                z=A[i][c]%p; A[i]=[(x-z*y)%p for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
        if r==len(A): break
    free=[c for c in range(ncols) if c not in piv]
    basis=[]
    for f in free:
        v=[0]*ncols; v[f]=1
        for rr,c in enumerate(piv): v[c]=(-A[rr][f])%p
        basis.append(v)
    return basis

def edge(n,m,i,a): return (i%n,(i+a)%n)

def bd2(n,path):
    x,y,z=path
    return {(y,z):1,(x,z):-1,(x,y):1}

def add_chain(dst,src,k=1):
    for e,c in src.items():
        dst[e]=dst.get(e,0)+k*c
        if dst[e]==0: del dst[e]

def check_identities(m):
    n=2*m+1
    # Tournament property.
    for i in range(n):
        for j in range(i+1,n):
            d=(j-i)%n
            a=(1<=d<=m); b=(1<=(-d)%n<=m)
            assert a ^ b
    # Hamiltonian unit-edge cycle.
    vertex=defaultdict(int)
    for i in range(n):
        u,v=edge(n,m,i,1); vertex[v]+=1; vertex[u]-=1
    assert all(v==0 for v in vertex.values())
    # Exact chord normal form from summed 2-boundaries.
    for i in range(n):
        for a in range(2,m+1):
            bsum={}
            for t in range(a-1):
                j=(i+t)%n; length=a-t
                q=(j,(j+1)%n,(j+length)%n)
                # Both step increments are allowed and the shortcut is allowed.
                assert 1<=1<=m and 1<=length-1<=m and 1<=length<=m
                add_chain(bsum,bd2(n,q),-1)
            target={edge(n,m,i,a):1}
            for t in range(a):
                e=edge(n,m,i+t,1); target[e]=target.get(e,0)-1
                if target[e]==0: del target[e]
            assert bsum==target
    # Displacement weight vanishes on every allowed elementary 2-path boundary.
    def delta(u,v): return (v-u)%n
    for i in range(n):
        for a in range(1,m+1):
            for b in range(1,m+1):
                y=(i+a)%n; z=(i+a+b)%n
                val=delta(y,z)-delta(i,z)+delta(i,y)
                assert val==0
    return n

def h1_dim_mod_p(m,p):
    n=2*m+1
    edges=[edge(n,m,i,a) for i in range(n) for a in range(1,m+1)]
    ei={e:k for k,e in enumerate(edges)}
    paths=[(i,(i+a)%n,(i+a+b)%n) for i in range(n) for a in range(1,m+1) for b in range(1,m+1)]
    # Ω2 is the kernel of coefficients of forbidden middle-deletion pairs.
    forbidden=sorted({(x,z) for x,y,z in paths if (x,z) not in ei})
    fi={e:k for k,e in enumerate(forbidden)}
    M=[[0]*len(paths) for _ in forbidden]
    for j,(x,y,z) in enumerate(paths):
        if (x,z) in fi: M[fi[(x,z)]][j]=-1
    ker=nullspace_mod(M,p,len(paths))
    # Allowed part of d2 applied to a basis of Ω2.
    D2=[[0]*len(ker) for _ in edges]
    for col,v in enumerate(ker):
        for j,c in enumerate(v):
            if not c: continue
            x,y,z=paths[j]
            for e,s in [((y,z),1),((x,z),-1),((x,y),1)]:
                if e in ei: D2[ei[e]][col]=(D2[ei[e]][col]+c*s)%p
    r2=rank_mod(D2,p)
    D1=[[0]*len(edges) for _ in range(n)]
    for j,(u,v) in enumerate(edges): D1[u][j]=-1; D1[v][j]=1
    r1=rank_mod(D1,p)
    return len(edges)-r1-r2

def main():
    for m in range(1,13):
        n=check_identities(m)
        print(f'identities m={m} n={n}: OK')
    for p in (2,3,5):
        vals=[]
        for m in range(1,6):
            b=h1_dim_mod_p(m,p); assert b==1; vals.append(b)
        print(f'H1 dimensions mod {p}, m=1..5: {vals}')
    print('VERIFY_OK')
if __name__=='__main__': main()
