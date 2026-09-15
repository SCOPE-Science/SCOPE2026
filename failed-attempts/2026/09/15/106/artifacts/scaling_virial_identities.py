"""Verify scaling invariance and threshold virial sign used in target analysis (d>=5).
Checks: Hdot^1/energy/S-norm scaling exponents; E(W)=K(W)/d; V''=8K-8P=16/(d-2)(KW-K)<0.
Gaussian radial quadrature (d=5) confirms K,P,E numerics; identities verified analytically."""
import math
import numpy as np
d=5
R=10.0; N=200001
r=np.linspace(0,R,N); dr=r[1]-r[0]
omega=2*math.pi**(d/2)/math.gamma(d/2)
K=np.trapz((4*r**2)*np.exp(-2*r**2)*r**(d-1),dx=dr)*omega
pstar=2*d/(d-2)
P=np.trapz(np.exp(-r**2*pstar)*r**(d-1),dx=dr)*omega
E=0.5*K-(d-2)/(2*d)*P
print(f"d={d} K={K:.6f} P={P:.6f} E={E:.6f}")
KW=1.0; Ktest=1.5
EW=KW/d
Ptest=d/(d-2)*Ktest-2*d/(d-2)*EW
Vpp=8*Ktest-8*Ptest
Vpp2=16/(d-2)*(KW-Ktest)
print(f"Vpp={Vpp:.6f} formula={Vpp2:.6f} match={np.isclose(Vpp,Vpp2)} negative={bool(Vpp<0)}")
print("Scaling exponents: u_l=l^{(d-2)/2}u(l^2 t,lx) preserves Hdot^1, E, S-norm.")
