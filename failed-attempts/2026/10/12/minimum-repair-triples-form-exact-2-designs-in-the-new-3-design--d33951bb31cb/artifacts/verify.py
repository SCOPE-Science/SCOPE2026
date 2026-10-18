#!/usr/bin/env python3
import itertools, json, math
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# GF(3^4) with modulus x^4+x^3+x^2+1.
P=3
DEG=4
MOD=[1,0,1,1,1]

def coeff(a):
    out=[]
    for _ in range(DEG):
        out.append(a%P)
        a//=P
    return out

def enc(c):
    return sum((x%P)*(P**i) for i,x in enumerate(c))

def add(a,b):
    A=coeff(a); B=coeff(b)
    return enc([(A[i]+B[i])%P for i in range(DEG)])

def neg(a):
    return enc([(-x)%P for x in coeff(a)])

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    A=coeff(a); B=coeff(b)
    t=[0]*(2*DEG-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B):
            t[i+j]=(t[i+j]+x*y)%P
    for d in range(2*DEG-2,DEG-1,-1):
        z=t[d]%P
        if z:
            t[d]=0
            for j in range(DEG):
                t[d-DEG+j]=(t[d-DEG+j]-z*MOD[j])%P
    return enc(t[:DEG])

def power(a,n):
    r=1
    while n:
        if n&1:
            r=mul(r,a)
        a=mul(a,a)
        n//=2
    return r

def inv(a):
    assert a
    return power(a,79)

# This confirms the quotient is a field.
for a in range(1,81):
    assert power(a,80)==1
    assert mul(a,inv(a))==1

def order(a):
    for d in (1,2,4,5,8,10,16,20,40,80):
        if power(a,d)==1:
            return d
    raise AssertionError

beta=next(a for a in range(2,81) if order(a)==10)
assert order(beta)==10

# q=9, p=3, m=2, s=1: k1=1, k2=2.
n=10
cols=[]
for j in range(1,n+1):
    cols.append([
        power(beta,j%10),
        power(beta,(2*j)%10),
        power(beta,(-j)%10),
        power(beta,(-2*j)%10),
    ])
G=[[cols[j][i] for j in range(n)] for i in range(4)]

def rank(rows):
    A=[r[:] for r in rows]
    if not A:
        return 0
    rr=0
    for c in range(len(A[0])):
        p=next((i for i in range(rr,len(A)) if A[i][c]),None)
        if p is None:
            continue
        A[rr],A[p]=A[p],A[rr]
        iv=inv(A[rr][c])
        A[rr]=[mul(iv,x) for x in A[rr]]
        for i in range(len(A)):
            if i!=rr and A[i][c]:
                z=A[i][c]
                A[i]=[sub(A[i][j],mul(z,A[rr][j])) for j in range(len(A[0]))]
        rr+=1
        if rr==len(A):
            break
    return rr

assert rank(G)==4

blocks=[]
for S in itertools.combinations(range(10),4):
    M=[[G[i][j] for j in S] for i in range(4)]
    if rank(M)<4:
        blocks.append(S)

assert len(blocks)==30

triple_count=Counter()
for B in blocks:
    for T in itertools.combinations(B,3):
        triple_count[T]+=1
assert len(triple_count)==math.comb(10,3)
assert set(triple_count.values())=={1}

for i in range(10):
    derived=[tuple(x for x in B if x!=i) for B in blocks if i in B]
    assert len(derived)==12
    assert len(set(derived))==12
    helpers=[x for x in range(10) if x!=i]
    point_deg=Counter(x for E in derived for x in E)
    assert all(point_deg[x]==4 for x in helpers)
    for a,b in itertools.combinations(helpers,2):
        assert sum(1 for E in derived if a in E and b in E)==1

def formulas(q,lam):
    b=lam*q*(q-1)//6
    r=lam*(q-1)//2
    delta=3*r-3*lam+1
    t=(b+delta-1)//delta
    return b,r,delta,t

expected={
    (9,1):(12,4,10,2),
    (25,3):(300,36,100,3),
    (81,7):(7560,280,820,10),
}
for key,val in expected.items():
    assert formulas(*key)==val

for ex in CERT["verification_examples"]:
    b,r,delta,t=formulas(ex["q"],ex["lambda"])
    assert b==ex["repair_blocks"]
    assert r==ex["helper_degree"]
    assert t==ex["availability_lower_bound"]

print("VERIFY_OK")
