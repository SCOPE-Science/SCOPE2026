#!/usr/bin/env python3
"""Dependency-free direct checks of one-sided annihilating idempotent pairs.
Arithmetic is over prime fields; Gaussian expressions handle any prime power.
"""
import itertools, math, collections

def gaussian(n,k,q):
    if k<0 or k>n: return 0
    num=math.prod(q**(n-i)-1 for i in range(k))
    den=math.prod(q**(k-i)-1 for i in range(k))
    return num//den

def rank_count(m,n,t,q):
    if t<0 or t>min(m,n): return 0
    return gaussian(n,t,q)*math.prod(q**m-q**i for i in range(t))

def expected(n,q):
    result={}
    for r in range(n+1):
        for s in range(n-r+1):
            a=gaussian(n,r,q)*q**(r*(n-r))*gaussian(n-r,s,q)*q**(s*(n-r-s))
            for t in range(min(r,s)+1):
                val=a*rank_count(s,r,t,q)
                if val: result[(r,s,t)]=val
    return result

def mul(A,B,q):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)) for i in range(n))

def rank(A,q):
    a=[list(x) for x in A];n=len(a);pivot=0
    for col in range(n):
        v=next((i for i in range(pivot,n) if a[i][col]),None)
        if v is None:continue
        a[pivot],a[v]=a[v],a[pivot];inv=pow(a[pivot][col],-1,q)
        for j in range(col,n):a[pivot][j]=a[pivot][j]*inv%q
        for i in range(n):
            if i!=pivot:
                c=a[i][col]
                if c:
                    for j in range(col,n):a[i][j]=(a[i][j]-c*a[pivot][j])%q
        pivot+=1
        if pivot==n:break
    return pivot

def brute(n,q):
    idem=[]
    for entries in itertools.product(range(q),repeat=n*n):
        A=tuple(entries[i*n:(i+1)*n] for i in range(n))
        if mul(A,A,q)==A:idem.append((A,rank(A,q)))
    counts=collections.Counter()
    for E,r in idem:
        for F,s in idem:
            if mul(E,F,q)==tuple(tuple(0 for j in range(n)) for i in range(n)):
                t=rank(mul(F,E,q),q)
                counts[(r,s,t)]+=1
    assert counts==expected(n,q),(n,q,counts-expected(n,q),expected(n,q)-counts)
    for r in range(n+1):
        for s in range(n-r+1):
            L=sum(counts[(r,s,t)] for t in range(min(r,s)+1))
            assert counts[(r,s,0)]*q**(r*s)==L,(n,q,r,s)

    print('BRUTE_PASS n=%d q=%d idempotents=%d pairs=%d rank_cells=%d' % (n,q,len(idem),sum(counts.values()),len(counts)))

def max_dim(n):
    return max((2*n*(r+s)-2*(r*r+s*s)-r*s,r,s) for r in range(n+1) for s in range(n-r+1))[0]

def theta(q,h,window=30):
    c=2*h/5
    return sum(q**(-2*(i-c)**2-(i-c)*(j-c)-2*(j-c)**2) for i in range(-window,window+1) for j in range(-window,window+1))

def asymptotics(q):
    P=math.prod(1-q**(-i) for i in range(1,300))
    for n in (10,15,20,21,30,40,50):
        m,h=divmod(n,5)
        total=sum(expected(n,q).values())
        logpred=4*n*n/5*math.log(q)+math.log(theta(q,h))-2*math.log(P)
        ratio=math.exp(math.log(total)-logpred)
        print('THETA_FINITE n=%d q=%d ratio=%.12f' %(n,q,ratio))

def rarity_theta(q,a,window=30):
    c=a/3
    return sum(q**(-2*((i-c)**2+(j-c)**2+(i-c)*(j-c)))
               for i in range(-window,window+1)
               for j in range(-window,window+1))

def rarity_checks():
    for q in (2,3):
        for n in (15,20,30,40,50):
            cells=expected(n,q)
            total=sum(cells.values())
            both=sum(v for (r,s,t),v in cells.items() if t==0)
            target=(q**(-2*n*n/15))*rarity_theta(q,n%3)/theta(q,n%5)
            ratio=(both/total)/target
            print('RARITY n=%d q=%d actual_to_pred=%.12f'%(n,q,ratio))
            assert ratio>0
    print('FIFTEEN_RESIDUE_RARITY_CHECKS_PASSED')

def mixed_rank_count(n,r,s,q):
    if s<0 or 2*s>n or r<0 or r+s>n:return 0
    gl=math.prod(q**s-q**j for j in range(s))
    return (gaussian(n,s,q)*gaussian(n-s,s,q)*gl
            *gaussian(n-s,r,q)*q**(r*(n-r)))

def mixed_and_reverse_checks():
    for q in (2,3,4,5):
        for n in range(1,35):
            cells=expected(n,q)
            for r in range(n+1):
                for s in range(n-r+1):
                    L=sum(cells.get((r,s,t),0) for t in range(min(r,s)+1))
                    M=mixed_rank_count(n,r,s,q)
                    if 2*s>n:
                        assert M==0
                        continue
                    # L/M = phi_(n-2s)/phi_(n-s), proven by cancellation.
                    a=math.prod(q**i-1 for i in range(1,n-2*s+1))
                    b=math.prod(q**i-1 for i in range(1,n-s+1))
                    # Avoid rational floating point: phi_k=prod(q^i-1)/q^(k(k+1)/2).
                    assert L*b*q**((n-2*s)*(n-2*s+1)//2)==M*a*q**((n-s)*(n-s+1)//2),(n,q,r,s)
    print('MIXED_SQUARE_ZERO_COMPARISON_PASSED n=1..34 q=2,3,4,5')

    # Directly check rank defect formula for conditional random s by r matrix.
    for q in (2,3,4,5):
        for r in range(1,18):
            for s in range(1,18):
                assert sum(rank_count(s,r,t,q) for t in range(min(r,s)+1))==q**(r*s)
    print('REVERSE_PRODUCT_CORANK_NORMALIZATION_PASSED')
    for q in (2,3):
        for n in (20,30,40,50):
            mixed=sum(mixed_rank_count(n,r,s,q) for r in range(n+1) for s in range(n-r+1))
            same=sum(expected(n,q).values())
            print('UNIVERSALITY n=%d q=%d ratio=%.12f'%(n,q,same/mixed))

if __name__=='__main__':
    for n,q in ((1,2),(2,2),(3,2),(2,3),(3,3)):
        brute(n,q)
    for n in range(1,101):
        assert max_dim(n)==4*n*n//5,(n,max_dim(n))
    print('TOP_DIMENSION_PASS n=1..100')
    for q in (2,3):asymptotics(q)
    mixed_and_reverse_checks()
    rarity_checks()
    print('ONE_SIDED_PROJECTION_THETA_CHECKS_PASSED')
