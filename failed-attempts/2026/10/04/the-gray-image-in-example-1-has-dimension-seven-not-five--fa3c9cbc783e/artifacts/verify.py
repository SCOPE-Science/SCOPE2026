#!/usr/bin/env python3
from itertools import product
from collections import Counter
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def mul4(x,y):
    a=x&1; b=(x>>1)&1
    c=y&1; d=(y>>1)&1
    A=(a*c)^(b*d)
    B=(a*d)^(b*c)^(b*d)
    return A|(B<<1)

assert mul4(2,2)==3
assert mul4(2,3)==1

rows=[
    ([1,0,1,1,1,0,0],[0,0,0,0]),
    ([0,1,0,1,1,1,0],[0,0,0,0]),
    ([0,0,1,0,1,1,1],[0,0,0,0]),
    ([1,1,0,1,0,0,0],[3,3,1,0]),
    ([0,1,1,0,1,0,0],[0,2,2,1]),
]

def scalar(d,row):
    b,f=row
    return ([((d&1)*x) for x in b],[mul4(d,x) for x in f])

def addrow(r,s):
    return ([x^y for x,y in zip(r[0],s[0])],
            [x^y for x,y in zip(r[1],s[1])])

def gray(row):
    b,f=row
    q=[(x>>1)&1 for x in f]
    pq=[(x&1)^((x>>1)&1) for x in f]
    return tuple(list(b)+q+pq)

mixed=set()
for a,b,c,d,e in product([0,1],[0,1],[0,1],range(4),range(4)):
    v=([0]*7,[0]*4)
    for coef,row in zip([a,b,c,d,e],rows):
        v=addrow(v,scalar(coef,row))
    mixed.add((tuple(v[0]),tuple(v[1])))

assert len(mixed)==128
gray_code={gray(v) for v in mixed}
assert len(gray_code)==128

basis=[gray(rows[i]) for i in range(3)]
for i in (3,4):
    basis.append(gray(scalar(1,rows[i])))
    basis.append(gray(scalar(2,rows[i])))

def rank2(A):
    A=[list(r) for r in A]
    r=0
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                A[i]=[x^y for x,y in zip(A[i],A[r])]
        r+=1
    return r

assert rank2(basis)==7
assert [list(r) for r in basis]==cert["binary_gray_generator"]

weights=Counter(sum(w) for w in gray_code)
expected=Counter({int(k):v for k,v in cert["weight_distribution"].items()})
assert weights==expected
assert min(k for k in weights if k!=0)==4
assert sum(weights.values())==128
assert cert["actual_binary_parameters"]==[15,7,4]
assert cert["cardinality_formula"]["value"]==128
assert cert["cardinality_formula"]["binary_dimension"]==7

print("VERIFY_OK")
