"""Independent continuous-surface quadrature for a tetrahedral Voronoi Slepian operator."""
import numpy as np
from scipy.integrate import quad_vec
from numpy.polynomial.legendre import leggauss
E=np.array([1,1,1])/np.sqrt(3)
U=np.array([1,-1,0])/np.sqrt(2)
V=np.array([1,1,-2])/np.sqrt(6)
H=np.array([[1,1,0],[1,0,1],[0,1,1]])/np.sqrt(2)
xx,ww=leggauss(48)

def integrand(phi):
 w=np.cos(phi)*U+np.sin(phi)*V
 aa=H@E; bb=H@w
 lower=max([0.0]+[float(-b/np.sqrt(a*a+b*b)) for a,b in zip(aa,bb) if b<0])
 u=(1-lower)*xx/2+(1+lower)/2
 weight=ww*(1-lower)/2
 r=u[:,None]*E[None,:]+np.sqrt(1-u*u)[:,None]*w[None,:]
 t=r@E; a=r@U; b=r@V
 q=np.array([(3*t*t-1)/2,np.sqrt(3)*t*a,np.sqrt(3)*t*b,
             np.sqrt(3)*(a*a-b*b)/2,np.sqrt(3)*a*b]).T
 return 5/(4*np.pi) * np.einsum('i,ij,ik->jk',weight,q,q)
res,err=quad_vec(integrand,0,2*np.pi,epsabs=2e-11,epsrel=2e-11,limit=3000)
rt=np.sqrt
p=np.pi
exact=np.array([
[1/4+rt(3)/(9*p),0,0,0,0],
[0,1/4+11*rt(3)/(54*p),0,0,-rt(6)/(27*p)],
[0,0,1/4+11*rt(3)/(54*p),-rt(6)/(27*p),0],
[0,0,-rt(6)/(27*p),1/4-7*rt(3)/(27*p),0],
[0,-rt(6)/(27*p),0,0,1/4-7*rt(3)/(27*p)]])
vals=[.25+(-rt(3)-rt(219))/(36*p),.25+4*rt(3)/(36*p),.25+(-rt(3)+rt(219))/(36*p)]
assert abs(float(np.trace(res))-1.25)<1e-8
assert np.max(np.abs(res-exact))<5e-9, (res,exact,np.max(np.abs(res-exact)))
nps=np.linalg.eigvalsh(res)
assert np.max(np.abs(nps-np.array([vals[0],vals[0],vals[1],vals[2],vals[2]])))<5e-9
print('independent quadrature PASS; max matrix error:',np.max(np.abs(res-exact)))
print('eigenvalues:',nps, 'quad error est:',err)
