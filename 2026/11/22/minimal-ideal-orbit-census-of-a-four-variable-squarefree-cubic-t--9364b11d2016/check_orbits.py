#!/usr/bin/env python3
"""Independent finite-field orbit enumeration for minimal ideals of squarefree cubic-truncated algebras.
No external libraries. Uses induced actions on the degree-two socle and BFS of projective vectors.
"""
from collections import Counter
from itertools import product
from math import gcd

EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
EDGE_NO = {e:i for i,e in enumerate(EDGES)}

def table(q):
    if q in (2,3,5,7,11):
        return (lambda a,b:(a+b)%q),(lambda a,b:(a*b)%q),2 if q in (3,5,11) else (3 if q==7 else 1)
    if q==4:
        def mul(a,b):
            v=0
            for k in range(2):
                if (b>>k)&1:v^=a<<k
            if v&4:v^=0b111 # x^2 = x+1
            return v
        return (lambda a,b:a^b),mul,2
    raise ValueError(q)

def normalize(v, q, mul):
    x=next((x for x in v if x),None)
    if x is None: return None
    inv=next(z for z in range(1,q) if mul(x,z)==1)
    return tuple(mul(z,inv) for z in v)

def apply_matrix(v, M, q, add, mul):
    res=[0]*6
    for col,(i,j) in enumerate(EDGES):
        if not v[col]:continue
        for row,(k,l) in enumerate(EDGES):
            coeff=add(mul(M[k][i],M[l][j]),mul(M[l][i],M[k][j]))
            res[row]=add(res[row],mul(v[col],coeff))
    return normalize(res,q,mul)

def identity():return [[int(i==j) for j in range(4)] for i in range(4)]

def generators(q):
    a, m, primitive=table(q)
    matrices=[]
    for i in range(3):
        M=identity()
        M[i],M[i+1]=M[i+1],M[i]
        matrices.append(M)
    if q%2:
        for i in range(4):
            M=identity();M[i][i]=primitive;matrices.append(M)
    else:
        for i in range(3):
            M=identity();M[i][i+1]=1;matrices.append(M)
        if q>2:
            M=identity();M[0][0]=primitive;matrices.append(M)
    return matrices

def orbit_census(q):
    add,mul,g=table(q)
    seen=set(); count=0; sizes=[]
    mats=generators(q)
    graph_counts=Counter()
    for vec in product(range(q),repeat=6):
        norm=normalize(vec,q,mul)
        if norm is None or norm in seen:continue
        queue=[norm];seen.add(norm);p=0
        while p<len(queue):
            x=queue[p];p+=1
            for M in mats:
                y=apply_matrix(x,M,q,add,mul)
                if y not in seen:
                    seen.add(y);queue.append(y)
        sizes.append(len(queue)); count+=1
        if q%2:
            e=sum(bool(z) for z in norm)
            graph_counts[e]+=1
    expected=(q*q+7*q+46+2*gcd(3,q-1))//6 if q%2 else 2
    assert count==expected,(q,count,expected)
    assert sum(sizes)==(q**6-1)//(q-1),(q,sum(sizes))
    print('field_order=',q,'orbit_count=',count,'predicted=',expected,'points=',sum(sizes),'orbits_by_support_size=',dict(sorted(graph_counts.items())))

if __name__=='__main__':
    for q in (2,3,4,5,7):orbit_census(q)
