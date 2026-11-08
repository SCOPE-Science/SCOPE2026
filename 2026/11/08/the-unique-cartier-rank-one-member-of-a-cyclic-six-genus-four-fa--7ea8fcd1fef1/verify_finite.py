#!/usr/bin/env python3
"""Independent direct F11 coefficient expansion and matrix reduction; stdlib only."""
from collections import Counter
P=11

def rank(A):
    M=[row[:] for row in A]; r=0
    for c in range(len(M[0])):
        pivot=next((i for i in range(r,len(M)) if M[i][c]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        inv=pow(M[r][c],-1,P)
        M[r]=[x*inv%P for x in M[r]]
        for i in range(len(M)):
            if i!=r:
                w=M[i][c]
                M[i]=[(x-w*y)%P for x,y in zip(M[i],M[r])]
        r+=1
    return r

def multiply(u,v):
    w=[0]*(len(u)+len(v)-1)
    for i,c in enumerate(u):
        for j,d in enumerate(v):w[i+j]=(w[i+j]+c*d)%P
    return w

counts=Counter(); examples={}; smooth=0
for a in range(P):
    for b in range(P):
        delta=(a*a-4*a*a*a+18*a*b-27*b*b-4*b)%P
        if b==0 or delta==0:continue
        smooth+=1
        f=[0]*11
        f[1]=b;f[4]=a;f[7]=1;f[10]=1
        power=[1]
        for _ in range(5):power=multiply(power,f)
        matrix=[[power[11*i-j] for j in range(1,5)] for i in range(1,5)]
        aval=4-rank(matrix)
        counts[aval]+=1
        examples.setdefault(aval,(a,b))
        formula=(a**5-2*a**3*b-3*a*a*b*b-3*a*b*b-2*b**3)%P
        expected=3 if (a,b)==(0,9) else 2 if formula==0 else 1
        assert aval==expected,(a,b,aval,expected)
assert smooth==101 and counts=={1:83,2:17,3:1},(smooth,counts)
assert examples[3]==(0,9)
print('VERIFY_FINITE_OK; smooth=101; a-number counts=(1:83,2:17,3:1); examples=',examples)
