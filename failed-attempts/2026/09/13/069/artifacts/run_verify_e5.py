from fractions import Fraction
import json
from rowsutil import le_lin
def sysrows(A,M,wn):
    R=[]
    def add(terms,rhs,sense):
        d={}
        for i,c in terms: d[i]=d.get(i,0)+c
        R.append((d,rhs,sense))
    for i in range(1,6):
        for j in range(1,6):
            s=i+j
            if s<6: add([(s,1),(i,-1),(j,-1)],0,'<=')
            elif s>6: add([(s-6,1),(i,-1),(j,-1)],1,'<=')
    for p in M:
        for q in range(1,6):
            if q==p: continue
            d,off=le_lin(p,q)
            add([(q,1),(p,-1),(d,-1)],-1-off,'<=')
    for a in A:
        for j in range(1,6):
            if j==a: continue
            d,off=le_lin(j,a)
            add([(a,1),(j,-1),(d,-1)],-1-off,'<=')
    nonmin=[j for j in range(1,6) if j not in A]
    for j,a in zip(nonmin,wn):
        d,off=le_lin(a,j)
        add([(j,1),(a,-1),(d,-1)],off,'>=')
    for i in range(1,6):
        add([(i,1)],1,'>=')
    return R
import ast
certs=json.load(open("e5certs.json"))
assert len(certs)==800
for key,cert in certs.items():
    sa,sm,sw=key.split("|")
    A=tuple(ast.literal_eval(sa)); M=tuple(ast.literal_eval(sm)); wn=tuple(ast.literal_eval(sw))
    R=sysrows(A,M,wn)
    A1=[r for r in R if r[2]=='<=']; A2=[r for r in R if r[2]=='>=']
    Y=[(j,Fraction(v)) for j,v in cert["Y"]]; Z=[(j,Fraction(v)) for j,v in cert["Z"]]
    assert all(v>=0 for _,v in Y+Z)
    for i in range(1,6):
        s=sum(v*(-A1[j][0].get(i,0)) for j,v in Y)+sum(v*(A2[j][0].get(i,0)) for j,v in Z)
        assert s==0,(key,i,s)
    v=sum(v*(-A1[j][1]) for j,v in Y)+sum(v*(A2[j][1]) for j,v in Z)
    assert v>0,(key,v)
print("lemma-A certs exactly verified: 800")
