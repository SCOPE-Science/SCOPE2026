"""Reproducibility checks for singular cyclic four-species Lotka--Volterra dynamics.

Requires Python 3, sympy, numpy and scipy.  Exact identities test the
interaction matrix and entropy certificate; finite integrations are illustrative.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

A = sp.symbols('a', positive=True)
E = (A*A-A+1)/A**3
C = sp.Matrix([[1,A,0,0],[0,1,A,0],[(1-E)*A,0,1,E*A],[A,0,0,1]])
q = sp.Matrix([-1/A, 1/A**2, -1/A**3, 1])
l = sp.Matrix([-1,A,-A**2,A**2-A+1])
D = sp.diag(A,A**3,A**5,A**2-A+1)
S = sp.simplify((D*C+C.T*D)/2)
B = S[:3,:3]
assert (C*q).applyfunc(sp.simplify) == sp.zeros(4,1)
assert (l.T*C).applyfunc(sp.simplify) == sp.zeros(1,4)
assert sp.simplify(sum(l)) == 0
assert (D*q-l).applyfunc(sp.simplify) == sp.zeros(4,1)
assert (S*q).applyfunc(sp.simplify) == sp.zeros(4,1)
assert sp.factor(B[0,0]) == A
assert sp.factor(B[:2,:2].det()) == 3*A**4/4
assert sp.factor(B.det()) == -A**10*(A*A-A+1)*(A**3-A*A+A-3)/4
assert sp.factor(C.det()) == 0
assert sp.factor(C[:3,:3].det()) == A*(A*A-A+1)
assert (C*sp.ones(4,1)-(1+A)*sp.ones(4,1)).applyfunc(sp.simplify) == sp.zeros(4,1)
critical = brentq(lambda a:a**3-a*a+a-3, 1.0,2.0)
assert 1.5747430 < critical < 1.5747432
print('EXACT_MATRIX_IDENTITIES 11; certificate_root={:.12f}'.format(critical))

cases = [(1.1,[0.11,0.41,0.92,0.31]),
         (1.3,[1.4,0.23,0.24,0.73]),
         (1.5,[0.38,1.1,0.15,0.2]),
         (1.56,[0.19,0.36,0.71,0.24])]
for a, x0 in cases:
    x0 = np.array(x0, dtype=float)
    c = 1/(1+a)
    mat = np.array(C.subs(A,a)).astype(float)
    qv = np.array(q.subs(A,a)).astype(float).ravel()
    lv = np.array(l.subs(A,a)).astype(float).ravel()
    def H(x): return float(np.dot(lv,np.log(x)))
    h0 = H(x0)
    t_star = brentq(lambda t:H(c*np.ones(4)+t*qv)-h0, -c+1e-14, a*c-1e-14)
    target = c*np.ones(4)+t_star*qv
    def rhs(t,x): return x*(1-mat@x)
    sol=solve_ivp(rhs,(0,2500),x0,rtol=1e-11,atol=1e-12)
    assert sol.success
    err = max(abs(sol.y[:,-1]-target))
    conservation = max(abs(H(sol.y[:,i])-h0) for i in range(0,len(sol.t),max(1,len(sol.t)//60)))
    assert err < 3e-5, (a,err)
    assert conservation < 5e-7, (a,conservation)
    eig = np.linalg.eigvalsh(np.array(S.subs(A,a)).astype(float))
    assert eig[1]>1e-4, (a,eig)
    print('FINITE_TRAJECTORY a={:.2f} limit_error={:.2g} conserved_error={:.2g} PSD_nonzero_min={:.5g}'.format(a,err,conservation,eig[1]))

for a in [1.8,2.0,2.3]:
    eig = np.linalg.eigvalsh(np.array(S.subs(A,a)).astype(float))
    assert eig[0] < -1e-4, (a,eig)
print('VERIFY_OK exact_kernel_and_minors=1 finite_trajectories=4 certificate_failure_checks=3')
