"""Verify LCW phase algebra: eikonal, special solutions, reflection frequencies."""
import sympy as sp

# Eikonal for Euclidean: G(dPhi,dPhi)=0 with Phi = x3 + i x1? Check: grad Phi=(i,0,1); dot= i^2+0+1=0. OK.
# General linear phases: zeta.zeta=0.
tau, s = sp.symbols('tau s', real=True)
xi1,xi2,xi3 = sp.symbols('xi1 xi2 xi3', real=True)
# Pick concrete xi=(2,1,3). Build eta1 horizontal perp to xi'.
import numpy as np
xi = np.array([2.0,1.0,3.0])
xip = xi[:2]
v = np.array([-xip[1], xip[0]]); v/=np.linalg.norm(v)  # perp to xi'
eta1 = np.array([v[0],v[1],0.0])
print("eta1:",eta1,"|eta1|=",np.linalg.norm(eta1),"eta1.xi=",eta1@xi)
# eta2 = orthonormal to both xi and eta1
a = xi/np.linalg.norm(xi)
# Gram-Schmidt: take e = R eta1? compute null space
M = np.stack([a,eta1])
# eta2 = normalized component of random vector orthogonal to both
r = np.array([0.0,0.0,1.0])
for b in [a,eta1]:
    r = r - (r@b)*b
r/=np.linalg.norm(r)
eta2=r
print("eta2:",eta2,"dots:",eta2@a,eta2@eta1)
nrm=np.linalg.norm(xi)
sval=np.sqrt(max(60.0**2-nrm**2/4,0))
tauval=60.0
zeta1 = tauval*eta1 + 1j*(xi/2 + sval*eta2)
zeta2 = -tauval*eta1 + 1j*(xi/2 - sval*eta2)
print("zeta1.zeta1=",np.vdot(zeta1,zeta1) if False else zeta1@zeta1)
print("zeta2.zeta2=",zeta2@zeta2)
print("(zeta1+zeta2)-i*xi =", (zeta1+zeta2)-1j*xi)
R=np.diag([1.0,1.0,-1.0])
Rz1=R@zeta1; Rz2=R@zeta2
print("doubly reflected sum - iRxi:", (Rz1+Rz2)-1j*(R@xi))
m1=Rz1+zeta2; m2=zeta1+Rz2
print("mixed m1 real part:",m1.real,"|imag|=",np.abs(m1.imag),"|freq|=",np.linalg.norm(m1.imag))
print("mixed m2 real part:",m2.real,"|imag|=",np.linalg.norm(m2.imag))
print("zeta1.zeta2/tau^2 =", (zeta1@zeta2)/tauval**2)
# vertical-frequency case xi=(0,0,4)
xi=np.array([0.0,0.0,4.0])
eta1=np.array([1.0,0.0,0.0])
a=xi/np.linalg.norm(xi)
r=np.array([0.0,1.0,0.0])
for b in [a,eta1]:
    r=r-(r@b)*b
r/=np.linalg.norm(r)
eta2=r
zeta1=tauval*eta1+1j*(xi/2+sval*eta2); zeta2=-tauval*eta1+1j*(xi/2-sval*eta2)
print("vertical: zeta.zeta:",zeta1@zeta1, zeta2@zeta2, "sum-i xi:",zeta1+zeta2-1j*xi)
print("vertical mixed real:",(R@zeta1+zeta2).real,"imag norm:",np.linalg.norm((R@zeta1+zeta2).imag))
print("PHASE_ALGEBRA_OK")
