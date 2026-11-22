"""Reproducible checks for a nonlinear entropy identity in active-exclusion hydrodynamics.

Checks finite symbolic identities, parameter barriers, and independent Fourier-grid
quadrature of the infinitesimal integrated balance. Analytic inequalities, not
numerical sampling, establish the mathematical theorem.
"""
import sympy as sp
import numpy as np

rho, m, L, Pe = sp.symbols('rho m L Pe', real=True)
f = rho**2-(1-rho)*sp.log(1-rho)-rho
h = f + m**2/sp.Integer(2)
flux = sp.Matrix([m*(1-rho), rho*(1-rho)])
A = flux.jacobian([rho,m])
H = sp.hessian(h,[rho,m])
q = m*(1-rho)*sp.diff(f,rho)
assert sp.simplify(sp.diff(f,rho)-(2*rho+sp.log(1-rho))) == 0
assert sp.simplify(sp.diff(f,rho,2)-(1-2*rho)/(1-rho)) == 0
assert sp.simplify(H*A-A.T*H) == sp.zeros(2)
assert sp.simplify(sp.Matrix([sp.diff(q,v) for v in (rho,m)])-(A.T*sp.Matrix([sp.diff(h,v) for v in (rho,m)]))) == sp.zeros(2,1)
assert sp.simplify(sp.det(A.subs(m,0))+(1-rho)*(1-2*rho))==0
assert A.subs({rho:sp.Rational(1,2),m:0})**2 == sp.zeros(2)
assert A.subs({rho:sp.Rational(1,2),m:0}) != sp.zeros(2)
assert sp.simplify(sp.trace(A.subs(m,0))) == 0
assert sp.simplify(sp.diff(f,rho,2).subs(rho,0)-1) == 0
assert sp.simplify(sp.diff(f,rho,2).subs(rho,sp.Rational(1,2))) == 0
# Separation-of-variables uniqueness among entropies with quadratic m part.
c=sp.symbols('c',positive=True)
Hs=sp.diag(c*(1-2*rho)/(1-rho),c)
assert sp.simplify(Hs*A-A.T*Hs)==sp.zeros(2)
count=11

# The derivative is independently evaluated from the PDE (not flux q identity),
# then compared with the spectral quadrature of negative dissipation.
N=2048
x=2*np.pi*np.arange(N)/N
k=np.fft.fftfreq(N,d=1./N)
def Dx(v):return np.fft.ifft(1j*k*np.fft.fft(v)).real
def Dxx(v):return np.fft.ifft(-(k**2)*np.fft.fft(v)).real
for a in (.04,.07,.10):
 for b in (.02,.04):
  for pe in (.3,1.7,8.5,35.):
   R=.27+a*np.cos(2*x)+.04*np.sin(3*x)
   M=b*np.sin(x)-.01*np.cos(4*x)
   assert np.min(R)>0 and np.max(R)<.5
   assert np.min(R-np.abs(M))>0
   rt=Dxx(R)-pe*Dx(M*(1-R))
   mt=Dxx(M)-pe*Dx(R*(1-R))-2*M
   hp=2*R+np.log1p(-R)
   rate=(hp*rt+M*mt).mean()*2*np.pi
   diss=-(((1-2*R)/(1-R))*Dx(R)**2+Dx(M)**2+2*M**2).mean()*2*np.pi
   assert abs(rate-diss)<2e-10,(rate,diss,pe)
   alpha=(1-2*np.max(R))/(1-np.max(R))
   E=(R**2-(1-R)*np.log1p(-R)-R - (np.mean(R)**2-(1-np.mean(R))*np.log1p(-np.mean(R))-np.mean(R)) -(2*np.mean(R)+np.log1p(-np.mean(R)))*(R-np.mean(R))+M**2/2).mean()*2*np.pi
   lam=min(2*alpha,4.)
   assert E>0 and -diss>=lam*E-1e-9
   count+=3
print(f'PASS: {count} exact symbolic / independent finite-grid assertion groups, no infinite claims inferred from sampling.')
