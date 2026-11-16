"""Independent Gauss-Legendre verification of cubic lunar concentration."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from math import pi,sqrt
q=100
z,wz=leggauss(q);t,wt=leggauss(q)
phi=(pi/4)*(t+1); wp=(pi/4)*wt
Z=z[:,None];X=np.sqrt(1-Z**2)*np.cos(phi)[None,:];Y=np.sqrt(1-Z**2)*np.sin(phi)[None,:]
P=np.stack([np.broadcast_to(Z*(5*Z**2-3),X.shape),Z*(X*X-Y*Y),2*X*Y*Z,X*(5*Z**2-1),Y*(5*Z**2-1),X*(X*X-3*Y*Y),Y*(3*X*X-Y*Y)],axis=-1)
N=np.array([16*pi/7,16*pi/105,16*pi/105,32*pi/21,32*pi/21,32*pi/35,32*pi/35])
T=np.einsum('ijk,ijl,i,j->kl',P,P,wz,wp)/np.sqrt(np.outer(N,N))
large=(5+sqrt(115))/(30*pi);small=(sqrt(115)-5)/(30*pi);zeta=sqrt(15)/(10*pi)
expect=np.sort(np.array([.25, .25-zeta,.25+zeta,.25-large,.25+large,.25-small,.25+small]))
assert np.max(np.abs(np.linalg.eigvalsh(T)-expect)) < 1e-12
print('PASS independent 100x100 Gauss-Legendre integration; sorted eigenvalues',np.round(np.linalg.eigvalsh(T),12),'max error',np.max(np.abs(np.linalg.eigvalsh(T)-expect)))
