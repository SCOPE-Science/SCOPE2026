"""Independent finite enumeration for elementary domains in full linear monoids.
Public scientific verification; no external dependencies.
"""
from itertools import product
from collections import defaultdict
from math import prod

def matmul(a,b,n,q):
    return tuple(sum(a[i*n+h]*b[h*n+j] for h in range(n))%q for i in range(n) for j in range(n))

def matvec(a,v,n,q):
    return tuple(sum(a[i*n+h]*v[h] for h in range(n))%q for i in range(n))

def subspace(vectors,n,q):
    return frozenset(vectors)

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-j)-1 for j in range(k))
    den=prod(q**(j+1)-1 for j in range(k))
    return num//den

def expected(n,k,c,q):
    if c<0 or c>min(k,n-k):return 0
    return gaussian(n,k,q)*gaussian(k,c,q)*gaussian(n-k,c,q)*q**((n-k-c)*(k-c))

def idempotent_expected(k,t,q):
    return sum(gaussian(t,r,q)*q**(r*(t-r)+2*r*(k-t)) for r in range(t+1))

def run(n,q):
    V=list(product(range(q),repeat=n))
    M=list(product(range(q),repeat=n*n))
    I=tuple(1 if i==j else 0 for i in range(n) for j in range(n))
    zero=(0,)*n
    by_pair={}
    by_domain={}
    actual_strata=defaultdict(int)
    for T in M:
        F=frozenset(v for v in V if matvec(T,v,n,q)==v)
        # im(T-I) = {Tv-v}
        U=frozenset(tuple((matvec(T,v,n,q)[i]-v[i])%q for i in range(n)) for v in V)
        D=frozenset(idx for idx,A in enumerate(M) if matmul(T,A,n,q)==A and matmul(A,T,n,q)==A)
        pair=(F,U)
        if pair in by_pair: assert by_pair[pair]==D
        else: by_pair[pair]=D
        if D in by_domain: assert by_domain[D]==pair
        else: by_domain[D]=pair
        k=0
        while q**k<len(F):k+=1
        assert q**k==len(F)
        c=0
        while q**c<len(F&U):c+=1
        assert q**c==len(F&U)
        assert len(D)==q**(k*k)
        actual_strata[(k,c)]+=1
    counts=defaultdict(int)
    for F,U in by_pair:
        k=0
        while q**k<len(F):k+=1
        c=0
        while q**c<len(F&U):c+=1
        counts[k,c]+=1
    assert len(by_pair)==sum(gaussian(n,k,q)**2 for k in range(n+1))
    assert len(by_domain)==len(by_pair)
    for k in range(n+1):
        for c in range(min(k,n-k)+1):
            assert counts[k,c]==expected(n,k,c,q),(n,q,k,c,counts[k,c],expected(n,k,c,q))
    # Inclusion-poset checks independently compare actual sets of matrices.
    for (F,U),D in by_pair.items():
        for (F2,U2),D2 in by_pair.items():
            assert D.issubset(D2)==(F.issubset(F2) and U2.issubset(U))
        k_rank=0
        while q**k_rank<len(F):k_rank+=1
        up=sum(1 for (F2,U2),D2 in by_pair.items() if len(F2)==q**(k_rank+1) and D.issubset(D2))
        down=sum(1 for (F2,U2),D2 in by_pair.items() if len(F2)*q==len(F) and D2.issubset(D))
        assert up == (gaussian(n-k_rank,1,q)**2 if k_rank<n else 0)
        assert down == (gaussian(k_rank,1,q)**2 if k_rank>0 else 0)
    for (F,U),D in by_pair.items():
        k=0
        while q**k<len(F):k+=1
        c=0
        while q**c<len(F&U):c+=1
        t=k-c
        idem=sum(1 for aidx in D if matmul(M[aidx],M[aidx],n,q)==M[aidx])
        assert idem==idempotent_expected(k,t,q),(n,q,k,c,idem,idempotent_expected(k,t,q))
    print('CASE_OK', 'n=',n,'q=',q,'matrices=',len(M),'distinct_domains=',len(by_domain),'strata=',dict(sorted(counts.items())))

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(2,3),(3,2)]:run(n,q)
    print('VERIFY_OK')
