"""Scientific numerical diagnostics for a rectangular box's paired width/brightness law."""
import math,itertools
import numpy as np
from scipy.stats import qmc

def props(a,b,c):
 v=np.array([a,b,c],float); w=np.array([b*c,a*c,a*b],float)
 L=np.stack([v,w]); G=L@L.T
 k=np.cross(v,w); k/=np.linalg.norm(k)
 p,q,r=-k[0],k[1],-k[2]
 assert 0<p<1 and 0<r<1 and q*q>.5
 amb=(4/math.pi)*(math.asin(2*p*q)+math.asin(2*q*r)-math.asin(p)-math.asin(r))
 assert 0<amb<1
 R=np.eye(3)-2*np.outer(k,k)
 H=np.vstack([np.eye(3),R]); vv=[]
 for i,j in itertools.combinations(range(6),2):
  x=np.cross(H[i],H[j]); n=np.linalg.norm(x)
  if n<1e-12: continue
  x/=n
  for u in (x,-x):
   if min(H@u)>-1e-9 and not any(np.linalg.norm(u-z[0])<1e-8 for z in vv):vv.append((u,(i,j)))
 assert len(vv)==6, len(vv)
 center=sum((u for u,_ in vv),np.zeros(3)); center/=np.linalg.norm(center)
 e1=vv[0][0]-(vv[0][0]@center)*center;e1/=np.linalg.norm(e1);e2=np.cross(center,e1)
 vv=sorted(vv,key=lambda v: math.atan2(v[0]@e2,v[0]@e1))
 def area3(u,v,w):
  return 2*math.atan2(abs(np.linalg.det(np.stack([u,v,w]))), 1+u@v+v@w+w@u)
 area=sum(area3(center,vv[i][0],vv[(i+1)%6][0]) for i in range(6))
 assert abs(2*area/math.pi-amb)<2e-12,(area,amb)
 # deterministic low-discrepancy points uniform on first octant of sphere
 zs=qmc.Sobol(2,scramble=True,seed=281).random_base2(17)
 x=np.cos(2*math.pi*zs[:,0])*np.sqrt(1-zs[:,1]**2); y=np.sin(2*math.pi*zs[:,0])*np.sqrt(1-zs[:,1]**2); z=zs[:,1]
 u=np.abs(np.stack((x,y,z),axis=1));u/=np.linalg.norm(u,axis=1)[:,None]
 t=u@L.T
 reflected=u@R
 mark=np.all(reflected>=0,axis=1)
 assert abs(mark.mean()-amb)<.0025,(mark.mean(),amb)
 rec=np.linalg.solve(G,t.T).T@L
 h=np.sqrt(np.maximum(0,1-np.einsum('ni,ni->n',rec,rec)))
 c1=rec+h[:,None]*k;c2=rec-h[:,None]*k
 assert max(np.min(np.linalg.norm(c1-u,axis=1)),np.min(np.linalg.norm(c2-u,axis=1)))<1e-9
 which=np.maximum(np.linalg.norm(c1-u,axis=1),np.linalg.norm(c2-u,axis=1))<1e-9
 assert np.mean(which)<1e-4
 flag=np.all(c1>=-1e-9,axis=1)&np.all(c2>=-1e-9,axis=1)
 assert np.array_equal(flag,mark)
 return (a,b,c,p,q,r,amb,mark.mean(),area,math.sqrt(np.linalg.det(G)))

if __name__=='__main__':
 for tup in [(1,2,3),(1,3,9),(1,1.2,1.5),(1,2,2.1),(1,1.01,3),(1,10,100)]:
  print(props(*tup))
 print('All analytic and sampled checks passed.')
