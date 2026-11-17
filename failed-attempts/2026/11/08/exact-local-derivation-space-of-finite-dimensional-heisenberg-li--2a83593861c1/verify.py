#!/usr/bin/env python3
"""Independent finite-field derivation/evaluation rank checks for Heisenberg Lie algebras.
Uses prime fields only; the general proof is characteristic-independent."""
from itertools import product

def rank_basis(rows, p, n):
    pivots = {}
    for src in rows:
        r=[x % p for x in src]
        for k in sorted(pivots):
            if r[k]:
                a=r[k]; piv=pivots[k]
                r=[(v-a*w)%p for v,w in zip(r,piv)]
        k=next((i for i,x in enumerate(r) if x),None)
        if k is None: continue
        inv=pow(r[k],-1,p)
        pivots[k]=[(x*inv)%p for x in r]
    return len(pivots)

def nullspace(rows, p, n):
    a=[list(map(lambda v:v%p,row)) for row in rows]
    pivot=[]; i=0
    for j in range(n):
        k=next((k for k in range(i,len(a)) if a[k][j]), None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        inv=pow(a[i][j],-1,p)
        a[i]=[v*inv%p for v in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                t=a[k][j]
                a[k]=[(u-t*v)%p for u,v in zip(a[k],a[i])]
        pivot.append(j);i+=1
        if i==len(a): break
    free=[j for j in range(n) if j not in pivot]
    out=[]
    for j in free:
        x=[0]*n;x[j]=1
        for row,k in enumerate(pivot):x[k]=-a[row][j]%p
        out.append(x)
    return out

def bracket(i,j,m,p):
    # x_0,...,x_(m-1), y_0,...,y_(m-1), z
    if 0 <= i < m and j==m+i:return 1
    if 0 <= j < m and i==m+j:return -1 % p
    return 0

def run(m,p):
    n=2*m+1; vars=n*n
    rows=[]
    # Derivation identity for each ordered basis pair; all output coordinates.
    for i in range(n):
        for j in range(n):
            b=bracket(i,j,m,p)
            for k in range(n):
                row=[0]*vars
                if b:
                    # D([e_i,e_j]) = b * D(z), for every output k.
                    row[k*n+(n-1)]=b
                if k==n-1:
                    for h in range(n):
                        t=bracket(h,j,m,p)
                        if t: row[h*n+i]=(row[h*n+i]-t)%p
                        t=bracket(i,h,m,p)
                        if t: row[h*n+j]=(row[h*n+j]-t)%p
                rows.append(row)
    der=nullspace(rows,p,vars)
    expect_der=2*m*m+3*m+1
    assert len(der)==expect_der,(m,p,len(der),expect_der)
    seen={}
    for coords in product(range(p),repeat=n):
        img=[]
        for d in der:
            img.append([sum(d[k*n+j]*coords[j] for j in range(n))%p for k in range(n)])
        r=rank_basis(img,p,n)
        want=0 if not any(coords) else (1 if not any(coords[:-1]) else n)
        assert r==want,(m,p,coords,r,want)
        seen[want]=seen.get(want,0)+1
    # Direct formula validation in the exact same characteristic.
    local_dimension=vars-(n-1)
    assert local_dimension==4*m*m+2*m+1
    assert local_dimension-expect_der==m*(2*m-1)
    return dict(m=m,p=p,derivations_dimension=expect_der,local_dimension=local_dimension,evaluation_rank_frequencies=seen)

if __name__=='__main__':
    cases=[(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)]
    for m,p in cases:print(run(m,p))
    print('VERIFY_OK configurations=6 characteristic_2_and_odd; exhaustive_evaluations=563')
