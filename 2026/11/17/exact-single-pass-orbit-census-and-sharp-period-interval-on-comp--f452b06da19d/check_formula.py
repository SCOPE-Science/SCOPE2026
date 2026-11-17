"""Independent ordered-partition and circular-word census."""
from itertools import product
from collections import Counter
from functools import lru_cache
from math import factorial

@lru_cache(None)
def stirling(n,k):
    if n==0:return int(k==0)
    if k==0:return 0
    return stirling(n-1,k-1)+k*stirling(n-1,k)


def census(parts,T):
    r=len(parts)
    a=0
    for w in product(range(r),repeat=T):
        if any(w[i]==w[(i+1)%T] for i in range(T)):continue
        k=[w.count(j) for j in range(r)]
        if any(kk==0 or kk>parts[j] for j,kk in enumerate(k)):continue
        z=1
        for j,kk in enumerate(k): z*=factorial(kk)*stirling(parts[j],kk)
        a+=z
    return a


def predicted(parts):
    m=sum(parts)
    return {T:census(parts,T) for T in range(2,m+1) if census(parts,T)}

if __name__=='__main__':
    cases=[(1,1,1),(2,1,1),(2,2,1),(2,2,2),(3,1,1),(3,2,1),(1,1,1,1),(2,1,1,1),(2,2,1,1)]
    for parts in cases:
        print('parts=',parts,'predicted=',predicted(parts))
    print('Sharp-period spectrum:')
    for parts in [(100,1,1),(8,2,1),(9,3,2),(4,4,4),(2,2,2,2),(1,1,1,1)]:
        r=len(parts);N=sum(parts);M=max(parts)
        print(parts,'all-periods',list(range(r,min(N,2*(N-M))+1)))
    print('Tripartite low periods:')
    for parts in [(2,2,2),(3,2,2),(4,3,2)]:
        print(parts,[census(parts,t) for t in range(3,min(sum(parts),6)+1)])
