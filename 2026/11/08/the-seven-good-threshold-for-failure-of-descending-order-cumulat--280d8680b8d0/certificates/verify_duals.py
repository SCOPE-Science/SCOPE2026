#!/usr/bin/env python3
"""Independent exact-arithmetic replay of the finite dual-certificate proof.

Usage: python3 certificates/verify_duals.py
Python standard library only; no numerical optimizer, random tests or internet.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def rows_objective(m, bits):
    if len(bits) != 2*(m-1) or any(x not in '01' for x in bits):
        raise ValueError('invalid sign code')
    h = [-1]+[1 if x=='1' else -1 for x in bits[:m-1]]
    s = [1]+[1 if x=='1' else -1 for x in bits[m-1:]]
    g=[]
    for i in range(m):
        e=[0]*m;e[i]=1
        prev=g[-1] if i else [0]*m
        g.append([h[i]*(prev[j]-e[j]) for j in range(m)])
    n=2*m
    A=[]
    for i in range(m-1):
        row=[0]*n;row[i]=-1;row[i+1]=1;A.append(row)
    row=[0]*n;row[m-1]=-1;A.append(row)
    for d in g:
        A.append([-x for x in d]+[0]*m)
    D=[0]*m
    for i in range(m):
        D[i]+=s[i]
        for sign in (-1,1):
            row=[sign*x for x in D]+[0]*m
            row[m+i]=-1
            A.append(row)
    c=[-sum(g[i][j] for i in range(m)) for j in range(m)]+[1]*m
    assert len(A)==4*m
    return A,c

def check():
    data=json.loads((ROOT/'dual_witnesses.json').read_text(encoding='utf8'))
    assert data['certificate_schema']==1
    cases=data['cases']
    seen=set();counts={m:0 for m in range(2,7)}
    for case in cases:
        m=case['m'];bits=case['bits']
        assert m in counts and isinstance(bits,str)
        key=(m,bits)
        assert key not in seen
        seen.add(key);counts[m]+=1
        A,c=rows_objective(m,bits)
        eta=Q(*case['eta'])
        assert eta>=0
        z=[Q(0)]*len(A)
        prev=-1
        for j,num,den in case['z']:
            assert isinstance(j,int) and prev<j<len(A)
            prev=j
            assert isinstance(num,int) and isinstance(den,int) and den>0 and num>0
            z[j]=Q(num,den)
        for col in range(2*m):
            lhs=-sum(z[r]*A[r][col] for r in range(len(A)))
            if col==0:lhs+=eta
            assert lhs==c[col],(key,col,lhs,c[col])
    for m in counts:
        expected={
            (m,''.join('1' if x==1 else '0' for x in h+s))
            for h in product((-1,1),repeat=m-1)
            for s in product((-1,1),repeat=m-1)
        }
        assert expected.issubset(seen)
        assert counts[m]==4**(m-1)
    # The exact seven-item witness and its global optimum.
    weights=(6,5,5,4,4,1,1)
    d=0;greedy_trace=[]
    for w in weights:
        d=abs(d-w)
        greedy_trace.append(d)
    assert greedy_trace==[6,1,4,0,4,3,2] and sum(greedy_trace)==20
    costs=[]
    for tail in product((-1,1),repeat=6):
        d=0;total=0
        for weight,sign in zip(weights,(1,)+tail):
            d+=sign*weight
            total+=abs(d)
        costs.append(total)
    assert len(costs)==64 and min(costs)==18
    alt=(1,-1,1,-1,-1,1,1)
    d=0;alt_trace=[]
    for weight,sign in zip(weights,alt):
        d+=sign*weight;alt_trace.append(abs(d))
    assert alt_trace==[6,1,6,2,2,1,0] and sum(alt_trace)==18
    print('PASS: 1364 exact rational dual certificates, every sign region for lengths 2-6')
    print('PASS: seven-item greedy 20, exhaustive optimum 18, 64 signed allocations')

if __name__=='__main__':check()
