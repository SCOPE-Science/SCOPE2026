#!/usr/bin/env python3
"""Exact, standalone state-enumeration checks for third edge cumulants on theta networks."""
from fractions import Fraction as F
from itertools import product
from math import gcd

def theta(lengths):
    assert len(lengths)==3 and all(L>=2 for L in lengths)
    edges=[];paths=[]; nxt=2
    for L in lengths:
        cur=0; indices=[]
        for j in range(L):
            if j+1==L:target=1
            else:target=nxt;nxt+=1
            indices.append(len(edges));edges.append((cur,target));cur=target
        paths.append(indices)
    return nxt,edges,paths

def weighted_moments(n,edges,weights,q,marks):
    Z=M1=M2=M3=M12=M13=M23=M123=F(0)
    for mask in range(1<<len(edges)):
        par=list(range(n))
        def root(u):
            while par[u]!=u:u=par[u]
            return u
        val=F(1)
        for j,(a,b) in enumerate(edges):
            if mask>>j&1:
                a,b=root(a),root(b)
                if a!=b:par[a]=b
                val*=weights[j]
        val*=q**len(set(root(i) for i in range(n)))
        Z+=val
        on=[bool(mask>>e&1) for e in marks]
        if on[0]:M1+=val
        if on[1]:M2+=val
        if on[2]:M3+=val
        if on[0] and on[1]:M12+=val
        if on[0] and on[2]:M13+=val
        if on[1] and on[2]:M23+=val
        if all(on):M123+=val
    return (M123*Z*Z-(M12*M3+M13*M2+M23*M1)*Z+2*M1*M2*M3)/Z**3

def formula(paths,weights,q,marks):
    p=[v/(q+v) for v in weights]
    a,b,c=[prod(p[i] for i in path) for path in paths]
    e1=a+b+c;e2=a*b+a*c+b*c;e3=a*b*c
    H=1+(q-1)*e2+(q-1)*(q-2)*e3
    Fq=(2-q)+2*(q-1)*e1+(q-1)*(q-2)*e2+(q-1)*(q*q-2*q+2)*e3
    return -(q-1)*e3*prod(1-p[i] for i in marks)*Fq/H**3

def prod(vals):
    z=F(1)
    for v in vals:z*=v
    return z

def run():
    checks=0
    for lengths in [(2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,2,4)]:
        n,edges,paths=theta(lengths)
        for q in [F(3,2),F(2),F(3),F(4)]:
            for scale in [F(1,10),F(1),F(10)]:
                weights=[scale*F(j+1,j+3) for j in range(1,len(edges)+1)]
                for marks in product(*paths):
                    got=weighted_moments(n,edges,weights,q,marks)
                    want=formula(paths,weights,q,marks)
                    assert got==want,(lengths,q,scale,marks,got,want)
                    checks+=1
    # For uniform K_{2,3} at q=3, low and high activities have opposite signs.
    n,edges,paths=theta((2,2,2))
    low=weighted_moments(n,edges,[F(1,10)]*len(edges),F(3),[path[0] for path in paths])
    high=weighted_moments(n,edges,[F(10)]*len(edges),F(3),[path[0] for path in paths])
    assert low>0 and high<0
    print('THETA_CUMULANT_EXACT_PASS',checks,'low_sign=+','high_sign=-')
if __name__=='__main__':run()
