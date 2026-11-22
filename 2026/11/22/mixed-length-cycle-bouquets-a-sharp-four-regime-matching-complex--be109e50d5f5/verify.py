#!/usr/bin/env python3
"""Finite consistency checks for matching complexes of vertex-bouquets of cycles.
All arithmetic uses explicit finite-field chain boundaries; no external dependencies.
The checks are finite corroboration, not a proof of the general statement.
"""
from itertools import combinations, product
from collections import defaultdict

def edges_for_petals(lengths):
    e=[];v=1
    for n in lengths:
        vertices=[0]+list(range(v,v+n-1))
        e.extend(tuple(sorted((vertices[j],vertices[(j+1)%n]))) for j in range(n))
        v+=n-1
    assert len(set(e))==sum(lengths)
    return e

def make_faces(edges):
    faces={():None}
    for i,(a,b) in enumerate(edges):
        for face in list(faces):
            if all(a not in edges[j] and b not in edges[j] for j in face):
                faces[face+(i,)]=None
    out=defaultdict(list)
    for face in faces:
        if face:out[len(face)-1].append(face)
    for v in out:out[v].sort()
    return out

def rank_mod(columns,p):
    piv={}
    for col in columns:
        x=dict(col)
        while x:
            row=min(x)
            coef=x[row]%p
            if coef==0:
                del x[row];continue
            if row not in piv:
                z=pow(coef,-1,p)
                piv[row]={k:(v*z)%p for k,v in x.items() if v%p}
                break
            for k,v in piv[row].items():
                x[k]=(x.get(k,0)-coef*v)%p
                if not x[k]:del x[k]
    return len(piv)

def bettis(lengths,p):
    faces=make_faces(edges_for_petals(lengths))
    dims=sorted(faces); ranks={-1:0}
    for d in dims[1:]:
        lower={f:i for i,f in enumerate(faces[d-1])}
        cols=[]
        for f in faces[d]:
            cols.append({lower[f[:i]+f[i+1:]]:(-1 if i%2 else 1)%p for i in range(len(f))})
        ranks[d]=rank_mod(cols,p)
    # dimension of B_0 is 0; use reduced H0 by dropping one
    return {d:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d in dims}, sum(map(len,faces.values()))

def expected(lengths):
    zero=sum(n%3==0 for n in lengths)
    two=sum(n%3==2 for n in lengths)
    S=sum(n//3 for n in lengths)
    if zero>=2:return {}
    if zero==1:return {S-1:2}
    if two==0:return {S-1:1}
    return {S:2*two-1}

def check(case):
    target=expected(case)
    prior=None
    for p in (2,3,5):
        b,num=bettis(case,p)
        actual={d:r for d,r in b.items() if r}
        assert actual==target,(case,p,actual,target)
        prior=num
    return prior

def main():
    cases=[]
    for k in range(1,4):
        cases.extend(tuple(x) for x in combinations((3,4,5,6,7,8),k) if sum(x)<=19)
        cases.extend(tuple(x) for x in combinations((3,3,4,4,5,5),k) if sum(x)<=19)
    cases=sorted(set(cases))
    count=0; maxfaces=0
    for case in cases:
        count+=1;maxfaces=max(maxfaces,check(case))
    print('PASS',count,'mixed cycle bouquets, 3 prime fields, largest nonempty face census',maxfaces)
    for q in ((3,3),(3,4),(3,5),(4,5),(5,5),(3,3,5),(3,4,5),(3,5,5),(4,4,5),(4,5,5),(5,5,5)):
        print(q,expected(q))
if __name__=='__main__':main()
