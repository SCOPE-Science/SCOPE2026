#!/usr/bin/env python3
"""Exact reproducible checks for the Tetranacci 2-adic value image."""

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def power(a,n):
    z=[[int(i==j) for j in range(4)] for i in range(4)]
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z
def mv(a,v):return [sum(a[i][j]*v[j] for j in range(4)) for i in range(4)]
A=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,1,1]]
I=power(A,0)
assert power(A,5)==[[1,2,2,2],[2,3,4,4],[4,6,7,8],[8,12,14,15]]
C=power(A,10)
B=[[(C[i][j]-I[i][j])//4 for j in range(4)] for i in range(4)]
assert C==[[29,44,52,56],[56,85,100,108],[108,164,193,208],[208,316,372,401]]
assert B==[[7,11,13,14],[14,21,25,27],[27,41,48,52],[52,79,93,100]]
# Exact integer companion powers, without modular reduction.
v=[0,0,0,1]
coeffs={}
for j in (1,4,5,8):
    w=mv(power(A,j),v)
    first=w[0]
    w=mv(B,w);b1=w[0]
    w=mv(B,w);b2=w[0]
    coeffs[j]=(first,b1,b2)
assert coeffs=={1:(0,27,4763),4:(1,193,34112),5:(2,372,65753),8:(15,2664,470913)},coeffs
# Independently enumerate the full periods from initial recurrence.
for k in range(1,13):
    q=1<<k
    length=5*(1<<(k-1))
    a=[0,0,0,1]
    seq=[]
    for n in range(length):
        seq.append(a[0])
        a=a[1:]+[sum(a)%q]
    assert a==[0,0,0,1],(k,a)
    image=set(seq)
    if k>=4:
        truth={x for x in range(q) if x%16 in {0,1,2,4,5,8,9,12,13,15}}
    else:
        truth=[{0,1},{0,1,2,3},{0,1,2,4,5,7}][k-1]
    assert image==truth,(k,len(image),truth-image,image-truth)
    if k==4:
        assert len(image)==10
# Verify the four decisive isometric subsequences over several scales
for k in range(1,9):
    q=1<<k
    mod=1<<(k+4)
    # direct recurrence for relevant n; spans 20*q
    vals=[0,0,0,1]
    for n in range(4,20*q+10):
        vals.append(sum(vals[-4:])%mod)
    for j,offset,scale,step in ((1,0,4,10),(4,1,4,10),(5,2,16,20),(8,15,16,20)):
        for t in range(q):
            num=(vals[step*t+j]-offset)
            assert num%scale==0,(k,j,t)
        # Since the output map at all these levels is a permutation of q residues
        y=[((vals[step*t+j]-offset)//scale)%q for t in range(q)]
        assert len(set(y))==q,(k,j)
print('CHECK_OK; exact matrices, four isometry branches, finite images through 2^12')
