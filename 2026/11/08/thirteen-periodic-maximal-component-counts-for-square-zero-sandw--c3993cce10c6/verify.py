#!/usr/bin/env python3
"""Direct finite-field checks for the idempotent/square-zero sandwich relation.
No dependencies beyond the Python standard library.
"""
from itertools import product
from collections import Counter
from math import prod

def mul(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))

def rank(a,n,q):
    m=[list(a[i*n:(i+1)*n]) for i in range(n)]
    rr=0
    for col in range(n):
        pivot=next((i for i in range(rr,n) if m[i][col]%q),None)
        if pivot is None: continue
        m[rr],m[pivot]=m[pivot],m[rr]
        inv=pow(m[rr][col],-1,q)
        m[rr]=[(inv*v)%q for v in m[rr]]
        for i in range(n):
            if i!=rr:
                v=m[i][col]
                m[i]=[(m[i][j]-v*m[rr][j])%q for j in range(n)]
        rr+=1
    return rr

def qbinom(a,b,q):
    if b<0 or b>a:return 0
    b=min(b,a-b)
    num=den=1
    for i in range(b):
        num*=q**(a-i)-1
        den*=q**(b-i)-1
    return num//den

def gl(h,q):return prod(q**h-q**i for i in range(h))

def predicted(n,q):
    out=Counter()
    for h in range(n//2+1):
        ns=qbinom(n,h,q)*qbinom(n-h,h,q)*gl(h,q)
        for r in range(n-h+1):
            for t in range(min(h,r)+1):
                count=(ns*qbinom(h,t,q)*qbinom(n-h-t,r-t,q)
                       *q**(t*(n-h)+r*(n-r-t)))
                if count:out[r,h,t]=count
    return out

def direct(n,q):
    zero=(0,)*(n*n)
    universe=product(range(q),repeat=n*n)
    proj=[];nil=[]
    for a in universe:
        aa=mul(a,a,n,q)
        if aa==a:proj.append((a,rank(a,n,q)))
        if aa==zero:nil.append((a,rank(a,n,q)))
    counts=Counter()
    for p,r in proj:
        for x,h in nil:
            np=mul(x,p,n,q)
            if mul(p,np,n,q)==zero:
                counts[r,h,rank(np,n,q)]+=1
    return counts,len(proj),len(nil)

def dim(n,h,r,t):
    return 2*h*(n-h)+2*r*(n-r)-h*r+h*t-t*t

def extrema(n):
    mx=-1;opt=[]
    for h in range(n//2+1):
        for r in range(n-h+1):
            for t in range(min(h,r)+1):
                d=dim(n,h,r,t)
                if d>mx:mx=d;opt=[(r,h,t)]
                elif d==mx:opt.append((r,h,t))
    return mx,sorted(opt)


def residue_certificate():
    """Exact small-lattice search justified by the completed-square bounds."""
    expected=(
        ((0,0,0),),
        ((0,0,0),(0,1,0),(0,1,1),(1,0,0)),
        ((1,1,0),(1,1,1)),
        ((1,1,0),(1,1,1),(1,2,1)),
        ((1,2,1),(2,2,1)),
        ((2,2,1),),
        ((2,3,1),(2,3,2)),
        ((3,3,1),(3,3,2)),
        ((3,4,2),),
        ((3,4,2),(4,4,2)),
        ((4,4,2),(4,5,2),(4,5,3)),
        ((4,5,2),(4,5,3)),
        ((4,6,3),(5,5,2),(5,5,3),(5,6,3))
    )
    for s in range(13):
        optimum=[]
        for r in range((5*s)//13,(5*s)//13+2):
            for h in range((6*s)//13,(6*s)//13+2):
                for t in range((3*s)//13-1,(3*s)//13+3):
                    # Check 13 times the exact completed-square residual.
                    if 11*s*s-13*dim(s,h,r,t)==(11*s*s)%13:
                        optimum.append((r,h,t))
        assert tuple(sorted(optimum))==expected[s],(s,optimum)
    print('EXACT_THIRTEEN_RESIDUE_CERTIFICATE_PASS')

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(3,2),(1,3),(2,3),(2,5)]:
        actual,pc,nc=direct(n,q)
        target=predicted(n,q)
        assert actual==target, (n,q,actual-target,target-actual)
        print(f'DIRECT_PASS n={n} q={q} idempotents={pc} square_zero={nc} cells={len(actual)} pairs={sum(actual.values())}')
    residue_certificate()
    period=[1,4,2,3,2,1,2,2,1,2,3,2,4] # residues 0..12 at n >=13
    for n in range(1,60):
        d,opts=extrema(n)
        assert d==11*n*n//13,(n,d)
        if n>=13:assert len(opts)==period[n%13],(n,len(opts),period[n%13])
    print('DIMENSION_AND_COMPONENT_PERIOD_PASS n=1..59')
    print('SANDWICH_IDEMPOTENT_SQUARE_ZERO_DIRECT_CHECK_PASS')
