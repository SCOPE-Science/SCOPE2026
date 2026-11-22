"""Exact integer verification of the ternary circular Abelian-square-2 transfer polynomial.
Run: python3 verify_spectrum.py . No third-party packages required.
"""
from itertools import product
from math import isqrt

states=list(product(range(3),repeat=3))
position={s:i for i,s in enumerate(states)}
size=len(states)
M=[[0]*size for _ in states]
for i,(a,b,c) in enumerate(states):
    for d in range(3):
        if sorted((a,b)) != sorted((c,d)):
            M[i][position[(b,c,d)]]+=1

def multiply(A,B):
    n=len(A); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b:out[i][j]+=a*b
    return out

I=[[int(i==j) for j in range(size)] for i in range(size)]
P=I
power_traces=[]
for k in range(1,size+1):
    P=multiply(P,M)
    power_traces.append(sum(P[i][i] for i in range(size)))
# Faddeev/Newton recurrence: det(I-zM)=1+sum a_k z^k,
# k a_k = -sum_{i=1}^k a_{k-i} tr(M^i)
a=[1]
for k in range(1,size+1):
    numerator=-sum(a[k-i]*power_traces[i-1] for i in range(1,k+1))
    assert numerator%k==0
    a.append(numerator//k)

def prod(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B): C[i+j]+=x*y
    return C
F=[1,-1,0,1]
G=[1,-1,-2,-3,-2]
H=[1,1,2,3,0,0,-3,-2]
expected=prod(prod(F,G),prod(H,H))
assert len(expected)==22
assert a==expected+[0]*6,(a,expected)
assert power_traces[:15]==[0,0,6,60,90,216,462,1332,3282,7980,18876,46812,115440,283626,691986]
print('EXACT determinant verified, all 27 coefficients; first 15 traces verified')
