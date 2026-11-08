#!/usr/bin/env python3
"""Independent finite-field linear constraint rank test on full matrix space of linear two-local maps."""
from checker import data, apply
from random import Random

def rref_kernel(matrix,p,ncols):
    a=[[v%p for v in row] for row in matrix]
    piv=[];r=0
    for c in range(ncols):
        i=next((i for i in range(r,len(a)) if a[i][c]),None)
        if i is None:continue
        a[r],a[i]=a[i],a[r]
        inv=pow(a[r][c],-1,p);a[r]=[(u*inv)%p for u in a[r]]
        for j in range(len(a)):
            if j!=r and a[j][c]:
                z=a[j][c];a[j]=[(u-z*v)%p for u,v in zip(a[j],a[r])]
        piv.append(c);r+=1
        if r==len(a):break
    non=[j for j in range(ncols) if j not in piv]
    ker=[]
    for j in non:
        v=[0]*ncols;v[j]=1
        for i,c in enumerate(piv):v[c]=(-a[i][j])%p
        ker.append(v)
    return ker

def add_rank(basis,vec,p):
    v=vec[:]
    while True:
        i=next((i for i,a in enumerate(v) if a%p),None)
        if i is None:return False
        if i not in basis:
            inv=pow(v[i],-1,p)
            basis[i]=[(x*inv)%p for x in v]
            return True
        z=v[i];v=[(a-z*b)%p for a,b in zip(v,basis[i])]

def main(m,p,N):
    derivs,_=data(m,p);n=len(derivs[0]);n=len(derivs[0]); rng=Random(m*176+p)
    basis={};target=n*n-(len(derivs)+1); attempted=0
    def process(x,y):
        nonlocal attempted
        trans=[list(apply(d,x,p)+apply(d,y,p)) for d in derivs]
        for h in rref_kernel(trans,p,2*n):
            row=[(h[i]*x[j]+h[n+i]*y[j])%p for i in range(n) for j in range(n)]
            add_rank(basis,row,p)
        attempted+=1
    # Emphasize same quotient with different central coordinates (structural obstruction)
    for _ in range(N):
        v=[rng.randrange(p) for _ in range(m)]
        z=[rng.randrange(p) for _ in range(n-m)]
        w=[rng.randrange(p) for _ in range(n-m)]
        x=tuple(v+z);y=tuple(v+w)
        process(x,y)
        if len(basis)>=target:break
    # Additional general pairs, useful even when the first family does not fill the constraints.
    if len(basis)<target:
        for _ in range(N):
            x=tuple(rng.randrange(p) for _ in range(n));y=tuple(rng.randrange(p) for _ in range(n))
            process(x,y)
            if len(basis)>=target:break
    assert len(basis)==target,(m,p,len(basis),target)
    print(f'm={m} p={p}: independent 2-local constraints rank={len(basis)}, resulting dimension={n*n-len(basis)}, predicted={len(derivs)+1}, sampled ordered pairs={attempted}; PASS')
if __name__=='__main__':
    main(2,3,150)
    main(3,3,800)
    main(3,5,800)
    main(4,3,800)
    print('FREE_TWO_STEP_TWO_LOCAL_LINEAR_SPACE_RANK_PASS')
