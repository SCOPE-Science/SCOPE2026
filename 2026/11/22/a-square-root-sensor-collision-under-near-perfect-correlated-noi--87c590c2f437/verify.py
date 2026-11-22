"""Supplementary checks for two-harmonic sensing with equicorrelated noise.

Python 3 with numpy, scipy, sympy. The analytic proof is in RESULT.md.
Finite searches below do not certify global optimality.
"""
from math import acos, cos, pi, sin, sqrt
import numpy as np
import sympy as sp
from scipy.optimize import differential_evolution, minimize_scalar

u, v = sp.symbols('u v', real=True)
P = u + 4 * (2*u - 1)**2 * v
D = 4 * (1-u) * (u-v)**2 / P
L = sp.Rational(25,16)
u0=sp.Rational(3,8)
assert sp.simplify(D.subs({u:u0, v:1})-L)==0
assert sp.simplify(sp.diff(D,u).subs({u:u0,v:1}))==0
assert sp.simplify(sp.diff(D,u,2).subs({u:u0,v:1})+56)==0
assert sp.simplify(sp.diff(D,v).subs({u:u0,v:1})-sp.Rational(35,8))==0
assert sp.factor(L*(16*u*u-15*u+4)-4*(1-u)**3)==(u+4)*(8*u-3)**2/16
assert sp.factor((1-u)*(1+4*u)-L)==-(8*u-3)**2/16
assert sp.simplify(sp.Rational(25,32)-5*sp.Rational(35,32)+sp.Rational(75,16))==0
rho_sym=sp.symbols('rho', real=True)
x1,x2,y1,y2=sp.symbols('x1 x2 y1 y2', real=True)
X=sp.Matrix([[x1,x2],[y1,y2]])
S=sp.Matrix([[1,rho_sym],[rho_sym,1]])
b=sp.Matrix([x1+y1,x2+y2]); d=sp.Matrix([x1-y1,x2-y2])
assert all(sp.simplify(z)==0 for z in (X.T*S.inv()*X - b*b.T/(2*(1+rho_sym))-d*d.T/(2*(1-rho_sym))))
uc=(1-rho_sym)/(4*(1+rho_sym))
f1=2*(1-u)/(1+rho_sym)
f2=8*u*(1-u)/(1-rho_sym)
ref=(3+5*rho_sym)/(2*(1+rho_sym)**2)
assert sp.simplify(f1.subs(u,uc)-f2.subs(u,uc))==0
assert sp.simplify(f1.subs(u,uc)-ref)==0
print('PASS: exact Gaussian information decomposition and reflected-pair optimum')
print('PASS: exact symbolic maximum, chord expansion and first-order coefficient')

# Verify the exact chord formula independently at pairs not near a collision.
rng=np.random.default_rng(2020)
for _ in range(2500):
    a,b=np.sort(rng.uniform(0,pi,2))
    if b-a<1e-6: continue
    p=np.array([sin(a),sin(2*a)])
    q=np.array([sin(b),sin(2*b)])
    d=np.linalg.det(np.vstack((p,q)))**2/np.dot(p-q,p-q)
    m=(a+b)/2
    formula=float(D.subs({u:cos(m)**2,v:cos((b-a)/2)**2}))
    assert abs(d-formula)<2e-12
print('PASS: 2500 independently evaluated chord identities')

def amp(s,t,rho):
    a=np.array([sin(s),sin(2*s)])
    b=np.array([sin(t),sin(2*t)])
    M=np.outer(a+b,a+b)/(2*(1+rho))+np.outer(a-b,a-b)/(2*(1-rho))
    return float(np.linalg.eigvalsh(M)[0])

th0=acos(sqrt(3/8))
print('angle target:',round(th0/pi,12))
for eps in [0.1,0.01,0.001,0.0001]:
    rho=1-eps
    result=differential_evolution(lambda z:-amp(z[0],z[1],rho),[(0,pi)]*2,seed=31,popsize=18,tol=1e-10)
    s,t=sorted(result.x)
    val=-result.fun
    exact_refl=(3+5*rho)/(2*(1+rho)**2)
    assert val+1e-7>=exact_refl
    if eps<=0.001:
        assert abs((t-s)/sqrt(eps)-sqrt(5))<0.05
        assert abs((s+t)/2-th0)<0.03 or abs((s+t)/2-(pi-th0))<0.03
    print(f'eps={eps:g} numerical_search={val:.10f} sites=({s/pi:.9f}, {t/pi:.9f}) '
          f'separation_over_sqrt_eps={(t-s)/sqrt(eps):.8f} asymptotic={25/16-75/16*eps:.10f} '
          f'best_reflected={exact_refl:.10f}')
print('PASS: supplementary optimizations, asymptotic locations, and reflected comparisons')
