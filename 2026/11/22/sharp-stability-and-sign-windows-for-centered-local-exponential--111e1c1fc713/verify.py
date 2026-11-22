#!/usr/bin/env python3
"""Exact checks for centered local polynomial heat propagators.

Requires SymPy.  No floating-point experiment is used as an infinite proof.
"""
import sympy as sp
import math

x, m, t = sp.symbols('x m t', real=True)
checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def local_weights(r):
    """Interpolate degree 2r polynomials then act by the truncated heat semigroup."""
    xs = list(range(-r, r+1))
    poly = {j: sp.prod((x-k)/sp.Integer(j-k) for k in xs if k!=j) for j in xs}
    # Independently construct the full polynomial second-derivative matrix.
    d2 = sp.Matrix([[sp.diff(poly[j], x, 2).subs(x, i) for j in xs] for i in xs])
    check(d2**(r+1) == sp.zeros(2*r+1), 'polynomial-derivative nilpotency')
    propagator = sp.eye(2*r+1)
    power = sp.eye(2*r+1)
    for a in range(1, r+1):
        power = power*d2
        propagator += m**a*power/sp.factorial(a)
    weights = {j: sp.factor(propagator[r,j+r]) for j in xs}
    other = {j: sp.factor(sum(m**a/sp.factorial(a)*sp.diff(poly[j],x,2*a).subs(x,0) for a in range(r+1))) for j in xs}
    for j in xs:
        check(sp.simplify(weights[j]-other[j])==0, f'dual construction r={r},j={j}')
        check(sp.simplify(weights[j]-weights[-j])==0, 'symmetry')
    check(sp.simplify(sum(weights.values())-1)==0, 'constant preservation')
    return weights

w1=local_weights(1)
w2=local_weights(2)
w3=local_weights(3)
for r,w in [(1,w1),(2,w2),(3,w3)]:
    # Asymptotic second-neighbor negative coefficient of all higher orders.
    if r>=2:
        coef=-sp.Rational(r*(r-1),2*(r+1)*(r+2))
        check(sp.diff(w[2],m).subs(m,0)==coef, 'general small-step barrier')
        check(sp.Poly(w[r-1],m).LC()==-sp.Rational(2*r,math.factorial(r)), 'large-step barrier')

W2=[(6*m*m-5*m+2)/2, -2*m*(3*m-2)/3, m*(6*m-1)/12]
W3=[-(60*m**3-84*m**2+49*m-18)/18,
    m*(10*m*m-13*m+6)/4,
    -m*(20*m*m-20*m+3)/20,
    m*(30*m*m-15*m+2)/180]
for r,W,w in [(2,W2,w2),(3,W3,w3)]:
    for j,form in enumerate(W):
        check(sp.simplify(form-w[j])==0, 'declared weights')

C=[sp.Integer(1), 1-2*t]
for j in range(2,4):
    C.append(sp.expand(2*(1-2*t)*C[-1]-C[-2]))
G2=sp.factor(w2[0]+2*sum(w2[j]*C[j] for j in range(1,3)))
G3=sp.factor(w3[0]+2*sum(w3[j]*C[j] for j in range(1,4)))
G2_expected=1-4*m*t+sp.Rational(4,3)*m*(6*m-1)*t*t
G3_expected=-(480*m**3*t**3-240*m**2*t**3-360*m**2*t**2+32*m*t**3+60*m*t**2+180*m*t-45)/45
check(sp.simplify(G2-G2_expected)==0,'five-point Fourier symbol')
check(sp.simplify(G3-G3_expected)==0,'seven-point Fourier symbol')
H=120*m*m*t*t-60*m*t*t-60*m*t+8*t*t+10*t+15
check(sp.simplify(sp.diff(G3,t)+4*m*H/15)==0,'seven-point spectral derivative')
check(sp.simplify(H-(120*(m*t-(t+1)/4)**2+(t*t-10*t+15)/2))==0,'positive decomposition')
F=480*m**3-600*m**2+272*m-90
check(sp.simplify(G3.subs(t,1)+1+F/45)==0,'Nyquist root')
check(sp.factor(sp.diff(F,m)- (1440*(m-sp.Rational(5,12))**2+22))==0,'strict cubic monotonicity')

lower=(5-sp.sqrt(10))/10
upper=(5+sp.sqrt(10))/10
check(sp.simplify(w3[2].subs(m,lower))==0,'lower positivity boundary')
check(sp.simplify(w3[2].subs(m,upper))==0,'upper positivity boundary')
check(sp.simplify(w3[0].subs(m,upper)-(16-4*sp.sqrt(10))/45)==0,'center positivity at upper')
check(sp.simplify(G3.subs({t:1,m:upper})+(13+8*sp.sqrt(10))/45)==0,'stable at positivity endpoint')
check(F.subs(m,upper)<0,'stability survives the seven-point positivity limit')

# Sampled independent Fourier and matrix tests are diagnostics, not proofs.
import numpy as np
for r,w in [(2,w2),(3,w3)]:
    grid=2*r+8  # even periodic grid containing Nyquist
    for mu0 in [0, 1/10, 1/5, 2/5, 3/5, 4/5, 9/10, 1]:
        vals=[float(w[j].subs(m,sp.Rational(str(mu0)))) for j in range(-r,r+1)]
        M=np.zeros((grid,grid))
        for i in range(grid):
            for j,v in zip(range(-r,r+1),vals):
                M[i,(i+j)%grid]+=v
        check(abs(np.max(abs(np.linalg.eigvalsh(M)))-max(abs(sum(v*np.exp(2j*np.pi*k*j/grid) for j,v in zip(range(-r,r+1),vals))) for k in range(grid)))<1e-9,'matrix-Fourier diagonalization')
        check(abs(M.sum(axis=1).min()-1)<1e-9, 'row sums')

if __name__=='__main__':
    root=float(sp.nroots(F)[0]) if False else float(sp.nsolve(F,m,0.84))
    assert abs(root-0.841360228011148)<1e-12
    assert root > float(upper)
    print('VERIFY_OK', checks, 'algebraic and matrix checks;', 'seven-point spectral root',format(root,'.15f'))
