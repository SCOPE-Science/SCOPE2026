"""Standalone symbolic and independent linear-state checks for the athermal harmonic-correlation phase theorem.
Run: python CHECK.py
Dependencies: sympy, numpy, scipy.
"""
import math
import sympy as s
import numpy as np
from scipy.linalg import expm

alpha, omega, lam, sig2 = s.symbols('alpha omega lam sig2', positive=True)
W2 = alpha**2 + omega**2
u = sig2/(W2 + lam*(lam+2*alpha))
A = u/(W2+lam*(lam-2*alpha))
V = u*(1+lam/(2*alpha))/W2
B = s.factor(V-A)
H = s.factor((alpha*B+lam*A)/omega)
# An oscillator with eigenvalues -alpha +- i omega and OU drive -lambda.
M = s.Matrix([[0,1,0],[-W2,-2*alpha,1],[0,0,-lam]])
S = s.Matrix(3,3, lambda i,j:s.symbols('s%d%d'%(min(i,j),max(i,j))))
Q = s.diag(0,0,2*lam*sig2)
eq = M*S + S*M.T + Q
sol = s.solve([eq[i,j] for i in range(3) for j in range(i,3)], list(set(S)), dict=True)
assert len(sol)==1
Ssol = S.subs(sol[0])
checks = 0
for lhs,rhs in [(Ssol[0,0],V),(Ssol[0,2],u),(Ssol[0,1],0),
                (Ssol[1,2],lam*u),(Ssol[1,1],lam*u/(2*alpha))]:
    assert s.factor(lhs-rhs)==0
    checks+=1
# Direct covariance solution: C(t)=A exp(-lambda t)+e^{-alpha t}(B cos omega t+H sin omega t).
assert s.factor((lam**2-2*alpha*lam+W2)*A-u)==0
assert s.factor(A+B-V)==0
assert s.factor(-lam*A-alpha*B+omega*H)==0
checks+=3
At=s.factor(A.subs(lam,alpha)); Bt=s.factor(B.subs(lam,alpha)); Ht=s.factor(H.subs(lam,alpha))
assert s.factor((Bt**2+Ht**2)/At**2-(4*alpha**2+omega**2)/(4*(alpha**2+omega**2)))==0
assert s.factor(At**2-Bt**2-Ht**2) == s.factor(3*sig2**2/(4*omega**2*(alpha**2+omega**2)*(4*alpha**2+omega**2)**2))
checks+=2
# Cross-check Fourier multiplier ratio by polynomial identity (no numerical integration).
xi=s.symbols('xi',real=True)
ratio=(lam/alpha)*(alpha**2+xi**2)/(lam**2+xi**2)
assert s.factor(ratio-(lam/alpha)*(1+(alpha**2-lam**2)/(lam**2+xi**2)))==0
checks+=1
# Independent matrix-exponential correlation check at several rational physical parameters.
params=[(1,2,s.Rational(1,2)),(1,2,1),(1,2,s.Rational(3,2)),
        (s.Rational(1,3),1,s.Rational(1,10)),(2,5,3),
        (3,s.Rational(91,10),s.Rational(31,10))]
for aa, ww, ll in params:
    av=float(aa); wv=float(s.sqrt(ww-aa*aa)); lv=float(ll)
    v=float(V.subs({alpha:aa,omega:s.sqrt(ww-aa*aa),lam:ll,sig2:1}))
    ar=float(A.subs({alpha:aa,omega:s.sqrt(ww-aa*aa),lam:ll,sig2:1}))
    br=float(B.subs({alpha:aa,omega:s.sqrt(ww-aa*aa),lam:ll,sig2:1}))
    hr=float(H.subs({alpha:aa,omega:s.sqrt(ww-aa*aa),lam:ll,sig2:1}))
    matrix=np.array([[0,1,0],[-float(ww),-2*av,1],[0,0,-lv]])
    var=np.array(Ssol.subs({alpha:aa,omega:s.sqrt(ww-aa*aa),lam:ll,sig2:1})).astype(float)
    for tt in [0.0,0.37,1.4,3.2,8.0]:
        direct=(expm(matrix*tt)@var)[0,0]
        closed=ar*math.exp(-lv*tt)+math.exp(-av*tt)*(br*math.cos(wv*tt)+hr*math.sin(wv*tt))
        assert abs(direct-closed)<2e-10*max(1,abs(direct),abs(closed)),(aa,ww,ll,tt,direct,closed)
        checks+=1
# At lambda<=alpha, verify a finite sample only: analytic proof uses a strictly positive convolution.
for av,wv in [(1,1),(0.1,1),(2,0.25)]:
    w0=av*av+wv*wv
    for lv in [0.1*av,0.8*av,av]:
        u0=1/(w0+lv*(lv+2*av)); a0=u0/(w0+lv*(lv-2*av)); v0=u0*(1+lv/(2*av))/w0
        b0=v0-a0; h0=(av*b0+lv*a0)/wv
        for tt in np.linspace(0,35/av,501):
            cv=a0*math.exp(-lv*tt)+math.exp(-av*tt)*(b0*math.cos(wv*tt)+h0*math.sin(wv*tt))
            assert cv > -2e-13
            checks+=1
print('PASS',checks,'independent symbolic/matrix/finite-sampling checks')
