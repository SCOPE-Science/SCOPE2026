"""Reproducibility checks for hard-core prism Fourier bottleneck theorem.

Runs without external data; requires Python 3, numpy, sympy.
All claims concern classical finite graph hard-core measures and their bulk limit.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, pi, sqrt
import numpy as np
import sympy as sp

r=sp.symbols('r',real=True,positive=True)
D=1+2*r-r*r
rho_s=-r*(1-r)/(1+r)
rho_a=-r
q=2*r/D
V_s=q*(1-q)/2
V_a=q/2
S=lambda V,rho,t:sp.factor(V*(1-rho**2)/(1-2*rho*t+rho**2))
S_s0=sp.factor(S(V_s,rho_s,1))
S_a0=sp.factor(S(V_a,rho_a,1))
S_sPi=sp.factor(S(V_s,rho_s,-1))
S_aPi=sp.factor(S(V_a,rho_a,-1))
assert sp.simplify(S_s0-r*(1-r*r)*(1+r*r)/D**3)==0
assert sp.simplify(S_a0-r*(1-r)/((1+r)*D))==0
assert sp.simplify(S_sPi-r*(1-r*r)/((1+r*r)*D))==0
assert sp.simplify(S_aPi-r*(1+r)/((1-r)*D))==0
assert sp.simplify(S_a0-S_s0 - 2*r*r*(1-r)*(1-3*r*r)/((1+r)*D**3))==0
assert sp.simplify(S_aPi-S_sPi - 2*r*r*(1+r)/((1-r)*(1+r*r)*D))==0
assert sp.simplify(S_aPi/S_s0-D**2/((1-r)**2*(1+r*r)))==0
assert sp.simplify(S_aPi/S_a0-((1+r)/(1-r))**2)==0
zstar=sp.simplify((r*(1+r)/(1-r)).subs(r,1/sp.sqrt(3)))
assert sp.simplify(zstar-(1+2/sp.sqrt(3)))==0
Klo=D**2/((1-r)**2*(1+r*r))
Khi=((1+r)/(1-r))**2
z_of_r=r*(1+r)/(1-r)
jump=sp.simplify(((sp.diff(Khi,r)-sp.diff(Klo,r))/sp.diff(z_of_r,r)).subs(r,1/sp.sqrt(3)))
assert sp.simplify(jump-9*(sp.sqrt(3)-1)/4)==0
print('EXACT_SYMBOLIC_BRANCHES_AND_SWITCH_PASS')

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def tr(A):return sum(A[i][i] for i in range(3))
def mat_pow(K,n):
    X=[[F(int(i==j)) for j in range(3)] for i in range(3)]
    while n:
        if n&1:X=mm(X,K)
        K=mm(K,K);n//=2
    return X

def exact_trace_checks(n,z):
    K=[[F(1),z,z],[F(1),F(0),z],[F(1),z,F(0)]]
    powers=[mat_pow(K,d) for d in range(n+1)]
    Z=tr(powers[n]); total=F(0)
    vals=[F(0)]*n
    pair=[F(0)]*n
    for state in product(range(3),repeat=n):
        if any(state[i]==state[(i+1)%n]!=0 for i in range(n)):continue
        w=z**sum(t!=0 for t in state)
        total+=w
        occ0=F(state[0]!=0)
        for d in range(n):
            vals[d]+=w*occ0*F(state[d]!=0)
            pair[d]+=w*F((state[0]==1)-(state[0]==2))*F((state[d]==1)-(state[d]==2))
    assert Z==total,(n,z,Z,total)
    E=F(0)
    for state in product(range(3),repeat=n):
        if any(state[i]==state[(i+1)%n]!=0 for i in range(n)):continue
        E+=z**sum(t!=0 for t in state)*F(state[0]!=0)
    E/=Z
    op=[[F(0),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
    om=[[F(0),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(-1)]]
    mean=tr(mm(op,powers[n]))/Z
    assert E==mean
    for d in range(n):
        bytrace=tr(mm(mm(mm(op,powers[d]),op),powers[n-d]))/Z
        bytrace_diff=tr(mm(mm(mm(om,powers[d]),om),powers[n-d]))/Z
        assert vals[d]/Z==bytrace,(n,z,d)
        assert pair[d]/Z==bytrace_diff,(n,z,d)
    return True

for z in [F(1,2),F(1),F(3)]:
    for n in range(3,10):exact_trace_checks(n,z)
print('EXHAUSTIVE_FINITE_RING_PROBABILITIES_VS_TRANSFER_PASS n=3..9; z=1/2,1,3')

def bulk_spectra(z,t):
    lam=(1+z+sqrt(1+6*z+z*z))/2
    r=z/lam
    D=1+2*r-r*r
    occ=2*r/D
    rho_s=-r*(1-r)/(1+r)
    return (occ*(1-occ)/2*(1-rho_s**2)/(1-2*rho_s*t+rho_s**2),
            occ/2*(1-r*r)/(1+2*r*t+r*r))

def finite_spectra(n,z):
    K=np.array([[1,z,z],[1,0,z],[1,z,0]],dtype=float)
    lam=(1+z+sqrt(1+6*z+z*z))/2
    K=K/lam
    powers=[np.eye(3)]
    for d in range(n):powers.append(powers[-1]@K)
    Z=np.trace(powers[n])
    op=np.diag([0,1,1.]);om=np.diag([0,1,-1.]);
    mean=np.trace(op@powers[n])/Z
    cs=[];ca=[]
    for d in range(n):
        cs.append((np.trace(op@powers[d]@op@powers[n-d])/Z-mean**2)/2)
        ca.append(np.trace(om@powers[d]@om@powers[n-d])/Z/2)
    return np.real(np.fft.fft(cs)),np.real(np.fft.fft(ca))

for z in [0.1,1.,1+2/sqrt(3),3.,10.]:
    for n in [32,64,96,128]:
        Cs,Ca=finite_spectra(n,z)
        pred=[bulk_spectra(z,cos(2*pi*k/n)) for k in range(n)]
        err=max(max(abs(Cs[k]-pred[k][0]),abs(Ca[k]-pred[k][1])) for k in range(n))
        if n==128:assert err<1e-7,(z,n,err)
        print(f'FINITE_BULK_CONVERGENCE z={z:.8g} n={n} maxerror={err:.2g}')
print('ALL_CHECKS_PASS')
