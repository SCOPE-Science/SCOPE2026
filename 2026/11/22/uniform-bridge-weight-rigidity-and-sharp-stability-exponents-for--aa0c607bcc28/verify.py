"""Exact symbolic identities and finite numerical cross-checks for bridge bottleneck mixing.
Only standard NumPy and SymPy; run: python verify.py
"""
import math
import random
import sympy as sp
import numpy as np

c=sp.symbols('c',real=True)
g=3-2*sp.sqrt(2)
cs=sp.sqrt(2)-1
x=1-c
f=c*x/(1+c)
C=6-sp.sqrt(2)
assert sp.simplify((g-f)*(1+c)-(c-cs)**2)==0
assert sp.simplify(C-4-2*g/(1-cs))==0
assert sp.simplify((1-cs)**2-2*g)==0
h=sp.symbols('h',real=True)
fh=1/(2/(1-cs-h)+1/cs)
assert sp.simplify(fh.subs(h,0)-g)==0
assert sp.simplify(-sp.diff(fh/g,h).subs(h,0)-1)==0

check_count=5

def kernel(p,q,bridge=float(cs),hold=0.0):
    n=p-1; r=q-1; w=1-bridge-hold
    assert n>=2 and r>=2 and 0<=hold and 0<bridge<1 and w>0
    P=np.zeros((p+q,p+q),float)
    a= w/n; b=w/r
    # Gateway indices are 0 and p; other clique vertices are 1..p-1, p+1..p+q-1.
    P[0,p]=P[p,0]=bridge
    P[0,0]=P[p,p]=hold
    for i in range(1,p):
        P[0,i]=P[i,0]=a
    for j in range(p+1,p+q):
        P[p,j]=P[j,p]=b
    for i in range(1,p):
        for j in range(1,p):
            P[i,j]=(1-w)/n if i==j else 1/n
    for i in range(p+1,p+q):
        for j in range(p+1,p+q):
            P[i,j]=(1-w)/r if i==j else 1/r
    return P

def fourblock(p,q,bridge,hold=0):
    n=p-1;r=q-1; w=1-bridge-hold
    return np.array([[1-w/n,w/math.sqrt(n),0,0],
     [w/math.sqrt(n),hold,bridge,0],
     [0,bridge,hold,w/math.sqrt(r)],
     [0,0,w/math.sqrt(r),1-w/r]],float)

def delta(P):
    ev=np.linalg.eigvalsh(P)
    return 1-max(abs(ev[:-1])),ev

for p in range(5,16):
 for q in range(5,16):
    P=kernel(p,q)
    assert np.max(abs(P-P.T))<1.e-14
    assert np.max(abs(np.sum(P,axis=1)-1))<1.e-14
    assert np.min(P)>=-1e-14
    actual,eigs=delta(P)
    block=np.linalg.eigvalsh(fourblock(p,q,float(cs)))
    predicted=sorted(list(block)+[-float(1-cs)/(p-1)]*(p-2)+[-float(1-cs)/(q-1)]*(q-2))
    assert np.max(abs(eigs-np.array(predicted)))<2e-13
    s=1/(p-1)+1/(q-1)
    assert float(g)*s/(1+float(C)*s)-1e-13 <= actual <=float(g)*s+1e-13
    check_count+=5

# Test exact Dirichlet-series bounds for random conductance allocations and Rayleigh spectra.
rng=random.Random(36047)
for p,q in [(5,5),(5,8),(7,12),(12,7),(15,15)]:
 for rep in range(45):
    P=np.eye(p+q)
    edges=[]
    for lo,hi in [(0,p),(p,p+q)]:
        for i in range(lo,hi):
            for j in range(i+1,hi):
                edges.append((i,j))
    edges.append((0,p))
    weights=[rng.random() for _ in edges]
    degrees=[0.]*(p+q)
    for (i,j),v in zip(edges,weights): degrees[i]+=v;degrees[j]+=v
    scale=.9/max(degrees)
    for (i,j),v in zip(edges,weights):
        P[i,j]=P[j,i]=scale*v
        P[i,i]-=scale*v;P[j,j]-=scale*v
    gap,eig=delta(P)
    c0=P[0,p]
    A=sum(P[0,i] for i in range(1,p))
    B=sum(P[p,j] for j in range(p+1,p+q))
    R=1/(1/A+1/c0+1/B)
    ss=1/(p-1)+1/(q-1)
    assert gap <= R*ss+1e-12, (p,q,gap,R*ss)
    assert R<=float(g)+1e-12
    check_count+=2

# Tight exponent tests: fixed perturbation and N growing.
for N in [30,100,300]:
 for offset,hold in [(0,0),(-.06,0),(.06,0),(0,.025)]:
    cc=float(cs)+offset; w=1-cc-hold
    B4=fourblock(N,N,cc,hold)
    ev=np.linalg.eigvalsh(B4)
    d=1-max(float(np.max(abs(ev[:-1]))),w/(N-1))
    sh=2/(N-1)
    conductance=1/(2/w+1/cc)
    assert abs(d/sh-conductance)<.15/N, (N,cc,hold,d/sh,conductance)
    check_count+=1
print('VERIFY_OK',check_count)
