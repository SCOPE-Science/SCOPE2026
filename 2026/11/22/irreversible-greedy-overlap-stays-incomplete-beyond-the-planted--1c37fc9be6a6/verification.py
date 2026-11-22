#!/usr/bin/env python3
"""Exact finite-state and fluid-limit checks for rate-biased irreversible dimers."""
from fractions import Fraction
from functools import lru_cache
import argparse


def compressed(n, w):
    w = Fraction(w)
    @lru_cache(None)
    def E(k, j):
        if k == 0: return Fraction(0)
        den = Fraction(k*k-j)+w*j
        out = Fraction(0)
        if j:
            out += w*j/den*(1+E(k-1,j-1))
        if j >= 2:
            out += Fraction(j*(j-1),1)/den*E(k-1,j-2)
        if j and k>j:
            out += Fraction(2*j*(k-j),1)/den*E(k-1,j-1)
        if k>j:
            out += Fraction((k-j)**2,1)/den*E(k-1,j)
        return out
    return E(n,n)


def labeled(n,w):
    w=Fraction(w)
    @lru_cache(None)
    def E(left,right):
        if left==0: return Fraction(0)
        edge_weights=[]
        for i in range(n):
            if not(left>>i&1): continue
            for j in range(n):
                if right>>j&1:
                    edge_weights.append((i,j,w if i==j else Fraction(1)))
        total=sum(z for _,_,z in edge_weights)
        return sum((z/total)*((i==j)+E(left^(1<<i),right^(1<<j))) for i,j,z in edge_weights)
    full=(1<<n)-1
    return E(full,full)


def run():
    checked=0
    for n in range(1,7):
        for w in (Fraction(1,3),Fraction(1),Fraction(7,4),Fraction(3*n)):
            a=compressed(n,w);b=labeled(n,w)
            assert a==b,(n,w,a,b)
            checked+=1
    print('exact independent state recurrences:',checked,'checks PASS')
    from scipy.integrate import solve_ivp
    def fluid(c):
        def ode(t,v):
            x,y,s=v
            return (-x*x-c*y,-2*x*y-c*y,c*y)
        sol=solve_ivp(ode,(0,100000),(1,1,0),rtol=1e-10,atol=1e-12,method='DOP853',dense_output=False)
        assert sol.success
        x,y,s=sol.y[:,-1]
        assert x>=-1e-9 and y>=-1e-9 and 0<s<1
        return s,x
    for c in (Fraction(1,10),Fraction(1),Fraction(4),Fraction(10)):
        f,x=fluid(float(c))
        assert 0<f<1-1/(2*(1+float(c)))+1e-8
        print('c=',c,'fluid overlap',round(f,10),'residual mass',round(x,9),'bound',round(1/(2*(1+float(c))),6))
        for n in (20,50,100):
            e=float(compressed(n,c*n))/n
            print(' n=',n,'E[S]/n=',round(e,8))
            assert abs(e-f)<0.2 # finite-size convergence sanity, not a proof
    print('fluid and exact finite sanity checks PASS')
if __name__=='__main__':run()
