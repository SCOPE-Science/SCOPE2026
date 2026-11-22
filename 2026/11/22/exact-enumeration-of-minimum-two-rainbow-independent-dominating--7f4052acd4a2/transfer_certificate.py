#!/usr/bin/env python3
"""Exact finite-state certificate for two-colour independent rainbow domination of cycle prisms."""
from itertools import product
from collections import Counter
import sympy as sp

COL = [s for s in product((0,1,2), repeat=2) if not (s[0] == s[1] != 0)]
compatible = lambda a,b: all(not (a[r] == b[r] != 0) for r in (0,1))
PAIRS = [(a,b) for a in COL for b in COL if compatible(a,b)]
INDEX = {p:i for i,p in enumerate(PAIRS)}

def legal(a,b,c):
    if not compatible(a,b) or not compatible(b,c): return False
    for r in (0,1):
        if b[r] == 0 and {1,2} - {a[r], b[1-r], c[r]}: return False
    return True

def phi(a,b):
    return -int(a==(0,0) and b in ((1,2),(2,1)))

m=len(PAIRS); B=sp.zeros(m); arcs=0; tight=0; reduced=Counter()
for i,(a,b) in enumerate(PAIRS):
    for c in COL:
        if not legal(a,b,c):continue
        j=INDEX[(b,c)]; w=int(b[0]!=0)+int(b[1]!=0)
        cost=w-1+phi(a,b)-phi(b,c)
        assert cost>=0,('negative reduced arc',(a,b,c,cost))
        arcs+=1; reduced[cost]+=1
        if cost==0:B[i,j]=1;tight+=1
assert m==35 and arcs==70 and tight==46
x=sp.symbols('x')
characteristic=sp.factor(B.charpoly(x).as_expr())
expected=x**25*(x-2)*(x-1)*(x+1)**4*(x*x+1)*(x*x-x+2)
assert sp.expand(characteristic-expected)==0
print('COLUMN_STATES=',len(COL),'PAIR_STATES=',m,'LEGAL_ARCS=',arcs,'TIGHT_ARCS=',tight)
print('REDUCED_COST_HISTOGRAM=',sorted(reduced.items()))
print('CHARACTERISTIC=',characteristic)

# Disjoint recurrent blocks give an independent check of the determinant.
# Tarjan strong-component analysis is implemented here without graph libraries.
def components(adj):
    timer=0; indices={}; low={}; stack=[]; active=set(); out=[]
    def dfs(v):
        nonlocal timer
        indices[v]=low[v]=timer; timer+=1; stack.append(v);active.add(v)
        for w in adj[v]:
            if w not in indices: dfs(w);low[v]=min(low[v],low[w])
            elif w in active:low[v]=min(low[v],indices[w])
        if low[v]==indices[v]:
            comp=[]
            while True:
                w=stack.pop();active.remove(w);comp.append(w)
                if w==v:break
            out.append(sorted(comp))
    for v in range(len(adj)):
        if v not in indices:dfs(v)
    return sorted(out,key=lambda c:(-len(c),c))
adj=[[j for j in range(m) if B[i,j]] for i in range(m)]
scc=components(adj)
assert sorted(map(len,scc))==[1]*19+[4,12]
expected_blocks={12:x**6*(x-2)*(x+1)**3*(x*x-x+2),4:(x-1)*(x+1)*(x*x+1)}
for comp in scc[:2]:
    block=B.extract(comp,comp)
    cp=sp.factor(block.charpoly(x).as_expr())
    assert sp.expand(cp-expected_blocks[len(comp)])==0
    print('RECURRENT_COMPONENT',len(comp),'STATE_IDS',comp,'BLOCK_CHARPOLY',cp)
print('TRANSIENT_SINGLETON_COMPONENTS',19)
C=sp.eye(m)
u=[2,1]
for n in range(2,81):u.append(u[-1]-2*u[-2])
for n in range(1,41):
    C=C*B
    exact=int(sp.trace(C)); expected_count=2**n+1+4*(-1)**n+(2 if n%4==0 else -2 if n%4==2 else 0)+u[n]
    assert exact==expected_count,(n,exact,expected_count)
    if 3<=n<=14: print('OPTIMUM_COUNT',n,exact)
print('ALL_N_1_TO_40_MATCH_RECURRENCE')
