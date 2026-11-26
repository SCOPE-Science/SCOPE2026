"""Reproduce the finite checks for exact reversible mixing on Mobius ladders.

Run: python verify_mobius.py
Requires numpy and scipy (see requirements.txt).
This tests examples of an analytically established infinite-family theorem;
finite computations alone do not prove the theorem or literature novelty.
"""
import math
import numpy as np
from scipy.optimize import linprog

checks = 0

def check(condition, what):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(what)

def near(x, y, tol=3e-9):
    return abs(float(x)-float(y)) <= tol

def data(m):
    t=math.pi/m
    E=2-2*math.cos(2*t)
    U=2-2*math.cos(t)
    V=4 if m%2 else 2+2*math.cos(t)
    D=V+2*E-U
    a=2/D
    b=(E-U)/D
    h=(V+E-4)/D
    mu=(V-U)/D
    return E,U,V,D,a,b,h,mu

def mode(m,j,a,b):
    delta=2-2*math.cos(math.pi*j/m)
    return 1-a*delta-2*b*(j%2)

def independent_lp(m):
    # This LP is assembled from all frequencies, not just certificate modes.
    A=[];B=[]
    for j in range(1,2*m):
        delta=2-2*math.cos(math.pi*j/m)
        z=2*(j%2)
        A.extend([[delta,z,-1],[-delta,-z,-1]])
        B.extend([1,-1])
    A.append([2,1,0]);B.append(1)
    r=linprog([0,0,1],A_ub=A,b_ub=B,bounds=[(0,None)]*3,method='highs')
    check(r.success, f'LP feasibility m={m}: {r.message}')
    return r.x

for m in range(4,121):
    E,U,V,D,a,b,h,mu=data(m)
    check(E>U>0 and V>U and D>0, ('domain',m))
    check(a>0 and b>0 and h>0 and 2*a+b<=1+1e-12, ('stochastic',m))
    check(near(h,1-2*a-b),('holding',m))
    check(near(mu,1-E*a),('even low',m))
    check(near(mu,1-U*a-2*b),('odd low',m))
    check(near(-mu,1-V*a-2*b),('odd high',m))
    for j in range(1,2*m):
        check(abs(mode(m,j,a,b))<=mu+2e-12,('Fourier mode',m,j))
    if m%2:
        check(near(h/b,2*(1+math.cos(math.pi/m))/(1+2*math.cos(math.pi/m))),('odd parity',m))
    else:
        check(near(h,b),('even parity',m))
    # Compare against the separately known Cartesian-prism optimum.
    Delta=2-2*math.cos(2*math.pi*(m//2)/m)
    prism_mu=Delta/(Delta+2*E)
    prism_a=2/(Delta+2*E)
    prism_b=E/(Delta+2*E)
    prism_h=1-2*prism_a-prism_b
    if m%2:
        check(near(mu,prism_mu),('odd twist isospectral optimum',m))
        check(near(a,prism_a),('odd same rim',m))
        check(near(b,prism_h),('odd swapped rung',m))
        check(near(h,prism_b),('odd swapped hold',m))
    else:
        check(mu<prism_mu,('even strict twist improvement',m))
        exactdiff=2*E*(1-math.cos(math.pi/m))/((2+E)*(2*math.cos(math.pi/m)+E))
        check(near(prism_mu-mu,exactdiff),('even exact twist advantage',m))
    # Explicitly independent linear-program solution at 80 sizes.
    if m<=83:
        al,bl,rl=independent_lp(m)
        check(near(rl,mu,2e-8),('LP objective',m))
        check(near(al,a,2e-8),('LP ring',m))
        check(near(bl,b,2e-8),('LP rung',m))
    # Full dense transition matrix eigenvalues for representative sizes.
    if m<=32:
        n=2*m
        P=np.zeros((n,n))
        for i in range(n):
            P[i,i]=h
            P[i,(i+1)%n]=a
            P[i,(i-1)%n]=a
            P[i,(i+m)%n]=b
        check(np.max(abs(P-P.T))<1e-13,('symmetry',m))
        check(np.max(abs(P.sum(axis=1)-1))<1e-12,('rows',m))
        ev=np.linalg.eigvalsh(P)
        check(near(ev[-1],1,2e-12),('top eigenvalue',m))
        check(near(max(abs(ev[:-1])),mu,2e-11),('full eigensystem',m))
        ft=sorted([mode(m,j,a,b) for j in range(2*m)])
        check(np.max(abs(ev-np.asarray(ft)))<2e-11,('DFT vs matrix',m))

# Check the three-mode minimax dual identity at numerous feasible allocations.
for m in (4,5,6,7,8,9,10,17,18,31,32):
    E,U,V,D,a,b,h,mu=data(m)
    alpha=(V-U)/E
    for ia in range(20):
        for ib in range(10):
            aa=0.5*ia/20
            bb=(1-2*aa)*ib/10
            u=1-E*aa
            v=1-U*aa-2*bb
            w=-1+V*aa+2*bb
            bound=(alpha*u+v+w)/(alpha+2)
            check(near(bound,mu,3e-12),('dual identity',m,ia,ib))
            check(max(u,v,w)>=mu-1e-12,('dual certificate',m,ia,ib))

# Asymptotic limits checked at high but finite sizes, NOT used as proof.
for m in (10001,10002,20001,20002):
    E,U,V,D,a,b,h,mu=data(m)
    cyc_gap=(2*U)/(4+U)
    ratio=(1-mu)/cyc_gap
    check(abs(ratio-4)<0.002,('fourfold limit',m))
    check(abs(m*m*b-3*math.pi**2/4)<0.003,('rung limit',m))
    target=math.pi**2 if m%2 else 3*math.pi**2/4
    check(abs(m*m*h-target)<0.004,('holding limit',m))
    if m%2==0:
        d=2-2*math.cos(2*math.pi*(m//2)/m)
        prism_mu=d/(d+2*E)
        diff_exact=2*E*(1-math.cos(math.pi/m))/((2+E)*(2*math.cos(math.pi/m)+E))
        check(abs(m**4*diff_exact-math.pi**4)<0.12,('even twist fourth-order limit',m))

print('VERIFY_OK', checks, 'assertions')
