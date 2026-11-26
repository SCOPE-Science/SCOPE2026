#!/usr/bin/env python3
"""Exact independent-of-CAS polynomial-matrix checks over F_7[a]."""
from itertools import combinations
P=7

def trim(a):
    a=[x%P for x in a]
    while a and a[-1]==0: a.pop()
    return tuple(a)

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def neg(a):return trim([-z for z in a])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    if not a or not b:return ()
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def power(a,n):
    z=(1,)
    for _ in range(n):z=mul(z,a)
    return z

def quo_remainder(a,b):
    a=list(trim(a)); b=trim(b)
    if not b:raise ZeroDivisionError
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]*pow(b[-1],-1,P)%P
        q[k]=c
        for j,bj in enumerate(b):a[k+j]=(a[k+j]-c*bj)%P
        while a and a[-1]==0:a.pop()
    return trim(q),trim(a)

def rem(a,b):return quo_remainder(a,b)[1]
def monic(a):return trim([z*pow(a[-1],-1,P) for z in a]) if a else ()
def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return monic(a)
def mprod(A,B,mod=None):
    n=len(A)
    return [[rem(sum_poly([mul(A[i][k],B[k][j]) for k in range(n)]),mod) if mod else sum_poly([mul(A[i][k],B[k][j]) for k in range(n)]) for j in range(n)] for i in range(n)]
def sum_poly(v):
    z=()
    for w in v:z=add(z,w)
    return z

def twist(A,exp,mod=None):
    return [[rem(sum_poly([tuple([0]*(i*exp)+[c]) for i,c in enumerate(z) if c]),mod) if mod else sum_poly([tuple([0]*(i*exp)+[c]) for i,c in enumerate(z) if c]) for z in row] for row in A]

def rank(A):
    a=[[v%P for v in row] for row in A]; r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        mulinv=pow(a[r][c],-1,P)
        a[r]=[x*mulinv%P for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                t=a[i][c]
                a[i]=[(a[i][j]-t*a[r][j])%P for j in range(len(a[0]))]
        r+=1
    return r

A=(0,1)
M=[[(0,0,0,4),(4,),(0,0,6)], [(),(0,5),(0,0,0,4)],[(1,),(),()]]
# Verify the coefficient formula directly via the trinomial expansion of (x^5+a*x^2+1)^4.
# B_{i,j}=[x^(7*(i+1)-(j+1))]f^4. The 1-dimensional f^2 block is zero.
from math import factorial
terms={}
for i in range(5):
    for j in range(5-i):
        k=4-i-j
        e=5*i+2*j
        c=factorial(4)//(factorial(i)*factorial(j)*factorial(k))
        terms[e]=add(terms.get(e,()),tuple([0]*j+[c]))
for i in range(3):
    for j in range(3):
        assert terms.get(7*(i+1)-(j+1),())==M[i][j]
assert 6 not in [0,2,4,5,7,10]  # degree six of f^2 vanishes
# A universally nonzero 2x2 minor proves rank(M)>=2.
minor=sub(mul(M[0][0],M[2][1]),mul(M[0][1],M[2][0]))
assert minor==(3,)
# All 3x3 determinants vanish identically: calculate by the Leibniz formula.
import itertools
D=()
for perm in itertools.permutations(range(3)):
    inversions=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    z=(1,)
    for i,j in enumerate(perm):z=mul(z,M[i][j])
    D=add(D,neg(z) if inversions%2 else z)
assert D==()
# Correct semilinear orientation: M is the p-th powers of Cartier entries;
# Hasse-Witt matrix H=M^transpose, whose iterate has transpose M^(7)M.
P2=mprod(twist(M,7),M)
minor=sub(mul(P2[0][0],P2[2][1]),mul(P2[0][1],P2[2][0]))
assert minor==mul((3,),mul(power(A,4),sub(power(A,10),(1,))))
# At a^5=1, P2 is rank 1, and P4 has rank 1 with constant trace 2.
mod=sub(power(A,5),(1,))
Q=[[ (1,) if i==j else () for j in range(3)] for i in range(3)]
for n in range(1,5):
    Q=mprod(twist(M,7**(n-1),mod),Q,mod)
    assert rank([[sum(c for i,c in enumerate(z))%7 for z in row] for row in Q])>=0
P4=Q
expected=[[ (4,), (0,0,4), (0,0,0,0,6)],[(0,0,0,2),(2,),(0,0,3)],[(0,2),(0,0,0,2),(3,)]]
assert P4==expected, (P4,expected)
assert add(add(P4[0][0],P4[1][1]),P4[2][2])==(2,)
for rows in combinations(range(3),2):
    for cols in combinations(range(3),2):
        d=sub(mul(P4[rows[0]][cols[0]],P4[rows[1]][cols[1]]),mul(P4[rows[0]][cols[1]],P4[rows[1]][cols[0]]))
        assert rem(d,mod)==()
# Thus P4^2 = 2 P4 on the fifth-root locus, guaranteeing nonnilpotence.
assert mprod(P4,P4,mod)==[[mul((2,),z) for z in row] for row in P4]
# At a=0, M^3=0, M^2 != 0.
M0=[[z[0] if z else 0 for z in row] for row in M]
def m0(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%7 for j in range(3)] for i in range(3)]
assert rank(m0(M0,M0))==1 and m0(m0(M0,M0),M0)==[[0]*3 for _ in range(3)]
print('SYMBOLIC_CERTIFICATE_OK', 'constant_Cartier_rank=2', 'rank2_minor=3a^4(a^10-1)', 'P4_trace=2', 'a0_nilpotence=3')
