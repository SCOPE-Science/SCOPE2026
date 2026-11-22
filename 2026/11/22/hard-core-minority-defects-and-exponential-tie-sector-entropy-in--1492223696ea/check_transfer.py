"""Independent exact-integer coefficient and matrix verification, Python >=3.8."""
from math import comb

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def trace_power(z,n):
    # States: new selected site, one zero after it, at least two zeros after it.
    M=[[0,1,0],[0,0,1],[z,0,1]]
    X=[[int(i==j) for j in range(3)] for i in range(3)]
    for _ in range(n):X=mm(X,M)
    return sum(X[i][i] for i in range(3))
def hard_core(n,r):
    if r==0:return 1
    if 3*r>n:return 0
    assert n*comb(n-2*r-1,r-1)%r==0
    return n*comb(n-2*r-1,r-1)//r

def B(n):
    return sum(6*hard_core(n,r) for r in range(1,n//3+1)
               if n>=3*r+2 and (n-r)%2==0)
for n in range(5,91):
    for z in (1,-1):
        assert trace_power(z,n)==sum(hard_core(n,r)*z**r for r in range(n//3+1))
    b=B(n)
    closed=3*(trace_power(1,n)+(-1)**n*trace_power(-1,n))-6*(n%2==0)-18*(n%3==0)
    assert b==closed,(n,b,closed)
print('EXACT TRANSFER PASS: all n=5..90, both signs and full stratum identity')
print('Sample counts:')
for n in (5,6,7,8,9,10,11,12,13,14,15,16,20,30,40,60,90):print(n,B(n))
