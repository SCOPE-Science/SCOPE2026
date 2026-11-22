#!/usr/bin/env python3
"""Exact reproducibility for the Klein 28--21 Levi critical group.
Requires SymPy (for independent fraction-free Smith forms and charpoly).
Uses rational pairs in Q[e], e^2+e+2=0; no floating-point arithmetic.
"""
import sympy as s
import json
from pathlib import Path
from fractions import Fraction
from collections import Counter
from math import gcd
from functools import reduce
from itertools import combinations
z=(0,0);one=(1,0);neg=(-1,0);e=(0,1);ne=(0,-1);em=( -1,1);nem=(1,-1)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def mul(a,b):return (a[0]*b[0]-2*a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def conj(a):return (a[0]-a[1],-a[1])
def norm(a):return a[0]*a[0]-a[0]*a[1]+2*a[1]*a[1]
def inv(a):
 n=norm(a);c=conj(a);return (Fraction(c[0],n),Fraction(c[1],n))
def div(a,b):return mul(a,inv(b))
def cross(v,w):return (sub(mul(v[1],w[2]),mul(v[2],w[1])),sub(mul(v[2],w[0]),mul(v[0],w[2])),sub(mul(v[0],w[1]),mul(v[1],w[0])))
def canon(v):
 for c in v:
  if c!=z:return tuple(div(a,c) for a in v)
 raise Exception('zero')
lines=[
(z,one,e), (z,one,ne), (e,neg,z), (z,e,neg), (nem,one,neg), (one,neg,em), (one,nem,one), (e,one,z), (one,ne,z), (one,neg,nem),
(one,one,em), (one,z,e), (one,e,z), (one,neg,one), (one,em,one), (z,e,one), (em,one,one), (e,z,one), (one,one,neg), (one,one,one),
(one,z,ne), (one,one,nem), (em,one,neg), (one,nem,neg), (one,em,neg), (em,neg,neg), (one,neg,neg), (e,z,neg)]
L=[(one,z,z),(z,one,one),(e,one,neg),(e,neg,one),(z,neg,one),(one,e,neg),(e,neg,neg),(neg,one,e),(e,one,one),(neg,e,one),(neg,neg,e),(one,z,one),(neg,e,neg),(one,e,one),(neg,z,one),(one,neg,e),(one,one,e),(z,z,one),(neg,one,z),(one,one,z),(z,one,z)]

from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from math import prod

# Construction A: intersections of all 28 listed Klein bitangents.
assert len(lines)==28 and len(set(canon(v) for v in lines))==28
points={}
for i,j in combinations(range(28),2):
    points.setdefault(canon(cross(lines[i],lines[j])),set()).update([i,j])
assert Counter(map(len,points.values()))=={2:252,4:21}
quad=[sorted(v) for v in points.values() if len(v)==4]
assert len(quad)==21 and Counter(i for q in quad for i in q)=={i:3 for i in range(28)}

# Construction B: 21 Klein lines and their 28 triple intersections.
assert len(L)==21 and len(set(canon(v) for v in L))==21
other={}
for i,j in combinations(range(21),2):
    other.setdefault(canon(cross(L[i],L[j])),set()).update([i,j])
assert Counter(map(len,other.values()))=={3:28,4:21}
triple=sorted([sorted(v) for v in other.values() if len(v)==3])
assert Counter(i for t in triple for i in t)=={i:4 for i in range(21)}

# Explicit independent graph-isomorphism certificate, 0-based labels.
f=[0,2,21,1,4,11,9,26,10,20,23,8,12,7,22,3,17,24,6,19,13,14,5,25,15,16,18,27]
g=[0,5,12,13,9,17,7,16,1,2,19,14,8,6,18,20,3,10,15,4,11]
assert sorted(f)==list(range(28)) and sorted(g)==list(range(21))
for j,qs in enumerate(quad):
    assert sorted(f[i] for i in qs)==[t for t,ts in enumerate(triple) if g[j] in ts]

# Recompute both full Laplacians from separate equation lists.
def laplacian_28(quad):
    B=s.zeros(28,21)
    for j,q in enumerate(quad):
        for i in q:B[i,j]=1
    full=s.diag(*([3]*28+[4]*21))
    for i in range(28):
        for j in range(21):
            if B[i,j]:full[i,28+j]-=1;full[28+j,i]-=1
    return B,full

def laplacian_21(triple):
    full=s.zeros(49)
    for j,ts in enumerate(triple):
        for i in ts:
            u=j;v=28+i
            full[u,u]+=1;full[v,v]+=1
            full[u,v]-=1;full[v,u]-=1
    return full

B,first=laplacian_28(quad)
second=laplacian_21(triple)
assert all(sum(first.row(i))==0 for i in range(49))
assert all(sum(second.row(i))==0 for i in range(49))
assert [first[i,i] for i in range(49)]==[3]*28+[4]*21
assert [second[i,i] for i in range(49)]==[3]*28+[4]*21

x=s.symbols('x')
assert s.factor((B*B.T-3*s.eye(28)).charpoly(x).as_expr())==s.factor(x**8*(x-9)*(x+3)**7*(x*x-2*x-7)**6)
assert s.factor(first.charpoly(x).as_expr())==s.factor(x*(x-7)*(x-3)**7*(x*x-7*x+9)**8*(x**4-14*x**3+65*x*x-112*x+56)**6)

expected=Counter({1:36,2:4,18:1,54:1,108:1,756:5})
for full in [first,second]:
    reduced=full[:48,:48]
    smith=smith_normal_form(reduced,domain=ZZ)
    factors=[abs(int(smith[i,i])) for i in range(48)]
    assert Counter(factors)==expected,(Counter(factors),expected)
    assert prod(factors)==2**18*3**23*7**5

# Independent prime-local elimination, without SymPy normal-form calls.
def local_valuations(mat,p,precision):
    n=mat.rows;mod=p**precision
    A=[[int(mat[i,j])%mod for j in range(n)] for i in range(n)]
    def vp(z):
        if z%mod==0:return precision
        e=0
        while z%p==0:z//=p;e+=1
        return e
    valuations=[]
    for k in range(n):
        v,i,j=min((vp(A[i][j]),i,j) for i in range(k,n) for j in range(k,n))
        if v>=precision:raise ArithmeticError('insufficient modular precision')
        A[k],A[i]=A[i],A[k]
        for r in range(n):A[r][k],A[r][j]=A[r][j],A[r][k]
        pk=p**v;sm=mod//pk
        invert=pow((A[k][k]//pk)%sm,-1,sm)
        for r in range(k+1,n):
            z=(A[r][k]//pk*invert)%sm
            if z:
                for c in range(k,n):A[r][c]=(A[r][c]-z*A[k][c])%mod
        for c in range(k+1,n):
            z=(A[k][c]//pk*invert)%sm
            if z:
                for r in range(k,n):A[r][c]=(A[r][c]-z*A[r][k])%mod
        assert all(A[r][k]==0 for r in range(k+1,n))
        assert all(A[k][c]==0 for c in range(k+1,n))
        valuations.append(v)
    return Counter(valuations)

for p,prec,expected_valuations in [(2,20,{0:36,1:6,2:6}),
                                   (3,24,{0:40,2:1,3:7}),
                                   (7,7,{0:43,1:5})]:
    got=local_valuations(second[:48,:48],p,prec)
    assert got==expected_valuations,(p,got,expected_valuations)

# The data attachment is generated from the first construction.
data=json.loads((Path(__file__).resolve().parent/'INCIDENCE.json').read_text(encoding='utf-8'))
assert data['bitangent_quadruple_incidence']==quad
assert data['klein_line_triple_incidence']==triple
assert data['bitangent_to_triple']==f
assert data['quadruple_to_klein_line']==g
print('KLEIN_BITANGENT_LEVI_SMITH_AND_LOCAL_CERTIFICATE_OK')
