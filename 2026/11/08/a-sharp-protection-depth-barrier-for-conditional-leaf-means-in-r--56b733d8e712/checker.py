"""Exact finite checks for protection-depth conditioned leaf counts in recursive trees."""
from fractions import Fraction as Q
from collections import defaultdict
from itertools import product
from math import factorial

MAX_N=21
MAX_H=10

def add(p,q):
    z=defaultdict(Q,p)
    for d,c in q.items(): z[d]+=c
    return {d:c for d,c in z.items() if c}

def mul(p,q):
    z=defaultdict(Q)
    for d,c in p.items():
        for e,b in q.items(): z[d+e]+=c*b
    return {d:c for d,c in z.items() if c}

# T_h(z,y): labeled EGF for rooted increasing trees whose root is h-protected.
# E_h(z,y) = exp(T_h(z,y)); polynomial coefficients are rational in y.
T=[];E=[]
for h in range(MAX_H+1):
    t=[{} for _ in range(MAX_N+1)]
    e=[{} for _ in range(MAX_N+1)]
    e[0]={0:Q(1)}
    for n in range(1,MAX_N+1):
        if h==0 and n==1:
            t[n]={1:Q(1)}
        elif n>1:
            t[n]={d:c/n for d,c in (e[n-1] if h==0 else E[h-1][n-1]).items()}
        tot={}
        for k in range(1,n+1):
            tot=add(tot,{d:k*c for d,c in mul(t[k],e[n-k]).items()})
        e[n]={d:c/n for d,c in tot.items()}
    T.append(t);E.append(e)

checks=0
for n in range(2,MAX_N+1):
    for h in range(1,min(MAX_H,n-1)+1):
        p=T[h][n]
        S=sum(p.values())
        assert S>0
        mu=sum(k*v for k,v in p.items())/S
        b=Q(n-h+1,2)
        assert (mu==b if (h<=2 or n<=h+3) else mu<b),(h,n,mu,b)
        checks+=1

# Verify the deficit derivative recurrence coefficient by coefficient.
# A_h[n] = coefficient T_h(z,1); B_h[n] = coefficient d_y T_h(z,y)|y=1.
A=[[sum(T[h][n].values()) for n in range(MAX_N+1)] for h in range(MAX_H+1)]
B=[[sum(k*v for k,v in T[h][n].items()) for n in range(MAX_N+1)] for h in range(MAX_H+1)]
D=[[2*B[h][n] -(n-h+1)*A[h][n] for n in range(MAX_N+1)] for h in range(MAX_H+1)]
for h in range(1,MAX_H+1):
    for n in range(MAX_N+1):
        assert (D[h][n] == 0 if h<=2 or n<=h+3 else D[h][n]<0)
        checks+=1

# Independent exhaustive enumeration over all uniform recursive trees up to 9 vertices.
for n in range(2,10):
    obs=defaultdict(lambda:defaultdict(int))
    for par in product(*(range(1,j) for j in range(2,n+1))):
        children=[[] for _ in range(n+1)]
        for child,parent in enumerate(par,start=2):children[parent].append(child)
        depth=[0]*(n+1)
        for j in range(n,0,-1):
            if children[j]: depth[j]=1+min(depth[k] for k in children[j])
        leaves=sum(not children[j] for j in range(1,n+1))
        for h in range(1,depth[1]+1):obs[h][leaves]+=1
    for h in range(1,n):
        predicted={k:int(c*factorial(n)) for k,c in T[h][n].items()}
        assert predicted==dict(obs[h]),(n,h,predicted,dict(obs[h]))
        checks+=len(predicted)+1

# First strict case h=3, n=7: 54 trees, leaf-count profile 1,31,21,1.
p=T[3][7]
assert {k:int(c*factorial(7)) for k,c in p.items()}=={1:1,2:31,3:21,4:1}
assert sum(k*v for k,v in p.items())/sum(p.values())==Q(65,27)
print('PASS',checks,'exact structural and independent-enumeration assertions')
