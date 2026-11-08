#!/usr/bin/env python3
"""Exact integer replay for the two parity Potts ground-state sequences.
No external modules required. Run: python3 verify.py
"""
from itertools import product

COLORS = range(3)
PAIRS = list(product(COLORS, repeat=2))
INDEX = {x:i for i,x in enumerate(PAIRS)}
DIM = len(PAIRS)

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(DIM))
             for j in range(DIM)] for i in range(DIM)]

def eye():return [[int(i==j) for j in range(DIM)] for i in range(DIM)]
def add(a,b,aa=1,bb=1):return [[aa*a[i][j]+bb*b[i][j] for j in range(DIM)] for i in range(DIM)]
def scale(a,v):return [[v*a[i][j] for j in range(DIM)] for i in range(DIM)]
def tr(a):return sum(a[i][i] for i in range(DIM))

# The central (hub) spin is fixed at 0.  The summed clone spin is z.
# A = coefficient of t^0; B = coefficient of t^1 in the transfer matrix.
A=[[0]*DIM for _ in range(DIM)]
B=[[0]*DIM for _ in range(DIM)]
for a,b in PAIRS:
    for c in COLORS:
        target = INDEX[(b,c)]
        for z in COLORS:
            exponent = (a==z)+(c==z)+(z==0)+(b==c)
            if exponent == 0:A[INDEX[(a,b)]][target]+=1
            if exponent == 1:B[INDEX[(a,b)]][target]+=1

# Characteristic polynomial by exact Faddeev-LeVerrier integer arithmetic.
C=eye(); characteristic=[1]
for k in range(1,DIM+1):
    C=matmul(A,C)
    assert tr(C)%k==0
    ck=-tr(C)//k
    characteristic.append(ck)
    C=add(C,scale(eye(),ck))
assert characteristic==[1,0,-5,0,6,0,-1,0,0,0],characteristic

P2=matmul(A,A);P4=matmul(P2,P2);P6=matmul(P4,P2)
Q=add(add(add(P6,P4,1,-5),P2,1,6),eye(),1,-1)
assert matmul(P4,Q)==[[0]*DIM for _ in range(DIM)]
assert tr(matmul(B,Q))==0
assert tr(matmul(matmul(B,P2),Q))==0
assert tr(matmul(P2,Q))==0

# Odd trace a_k = tr(B A^(2k)), k >= 0
odd=[tr(B)]
even=[]
P=eye()
for k in range(1,13):
    P=matmul(P,P2)
    odd.append(tr(matmul(B,P)))
    even.append(tr(P))
assert odd[:7] == [4,12,44,152,508,1672,5464]
assert even[:6] == [10,26,76,234,740,2372]
for k in range(len(odd)-3):
    assert odd[k+3]==5*odd[k+2]-6*odd[k+1]+odd[k]
for k in range(len(even)-3):
    assert even[k+3]==5*even[k+2]-6*even[k+1]+even[k]
# The denominator 1 - 5y + 6y^2 - y^3 and initial odd terms
# give numerator 4 - 8y + 8y^2, and sum of three cubic roots
# has initial power sums 5,13,38, so even trace = twice this sum.

# Independent exhaustive enumeration of the underlying original and clone
# spins, with fixed hub; written without transfer matrices.
def direct_count(n):
    edges=[]
    for i in range(n):
        edges.extend([(i,(i+1)%n), (i,n+(i+1)%n), ((i+1)%n,n+i), (n+i,2*n)])
    edges=sorted({tuple(sorted(e)) for e in edges})
    minimum=10**9;count=0
    for spins in product(COLORS, repeat=2*n+1):
        b=sum(spins[u]==spins[v] for u,v in edges)
        if b < minimum:minimum=b;count=1
        elif b==minimum:count+=1
    return minimum,count

for n in (4,5,6):
    actual=direct_count(n)
    expected=(0,3*even[n//2-1]) if n%2==0 else (1,3*n*odd[(n-1)//2])
    assert actual==expected, (n,actual,expected)
    print('exhaustive',n,actual)
print('VERIFY_OK: exact matrix identities, recurrence, and independent enumeration')
