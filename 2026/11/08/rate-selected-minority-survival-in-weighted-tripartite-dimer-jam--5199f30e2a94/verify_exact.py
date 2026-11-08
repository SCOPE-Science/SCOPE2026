#!/usr/bin/env python3
"""Exact rational tests for edge-weighted dimer adsorption on tripartite graphs."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product

@lru_cache(None)
def counts(i,j,k,r):
    den=i*j+i*k+r*j*k
    if not den:
        return {(i,j,k): Q(1)}
    out={}
    for rate,sub in ((i*j,(i-1,j-1,k)),(i*k,(i-1,j,k-1)),(r*j*k,(i,j-1,k-1))):
        if not rate:continue
        for state,p in counts(*sub,r).items():
            out[state]=out.get(state,Q(0))+Q(rate,den)*p
    return out

def brute(i,j,k,r):
    colors=(0,)*i+(1,)*j+(2,)*k
    N=len(colors)
    @lru_cache(None)
    def f(mask):
        ed=[]
        for u in range(N):
            if not(mask>>u)&1:continue
            for v in range(u+1,N):
                if not(mask>>v)&1 or colors[u]==colors[v]:continue
                weight=r if {colors[u],colors[v]}=={1,2} else Q(1)
                ed.append((u,v,weight))
        if not ed:
            return {tuple(sum((mask>>v)&1 and colors[v]==c for v in range(N)) for c in range(3)):Q(1)}
        den=sum(w for _,_,w in ed)
        ans={}
        for u,v,w in ed:
            for st,p in f(mask&~(1<<u)&~(1<<v)).items():
                ans[st]=ans.get(st,Q(0))+w/den*p
        return ans
    return f((1<<N)-1)

for rho in (Q(1,2),Q(1),Q(3,2),Q(2),Q(3)):
    for a,b,c in product(range(1,4),repeat=3):
        if a+b+c>7:continue
        p=counts(a,b,c,rho)
        assert sum(p.values())==1
        assert p==brute(a,b,c,rho), (a,b,c,rho,p,brute(a,b,c,rho))
        assert all(sum(bool(n) for n in st)<=1 for st in p)
print('PASS: exact weighted count-state law equals independent labeled-edge recursion (all positive a,b,c<=3, sum<=7, five rational rates).')
for rho in (Q(1),Q(3,2),Q(2),Q(3)):
    for n in (2,3,4,5):
        law=counts(n,n,n,rho)
        p_A=sum(p for (i,j,k),p in law.items() if i>0)
        mean_A=sum(i*p for (i,j,k),p in law.items())
        print('rho=',rho,'n=',n,'P(A survives)=',p_A,'E[remaining A]=',mean_A)
