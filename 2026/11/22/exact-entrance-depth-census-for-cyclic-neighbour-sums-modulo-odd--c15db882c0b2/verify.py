#!/usr/bin/env python3
"""Independent exact arithmetic checks for cyclic-sum entrance-time theorem."""
from itertools import product
from math import comb


def smith2_kernel_exponent(matrix, p):
    """Count the kernel of a square matrix modulo p**2 using unit row/col pivots."""
    a = [list(map(lambda z:z%(p*p), row)) for row in matrix]
    n=len(a);m=p*p;k=0;ans=0
    while k<n:
        candidates=[(0 if a[i][j]%p else 1, i,j) for i in range(k,n) for j in range(k,n) if a[i][j]]
        if not candidates:
            ans+=2*(n-k); break
        v,i,j=min(candidates)
        a[i],a[k]=a[k],a[i]
        for row in a:row[k],row[j]=row[j],row[k]
        pivot=a[k][k]
        if v==0: inv=pow(pivot,-1,m)
        else:inv=pow(pivot//p,-1,p)
        for ii in range(k+1,n):
            if a[ii][k]:
                fac=(a[ii][k]*inv)%m if v==0 else ((a[ii][k]//p)*inv)%p
                for jj in range(k,n):a[ii][jj]=(a[ii][jj]-fac*a[k][jj])%m
                assert a[ii][k]==0
        for jj in range(k+1,n):
            if a[k][jj]:
                fac=(a[k][jj]*inv)%m if v==0 else ((a[k][jj]//p)*inv)%p
                for ii in range(k,n):a[ii][jj]=(a[ii][jj]-fac*a[ii][k])%m
                assert a[k][jj]==0
        ans+=v;k+=1
    return ans


def matmul(a,b,m):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))%m for j in range(n)] for i in range(n)]


def test_local(p,q):
    n=q;m=p*p
    # Multiplication by 1+x in Z/p^2[x]/(x^q+1) for odd p.
    a=[[int(i==j)+(int(i==j+1) if i else (-int(j==q-1))) for j in range(q)] for i in range(q)]
    powmat=[[int(i==j) for j in range(q)] for i in range(q)]
    d=q//p
    for t in range(2*q+2):
        exponent=smith2_kernel_exponent(powmat,p)
        expected=min(2*t,t+d,2*q)
        assert exponent==expected, (p,q,t,exponent,expected)
        powmat=matmul(powmat,a,m)


def test_cyclic_full(p,n):
    assert n%2==0 and n%p==0
    q=1
    while n% (q*p)==0:q*=p
    d=q//p;m=p*p
    a=[[int(i==j)+int((i+1)%n==j) for j in range(n)] for i in range(n)]
    powmat=[[int(i==j) for j in range(n)] for i in range(n)]
    for t in range(2*q-d+3):
        exponent=smith2_kernel_exponent(powmat,p)
        expected=min(2*t,t+d,2*q)
        assert exponent==expected, (p,n,t,exponent,expected)
        powmat=matmul(powmat,a,m)


def test_count_all_small():
    # Exhaustively distinguish all trajectory entrance times for n=6, p=3.
    p=3;n=6;m=p*p;q=3;d=1
    buckets=[0]*(2*q-d+1)
    for v in product(range(m),repeat=n):
        w=v
        for t in range(2*q-d+1):
            if all((w[r]-w[r+q])%m==0 for r in range(q)):
                buckets[t]+=1;break
            w=tuple((w[i]+w[(i+1)%n])%m for i in range(n))
        else:raise AssertionError(('not entering',v))
    cumulative=0
    for t,b in enumerate(buckets):
        cumulative+=b
        expected=p**(2*(n-q)+min(2*t,t+d,2*q))
        assert cumulative==expected, (t,cumulative,expected)
    return buckets


def main():
    for p,q in [(3,3),(3,9),(5,5),(7,7)]:test_local(p,q)
    for p,n in [(3,6),(3,12),(3,18),(5,10),(7,14)]:test_cyclic_full(p,n)
    buckets=test_count_all_small()
    print('VERIFY_OK local_pairs=4 whole_matrix_pairs=5 full_states=531441 n6_depth_buckets='+repr(buckets))
if __name__=='__main__':main()
