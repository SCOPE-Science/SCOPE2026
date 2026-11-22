#!/usr/bin/env python3
"""Exact integer transfer and characteristic-polynomial verification for four-phase wheel waves."""
from fractions import Fraction

K=4
pairs=[(a,b) for a in range(K) for b in range(K)]
idx={ab:i for i,ab in enumerate(pairs)}
T=[[0]*16 for _ in range(16)]
for a,b in pairs:
    for c in range(4):
        if b==3 or a==(b+1)%4 or c==(b+1)%4:
            T[idx[(a,b)]][idx[(b,c)]]=1
S=[idx[(a,b)] for a,b in pairs if a!=1 and b!=1]
U=[[T[i][j] for j in S] for i in S]

def mul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def trace(A):return sum(A[i][i] for i in range(len(A)))
def charpoly(A):
    # Faddeev--LeVerrier, integer arithmetic checked at each step.
    n=len(A)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    coeff=[1]
    for k in range(1,n+1):
        C=mul(A,B)
        t=trace(C)
        assert t%k==0,(k,t)
        c=-t//k
        coeff.append(c)
        B=[[C[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
    assert all(v==0 for row in B for v in row),"Cayley-Hamilton remainder nonzero"
    return coeff

cpT=charpoly(T)
cpU=charpoly(U)
# chi_T(x)=x^9(x^2+1)(x^5-x^4-2x^3-2x^2-x-1).
# chi_U(x)=x^6(x^3-x^2-x-1).
assert cpT==[1,-1,-1,-3,-3,-3,-1,-1]+[0]*9,cpT
assert cpU==[1,-1,-1,-1]+[0]*6,cpU
A=[[int(i==j) for j in range(16)] for i in range(16)]
B=[[int(i==j) for j in range(9)] for i in range(9)]
expected={3:24,4:80,5:200,6:480,7:1232,8:3024,9:7296,10:17520,11:41800,12:99248}
for n in range(1,15):
    A=mul(A,T);B=mul(B,U)
    count=4*(trace(A)-trace(B))
    if n>=3 and n in expected:assert count==expected[n],(n,count)
    if n<=2:assert count==0
    print(f"rim={n} labeled_primitive_four_states={count} temporal_orbits={count//4}")
print('PASS exact characteristic polynomials, CH identities, transfer traces')
