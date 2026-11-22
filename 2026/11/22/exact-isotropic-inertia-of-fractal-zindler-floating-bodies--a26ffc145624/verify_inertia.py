import numpy as np
for beta,alpha in [(7,8.),(9,10.5)]:
 for K in [1,2,3]:
  r=25.
  w=np.array([beta**k for k in range(1,K+1)],float);a=np.array([alpha**(-k) for k in range(1,K+1)],float)
  N=2**18; t=np.arange(N)*2*np.pi/N
  q=np.sum(a[:,None]*np.sin(w[:,None]*t),axis=0)
  p=np.sum((a*w)[:,None]*np.cos(w[:,None]*t),axis=0)
  qpp=np.sum(-(a*w*w)[:,None]*np.sin(w[:,None]*t),axis=0)
  Jnumeric=np.pi/2*np.mean((q*q+(r+p)**2)*(q*(q+qpp)+r*(r+p)))
  A=np.sum(a*a);B=np.sum((a*w)**2);C=np.sum(a**4);D=np.sum((a*w)**4);E=np.sum(a**4*w*w)
  T=3*A*A/4-3*C/8-A*B/2+E/4-B*B/4+D/8
  Jformula=np.pi/2*(r**4+r*r*(A+B)+T)
  assert abs(Jnumeric-Jformula) < 2e-9, (beta,alpha,K,Jnumeric,Jformula)
  print('PASS',beta,alpha,K,'error',Jnumeric-Jformula)
