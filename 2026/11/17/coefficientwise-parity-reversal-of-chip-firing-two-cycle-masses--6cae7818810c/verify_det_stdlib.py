#!/usr/bin/env python3
"""Exact two-variable determinant from the local model; standard library only."""
from itertools import permutations
from collections import defaultdict

# Sparse polynomial dictionaries keyed (lambda power, mass-variable power).
def add(a,b,scale=1):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,0)+scale*v
    return {k:v for k,v in c.items() if v}
def mul(a,b):
    if not a or not b:return {}
    c=defaultdict(int)
    for (i,j),v in a.items():
        for (h,k),w in b.items():c[(i+h,j+k)]+=v*w
    return {k:v for k,v in c.items() if v}
def term(i,j,v=1):return {(i,j):v}

def plus(*args):
    out={}
    for a in args:out=add(out,a)
    return out

def local(p,r,t):
    result=term(0,0)
    for k in (0,1):
        c=int(r[k]!=p[k])+int(r[k]!=t[k])+int(r[k]!=r[1-k])
        if c==0:return {}
        lo=3 if r[k] else 3-c
        result=mul(result,{(0,lo+j):1 for j in range(c)})
    return result

cols=[(a,b) for a in (0,1) for b in (0,1)]
states=[(p,r) for p in cols for r in cols]
swap=lambda p:(p[1],p[0])
J=lambda s:(swap(s[0]),swap(s[1]))
reps=[s for s in states if s<J(s)]
def trans(s,t):return local(s[0],s[1],t[1]) if s[1]==t[0] else {}
N=[[add(trans(s,t),trans(s,J(t)),-1) for t in reps] for s in reps]
B=[[add(term(1,0) if i==j else {},N[i][j],-1) for j in range(6)] for i in range(6)]

ans={}
for perm in permutations(range(6)):
    inv=sum(perm[i]>perm[j] for i in range(6) for j in range(i+1,6))
    f=term(0,0)
    for i,j in enumerate(perm):
        f=mul(f,B[i][j]);
        if not f:break
    if f:ans=add(ans,f,(-1)**inv)

lam=term(1,0)
z5=term(0,5)
one=term(0,0)
a=plus(term(0,3),term(0,4,2),term(0,5))
b=plus(term(0,5),term(0,6,2),term(0,7))
F0=add(term(2,0),term(0,10),-1)
F1=add(plus(term(2,0),mul(lam,a)),term(0,8),-1)
F2=add(plus(term(2,0),mul(lam,b)),term(0,12),-1)
expect=mul(mul(F0,F1),F2)
assert ans==expect,(len(ans),len(expect),add(ans,expect,-1))
print('exact 6x6 determinant from 720 signed permutations: PASS')
print('polynomial monomial count:',len(ans))
print('max lambda degree:',max(x[0] for x in ans))
print('max mass degree:',max(x[1] for x in ans))
