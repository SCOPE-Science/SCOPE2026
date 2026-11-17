#!/usr/bin/env python3
"""Exact combinatorial and integral-chain checks for two ordered points on a generalized theta graph.
No external dependencies. The complete parameter formula is proved separately.
"""
from itertools import permutations
from collections import defaultdict

def complex_data(m):
    # vertices A=0, B=1, and (i,1),(i,2) represented by 2+2*i,3+2*i.
    A,B=0,1
    edges=[]
    for i in range(m):
        u,w=2+2*i,3+2*i
        edges.extend(((A,u),(u,w),(w,B)))
    vertices=range(2+2*m)
    C0=[(u,v) for u in vertices for v in vertices if u!=v]
    C1=[]
    for e,(u,w) in enumerate(edges):
        for v in vertices:
            if v!=u and v!=w:
                C1.extend((('e',e,v),('v',v,e)))
    C2=[(i,j) for i,(a,b) in enumerate(edges) for j,(c,d) in enumerate(edges) if not ({a,b}&{c,d})]
    return edges,C0,C1,C2

def act_v(v,sigma,p):
    if v<2:return v if p==0 else 1-v
    i,j=divmod(v-2,2)
    return 2+2*sigma[i]+(j if p==0 else 1-j)

def act_e(e,sigma,p):
    i,k=divmod(e,3)
    return 3*sigma[i]+(k if p==0 else 2-k),(-1 if p else 1)

def act_cell(cell,dim,sigma,p,t):
    if dim==0:
        a,b=map(lambda x:act_v(x,sigma,p),cell)
        return ((b,a) if t else (a,b)),1
    if dim==1:
        typ,a,b=cell
        if typ=='e':e,s=act_e(a,sigma,p);v=act_v(b,sigma,p);return ((('v',v,e) if t else ('e',e,v))),s
        else:v=act_v(a,sigma,p);e,s=act_e(b,sigma,p);return ((('e',e,v) if t else ('v',v,e))),s
    a,b=cell
    ea,sa=act_e(a,sigma,p); eb,sb=act_e(b,sigma,p)
    return ((eb,ea) if t else (ea,eb)),sa*sb*(-1 if t else 1)

def trace(cells,dim,sigma,p,t):
    return sum(s for c in cells for d,s in [act_cell(c,dim,sigma,p,t)] if d==c)

def known_char(sigma,p,t):
    m=len(sigma);f=sum(sigma[i]==i for i in range(m));c2=sum(sigma[i]!=i and sigma[sigma[i]]==i for i in range(m))//2
    return (-1 if p else 1)*((f*f-f-1) if t==0 else (1-2*c2))

def boundary1(cell,edges):
    typ,a,b=cell
    e,v=(a,b) if typ=='e' else (b,a)
    x,y=edges[e]
    return {(y,v):1,(x,v):-1} if typ=='e' else {(v,y):1,(v,x):-1}

def boundary2(cell,edges):
    i,j=cell
    a,b=edges[i];c,d=edges[j]
    return {('v',b,j):1,('v',a,j):-1,('e',i,d):-1,('e',i,c):1}

def test(m,all_perms=True):
    edges,C0,C1,C2=complex_data(m)
    # Verify full boundary-square identities in integral chains.
    for c in C2:
        b=defaultdict(int)
        for k,n in boundary2(c,edges).items():
            for q,z in boundary1(k,edges).items():b[q]+=n*z
        assert all(x==0 for x in b.values()),(m,c)
    # Check every group element on small m; for m=6 use generators to limit effort.
    perm_list=list(permutations(range(m))) if all_perms else [tuple(range(m))]+[tuple((i+1)%m for i in range(m)),(1,0)+tuple(range(2,m))]
    actions=0
    for sigma in perm_list:
        for p in range(2):
            for t in range(2):
                T=(trace(C0,0,sigma,p,t)-trace(C1,1,sigma,p,t)+trace(C2,2,sigma,p,t))
                got=1-T
                assert got==known_char(sigma,p,t),(m,sigma,p,t,got,known_char(sigma,p,t))
                actions+=1
    # Chain equivariance for natural group generators and every degree 1 and 2 cell.
    generators=[(tuple((i+1)%m for i in range(m)),0,0),(tuple([1,0]+list(range(2,m))),0,0),(tuple(range(m)),1,0),(tuple(range(m)),0,1)]
    for sigma,p,t in generators:
        for x in C1:
            y,sgn=act_cell(x,1,sigma,p,t)
            lhs={q:sgn*z for q,z in boundary1(y,edges).items()}
            rhs=defaultdict(int)
            for q,z in boundary1(x,edges).items():
                q1,s=act_cell(q,0,sigma,p,t);rhs[q1]+=z*s
            assert lhs==dict(rhs)
        for x in C2:
            y,sgn=act_cell(x,2,sigma,p,t)
            lhs={q:sgn*z for q,z in boundary2(y,edges).items()}
            rhs=defaultdict(int)
            for q,z in boundary2(x,edges).items():
                q1,s=act_cell(q,1,sigma,p,t);rhs[q1]+=z*s
            assert lhs==dict(rhs)
    b=m*m-m-1
    print('m',m,'cells',len(C0),len(C1),len(C2),'Euler',len(C0)-len(C1)+len(C2),'b1',b,'symmetries',actions,'chain_equivariance_PASS')
    return actions

if __name__=='__main__':
    s=0
    for m in range(3,7):
        s+=test(m,all_perms=True)
    print('THETA_ORDERED_TWO_PARTICLE_FULL_JOINT_CHARACTER_PASS','actions',s)
