#!/usr/bin/env python3
"""Exact rational checks for sharp fourth moments of fixed-rank signed rook matrices."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from random import Random


def signed_rooks(n,k):
    for rows in combinations(range(n), k):
        for cols in combinations(range(n), k):
            for target in permutations(cols):
                for signs in product((-1,1), repeat=k):
                    yield tuple((rows[i],target[i],signs[i]) for i in range(k))


def moments_direct(A,k):
    n=len(A)
    total=0
    sm2=sm4=0
    for M in signed_rooks(n,k):
        y=sum(A[i][j]*e for i,j,e in M)
        sm2+=y*y
        sm4+=y**4
        total+=1
    return Q(sm2,total),Q(sm4,total)


def moments_formula(A,k):
    n=len(A)
    b=[[v*v for v in row] for row in A]
    s=sum(map(sum,b));u=sum(x*x for row in b for x in row)
    d=(s*s-sum(t*t for t in map(sum,b))-sum(sum(b[i][j] for i in range(n))**2 for j in range(n))+u)//2
    e2=Q(k,n*n)*s
    e4=Q(k,n*n)*u +Q(6*k*(k-1),n*n*(n-1)**2)*d
    return e2,e4


def H(x,n,k):
    q=Q(3*(k-1),(n-1)**2)
    T=sum(v*v for row in x for v in row)
    D=(1-sum(sum(row)**2 for row in x)-sum(sum(x[i][j] for i in range(n))**2 for j in range(n))+T)/2
    return T+2*q*D


def project(x):
    n=len(x)
    r=[sum(row) for row in x]
    c=[sum(x[i][j] for i in range(n)) for j in range(n)]
    Z=[[x[i][j]-(r[i]+c[j])/n+Q(1,n*n) for j in range(n)] for i in range(n)]
    return r,c,Z


def lower_certificate(x,n,k):
    q=Q(3*(k-1),(n-1)**2)
    h=H(x,n,k)
    r,c,z=project(x)
    norm_z=sum(t*t for row in z for t in row)
    unif=Q(1,n*n)+q*Q((n-1)**2,n*n)
    row_sq=sum((v-Q(1,n))**2 for v in r)
    col_sq=sum((v-Q(1,n))**2 for v in c)
    if q < Q(1,n-1):
        rhs=Q(1-q*(n-1),n)*(row_sq+col_sq)+(1+q)*norm_z
        assert h-unif==rhs
    else:
        theta=Q(q*(n-1)-1,2)
        # Full-permutation variance, enumerated symbolically as E(Y^2)-(EY)^2.
        T=sum(v*v for row in x for v in row)
        D=(1-sum(sum(row)**2 for row in x)-sum(sum(x[i][j] for i in range(n))**2 for j in range(n))+T)/2
        varY=Q(T,n)+Q(2*D,n*(n-1))-Q(1,n*n)
        assert varY>=0
        rhs=(1-theta)*Q(n,n-1)*norm_z+theta*(n*varY+Q(4,n-1)*D)
        assert h-Q(1,n)==rhs
        assert rhs>=0


def witness(n,k,kind):
    A=[[0]*n for i in range(n)]
    if kind=='single': A[0][0]=3
    elif kind=='row': A[0]=[1]*n
    elif kind=='flat': A=[[1]*n for _ in range(n)]
    elif kind=='matching':
        for i in range(n):A[i][i]=1
    elif kind=='additive':
        # q critical, positive additive mass not uniform: row bias plus column bias.
        A=[[0]*n for i in range(n)]
        # sqrt unnecessary: returns squared masses test separately
        return None
    return A


def quotient(A,k):
    e2,e4=moments_formula(A,k)
    return e4/e2**2


def check():
    count=0
    for n in range(2,5):
        for k in range(1,n+1):
            sample=[witness(n,k,s) for s in ('single','row','flat','matching')]
            rng=Random(100*n+k)
            sample += [[[rng.randint(-2,2) for _ in range(n)] for _ in range(n)] for _ in range(4)]
            for A in sample:
                if sum(v*v for row in A for v in row)==0:continue
                assert moments_direct(A,k)==moments_formula(A,k),(n,k,A)
                count+=1
    print('EXACT_DIRECT_SIGNED_ROOK_ENUMERATION_OK',count)
    for n in range(2,27):
        for k in range(1,n+1):
            lower=min(Q(3*k-2,k),Q(n,k))
            upper=max(Q(n*n,k),Q(4))
            if (n,k) in ((2,2),(3,3)): upper=4
            if (n,k)==(2,1):upper=4
            for kind in ('single','row','flat','matching'):
                A=witness(n,k,kind)
                K=quotient(A,k)
                assert lower<=K<=upper,(n,k,kind,K,lower,upper)
            assert quotient(witness(n,k,'single'),k)==Q(n*n,k)
            assert quotient(witness(n,k,'row'),k)==Q(n,k)
            assert quotient(witness(n,k,'flat'),k)==Q(3*k-2,k)
            if n in (2,3) and k==n:
                assert quotient(witness(n,k,'matching'),k)==4
            if n==4 and k==n:
                assert quotient(witness(n,k,'matching'),k)==Q(4)
    print('EXACT_ENDPOINT_WITNESSES_AND_RANK_PHASE_OK n=2..26')
    count=0
    for n in range(2,16):
        rng=Random(n)
        for k in range(1,n+1):
            samples=[]
            for _ in range(20):
                entries=[Q(rng.randint(0,15)) for _ in range(n*n)]
                S=sum(entries)
                samples.append([[entries[n*i+j]/S for j in range(n)] for i in range(n)])
            for x in samples:
                lower_certificate(x,n,k)
                count+=1
    print('EXACT_NONNEGATIVE_DEFICIT_IDENTITIES_OK',count)
    for n in (4,7,10,13,16):
        k=(n+2)//3
        assert 3*(k-1)==n-1
        # independent positive additive mass: (r_i+c_j-1/n)/n
        r=[Q(2,n+1)]+[Q(1,n+1)]*(n-1)
        c=[Q(1,n)]*n
        x=[[(r[i]+c[j])/n-Q(1,n*n) for j in range(n)] for i in range(n)]
        assert all(v>=0 for row in x for v in row)
        assert sum(map(sum,x))==1
        assert H(x,n,k)==Q(1,n)
        assert sum(v*v for row in x for v in row)!=Q(1,n*n)
    print('EXACT_CRITICAL_ADDITIVE_EQUALITY_FAMILIES_OK')
    print('ALL_FIXED_RANK_ROOK_FOURTH_MOMENT_CHECKS_OK')

if __name__=='__main__':check()
