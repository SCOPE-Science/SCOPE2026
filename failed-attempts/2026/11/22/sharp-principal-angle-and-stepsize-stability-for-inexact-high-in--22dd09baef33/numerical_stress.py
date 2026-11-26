import numpy as np
from math import sin,cos,pi
rng=np.random.default_rng(271828)
maxbad=0
cases=0
for n in [2,3,5,8,12]:
 for k in range(1,n):
  for it in range(40):
   basis,_=np.linalg.qr(rng.normal(size=(n,n)))
   d=rng.uniform(.3,5,size=n)
   d[0]=.3; d[-1]=5
   S=basis@np.diag([-1]*k+[1]*(n-k))@basis.T
   P=(np.eye(n)-S)/2
   # sample Q by rotating source subspace toward complement, Givens in one plane
   theta=float(rng.uniform(0,np.pi/4-0.025))
   v=basis[:,0]*cos(theta)+basis[:,k]*sin(theta)
   C=np.column_stack([v,*[basis[:,j] for j in range(1,k)]])
   Q=C@C.T
   U=(np.eye(n)-2*Q)@S
   co=cos(2*theta)
   eta=float(rng.uniform(.001,2*co/5*.98))
   D=basis@np.diag(d)@basis.T
   Dhalf=basis@np.diag(np.sqrt(d))@basis.T
   L=max(d);mu=min(d)
   T=np.eye(n)-eta*Dhalf@U@Dhalf
   b=1-eta*mu*(2*co-eta*L)
   gap=np.linalg.eigvalsh(b*np.eye(n)-T.T@T)[0]
   if gap<-1e-9:
    print('FAIL', n,k,it,gap,theta,eta);raise SystemExit(1)
   assert np.linalg.norm((U+U.T)/2-(np.eye(n)-2*(P-Q)@(P-Q)))<1e-10
   assert np.linalg.norm(P-Q,ord=2)<=sin(theta)+1e-10
   maxbad=max(maxbad,-gap)
   cases+=1
print('PASS random projector stress',cases,'maximum violation',maxbad)
# two dimensional sharp witness in D=L I
for t in [0.12,0.35,pi/4,1.0]:
 c=cos(2*t)
 P=np.diag([1,0]);v=np.array([cos(t),sin(t)]);Q=np.outer(v,v)
 U=(np.eye(2)-2*Q)@np.diag([-1,1])
 for eta in [.0001, .11, .5,1.2]:
  T=np.eye(2)-eta*U
  val=max(np.linalg.svd(T,compute_uv=False))**2
  formula=1-2*eta*c+eta**2
  assert abs(val-formula)<1e-12,(val,formula)
print('PASS sharp 2x2 witnesses')
