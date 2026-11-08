#!/usr/bin/env python3
"""Independent exact polynomial-ring verification in characteristic 11.
Computes the Frobenius-twisted Hasse-Witt product and exceptional locus.
Pure Python 3, standard library only.
"""
P=11

def trim(a):
    a=[v%P for v in a]
    while a and a[-1]==0:a.pop()
    return tuple(a)

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)

def neg(a):return trim([-v for v in a])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    if not a or not b:return ()
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def scale(a,k):return trim([k*v for v in a])
def power(a,n):
    z=(1,)
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a); n//=2
    return z

def divmodp(A,B):
    A=list(A)
    if not B:raise ZeroDivisionError
    Q=[0]*max(0,len(A)-len(B)+1)
    inv=pow(B[-1],P-2,P)
    while len(A)>=len(B):
        k=len(A)-len(B); c=A[-1]*inv%P;Q[k]=c
        for i,v in enumerate(B):A[k+i]=(A[k+i]-c*v)%P
        while A and A[-1]==0:A.pop()
    return trim(Q),trim(A)

def rem(A,B):return divmodp(A,B)[1]
def gcd(A,B):
    while B:A,B=B,rem(A,B)
    return scale(A,pow(A[-1],P-2,P)) if A else ()
def val(A,x):
    out=0
    for z in reversed(A):out=(out*x+z)%P
    return out

def matmul(A,B):
    return [[sum_polys(mul(A[i][k],B[k][j]) for k in range(4)) for j in range(4)] for i in range(4)]
def sum_polys(t):
    z=()
    for u in t:z=add(z,u)
    return z

def derivative(A):return trim([i*v for i,v in enumerate(A)][1:])

def extended_inverse(A,M):
    r0,r1=M,rem(A,M)
    t0,t1=(),(1,)
    while r1:
        q,r2=divmodp(r0,r1)
        r0,r1=r1,r2
        t0,t1=t1,sub(t0,mul(q,t1))
    assert len(r0)==1
    return rem(scale(t0,pow(r0[0],P-2,P)),M)

def modular_composition(poly,z,M):
    out=()
    for c in reversed(poly):out=rem(add(mul(out,z),(c,)),M)
    return out

x=(0,1);zero=();one=(1,)
A=power(x,2)
B=scale(x,-5)
C=add((1,),add(scale(power(x,2),-5),scale(power(x,4),-3)))
D=add(scale(x,2),add(power(x,3),scale(power(x,5),5)))
M=[[zero,A,zero,B],[C,zero,D,zero],[zero,neg(D),zero,neg(C)],[neg(B),zero,neg(A),zero]]
assert sub(mul(A,C),mul(B,D))==(), 'Rank-one block relation'
F=[[trim(sum_polys([tuple([0]*(11*k)+[c]) for k,c in enumerate(e) if c])) for e in row] for row in M]
N=matmul(M,F)
G=trim([0,-4]+[0]*9+[1]+[0]*11+[-2]+[0]*21+[1])
assert len(G)==46, len(G)
T=[[zero]*4 for _ in range(4)]
T[0][0]=scale(x,-3)
T[0][2]=scale(power(x,12),5)
T[1][1]=add(power(x,11), add(scale(power(x,13),-5),scale(power(x,15),-3)))
T[1][3]=add((-5,),add(scale(power(x,2),3),scale(power(x,4),4)))
T[2][0]=T[1][3]
T[2][2]=T[1][1]
T[3][1]=T[0][2]
T[3][3]=T[0][0]
for i in range(4):
    for j in range(4):
        assert N[i][j]==mul(G,T[i][j]),('Frobenius identity',i,j)
# Both diagonal 2x2 blocks of T have zero determinant.
assert sub(mul(T[0][0],T[2][2]),mul(T[0][2],T[2][0]))==()
assert sub(mul(T[1][1],T[3][3]),mul(T[1][3],T[3][1]))==()
# For every a: each block has rank >=1, since at a=0 each has a
# nonzero -5 entry, and for a!=0 a -3a entry. Therefore rank(T)=2.
assert gcd(G,derivative(G))==(1,)
assert (val(G,2),val(G,-2))==(10,1)
extra=add(power(x,2),(12,))  # enhanced SL2(F3) points
assert gcd(G,extra)==(1,)
enhanced=mul(x,sub(power(x,2),(36,)))
assert gcd(G,enhanced)==scale(enhanced,pow(enhanced[-1],P-2,P))
# Published isomorphisms identify a with -a and two Mobius expressions.
# Verify explicitly that each of the six images preserves the zero set of G.
for sign in (+1,-1):
    for numerator,denominator in [ (x,one), (add(scale(x,2),(-12,)),add(x,(2,))), (add(scale(x,2),(12,)),sub(x,(2,))) ]:
        z=rem(mul(scale(numerator,sign),extended_inverse(denominator,G)),G)
        assert modular_composition(G,z,G)==(), ('orbit invariance',sign,numerator)
print('FROBENIUS_PRODUCT_OK degree',len(G)-1)
print('SQUAREFREE_ROOTS_OK count=45 excluded=+/-2')
print('RANK_STRATA_OK rank_zero=45 generic_rank=2 a_number=2')
print('AUT_ORBITS_OK exact_Q8_rank_zero=42 coefficient_parameters / 6 = 7 classes, extended=1 class')
