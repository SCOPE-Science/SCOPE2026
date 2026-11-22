#!/usr/bin/env python3
"""Independent exact coefficient and finite-field tests for a cyclic quartic family."""
import itertools
from collections import Counter
P=3

def trim(f):
    while len(f)>1 and f[-1]%3==0:f.pop()
    return [i%3 for i in f]
def divrem(a,b):
    a=trim(a[:]);b=trim(b[:]);assert b!=[0]
    while len(a)>=len(b) and a!=[0]:
        c=a[-1]*pow(b[-1],-1,3)%3; k=len(a)-len(b)
        for j,x in enumerate(b): a[k+j]=(a[k+j]-c*x)%3
        a=trim(a)
    return a
def gcd(a,b):
    while b!=[0]: a,b=b,divrem(a,b)
    return a

def rank(A):
    A=[row[:] for row in A]; m=len(A);n=len(A[0]); r=0
    for col in range(n):
        piv=next((i for i in range(r,m) if A[i][col]%3),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]; iv=pow(A[r][col],-1,3)
        A[r]=[(v*iv)%3 for v in A[r]]
        for i in range(m):
            if i!=r and A[i][col]:
                k=A[i][col];A[i]=[(a-k*b)%3 for a,b in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%3 for j in range(len(B[0]))] for i in range(len(A))]

def calc(a,b,c,d):
    # h_0=dx/y, h_1=dx/y²,h_2=x dx/y², h_3=dx/y³,h_4=x dx/y³,h_5=x² dx/y³
    f=[d,c,b,a,0,1]; f2=[sum(f[i]*f[k-i] for i in range(6) if 0<=k-i<6)%3 for k in range(11)]
    T=[[0]*6 for _ in range(6)]
    # Formula C(x^i dx/y^j) = sum_k ([x^{3k+2-i}] f^e)^(1/3) x^k dx/y^{j'}; in F3 cube root identity.
    for col,(i,j) in enumerate([(0,1),(0,2),(1,2),(0,3),(1,3),(2,3)]):
        e={1:2,2:1,3:0}[j]; jj={1:3,2:2,3:1}[j]
        poly= {0:[1],1:f,2:f2}[e]
        for row,(k,jr) in enumerate([(0,1),(0,2),(1,2),(0,3),(1,3),(2,3)]):
            if jj==jr:
                z=3*k+2-i
                if 0<=z<len(poly):T[row][col]=poly[z]
    expect=[[0]*6 for _ in range(6)]
    expect[3][0]=(c*c-b*d)%3;expect[4][0]=(-d-a*b)%3;expect[5][0]=-a%3
    expect[1][1]=b;expect[2][1]=1;expect[1][2]=c;expect[0][5]=1
    expect=[[v%3 for v in row] for row in expect]
    assert T==expect, (a,b,c,d,T,expect)
    sqfree = gcd(f,[(i*f[i])%3 for i in range(1,6)])==[1] or (lambda gg:len(gg)==1 and gg[0]!=0)(gcd(f,[(i*f[i])%3 for i in range(1,6)]))
    # All polynomials are monic, gcd constant unit indicates squarefree
    if not sqfree:return None
    r=[]; P=T
    for _ in range(8):
        r.append(rank(P));P=matmul(P,T)
    rankstable=r[-1]; pred=(2 if a else 0)+(2 if c else (1 if b else 0))
    assert rankstable==pred,(a,b,c,d,rankstable,pred,r)
    assert 6-r[0] == (2 if c else 3),(a,b,c,d,r)
    return pred,6-r[0],r

freq=Counter(); examples={}; profiles=Counter()
for a,b,c,d in itertools.product(range(3),repeat=4):
    out=calc(a,b,c,d)
    if out is None:continue
    pr,an,rs=out;freq[(pr,an)]+=1;examples.setdefault(pr,(a,b,c,d,rs));profiles[tuple(rs)]+=1
print('counts',sorted(freq.items()))
print('examples',examples)
print('profiles',sorted(profiles.items()))
assert set(examples)=={0,1,2,3,4}
assert sum(freq.values())>0
print('CYCLIC_QUARTIC_CHAR3_CARTIER_TESTS_OK')
