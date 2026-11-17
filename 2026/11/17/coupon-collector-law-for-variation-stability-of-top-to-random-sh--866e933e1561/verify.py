"""Exact rational checks for path-variation norms of positional shuffle averages."""
from fractions import Fraction as F
from math import comb

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(col) for col in zip(*A)]

def shuffle_matrix(n, reverse=False):
    A=[[F(0) for j in range(n)] for i in range(n)]
    for k in range(n):
        order=list(range(1,n))
        order.insert(k,0)  # remove top, reinsert at position k
        if reverse:
            inv=[0]*n
            for i,j in enumerate(order):inv[j]=i
            order=inv
        for i,j in enumerate(order): A[i][j]+=F(1,n)
    return A

def path_norm(A):
    n=len(A)
    return max((sum((abs(sum((A[i+1][j]-A[i][j] for j in range(k,n)), F(0)))
                     for i in range(n-1)), F(0)) for k in range(1,n)),default=F(0))

def coupon_tail(N,r):
    if r==0: return F(1)
    # State k = number of different coupons seen after draws.
    p=[F(1)]+[F(0)]*N
    for _ in range(r):
        q=[F(0)]*(N+1)
        for k in range(N+1):
            q[k]+=p[k]*F(k,N)
            if k<N:q[k+1]+=p[k]*F(N-k,N)
        p=q
    return F(1)-p[N]

def spectral_tail(N,r):
    if r==0:return F(1)
    return sum(((-1)**(j+1)*comb(N,j)*F(N-j,N)**r for j in range(1,N+1)), F(0))

for n in range(2,12):
    S=shuffle_matrix(n)
    T=shuffle_matrix(n,reverse=True)
    assert T==transpose(S)
    assert all(sum(row)==1 for row in S)
    assert path_norm(T)==(F(0) if n==2 else F(1) if n==3 else F(2*n-2,n))
    P=identity(n)
    for r in range(26):
        actual=path_norm(P)
        expect=F(n-1,n)**r*coupon_tail(n-1,r) if r else F(1)
        assert actual==expect,(n,r,actual,expect)
        assert coupon_tail(n-1,r)==spectral_tail(n-1,r)
        if 1<=r<=n-2:assert actual==F(n-1,n)**r
        if r==n-1: assert actual==F(n-1,n)**r-F(__import__('math').factorial(n-1),n**r)
        P=matmul(S,P)
    print('N',n,'EXACT_26_ITERATES_AND_COUPON_IDENTITY_PASS')
print('ADJOINT_ONE_STEP_VARIATION_ASYMMETRY_PASS')
print('ALL_SHUFFLE_BV_CERTIFICATES_PASS')
