#!/usr/bin/env python3
"""Exact cyclotomic and valuation verification of three-point Fourier minors.

No floating point, third-party packages, or network access. The enumerator
uses row/column translation to reduce an unordered index triple to (0,a,b).
"""
from itertools import combinations
from math import comb


def valuation(x,p,k):
    if x % (p**k) == 0:
        return k
    t=0
    while x%p==0:
        t+=1
        x//=p
    return t


def levels(R,p,k):
    vals=[valuation(b-a,p,k) for a,b in combinations(R,2)]
    return min(vals),max(vals)


def rank_by_cyclotomic(R,C,p,k):
    """Exact rank by 2-minor exponents and a 3-minor polynomial modulo Phi."""
    N=p**k
    same_all=all((b-a)*(d-c)%N==0
                 for a,b in combinations(R,2) for c,d in combinations(C,2))
    if same_all:
        return 1
    # determinant's six signed exponents, no evaluation at approximate roots
    pos=[(R[0]*C[0]+R[1]*C[1]+R[2]*C[2])%N,
         (R[0]*C[1]+R[1]*C[2]+R[2]*C[0])%N,
         (R[0]*C[2]+R[1]*C[0]+R[2]*C[1])%N]
    neg=[(R[0]*C[0]+R[1]*C[2]+R[2]*C[1])%N,
         (R[0]*C[1]+R[1]*C[0]+R[2]*C[2])%N,
         (R[0]*C[2]+R[1]*C[1]+R[2]*C[0])%N]
    counts=[0]*N
    for x in pos:counts[x]+=1
    for x in neg:counts[x]-=1
    m=N//p
    zero=all(all(counts[r+j*m]==counts[r] for j in range(1,p)) for r in range(m))
    return 2 if zero else 3


def formula_counts(p,k):
    N=p**k
    A={}
    for t in range(k):
        for u in range(t,k):
            if t==u:
                a=N*(p-1)*(p-2)*p**(2*(k-t-1))//6
            else:
                a=N*(p-1)**2*p**(2*k-t-u-2)//2
            A[t,u]=a
    assert sum(A.values())==comb(N,3)
    T={t:sum(a for (s,u),a in A.items() if s==t) for t in range(k)}
    rank1=sum(T[t]*T[s] for t in range(k) for s in range(k) if t+s>=k)
    singular=sum(a*b for (t,u),a in A.items() for (s,v),b in A.items()
                 if u+s>=k or v+t>=k)
    rank2=singular-rank1
    rank3=comb(N,3)**2-singular
    assert min(rank1,rank2,rank3)>=0
    return (rank1,rank2,rank3)


def direct_counts(p,k):
    N=p**k
    indices=list(combinations(range(1,N),2))
    raw=[0,0,0,0]
    for a,b in indices:
        R=(0,a,b)
        t,u=levels(R,p,k)
        for c,d in indices:
            C=(0,c,d)
            s,v=levels(C,p,k)
            pred=(1 if t+s>=k else 2 if u+s>=k or v+t>=k else 3)
            actual=rank_by_cyclotomic(R,C,p,k)
            assert pred==actual, (p,k,R,C,pred,actual)
            raw[actual]+=1
    # For each pair (R,C), the normalized representation with 0 as
    # an index occurs 9/N^2 times, counting the 3 choices of anchor on
    # each side. Consequently each rank's full count is N^2/9 * raw.
    out=[]
    for n in raw[1:]:
        assert n*N*N%9==0
        out.append(n*N*N//9)
    return tuple(out)


def main():
    tests=[(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(5,2),(7,1)]
    for p,k in tests:
        predicted=formula_counts(p,k)
        actual=direct_counts(p,k)
        assert actual==predicted,(p,k,actual,predicted)
        print('p=%d k=%d N=%d ranks=(%d,%d,%d) MATCH' %
              (p,k,p**k,*actual),flush=True)
    for p,k in [(3,4),(5,3),(7,3),(11,4)]:
        print('formula-only p=%d k=%d N=%d ranks=%r' %
              (p,k,p**k,formula_counts(p,k)),flush=True)
    print('PRIME_POWER_TRIPLE_FOURIER_EXACT_CHECKS_PASS')


if __name__=='__main__':
    main()
