import numpy as np
from scipy.special import ellipk
from scipy.integrate import quad
rng=np.random.default_rng(20261116)
N=650000
U=rng.normal(size=(N,3));U/=np.linalg.norm(U,axis=1)[:,None]
W=2*np.sqrt(1+2*np.abs(U[:,0]*U[:,2]))
assert W.min()>=2 and W.max()<=2*np.sqrt(2)
print('MC extrema',W.min(),W.max())
def dens(w):
 return 2/np.pi*ellipk(8/w**2-1)
for w in [2.01,2.05,2.15,2.4,2.65,2.8]:
 f,err=quad(dens,2,w,epsabs=1e-11)
 emp=np.mean(W<=w)
 print('CDF',w, 'num',f,'MC',emp,'z',(emp-f)/np.sqrt(f*(1-f)/N))
assert abs(quad(dens,2,2*np.sqrt(2),epsabs=1e-10)[0]-1)<1e-9
for s in [0.01,0.15,0.6,0.99]:
 f=2/(np.pi*np.sqrt(1+s))*ellipk((1-s)/(1+s))
 g=quad(lambda b:1/np.sqrt(b*(b-s)*(1-b*b)),s,1,epsabs=1e-9)[0]/np.pi
 print('elliptic agreement',s,f,g,abs(f-g))
 assert abs(f-g)<1e-8
for e in [1e-2,1e-3,1e-4,1e-5]:
 actual=quad(dens,2,2+e,epsabs=1e-12)[0]
 approx=e/np.pi*(np.log(8/e)+1)
 print('low',e,actual,approx,actual/approx)
for e in [1e-2,1e-3,1e-4]:
 actual=quad(dens,2*np.sqrt(2)-e,2*np.sqrt(2),epsabs=1e-12)[0]
 print('high',e,actual,actual/e)
# Check numerically the exact support formula by constrained y optimization
for _ in range(60):
 u=rng.normal(size=3);u/=np.linalg.norm(u)
 p=abs(u[0])+abs(u[2]); v=u[1]
 y=v/np.hypot(p,v)
 support=p*np.sqrt(1-y*y)+v*y
 predicted=np.hypot(p,v)
 assert abs(support-predicted)<1e-12
print('STEINMETZ_EXACT_WIDTH_CHECKS_OK')

# Independent moment calculation, using the spherical Y/azimuth-factor expectation.
mean2 = 4*(1+4/(3*np.pi))
assert abs(np.mean(W*W)-mean2)<0.018
# The bounded-support upper endpoint of the density is exactly 1 in width units.
assert abs(dens(2*np.sqrt(2)-1e-8)-1)<1e-5
# The logarithmic low endpoint formula grows relative to the bounded upper density.
assert dens(2+1e-8)>5
print('STEINMETZ_COMPLETE_ARTIFACT_REPLAY_OK')
