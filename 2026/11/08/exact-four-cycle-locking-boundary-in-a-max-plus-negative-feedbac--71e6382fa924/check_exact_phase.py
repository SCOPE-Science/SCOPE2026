#!/usr/bin/env python3
"""Exact-rational, all-parameter checker for primitive four-periodic states.
The 81 linear-mode words are exhaustive after a proven reduction.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict

def add(*parts):
    return (sum(v[0] for v in parts),sum(v[1] for v in parts))
def neg(v): return (-v[0],-v[1])
def mul(c,v):return (c*v[0],c*v[1])
def solve(mode):
    a=[[Q(0) for _ in range(4)] for _ in range(4)]
    b=[(Q(0),Q(0)) for _ in range(4)]
    for k,s in enumerate(mode):
        a[k][(k+2)%4]+=1
        if s=='D':
            a[k][(k+1)%4]-=1
            b[k]=(Q(1),Q(-1))
        elif s=='H':
            a[k][k]+=2
            b[k]=(Q(1),Q(0))
        else:
            b[k]=(Q(1),Q(0))
    for j in range(4):
        piv=next((i for i in range(j,4) if a[i][j]),None)
        if piv is None:return None
        a[j],a[piv]=a[piv],a[j]
        b[j],b[piv]=b[piv],b[j]
        factor=a[j][j]
        a[j]=[v/factor for v in a[j]]
        b[j]=mul(1/factor,b[j])
        for k in range(4):
            if k==j:continue
            factor=a[k][j]
            if not factor:continue
            a[k]=[a[k][i]-factor*a[j][i] for i in range(4)]
            b[k]=add(b[k],neg(mul(factor,b[j])))
    assert all(a[i][j]==(1 if i==j else 0) for i in range(4) for j in range(4))
    return b

def intervals(word,x):
    lo,hi=Q(3,2),Q(2)
    constraints=[]
    for i in range(4):
        v=x[i]; w=x[(i+1)%4]
        constraints += [add(v,(Q(1),Q(0))),add((Q(1),Q(0)),neg(v))] # -1<=x<=1
        if word[i]=='D':
            constraints += [v,add(mul(2,v),w,(Q(0),Q(-1)))]
        elif word[i]=='H':
            constraints += [v,add((Q(0),Q(1)),neg(mul(2,v)),neg(w))]
        else:
            constraints += [neg(v),add((Q(0),Q(1)),neg(w))]
    for a,b in constraints:
        if b>0:lo=max(lo,-a/b)
        elif b<0:hi=min(hi,-a/b)
        elif a<0:return None
        if lo>hi:return None
    if lo<=hi and (hi>Q(3,2) and lo<Q(2)):
        return (lo,hi)
    return None

def map_f(x,y,t):
    return (max(x-t,y),max(y+Q(1)-t,Q(1)-max(Q(0),2*x)))
def period(x,t):
    z=(x[0],x[1]); o=z
    for k in range(1,5):
        z=map_f(*z,t)
        if z==o:return k
    raise AssertionError((x,t,z,o))

def main():
    hits=[]
    singular=[]
    for mode in product('DHS',repeat=4):
        word=''.join(mode)
        vals=solve(word)
        if vals is None:
            singular.append(word);continue
        iv=intervals(word,vals)
        if iv is not None:
            hits.append((word,iv,tuple(vals)))
    print('singular:',singular)
    print('valid mode words:')
    for word,iv,vals in hits:
        print(word,iv,[f'{z[0]}+({z[1]})t' for z in vals])
        mid=(max(iv[0],Q(3,2))+min(iv[1],Q(2)))/2
        for t in set([mid,iv[0],iv[1]]):
            if not Q(3,2)<t<Q(2):continue
            z=tuple(a+b*t for a,b in vals)
            assert period(z,t) in (1,4),(word,t,z)
    assert singular==['DDDD']
    assert len(hits)==9,len(hits)
    assert {w for w,iv,v in hits}=={'HHHH','DDHS','DHSD','DHSH','HDHS','HSDD','HSHD','SDDH','SHDH'}
    for t,expected in [(Q(8,5),0),(Q(5,3),1),(Q(7,4),2)]:
        cycles=set()
        for word,iv,vals in hits:
            if iv[0]<=t<=iv[1]:
                x=tuple(a+b*t for a,b in vals)
                if period(x,t)==4:cycles.add(min(tuple(x[i:]+x[:i]) for i in range(4)))
        print('t=',t,'four-cycles=',len(cycles),cycles)
        assert len(cycles)==expected
    jac = {'H':((0,1),(-2,0)),'S':((0,1),(0,0)),'D':((0,1),(0,1))}
    def matmul(A,B):
        return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    expected_jac = {'HSDD':((0,0),(0,0)),'HSHD':((4,0),(4,0))}
    for mode, exp in expected_jac.items():
        matrix=((1,0),(0,1))
        for c in mode:matrix=matmul(jac[c],matrix)
        assert matrix==exp
    print('All exact mode-word, primitive-period and return-multiplier checks passed.')
if __name__=='__main__':main()
