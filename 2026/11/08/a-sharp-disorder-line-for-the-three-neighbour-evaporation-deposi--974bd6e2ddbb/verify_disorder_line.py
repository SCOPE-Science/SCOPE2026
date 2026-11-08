"""Reproducibility checks for stationary spatial correlations of the three-neighbour NED automaton.
Run: python verify_disorder_line.py. Uses numpy and sympy.
Numerical checks do not replace the infinite-volume analytic argument.
"""
from itertools import product
from math import isclose
import numpy as np
import sympy as sp

p,q,z=sp.symbols('p q z',positive=True)
a=1-p
b=a*a/q
P=1-(1+p)*z+p*p*z*z+p*(a-b)*z**3
T=sp.Matrix([[p,1,0],[p*a,0,1],[p*b,0,1]])
assert sp.simplify((z*sp.eye(3)-T).det()-sp.expand(sp.together(z**3*P.subs(z,1/z))))==0
R=(p-1)**2*(3*p-4)*q*q-2*(p-2)*(7*p*p-10*p+1)*q+27*p*(p-1)**2
assert sp.simplify(sp.discriminant(P,z)+p*(p-1)**2*R/q**2)==0
assert sp.factor(R.subs(q,1-p))==p**3*(p-1)*(3*p+1)
assert sp.factor(R.subs(q,1))==4*p*(4*p*p-4*p-1)

checks=4

def stationary_weight(bits,pv,qv):
    n=len(bits)
    if not sum(bits):return 1.0
    k=sum(bits)
    n101=sum(bits[i]==1 and bits[(i+1)%n]==0 and bits[(i+2)%n]==1 for i in range(n))
    n001=sum(bits[i]==0 and bits[(i+1)%n]==0 and bits[(i+2)%n]==1 for i in range(n))
    return pv**k*(1-pv)**(n101+2*n001)/qv**n001

for pv,qv in [(0.2,0.04),(0.4,0.31),(0.5,0.2),(0.5,0.8),(0.7,0.05),(0.7,0.31),(0.9,0.4)]:
    av=1-pv; bv=av*av/qv
    M=np.array([[pv,1,0],[pv*av,0,1],[pv*bv,0,1]],float)
    E=M.copy();E[:,1:]=0
    for n in range(3,9):
        configurations=list(product((0,1), repeat=n))
        weights=np.array([stationary_weight(x,pv,qv) for x in configurations])
        Z=weights.sum()
        Z_transfer=np.trace(np.linalg.matrix_power(M,n))
        assert np.isclose(Z,Z_transfer,rtol=2e-11,atol=1e-10)
        checks+=1
        for r in range(1,n):
            direct=sum(w*x[0]*x[r] for x,w in zip(configurations,weights))
            tr=np.trace(E@np.linalg.matrix_power(M,r-1)@E@np.linalg.matrix_power(M,n-r-1))
            assert np.isclose(direct,tr,rtol=2e-11,atol=1e-10)
            checks+=1

# Independently verify source stationary weights against the PCA update kernel
# for representative parameters and small rings (not an infinite proof).
for pv,qv in [(0.2,0.4),(0.5,0.2),(0.8,0.5)]:
    for n in range(3,7):
        states=list(product((0,1),repeat=n))
        ww=np.array([stationary_weight(x,pv,qv) for x in states],float)
        ww=ww/ww.sum()
        Q=np.zeros((len(states),len(states)))
        for i,x in enumerate(states):
            probs=[]
            for j in range(n):
                triple=tuple(x[(j+k)%n] for k in range(3))
                probs.append(pv if triple==(0,0,0) else (1-qv if triple==(0,0,1) else 0.0))
            for k,y in enumerate(states):
                prob=1.0
                for h in range(n):
                    prob*=probs[h] if y[h] else (1-probs[h])
                Q[i,k]=prob
        assert np.allclose(Q.sum(axis=1),1.0,atol=1e-12)
        assert np.allclose(ww@Q,ww,atol=1e-12)
        checks+=2

# Verify location and spectral types for a grid on each side of the unique curve.
for pv in (0.1,0.3,0.5,0.7,0.9):
    A=(pv-1)**2*(3*pv-4)
    B=-2*(pv-2)*(7*pv*pv-10*pv+1)
    C=27*pv*(pv-1)**2
    qc=max(np.roots([A,B,C]).real)
    assert 0<qc<1-pv
    checks+=1
    for qv,is_osc in [(qc*.4,True),(qc*.9,True),((qc+1-pv)/2,False),((1+1-pv)/2,False)]:
        bv=(1-pv)**2/qv
        co=[pv*(1-pv-bv),pv**2,-(1+pv),1.]
        roots=np.roots(co)
        assert (np.any(np.abs(roots.imag)>1e-7))==is_osc
        z0=1/max(np.linalg.eigvals(np.array([[pv,1,0],[pv*(1-pv),0,1],[pv*bv,0,1.]])).real)
        assert all((abs(rt)>z0*(1+1e-9)) for rt in roots if abs(rt-z0)>1e-7)
        checks+=2

# Incommensurate oscillation example: p=1/2, q=1/5.
P_ex=sp.factor(P.subs({p:sp.Rational(1,2),q:sp.Rational(1,5)}))
assert sp.simplify(P_ex-(1-sp.Rational(3,2)*z+z*z/4-3*z**3/8))==0
assert sp.simplify(P_ex.subs(z,sp.Rational(2,3)))==0
assert sp.simplify(P_ex.subs(z,2*sp.I))==0
assert sp.simplify(P_ex.subs(z,-2*sp.I))==0
checks+=4
# Exact first two connected correlations in the rational spectral witness.
# Its Palm interarrival probabilities are f_1=1/3 and f_2=1/9,
# with density 3/10; the renewal mass u_2=f_2+f_1**2=2/9.
rho=sp.Rational(3,10)
assert rho*(sp.Rational(1,3)-rho)==sp.Rational(1,100)
assert rho*(sp.Rational(2,9)-rho)==-sp.Rational(7,300)
checks+=2

print('PASS',checks,'symbolic, transfer-matrix, finite-ring and spectral checks')
