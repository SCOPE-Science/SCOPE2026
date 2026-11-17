#!/usr/bin/env python3
"""Exact polynomial-quotient identity checker for three residual norm identities.
Every operation is in Z[t]/(t^3-t^2-1), with no symbolic library.
"""
def add(a,b):return tuple(a[i]+b[i] for i in range(3))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=[0]*5
    for i in range(3):
        for j in range(3):c[i+j]+=a[i]*b[j]
    for d in (4,3):
        v=c[d]; c[d]=0
        c[d-1]+=v; c[d-3]+=v
    return tuple(c[:3])
def pw(a,n):
    v=(1,0,0)
    for _ in range(n):v=mul(v,a)
    return v
def scale(a,n):return tuple(n*x for x in a)
T=(0,1,0);ONE=(1,0,0);ZERO=(0,0,0)
assert mul(T,sub(pw(T,2),T))==ONE
B=((0,0,1),(1,0,0),(0,1,1))
def matmul(A,C):
    return tuple(tuple(sum(A[i][k]*C[k][j] for k in range(3)) for j in range(3)) for i in range(3))
BM=((1,0,0),(0,1,0),(0,0,1))
R=(T,ONE,pw(T,2));L=(ONE,T,pw(T,2))
N=ZERO
for i in range(3):N=add(N,mul(R[i],L[i]))
D2=(T,sub(pw(T,2),T),ONE)
invD2=(sub(pw(T,2),T),T,ONE)
for m in range(1,6):
    BM=matmul(BM,B)
    if m not in (3,4,5):continue
    lhs=ZERO
    for i in range(3):
        for j in range(3):
            q=sub(scale(N,BM[i][j]),mul(pw(T,m),mul(R[i],L[j])))
            term=mul(mul(q,q),mul(D2[j],invD2[i]))
            lhs=add(lhs,term)
    rhs={3:sub(scale(ONE,3),pw(T,2)),
         4:add(sub(scale(pw(T,2),3),scale(T,8)),scale(ONE,6)),
         5:add(sub(scale(pw(T,2),6),scale(T,12)),scale(ONE,5))}[m]
    assert lhs==mul(rhs,mul(N,N)),(m,lhs,rhs)
print('EXACT_RESIDUAL_NORM_IDENTITIES_PASS', 'powers=3,4,5')
