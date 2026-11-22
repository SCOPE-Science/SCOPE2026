#!/usr/bin/env python3
"""Independent finite-field checks for endomorphisms of a 3D evolution algebra."""
from itertools import product
from collections import Counter


def mul(a,b,p,lam):
    # Basis u=e1+e3, v=e2+e3, w=e3; structure constants.
    u = (a[0]*b[1]+a[1]*b[0]+a[0]*b[2]+a[2]*b[0]-a[1]*b[1]
         +a[1]*b[2]+a[2]*b[1]+a[2]*b[2]) % p
    v = (lam*a[1]*b[1]) % p
    return (u,v,0)

def rank(cols,p):
    a=[[cols[c][r]%p for c in range(3)] for r in range(3)]
    n=0
    for c in range(3):
        pivot=next((i for i in range(n,3) if a[i][c]%p), None)
        if pivot is None:continue
        a[n],a[pivot]=a[pivot],a[n]
        inv=pow(a[n][c],-1,p)
        a[n]=[x*inv%p for x in a[n]]
        for i in range(3):
            if i==n:continue
            factor=a[i][c]
            a[i]=[(a[i][j]-factor*a[n][j])%p for j in range(3)]
        n+=1
    return n

def valid(cols,p,lam):
    bas=[(1,0,0),(0,1,0),(0,0,1)]
    for i in range(3):
        for j in range(i,3):
            x=mul(bas[i],bas[j],p,lam)
            lhs=tuple(sum(x[k]*cols[k][r] for k in range(3))%p for r in range(3))
            rhs=mul(cols[i],cols[j],p,lam)
            if lhs!=rhs:return False
    return True

def candidates(p,lam):
    # Normal-form FAMILY, all parameters checked against original multiplication.
    zero=(0,0,0)
    out=set()
    # Branch (T|E^2)=0
    for a in range(p):
        for r in range(p):
            if r*(2*a+r)%p==0:
                out.add((zero,zero,(a,0,r)))
    # Branch T(v)=c u + v
    for c in range(p):
        a=(1+(lam-2)*c)%p
        for p0 in range(p):
            for r in range(p):
                if a*(r-1)%p==0 and (c*r+p0+r-a)%p==0 and (2*p0*r+r*r-a)%p==0:
                    out.add(((a,0,0),(c,1,0),(p0,0,r)))
    return out

def predicted(p,lam):
    if p==2:return Counter({0:1,1:p,3:1})
    if lam==2:return Counter({0:1,1:2*p-2,3:1})
    if lam==4%p:return Counter({0:1,1:2*p-1,2:p-1,3:p-1})
    return Counter({0:1,1:2*p-1,3:1})

def main():
    checks=0
    for p in [2,3,5,7,11]:
        for lam in range(1,p):
            cand=candidates(p,lam)
            assert all(valid(c,p,lam) for c in cand),(p,lam,'candidate invalid')
            observed=Counter(rank(c,p) for c in cand)
            assert observed==predicted(p,lam),(p,lam,observed,predicted(p,lam))
            if p<=3:
                # Full 9-coordinate search, does not use classification assumptions.
                every=set()
                for vec in product(range(p),repeat=9):
                    cols=tuple(tuple(vec[3*i+j] for j in range(3)) for i in range(3))
                    if valid(cols,p,lam):every.add(cols)
                assert every==cand,(p,lam,len(every),len(cand))
            checks+=1
    print('VERIFY_OK',checks,'prime-field parameters; exhaustive all 3x3 maps for p=2,3')
if __name__=='__main__':main()
