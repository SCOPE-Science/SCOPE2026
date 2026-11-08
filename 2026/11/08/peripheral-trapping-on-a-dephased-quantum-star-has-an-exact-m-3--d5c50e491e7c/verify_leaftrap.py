import numpy as np

def solve(n,J,gamma,kappa):
  # star: hub 0, trap leaf 1, m=n-2 other leaves 2..n-1
  H=np.zeros((n,n));H[0,1:]=J;H[1:,0]=J
  P=np.zeros((n,n));P[1,1]=1
  # vec col-major; dρ=-i[H,ρ]-gamma offdiag -kappa/2{P,ρ}
  I=np.eye(n)
  L=-1j*(np.kron(I,H)-np.kron(H.T,I))
  for x in range(n):
    for y in range(n):
      if x!=y: L[x+n*y,x+n*y]-=gamma
      if x==1 or y==1:L[x+n*y,x+n*y]-=kappa*(int(x==1)+int(y==1))/2
  rho=np.zeros((n,n));rho[2,2]=1
  v=np.linalg.solve(-L,rho.reshape(-1,order='F')).reshape((n,n),order='F')
  return np.trace(v).real

def formula(m,J,gamma,kappa):
 return (m+2)/kappa + m*(m-1)/(2*(gamma+kappa/2)) + (m-1)/gamma + ((m+2)*gamma+(m+1)*kappa/2)/(2*J*J)
if __name__=='__main__':
 for m in (1,2,3,4,7):
  for J in (.7,1.0,2.1):
   for g in (.1,1.1,3.7):
    for k in (.7,1.4):
     a=solve(m+2,J,g,k);b=formula(m,J,g,k)
     if abs(a-b)>1e-7:print('FAIL',m,J,g,k,a,b);raise SystemExit(1)
 print('All 90 full quantum Lindblad comparisons passed')
