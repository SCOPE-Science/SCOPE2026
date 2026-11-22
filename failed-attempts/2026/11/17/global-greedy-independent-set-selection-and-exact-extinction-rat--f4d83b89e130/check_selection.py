"""Reproducible symbolic identities and finite-trajectory checks for a directed vacancy-limited competitive chain.

Requires Python 3, NumPy, SciPy, and SymPy. Numerical tests are not a proof
of the all-dimensional or infinite-time theorem.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def symbolic_check(n=6):
    x=sp.symbols('x0:'+str(n), positive=True)
    r,d=sp.symbols('r d',positive=True)
    p=sp.symbols('p0:'+str(n-1),positive=True)
    s=sum(x)
    dx=[x[i]*(r*(1-s)-d-(p[i-1]*x[i-1] if i else 0)) for i in range(n)]
    assert sp.simplify(sum(dx)-((r-d)*s-r*s*s-sum(p[i-1]*x[i-1]*x[i] for i in range(1,n))))==0
    for i in range(1,n):
        deriv=sp.simplify((dx[i]*x[0]-x[i]*dx[0])/x[0]**2)
        assert sp.simplify(deriv+p[i-1]*x[i-1]*x[i]/x[0])==0
    return n-1


def greedy_indices(initial):
    result=[]; predecessor_selected=False
    for i,u in enumerate(initial):
        selected=(u>0 and not predecessor_selected)
        if selected:result.append(i)
        predecessor_selected=selected
    return result


def sample_check(initial, r, d, p, duration=350):
    n=len(initial)
    init=np.array(initial,dtype=float)
    assert np.any(init>0) and sum(init)<1
    def rhs(t,u):
        x=u[:n]; s=sum(x)
        growth=(r*(1-s)-d)*np.ones(n)
        growth[1:]-=p*x[:-1]
        return np.r_[x*growth,x]
    sol=solve_ivp(rhs,(0,duration),np.r_[init,np.zeros(n)],method='DOP853',rtol=2e-12,atol=2e-14)
    assert sol.success
    x=sol.y[:n,-1]; integrals=sol.y[n:,-1]
    K=1-d/r
    picked=greedy_indices(init)
    assert abs(sum(x)-K)<3e-6,(picked,sum(x),K)
    for i in range(n):
        if i in picked:assert x[i]>3e-4,(i,x,picked)
        else:assert abs(x[i])<3e-6,(i,x,picked)
    m=min(np.flatnonzero(init>0))
    for i in picked:
        if i>m:
            predicted=(init[i]/init[m])*math.exp(-p[i-1]*integrals[i-1])
            assert abs(x[i]/x[m]-predicted)<1e-8,(i,predicted,x[i]/x[m])
    for i in range(1,n):
        if i not in picked and init[i]>0 and i-1 in picked:
            predicted=-p[i-1]*x[i-1]
            observed=-p[i-1]*integrals[i-1]/duration
            # The integral form avoids underflow in exponentially extinct coordinates.
            assert abs(observed-predicted)<0.04,(i,observed,predicted)
    return len(picked)


def main():
    assert symbolic_check()==5
    rng=np.random.default_rng(20261108)
    p=np.array([1.9,2.5,2.1,2.7,2.4,2.2,2.6])
    masks=[0b11111111,0b11111110,0b01011011,0b10111010,0b01101101,0b01010101,0b10001001,0b00000001,0b10000000]
    n=8
    tested=0
    for mask in masks:
        init=np.zeros(n)
        support=[j for j in range(n) if mask & (1<<j)]
        picked=greedy_indices([1 if j in support else 0 for j in range(n)])
        for j in support:
            init[j]=(0.65/len(picked) if j in picked else 0.004)
        sample_check(init,1.1,0.17,p)
        tested+=1
    print(f'VERIFY_OK exact_ratio_identities=5 exact_total_identity=1 finite_support_patterns={tested} maximal_independent_selection=1')

if __name__=='__main__': main()
