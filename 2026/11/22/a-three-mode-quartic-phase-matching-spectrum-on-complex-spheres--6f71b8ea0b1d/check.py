"""Exact and independent numerical checks of quartic phase-matching compression."""
from itertools import product
from math import comb, factorial
import sympy as sp
import numpy as np

def exps(d, degree=4):
    return [v for v in product(range(degree + 1), repeat=d) if sum(v) == degree]

def coeff(a,b):
    delta = [ai-bi for ai,bi in zip(a,b)]
    if any(delta[3:]) or not (delta[0] and delta[0] == delta[1] and delta[2] == -2*delta[0] and abs(delta[0]) % 2):
        return sp.S(0)
    j = abs(delta[0]); c = (-1)**((j-1)//2)/(sp.pi*j)
    for ai,bi in zip(a,b):
        c *= sp.gamma(sp.Rational(ai+bi,2)+1) / sp.sqrt(sp.factorial(ai)*sp.factorial(bi))
    return sp.simplify(c)

def matrix(d):
    a=exps(d)
    return a,sp.Matrix([[sp.Rational(1,2) if i==j else coeff(a[i],a[j]) for j in range(len(a))] for i in range(len(a))])

def expected(d):
    r=d-3
    E={}
    def add(delta,mult):
        if mult==0:return
        for sig in (-1,1):
            key=sp.simplify(sp.Rational(1,2)+sig*delta)
            E[key]=E.get(key,0)+mult
    add(sp.sqrt(354)/64,1)
    add(sp.sqrt(3)/8,2)
    add(5*sp.sqrt(6)/64,2)
    add(1/(2*sp.sqrt(6)),r)
    add(sp.Rational(3,16),2*r)
    add(1/(4*sp.sqrt(2)),r*(r+1)//2)
    E[sp.Rational(1,2)]=comb(d+3,4)-(d-1)*(d+2)
    return E

def components(d):
    mm=exps(d)
    unseen=set(mm); out=[]
    while unseen:
        a=min(unseen); stack=[a]; comp=[]; unseen.remove(a)
        while stack:
            b=stack.pop();comp.append(b)
            for c in tuple(unseen):
                if coeff(b,c):unseen.remove(c);stack.append(c)
        out.append(comp)
    return out

for d in range(3,8):
    comps=components(d)
    observed={}
    for cc in comps:
        M=sp.Matrix([[sp.Rational(1,2) if a==b else coeff(a,b) for b in cc] for a in cc])
        ev=M.eigenvals()
        for val,mul in ev.items():
            val=sp.simplify(val)
            observed[val]=observed.get(val,0)+mul
    assert observed==expected(d),(d,observed,expected(d))
    print('exact d',d,'dimension',len(exps(d)),'blocks',len(comps),'PASS')

for d in (3,4,6):
    rng=np.random.default_rng(20261115+d)
    n=160000
    z=(rng.standard_normal((n,d))+1j*rng.standard_normal((n,d)))
    z/=np.linalg.norm(z,axis=1)[:,None]
    ang=np.angle(z[:,0]*z[:,1]*np.conj(z[:,2])**2)
    mask=(np.cos(ang)>0).astype(float)
    tt=[(0,0,4),(1,1,2),(2,2,0)]
    B=np.zeros((n,3),complex)
    poch=np.prod(np.arange(d,d+4))
    for j,a in enumerate(tt):
        norm=np.sqrt(poch/np.prod([factorial(v) for v in a]))
        B[:,j]=norm*z[:,0]**a[0]*z[:,1]**a[1]*z[:,2]**a[2]
    G=(B.conj().T@(mask[:,None]*B))/n
    W=np.array([[0,float(sp.sqrt(3)/8),0],[float(sp.sqrt(3)/8),0,float(9*sp.sqrt(2)/64)],[0,float(9*sp.sqrt(2)/64),0]])+.5*np.eye(3)
    error=float(np.max(np.abs(G-W)))
    assert error<.025,(d,error,G)
    print('independent Monte Carlo d',d,'error',round(error,6),'PASS')

print('CONDITION',float((32+sp.sqrt(354))/(32-sp.sqrt(354))))
