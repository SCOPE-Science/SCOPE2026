"""Finite checks for the rank spectrum of multiplication by J^(n-2) in Lambda(F_q^n).
Self-contained; prime fields only for experimental checks. The proof applies to all finite fields.
"""
from itertools import combinations, product
from collections import Counter
from random import Random


def sgn(a,b,n):
    if a & b: return 0
    flips=sum((b & ((1<<i)-1)).bit_count() for i in range(n) if a>>i&1)
    return -1 if flips%2 else 1


def rank(matrix,p):
    a=[list(row) for row in matrix]
    if not a:return 0
    m,k=len(a),len(a[0]);r=0
    for j in range(k):
        pivot=next((i for i in range(r,m) if a[i][j]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j]%p,-1,p)
        for c in range(j,k):a[r][c]=a[r][c]*inv%p
        for i in range(r+1,m):
            f=a[i][j]
            if f:
                for c in range(j,k):a[i][c]=(a[i][c]-f*a[r][c])%p
        r+=1
        if r==m:break
    return r


def gaussian(n,k,q):
    v=1
    for j in range(k):v=v*(q**(n-j)-1)//1 # use rational end
    # direct exact quotient
    num=1;den=1
    for j in range(k):num*=q**(n-j)-1;den*=q**(k-j)-1
    return num//den


def alt_count(n,r,q):
    val=gaussian(n,2*r,q)*q**(r*(r-1))
    for j in range(1,r+1):val*=q**(2*j-1)-1
    return val


def predicted_counts(n,q):
    counts={0:1,1:q-1,2:q*(q**n-1)}
    for r in range(1,n//2+1):counts[2+2*r]=q**(n+1)*alt_count(n,r,q)
    assert sum(counts.values())==q**(n*(n-1)//2+n+1)
    return counts


def direct_rank(n,coeff,p):
    low=[m for m in range(1<<n) if m.bit_count()<=2]
    hi=[m for m in range(1<<n) if m.bit_count()>=n-2]
    mat=[[sum(c*sgn(z,x,n) for z,c in coeff.items() if (x&z)==0 and (x|z)==y)%p for x in low] for y in hi]
    return rank(mat,p)


def dual_alt_rank(n,coeff,p):
    # B_ij defined via e_i wedge e_j wedge degree-(n-2) leading component
    top=(1<<n)-1
    a=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:row.append(0);continue
            x=(1<<i)|(1<<j)
            row.append(sum(c*sgn(1<<i,1<<j,n)*sgn(x,z,n) for z,c in coeff.items() if z.bit_count()==n-2 and not(x&z) and (x|z)==top)%p)
        a.append(row)
    return rank(a,p)


def expected_rank(n,coeff,p):
    alpha={z:c for z,c in coeff.items() if z.bit_count()==n-2 and c}
    beta={z:c for z,c in coeff.items() if z.bit_count()==n-1 and c}
    gamma={z:c for z,c in coeff.items() if z.bit_count()==n and c}
    if alpha:return 2+dual_alt_rank(n,alpha,p)
    if beta:return 2
    if gamma:return 1
    return 0


def test(n,p,samples):
    rng=Random(8917+100*n+p)
    masks=[m for m in range(1<<n) if m.bit_count()>=n-2]
    cases=[]
    # force every possible rank stratum via chosen alternating normal forms
    for r in range(1,n//2+1):
        eta={}
        top=(1<<n)-1
        for j in range(r):
            pair=(1<<(2*j))|(1<<(2*j+1))
            eta[top^pair]=1
        cases.append(eta)
        cases.append({**eta,**{x:rng.randrange(p) for x in masks if x.bit_count()>n-2}})
    cases+= [{},{masks[-1]:1},{next(x for x in masks if x.bit_count()==n-1):1}]
    for _ in range(samples):
        coeff={m:rng.randrange(p) for m in masks}
        coeff={x:v for x,v in coeff.items() if v}
        cases.append(coeff)
    histogram=Counter()
    for c in cases:
        got=direct_rank(n,c,p)
        want=expected_rank(n,c,p)
        assert got==want,(n,p,c,got,want)
        histogram[got]+=1
    return histogram,len(cases)

if __name__=='__main__':
    for n in (5,6,7):
        for p in (2,3,5):
            counts,k=test(n,p,120)
            print('n=%d q=%d direct=%d ranks=%s'%(n,p,k,sorted(counts.items())))
            print('  exact distribution polynomial:',sorted(predicted_counts(n,p).items()))
    print('NEAR_SOCLE_CHECKS_OK')
