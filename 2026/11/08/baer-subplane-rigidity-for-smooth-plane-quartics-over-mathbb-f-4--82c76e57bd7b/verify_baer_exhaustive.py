#!/usr/bin/env python3
"""Independent GF(4) coefficient/evaluation census (Python 3 standard library).
Run: python3 verify_baer_exhaustive.py
"""
import itertools
MUL=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
INV=(0,1,3,2)
def mul(a,b):return MUL[a][b]
def power(a,n):
    v=1
    for _ in range(n):v=mul(v,a)
    return v

def points():
    P=set()
    for p in itertools.product(range(4),repeat=3):
        if not any(p):continue
        inv=INV[next(t for t in p if t)]
        P.add(tuple(mul(inv,t) for t in p))
    return sorted(P)
P=points(); B=[p for p in P if set(p)<={0,1}]; O=[p for p in P if p not in B]
assert len(P)==21 and len(B)==7 and len(O)==14

def monoms(degree):
    return [(i,j,degree-i-j) for i in range(degree+1) for j in range(degree+1-i)]
def eval_mon(m,p):
    v=1
    for x,e in zip(p,m):v=mul(v,power(x,e))
    return v

def nullspace(Brows,n):
    R=[list(r) for r in Brows]
    piv=[];h=0
    for c in range(n):
        k=next((i for i in range(h,len(R)) if R[i][c]),None)
        if k is None:continue
        R[h],R[k]=R[k],R[h]
        R[h]=[mul(INV[R[h][c]],v) for v in R[h]]
        for i in range(len(R)):
            if i==h:continue
            w=R[i][c]
            if w:R[i]=[u^mul(w,v) for u,v in zip(R[i],R[h])]
        piv.append(c);h+=1
        if h==len(R):break
    free=[j for j in range(n) if j not in piv]
    basis=[]
    for k in free:
        v=[0]*n;v[k]=1
        for i,j in enumerate(piv):v[j]=R[i][k]
        basis.append(v)
    return h,basis

def census(degree,need_derivatives=False):
    mons=monoms(degree)
    E={p:[eval_mon(m,p) for m in mons] for p in P}
    rank,basis=nullspace([E[p] for p in B],len(mons))
    Eo=[[0]*len(basis) for _ in O]
    for i,p in enumerate(O):
        for j,v in enumerate(basis):
            acc=0
            for c,e in zip(v,E[p]):acc^=mul(c,e)
            Eo[i][j]=acc
    D=[]
    if need_derivatives:
        for p in B:
            dp=[]
            for t in range(3):
                dmono=[]
                for m in mons:
                    mm=list(m)
                    if not (mm[t]%2):dmono.append(0)
                    else:
                        mm[t]-=1;dmono.append(eval_mon(mm,p))
                row=[]
                for v in basis:
                    acc=0
                    for c,e in zip(v,dmono):acc^=mul(c,e)
                    row.append(acc)
                dp.append(row)
            D.append(dp)
    exact=0; nonsing=0; normalized=set(); vectors=[]
    for d in itertools.product(range(4),repeat=len(basis)):
        if not any(d):continue
        if any(not __import__('functools').reduce(lambda a,t:a^mul(t[0],t[1]),zip(d,row),0) for row in Eo):
            continue
        exact+=1
        if need_derivatives:
            if any(all(not __import__('functools').reduce(lambda a,t:a^mul(t[0],t[1]),zip(d,row),0) for row in dp) for dp in D):
                continue
            nonsing+=1
            first=next(x for x in d if x)
            v=[0]*len(mons)
            for coeff,base in zip(d,basis):
                for i,t in enumerate(base):v[i]^=mul(coeff,t)
            v=tuple(mul(INV[first],t) for t in v)
            normalized.add(v);vectors.append(v)
    return len(mons),rank,len(basis),exact,nonsing,normalized

_,r2,d2,e2,_,_=census(2)
_,r3,d3,e3,_,_=census(3)
_,r4,d4,e4,n4,V=census(4,True)
assert (r2,d2,e2)==(6,0,0)
assert (r3,d3,e3)==(7,3,0)
assert (r4,d4,e4,n4,len(V))==(7,8,1080,72,24)
assert all(set(v)<={0,1} for v in V)
print('BAER_EXHAUSTIVE_PASS',r2,d2,e2,r3,d3,e3,r4,d4,e4,n4,len(V))
print('COEFFICIENT_DESCENT_PASS',len(V))
