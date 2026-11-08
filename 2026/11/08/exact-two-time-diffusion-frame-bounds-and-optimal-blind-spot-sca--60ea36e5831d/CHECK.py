import numpy as np
from scipy.optimize import minimize_scalar,brentq
from math import exp,sinh,cosh

def eig(u,t):
 a=exp(-t*(1-u));b=exp(-t*(1+u))
 M=np.array([[1,1],[a,b]],dtype=float)/np.sqrt(2)
 return np.linalg.eigvalsh(M.T@M)

def formula(u,t):
 d=exp(-2*t)*sinh(t*u)**2
 T=1+exp(-2*t)+2*d
 root=np.sqrt(T*T-4*d)
 return np.array([2*d/(T+root), (T+root)/2]) # smallest stable

ctr=0
for c in [.01,.05,.25,.5,.8,.95,.99]:
 for t in [.1,.5,1,1.1,2,4,7]:
  grid=np.linspace(c,1,1001)
  spec=np.array([eig(u,t) for u in grid]);
  A,B=formula(c,t)[0],formula(1,t)[1]
  assert np.max(np.abs(spec[0]-formula(c,t)))<1e-12
  assert abs(spec[:,0].min()-A)<1e-12
  assert abs(spec[:,1].max()-B)<1e-12
  assert np.all(np.diff(spec[:,0])>=-1e-12), (c,t)
  assert np.all(np.diff(spec[:,1])>=-1e-12), (c,t)
  ctr+=1
candidates=[]
for c in [.0002,.001,.01,.03,.1,.4,.8,.98]:
 res=minimize_scalar(lambda t:-formula(c,t)[0],bounds=(1e-5,100),method='bounded',options={'xatol':1e-12})
 candidates.append((c,res.x,-res.fun,(-res.fun)/(c*c)))
t0=brentq(lambda t:t-1-exp(-2*t),1,1.5)
lim=t0*t0/(1+exp(2*t0))
print('ALIAS_SPECTRAL_TESTS_PASSED',ctr,'time_opt',candidates,'t0',t0,'limit',lim)
# independent: periodic N=512, frequencies DFT eigenframe directly
for N in (128,256):
 for c in (.05,.4,.9):
  theta=2*np.pi*np.fft.fftfreq(N)
  allowed=(np.abs(np.cos(theta))>=c+1e-10)
  basis=np.flatnonzero(allowed)
  # normalized Fourier basis phi_j(n)=exp(i theta_j n)/sqrt(N)
  X=np.exp(1j*np.outer(np.arange(N),theta[basis]))/np.sqrt(N)
  L=np.eye(N)-0.5*(np.roll(np.eye(N),1,axis=0)+np.roll(np.eye(N),-1,axis=0))
  # use exact evolution via each Fourier eigenvector
  t=1.1
  Y=np.concatenate([X[::2,:],(X*np.exp(-t*(1-np.cos(theta[basis]))))[::2,:]],axis=0)
  ew=np.linalg.eigvalsh(Y.conj().T@Y)
  assert ew.min()+1e-10>=formula(c,t)[0]
  assert ew.max()-1e-10<=formula(1,t)[1]
  # compare to exact fiber eigenvalues
  u=np.abs(np.cos(theta[:N//2]));
  selected=np.where(u>=c+1e-10)[0]
  reference=np.sort(np.concatenate([formula(uu,t) for uu in u[selected]]))
  assert np.max(np.abs(reference-np.sort(ew)))<1e-10, (N,c,len(reference),len(ew))
print('FINITE_LATTICE_INDEPENDENT_CHECKS_PASSED')
