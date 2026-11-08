"""Finite-field checks for the Jordan-type formula for multiplication by a two-form.
Only Python standard library; prime fields are used for direct multiplication.
"""
from itertools import combinations,product
from math import comb,prod, factorial
from collections import Counter


def rank_mod(mat,p):
    if not mat: return 0
    a=[list(row) for row in mat]
    m,n=len(a),len(a[0]); rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,m) if a[i][j]%p),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,p)
        a[rank]=[(x*inv)%p for x in a[rank]]
        for i in range(rank+1,m):
            if a[i][j]%p:
                v=a[i][j]
                a[i]=[(x-v*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==m:break
    return rank


def wilson_rank(N,d,k,p):
    if d<0 or k<0 or d+k>N:return 0
    t=min(d,N-d-k); u=t+k
    return sum((comb(N,i)-(comb(N,i-1) if i else 0)) for i in range(t+1)
               if comb(u-i,t-i)%p!=0)


def rank_powers_formula(n,r,p):
    val=[2**n]
    for k in range(1,p+1):
        rk=0
        if k<p:
            for j in range(r+1):
                if j>=k:
                    sr=sum(wilson_rank(j,d,k,p) for d in range(j-k+1))
                    rk+=comb(r,j)*2**(r-j)*sr
            rk*=2**(n-2*r)
        val.append(rk)
    val.append(0)
    return val


def jordan_from_ranks(rr):
    return tuple(rr[i-1]-2*rr[i]+rr[i+1] for i in range(1,len(rr)-1))


def gauss(N,K,q):
    if K<0 or K>N:return 0
    num=prod(q**(N-i)-1 for i in range(K))
    den=prod(q**(K-i)-1 for i in range(K))
    return num//den


def alternating_count(n,r,q):
    return gauss(n,2*r,q)*q**(r*(r-1))*prod(q**(2*i-1)-1 for i in range(1,r+1))


def mat_rank_form(n,coeffs,p):
    M=[[0]*n for _ in range(n)]
    for (i,j),c in zip(combinations(range(n),2),coeffs):
        M[i][j]=c%p;M[j][i]=-c%p
    return rank_mod(M,p)


def mulmat(n,coeffs,p):
    basis=1<<n
    M=[[0]*basis for _ in range(basis)]
    for (i,j),c in zip(combinations(range(n),2),coeffs):
        mask=(1<<i)|(1<<j)
        if not c:continue
        for x in range(basis):
            if x&mask:continue
            # sign from sorting (i,j) followed by x, irrelevant in characteristic two
            inversions=sum(1 for bit in range(n) if x>>bit&1 and bit<i)
            inversions+=sum(1 for bit in range(n) if x>>bit&1 and bit<j)
            sign=-1 if inversions%2 else 1
            M[mask|x][x]=(M[mask|x][x]+sign*c)%p
    return M


def mm(A,B,p):
    n=len(A);out=[[0]*n for _ in range(n)]
    for i,row in enumerate(A):
        for k,aa in enumerate(row):
            if aa%p:
                for j,x in enumerate(B[k]):
                    out[i][j]=(out[i][j]+aa*x)%p
    return out


def direct_ranks(n,coeffs,p):
    M=mulmat(n,coeffs,p)
    P=[[int(i==j) for j in range(1<<n)] for i in range(1<<n)]
    ans=[1<<n]
    for k in range(1,p+1):
        P=mm(P,M,p)
        ans.append(rank_mod(P,p))
    ans.append(0)
    return ans


def check():
    for p,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(5,4)]:
        cnt=Counter(); count=0
        for coeffs in product(range(p),repeat=comb(n,2)):
            r=mat_rank_form(n,coeffs,p)//2
            observed=direct_ranks(n,coeffs,p)
            expected=rank_powers_formula(n,r,p)
            if observed!=expected:
                raise AssertionError((p,n,coeffs,observed,expected))
            cnt[r]+=1;count+=1
        want={r:alternating_count(n,r,p) for r in range(n//2+1)}
        if cnt!=Counter(want):raise AssertionError((p,n,cnt,want))
        print(f'p={p}, n={n}, direct_quadratics={count}, alternating_counts={dict(sorted(cnt.items()))}, checked_all_Jordan_powers=PASS')
    for n in range(1,12):
        for q in (2,3,4,5,8,9):
            assert sum(alternating_count(n,r,q) for r in range(n//2+1))==q**comb(n,2)
    print('ALT_FORM_COUNT_POLYNOMIAL_TOTAL_PASS n=1..11 q=2,3,4,5,8,9')
    for r in range(1,7):
        for p in (2,3,5,7):
            data=rank_powers_formula(2*r,r,p)
            blocks=jordan_from_ranks(data)
            assert all(x>=0 for x in blocks) and sum((i+1)*x for i,x in enumerate(blocks))==4**r
            if r<=3:print(f'r={r}, p={p}, Jordan_blocks={blocks}')
    print('QUADRATIC_EXTERIOR_JORDAN_WILSON_PASS')

if __name__=='__main__':check()
