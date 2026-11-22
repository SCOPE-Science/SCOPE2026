#!/usr/bin/env python3
"""Independent finite checks for exact oriented-tree modal validity and labeled EGF."""
from itertools import product
from math import comb
from heapq import heapify,heappop,heappush

N=9

def prod(a,b):
    c=[0]*(N+1)
    for n in range(N+1):
        c[n]=sum(comb(n,k)*a[k]*b[n-k] for k in range(n+1))
    return c

def exponential(a):
    assert a[0]==0
    out=[0]*(N+1); out[0]=1
    for n in range(1,N+1):
        out[n]=sum(comb(n-1,k-1)*a[k]*out[n-k] for k in range(1,n+1))
    return out

def add(*args):return [sum(z[n] for z in args) for n in range(N+1)]
def sub(a,b):return [a[n]-b[n] for n in range(N+1)]
def scalar_z(a):return [0]+[n*a[n-1] for n in range(1,N+1)]
ONE=[1]+[0]*N
f00=f01=f10=f11=[0]*(N+1)
for rep in range(N+1):
    I=add(f10,f11); O=add(f00,f01)
    a=exponential(I); b=exponential(f10); c=exponential(f00)
    next10=scalar_z(a)
    next00=scalar_z(prod(a,add(ONE,O)))
    next11=scalar_z(prod(b,sub(c,ONE)))
    next01=scalar_z(prod(b,sub(sub(c,ONE),f00)))
    f00,f01,f10,f11=next00,next01,next10,next11
root=add(f00,f01)
counts={n:root[n]//n for n in range(1,N+1)}
assert all(root[n]%n==0 for n in counts)
print('EGF_VALID_ORIENTED_LABELLED_TREES',counts)

def prufer_edges(n,seq):
    if n==1:return []
    deg=[1]*n
    for a in seq:deg[a]+=1
    Q=[i for i,d in enumerate(deg) if d==1];heapify(Q)
    E=[]
    for a in seq:
        v=heappop(Q); E.append((v,a)); deg[v]-=1;deg[a]-=1
        if deg[a]==1:heappush(Q,a)
    E.append(tuple(i for i,d in enumerate(deg) if d==1))
    return E

def valid_via_branch(n,E,orient):
    out=[0]*n
    for i,(u,v) in enumerate(E):
        out[(u,v)[(orient>>i)&1]]+=1
    return not any(out[u]>=2 and out[v]>=2 for u,v in E)

def valid_via_semantics(n,E,orient):
    succ=[0]*n
    for i,(u,v) in enumerate(E):
        a,b=(u,v) if not (orient>>i)&1 else (v,u)
        succ[a] |= 1<<b
    full=(1<<n)-1
    for values in range(1<<n):
        delta=[(succ[u]&values ==0 or succ[u]&values==succ[u]) for u in range(n)]
        delta_mask=sum(1<<u for u in range(n) if delta[u])
        for u in range(n):
            if delta[u] and not ((succ[u]&delta_mask==0) or (succ[u]&delta_mask==succ[u])):
                return False
    return True

for n in range(1,8):
    total=0; tree_cases=0;orientation_cases=0
    for seq in product(range(n),repeat=max(0,n-2)) if n>=2 else [()]:
        E=prufer_edges(n,seq);tree_cases+=1
        for orient in range(1<<(n-1)):
            actual=valid_via_branch(n,E,orient)
            if n<=6:
                semantic=valid_via_semantics(n,E,orient)
                assert actual==semantic,(n,E,orient,actual,semantic)
            total+=actual
            orientation_cases+=1
    assert counts[n]==total,(n,counts[n],total)
    print('VERIFIED',n,'labelled_trees',tree_cases,'orientations',orientation_cases,'satisfying',total,'semantic_crosscheck',n<=6)
print('VERIFY_OK')

# Additional bivariate EGF check with exact integer q-polynomials.
from collections import defaultdict,Counter

def p_add(*ps):
    v=defaultdict(int)
    for p in ps:
        for k,x in p.items():v[k]+=x
    return {k:x for k,x in v.items() if x}
def p_mul(a,b):
    v=defaultdict(int)
    for i,x in a.items():
        for j,y in b.items():v[i+j]+=x*y
    return {k:x for k,x in v.items() if x}
def p_neg(a):return {i:-x for i,x in a.items()}
def p_scale(a,v):return {i:v*x for i,x in a.items() if v*x}
def p_q(a):return {i+1:x for i,x in a.items()}
Z=[{} for _ in range(N+1)]
UNIT=[{0:1}]+[{} for _ in range(N)]
def pp_sum(*arr):return [p_add(*(a[n] for a in arr)) for n in range(N+1)]
def pp_sub(a,b):return pp_sum(a,[p_neg(p) for p in b])
def pp_mul(a,b):return [p_add(*(p_scale(p_mul(a[k],b[n-k]),comb(n,k)) for k in range(n+1))) for n in range(N+1)]
def pp_exp(a):
    assert not a[0]
    h=[{} for _ in range(N+1)];h[0]={0:1}
    for n in range(1,N+1):
        h[n]=p_add(*(p_scale(p_mul(a[k],h[n-k]),comb(n-1,k-1)) for k in range(1,n+1)))
    return h
def pp_z(a,q=False):return [{}]+[p_q(p_scale(a[n-1],n)) if q else p_scale(a[n-1],n) for n in range(1,N+1)]
pa=pb=pc=pd=[{} for _ in range(N+1)]
for repeat in range(N+1):
    I=pp_sum(pa,pb);O=pp_sum(pc,pd)
    eI=pp_exp(I);eA=pp_exp(pa);eC=pp_exp(pc)
    pa,pb,pc,pd=(pp_z(eI),pp_z(pp_mul(eA,pp_sub(eC,UNIT)),True),pp_z(pp_mul(eI,pp_sum(UNIT,O))),pp_z(pp_mul(eA,pp_sub(pp_sub(eC,UNIT),pc)),True))
polyroot=pp_sum(pc,pd)
poly={n:{j:c//n for j,c in polyroot[n].items()} for n in range(1,N+1)}
assert all(c%n==0 for n in poly for c in polyroot[n].values())
assert all(sum(poly[n].values())==counts[n] for n in poly)
expected={1:{0:1},2:{0:2},3:{0:9,1:3},4:{0:64,1:64},5:{0:625,1:1255,2:60},6:{0:7776,1:26196,2:4320},7:{0:117649,1:599529,2:216510,3:3360}}
for n,e in expected.items():assert poly[n]==e,(n,poly[n],e)
print('BIVARIATE_EGF_POLYNOMIALS',poly)
print('BIVARIATE_VERIFY_OK')
