#!/usr/bin/env python3
"""Reproduce finite-rate stationary spin-memory calculations.

Python 3.10+; requires numpy, scipy, sympy. Analytic proof is in RESULT.md.
This script tests exact algebra, independent finite-chain dynamics,
and asymptotic signs; finite tests are not a proof of the infinite assertion.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import jv
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply

checks = 0

def test(condition, msg):
    global checks
    checks += 1
    if not bool(condition):
        raise AssertionError(msg)

def parameters(z, g):
    e = 2*z/(1+z*z)
    assert 0 < z < 1 and e < g < 1
    omega = math.sqrt(g*g-e*e)
    h = math.sqrt((g+e)/(g-e))
    q, p = z*h, -z/h
    return e, omega, q, p

def scaled_series(z, g, t):
    e, omega, q, p = parameters(z, g)
    x = omega*t
    ns = np.arange(1, max(200, int(x+110)), dtype=int)
    # Under q>1 the q**n series grows; valid for the bounded t tested here.
    return float(jv(0,x)+np.dot(jv(ns,x), np.power(q,ns)+np.power(p,ns)))

def scaled_fourier(z, g, t):
    e = 2*z/(1+z*z)
    f = lambda k: (1-z*z)/(1-2*z*math.cos(k)+z*z) * math.exp(e*t*math.cos(k)) * math.cos(g*t*math.sin(k))
    return quad(f,0,math.pi,epsabs=1e-11,epsrel=1e-11,limit=150)[0]/math.pi

z, g = sp.symbols('z g', positive=True, real=True)
e = 2*z/(1+z*z)
s = 2*z/(1-z*z)
c = 1-g*(1-z*z)/(2*z)
test(sp.simplify(e*(z+1/z)/2-1)==0, 'Gibbs reduction')
test(sp.simplify(s/e-(1+z*z)/(1-z*z))==0,'separate thresholds')
test(sp.simplify(c.subs(g,s))==0,'critical exponent')
test(sp.simplify(s.subs(z,sp.sqrt(2)-1)-1)==0,'boundary temperature')
q,p = sp.symbols('q p',real=True)
H = 1/(1+sp.I*q)+1/(1+sp.I*p)-1
test(sp.simplify(H-(1+q*p)/((1+sp.I*q)*(1+sp.I*p)))==0,'nonzero leading oscillation')

for zz,gg in [(0.2,.7),(.3,.7),(.3,.6),(.5,.9),(.2,.42)]:
    for tt in [.1,.5,1.,2.,3.,4.,7.,10.,15.]:
        a=scaled_series(zz,gg,tt); b=scaled_fourier(zz,gg,tt)
        test(abs(a-b) < 3e-9*max(1,abs(b)), f'Bessel/Fourier {zz},{gg},{tt}: {a},{b}')

# For a strong bias, the signed stationary autocorrelation alternates
# at increasingly late predicted extrema; test sign and asymptotic amplitude.
zz,gg=.2,.7
ee,omega,qq,pp=parameters(zz,gg)
Hval=(1-zz*zz)/((1+1j*qq)*(1+1j*pp))
for m in range(7,20):
    for sign,phase in [(1,0),(-1,math.pi)]:
        tt=(2*math.pi*m+math.pi/4-np.angle(Hval)+phase)/omega
        measured=scaled_series(zz,gg,tt)
        approx=math.sqrt(2/(math.pi*omega*tt))*abs(Hval)*sign
        test(sign*measured>0, f'strong-bias alternating sign at {tt}')
        test(abs(measured/approx-1)<.1, f'large-time oscillatory amplitude at {tt}')

# Exponential pole sector, with identity coefficient one.
for zz,gg in [(.3,.6),(.5,.9),(.2,.4)]:
    ee,omega,qq,pp=parameters(zz,gg)
    cc=1-gg*(1-zz*zz)/(2*zz)
    test(qq>1 and cc>0,'pole regime')
    for tt in [40.,60.,85.]:
        ratio=scaled_series(zz,gg,tt)/math.exp(cc*tt)
        test(abs(ratio-1)<.05,f'pole amplitude at t={tt}: {ratio}')

# Exact critical one-way dynamics; the Bessel series equals the Poisson sum.
for zz in [.1,.2,.3,.5]:
    ee=2*zz/(1+zz*zz)
    gg=ee
    for tt in [.2,1.,5.,20.]:
        got=scaled_fourier(zz,gg,tt)
        expect=math.exp(ee*zz*tt)
        test(abs(got-expect) < 1e-9*max(1,expect),'one-way critical formula')

# Independent finite-ring Markov generator: rate-jump calculation,
# using the exact finite-ring Gibbs distribution rather than the infinite limit.
N=9
zz=.2; gg=.7; ee=2*zz/(1+zz*zz)
size=1<<N
row=[]; col=[]; data=[]
spins=np.empty((size,N),dtype=int)
for x in range(size):
    spins[x]=[1 if (x>>i)&1 else -1 for i in range(N)]
for x in range(size):
    total=0.
    for i in range(N):
        sv=spins[x]
        field=.5*(ee*(sv[(i-1)%N]+sv[(i+1)%N])+gg*(sv[(i-1)%N]-sv[(i+1)%N]))
        w=.5*(1-sv[i]*field)
        test(w>0, 'strictly positive flip rate')
        row.append(x); col.append(x^(1<<i)); data.append(w)
        total+=w
    row.append(x); col.append(x); data.append(-total)
Q=csr_matrix((data,(row,col)),shape=(size,size))
spin0=spins[:,0].astype(float)
# Gibbs chain: tanh(kappa)=z, with all nearest-neighbor periodic bonds.
kappa=np.arctanh(zz)
logweights=np.array([kappa*sum(spins[x,i]*spins[x,(i+1)%N] for i in range(N)) for x in range(size)])
weights=np.exp(logweights-logweights.max());weights/=weights.sum()
test(np.max(abs(weights@Q))<1e-12,'finite-ring exact invariant law')
for tt in [.1,.5,1.,2.]:
    evolved=expm_multiply(tt*Q,spin0)
    cn=float(np.sum(weights*spin0*evolved))
    cinf=math.exp(-tt)*scaled_series(zz,gg,tt)
    test(abs(cn-cinf)<3e-5,f'finite ring vs infinite t={tt}, {cn}, {cinf}')

print(f'PASS {checks} deterministic assertions')
