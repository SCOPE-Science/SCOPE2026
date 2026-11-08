import numpy as np, math
rng=np.random.default_rng(2026)
checks=0
for m in range(2,9):
 for _ in range(25):
  diag=np.sort(rng.uniform(0.5,5,size=m)); edges=rng.uniform(0.1,2,size=m-1)
  mat=np.diag(diag)+np.diag(edges,k=1)
  r=float(rng.uniform(.02,7))
  if min(abs(r-diag))<0.01:continue
  r0=np.linalg.norm(np.linalg.inv(mat-r*np.eye(m)),2)
  for theta in np.linspace(0,2*np.pi,33):
   c=np.linalg.norm(np.linalg.inv(mat-r*np.exp(1j*theta)*np.eye(m)),2)
   assert c<=r0*(1+2e-10),(m,theta,c,r0)
   checks+=1
for _ in range(600):
 a,b=sorted(rng.uniform(.1,6,2));gamma=rng.uniform(.01,5)
 h=(b-a)/2;c=gamma**2/2;eps=(np.sqrt((b-a)**2+gamma**2)-gamma)/2
 x=rng.uniform(-h,h);r=(a+b)/2+x
 B=np.array([[a-r,gamma],[0,b-r]])
 sv=np.linalg.svd(B,compute_uv=False)[-1]
 f2=x*x+h*h+c-np.sqrt((2*h*h+c)*(2*x*x+c))
 assert abs(sv**2-f2)<5e-12, (a,b,gamma,x,sv,f2)
 svmid=np.linalg.svd(np.array([[-h,gamma],[0,h]]),compute_uv=False)[-1]
 assert abs(svmid-eps)<5e-12
 checks+=2
print('diagnostics',checks,'passed')
