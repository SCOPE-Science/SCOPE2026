"""Direct subspace enumeration for the standard filiform Lie algebra."""
from itertools import combinations, product
from math import prod
import json, sys


def gaussian(n,k,q):
    if k<0 or k>n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def subspaces(n,q):
    for d in range(n+1):
        for piv in combinations(range(n), d):
            slots=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
            for values in product(range(q), repeat=len(slots)):
                B=[[0]*n for _ in piv]
                for i,p in enumerate(piv):B[i][p]=1
                for (i,j),v in zip(slots,values):B[i][j]=v
                yield tuple(tuple(v) for v in B)

def rref(rows,q):
    if not rows:return ()
    r=[list(v) for v in rows]
    n=len(r[0]); pivot=0
    for col in range(n):
        found=next((idx for idx in range(pivot,len(r)) if r[idx][col]%q),None)
        if found is None:continue
        r[pivot],r[found]=r[found],r[pivot]
        fac=pow(r[pivot][col]%q,-1,q)
        r[pivot]=[(x*fac)%q for x in r[pivot]]
        for idx in range(len(r)):
            if idx==pivot:continue
            fac=r[idx][col]%q
            if fac:r[idx]=[(a-fac*b)%q for a,b in zip(r[idx],r[pivot])]
        pivot+=1
        if pivot==len(r):break
    return tuple(tuple(x) for x in r[:pivot])

def bracket(a,b,q):
    n=len(a)
    c=[0]*n
    for j in range(2,n):c[j]=(a[0]*b[j-1]-b[0]*a[j-1])%q
    return tuple(c)

def subalg(B,q):
    for i in range(len(B)):
        for j in range(i+1,len(B)):
            v=bracket(B[i],B[j],q)
            if len(rref((*B,v),q))>len(B):return False
    return True

def theoretical(m,q):
    G=sum(gaussian(m,d,q) for d in range(m+1))
    B=sum(q**(m-j) for j in range(m+1))
    R=sum(q**(m-j)*sum(sum(gaussian(j,s,q)*q**((ell-j)*(j-s)) for s in range(j+1)) for ell in range(j,m+1)) for j in range(m+1))
    Q=1+sum((2*u-1)*q**(u+1)+2*q**u for u in range(1,m+1))
    P=G*G+2*R+Q
    return {'G':G,'B':B,'R':R,'Q':Q,'T':G+B,'P':P}

def direct(n,q):
    cand=list(subspaces(n,q))
    A=[x for x in cand if subalg(x,q)]
    count=0
    nA=len(A)
    for i,X in enumerate(A):
        for Y in A:
            Z=rref(X+Y,q)
            if subalg(Z,q):count+=1
    th=theoretical(n-1,q)
    assert nA==th['T'],(n,q,nA,th)
    assert count==th['P'],(n,q,count,th)
    return {'n':n,'q':q,'ambient_subspaces':len(cand),'subalgebras':nA,'permuting_ordered_pairs':count,'theoretical_parts':th}

if __name__=='__main__':
    tests=[(3,2),(4,2),(5,2),(6,2),(3,3),(4,3),(5,3),(3,5),(4,5)]
    print('FILIFORM_SUBALGEBRA_PERMUTABILITY_DIRECT_PASS')
    for n,q in tests:
        r=direct(n,q)
        print(json.dumps(r,sort_keys=True,separators=(',',':')))
    print('ALL_CASES_PASS')
