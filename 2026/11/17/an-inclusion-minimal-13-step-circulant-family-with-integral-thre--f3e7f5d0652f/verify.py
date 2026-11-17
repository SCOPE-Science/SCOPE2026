"""Exact short-addition certificate for an odd-primary path-homology example.
Usage: python verify.py (requires SymPy)."""
from collections import defaultdict
from pathlib import Path
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

OFFSETS=(-47,-44,-36,-30,-22,-15,-10,-5,0,11)

def steps(t):
    return (1,2,3)+tuple(t+x for x in OFFSETS)

def rels(S):
    assert len(set(S))==len(S) and all(s>0 for s in S)
    groups=defaultdict(list); idx={s:i for i,s in enumerate(S)}
    for i,a in enumerate(S):
        for j in range(i,len(S)):
            b=S[j];v=[0]*len(S);v[i]+=1;v[j]+=1;groups[a+b].append(tuple(v))
    for s in S:
        v=[0]*len(S);v[idx[s]]=1;groups[s].append(tuple(v))
    out=[]
    for sum_val in sorted(groups):
        vectors=groups[sum_val]
        for v in vectors[1:]:
            r=tuple(x-y for x,y in zip(v,vectors[0]))
            if any(r):out.append(r)
    return sorted(out)

def factors(R,n):
    D=smith_normal_form(Matrix(R),domain=ZZ)
    vals=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0]
    return tuple(vals), n-len(vals)

def modrank(rows,p):
    M=[[z%p for z in r] for r in rows]
    if not M:return 0
    rank=0
    for j in range(len(M[0])):
        k=next((k for k in range(rank,len(M)) if M[k][j]),None)
        if k is None:continue
        M[rank],M[k]=M[k],M[rank]
        b=pow(M[rank][j],-1,p)
        M[rank]=[(v*b)%p for v in M[rank]]
        for i in range(rank+1,len(M)):
            f=M[i][j]
            if f:M[i]=[(a-f*b)%p for a,b in zip(M[i],M[rank])]
        rank+=1
    return rank

R109=rels(steps(109))
C=json.loads((Path(__file__).resolve().parent/"CERTIFICATE.json").read_text(encoding="utf8"))
assert C["steps"]==list(steps(109))
assert C["relation_matrix"]==[list(r) for r in R109]
assert C["integer_smith_nonzero_factors"]==[1]*10+[3]
assert len(R109)==13
assert factors(R109,13)==((1,)*10+(3,),2)
assert modrank(R109,3)==10 and modrank(R109,101)==11
for t in (110,111,113,125,191,1009):
    assert rels(steps(t))==R109,(t,'additive-type mismatch')
    assert factors(rels(steps(t)),13)==((1,)*10+(3,),2)
# Independent deletion checks: a torsion-minimal presentation.
for omitted in steps(109):
    S=tuple(s for s in steps(109) if s!=omitted)
    invariant,free=factors(rels(S),12)
    assert all(v==1 for v in invariant),(omitted,invariant)
R93=rels(steps(93))
assert factors(R93,13)==((1,)*11+(3,),1)
print('PASS: 13 generator columns, 13 short-relation rows, rank 11.')
print('PASS: invariant factors 1 x 10 and 3; free rank 2, mod-3 rank 10.')
print('PASS: symbolic offset-type stability at 7 sample parameters; symbolic separation for all t>=109 stated in proof.')
print('PASS: all 13 single-step deletions remove torsion from the short-relation lattice.')
print('PASS: t=93 exceptional group Z + Z/3 (distinct from stable tail).')
