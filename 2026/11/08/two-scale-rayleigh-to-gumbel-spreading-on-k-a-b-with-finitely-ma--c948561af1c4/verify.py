"""Reproducibility checks for two-scale push--pull spreading on K(a,b)."""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, comb, exp, sqrt
from scipy.integrate import solve_ivp
import numpy as np


def lumped_expectation(a,b):
    c=Q(1,a)+Q(1,b)
    @lru_cache(None)
    def F(h,l):
        if (h,l)==(a,b): return Q(0)
        Rleaf=(b-l)*h*c
        Rhub=(a-h)*l*c
        total=Rleaf+Rhub
        return (Q(1)+Rleaf*(F(h,l+1) if l<b else 0)+Rhub*(F(h+1,l) if h<a else 0))/total
    return F(1,0)

def labeled_expectation(a,b):
    N=a+b
    adjacency=[[j for j in range(a,N)] for i in range(a)] + [list(range(a)) for _ in range(b)]
    @lru_cache(None)
    def F(mask):
        if mask==(1<<N)-1:return Q(0)
        nxt={}
        for u in range(N):
            if not ((mask>>u)&1):continue
            for v in adjacency[u]:
                if (mask>>v)&1:continue
                rate=Q(1,len(adjacency[u]))+Q(1,len(adjacency[v]))
                nxt[mask | (1<<v)]=nxt.get(mask |(1<<v),Q(0))+rate
        s=sum(nxt.values(),Q(0))
        return (1+sum((r*F(nm) for nm,r in nxt.items()),Q(0)))/s
    return F(1)

def second_hub_moment_a2(b):
    c=Q(1,2)+Q(1,b)
    # integrate exp(-b*c*t)*(1+c*t)^b dt exactly.
    return sum((Q(comb(b,j)*factorial(j), b**(j+1)) for j in range(b+1)),Q(0))/c

def second_hub_markov_a2(b):
    c=Q(1,2)+Q(1,b)
    @lru_cache(None)
    def F(l):
        le=(b-l)*c
        he=l*c
        if not le:return Q(1,he)
        return (Q(1)+le*F(l+1))/(le+he)
    return F(0)

def survival_formula(a,b,t):
    c=1/a+1/b
    if a==2:return (exp(-c*t)*(1+c*t))**b
    return (((a-1)*exp(-c*t)-exp(-(a-1)*c*t))/(a-2))**b

def survival_generator(a,b,t):
    # transient states (h=1, l=0..b): absorbing on first second-hub event
    c=1/a+1/b
    Qmat=np.zeros((b+1,b+1))
    for l in range(b+1):
        birth=(b-l)*c
        kill=(a-1)*l*c
        Qmat[l,l]=-(birth+kill)
        if l<b:Qmat[l,l+1]=birth
    e=np.zeros(b+1);e[0]=1
    return float(sum(solve_ivp(lambda u,p: p @ Qmat, (0,t), e, rtol=2e-13, atol=2e-15).y[:,-1]))

def main():
    exact=0
    for a in range(2,5):
        for b in range(2,7):
            x=lumped_expectation(a,b)
            y=labeled_expectation(a,b)
            assert x==y,(a,b,x,y)
            exact+=1
    for b in range(1,15):
        assert second_hub_moment_a2(b)==second_hub_markov_a2(b), b
    survival=0
    for a in (2,3,4,6):
        for b in (1,2,5,12):
            for t in (0.1,0.35,1.1):
                x=survival_formula(a,b,t)
                y=survival_generator(a,b,t)
                assert abs(x-y)<1e-11,(a,b,t,x,y)
                survival+=1
    # Exact finite a=2 first-hub Rayleigh at x=1 and early limit tendency
    limits=[]
    for b in (100,1000,10000):
        x=survival_formula(2,b,2/sqrt(b))
        limits.append(abs(x-exp(-0.5)))
    assert limits[2]<limits[1]<limits[0]
    print(f'PASS: {exact} labeled-vs-lumped rational expectations; 14 exact first-hub moments; {survival} finite survival comparisons; Rayleigh convergence diagnostics {limits}')

if __name__=='__main__':main()
