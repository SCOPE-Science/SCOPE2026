"""Independent numerical checks for two-mode one-delay stochastic gradient recurrences.

Run with: python3 check.py
Requires numpy, scipy, sympy. Deterministic random seed. This is
supporting verification, not a proof of the asymptotic assertions.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def dream_coeff(q, t):
    beta = 1-q+q*q/2
    delta = (2-q*q)/8
    dnu = (4-4*q+q*q)/8
    return 1+beta, -beta-t*(delta+dnu), t*dnu


def stationary_factor(a,b,c):
    numerator = 1-b-c*c-a*c
    denom = (1+a-b+c)*(1-a-b-c)*(1+b-c*c+a*c)
    return numerator / denom


def companion_var(a,b,c):
    M = np.array([[a,b,c],[1,0,0],[0,1,0]],dtype=float)
    E = np.zeros((3,3))
    E[0,0] = 1
    P = solve_discrete_lyapunov(M,E)
    return P[0,0], max(abs(np.linalg.eigvals(M)))


count=0
rng = np.random.default_rng(20261106)
for q in np.linspace(0.035, 0.975, 61):
    for t in [q*q,1.0] + list(rng.uniform(q*q,1.0,5)):
        a,b,c = dream_coeff(q,t)
        val = stationary_factor(a,b,c)
        independent, radius = companion_var(a,b,c)
        assert radius < 1 + 1e-10, (q,t,radius)
        assert val > 0
        assert math.isclose(val,independent,rel_tol=3e-5,abs_tol=3e-6), (q,t,val,independent)
        count+=1

for q in [0.03,0.02,0.01,0.005]:
    a,b,c = dream_coeff(q,q*q)
    low = stationary_factor(a,b,c)
    a,b,c = dream_coeff(q,1)
    high = stationary_factor(a,b,c)
    assert abs(q**3*low/2-1)<0.018
    assert abs(q*high/(16/7)-1)<0.03
    count+=2

# Independent direct simulation from a stable 3-state recurrence for fixed q,
# compared with its theoretical Lyapunov variance (unit noise input).
for q,t in [(0.5,0.25),(0.5,1.0),(0.8,0.64)]:
    a,b,c = dream_coeff(q,t)
    target = stationary_factor(a,b,c)
    x=np.zeros(3)
    vals=[]
    for k in range(160_000):
        x=np.array([a*x[0]+b*x[1]+c*x[2]+rng.standard_normal(),x[0],x[1]])
        if k>25_000: vals.append(x[0]**2)
    sample=float(np.mean(vals))
    assert abs(sample-target)<0.10*target, (q,t,sample,target)
    count+=1

# Verify the exact delayed-GD minimax intersection and stationary Yule-Walker law.
for kappa in [1,2,4,16,100,10000]:
    hL=kappa**2/(kappa+1)**2
    r=kappa/(kappa+1)
    def root_radius(t):
        return (1+math.sqrt(1-4*t))/2 if t<=.25 else math.sqrt(t)
    assert math.isclose(root_radius(hL/kappa),r,rel_tol=1e-10)
    assert math.isclose(root_radius(hL),r,rel_tol=1e-10)
    for t in [hL/kappa,hL]:
        closed = (1+t)/(t*(1-t)*(2+t))
        lyap,rad=companion_var(1,-t,0)
        assert math.isclose(closed,lyap,rel_tol=1e-9)
        count+=1

print('PASS:',count,'independent Lyapunov, eigenvalue, simulation and asymptotic diagnostics')

# Independent exact-rational Yule--Walker reconstruction of the cubic formula.
import sympy as sp
v0,v1,v2=sp.symbols('v0 v1 v2')
for q in [sp.Rational(1,2),sp.Rational(1,3),sp.Rational(2,3)]:
    for t in [q*q,sp.Rational(1,2),sp.Integer(1)]:
        a,b,c=dream_coeff(q,t)
        v3=a*v2+b*v1+c*v0
        equations=[v1-a*v0-b*v1-c*v2,
                   v2-(a+c)*v1-b*v0,
                   v0-a*v1-b*v2-c*v3-1]
        vals=sp.solve(equations,[v0,v1,v2],dict=True)[0]
        assert sp.simplify(vals[v0]-stationary_factor(a,b,c))==0
        count+=1
print('PASS EXACT-RATIONAL YULE-WALKER:',9, '; TOTAL:',count)
