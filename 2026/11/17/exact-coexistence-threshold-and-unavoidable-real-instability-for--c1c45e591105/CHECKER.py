import math
import numpy as np
from scipy.optimize import brentq

def test(a,l,b,m,d,tau,alpha=2.,mu=1.):
 a=np.array(a,float);l=np.array(l,float);b=np.array(b,float);m=np.array(m,float);d=np.array(d,float);tau=np.array(tau,float)
 e=np.exp(-mu*tau);p=a*(1-b*e);assert min(p)>-1e-10
 def q(s,u):return d/(m+p*s+l*u)
 def g(s,u):return mu*u-s*np.sum(a*(1-e)*q(s,u))
 def u(s):return brentq(lambda uu:g(s,uu),0.,max(1.,s*sum(a*(1-e)*d/m)/mu+1))
 s=brentq(lambda ss:sum(a*q(ss,u(ss)))-alpha,0,1e5);ui=u(s);qi=q(s,ui)
 D=m+p*s+l*ui
 fs=-sum(a*qi*p/D);fu=-sum(a*qi*l/D)
 gs=-sum(a*(1-e)*qi*(m+l*ui)/D);gu=mu+s*sum(a*(1-e)*qi*l/D)
 det_expected=s*np.prod(D)*(fs*gu-fu*gs)
 def charmat(lam):
  M=np.eye(2+len(a))*lam
  # instantaneous Jacobian
  J=np.zeros_like(M)
  J[0,2:]=-s*a
  J[1,0]=alpha;J[1,1]=-mu;J[1,2:]=s*a
  for i in range(len(a)):
   J[2+i,0]=-a[i]*qi[i];J[2+i,1]=-l[i]*qi[i];J[2+i,2+i]=-(m[i]+a[i]*s+l[i]*ui)
  M-=J
  for i in range(len(a)):
   discount=math.exp(-lam*tau[i]);
   M[1,0]+=a[i]*e[i]*qi[i]*discount
   M[1,2+i]+=s*a[i]*e[i]*discount
   M[2+i,0]-=a[i]*b[i]*e[i]*qi[i]*discount
   M[2+i,2+i]-=a[i]*b[i]*e[i]*s*discount
  return M
 det0=np.linalg.det(charmat(0.))
 assert np.isclose(det0,det_expected,rtol=1e-8,atol=1e-8),(det0,det_expected)
 root=brentq(lambda x: np.linalg.det(charmat(x)),0,100)
 v=np.linalg.svd(charmat(root))[2][-1]
 # compatibility for growing eigenmode
 rhs=sum(a[i]*(v[2+i]*s+v[0]*qi[i])*(1-math.exp(-(root+mu)*tau[i]))/(root+mu) for i in range(len(a)))
 assert abs(v[1]-rhs)<2e-7
 print('n',len(a),'s',s,'I',ui,'det0',det0,'Ddet',det_expected,'root',root,'compatibility residual',v[1]-rhs)

test([1,2],[1,1],[1,2],[1,1],[2,2],[math.log(2),math.log(3)])
test([1,2,1.5],[2,1,3],[1,2,1.1],[1.3,1.2,1.1],[2,1,3],[math.log(2),math.log(4),math.log(2.5)])
test([1,2],[1,1],[2,3],[1,1],[2,2],[math.log(2),math.log(3)])
