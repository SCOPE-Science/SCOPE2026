"""Independent nonuniform aspect-ratio check of the full central-section law."""
import numpy as np,math
from scipy.spatial import ConvexHull
rng=np.random.default_rng(74133)
for h in (0.2,0.5,math.sqrt(math.sqrt(2))/2,1.5,4.0):
 V=np.array([(1,0,h),(0,1,h),(-1,0,h),(0,-1,h)]+[(i/math.sqrt(2),j/math.sqrt(2),-h) for i in (-1,1) for j in (-1,1)],float)
 E={(i,(i+1)%4) for i in range(4)}
 # bottom ring adjacency is based on the four diagonal-square edges.
 for i,j in ((4,5),(4,6),(5,7),(6,7)):E.add((i,j))
 for i in range(4):
  nn=sorted(range(4,8),key=lambda j:np.linalg.norm(V[i]-V[j]))
  for j in nn[:2]:E.add(tuple(sorted((i,j))))
 assert len(E)==16,(h,len(E))
 G=rng.normal(size=(100000,3));G/=np.linalg.norm(G,axis=1)[:,None]
 D=G@V.T
 count=np.zeros(len(G),dtype=int)
 for i,j in E:count+=(D[:,i]*D[:,j]<0)
 assert set(np.unique(count))=={6,8},(h,set(count))
 A=math.acos(h*h/(1+h*h)); B=math.acos((1/math.sqrt(2)-h*h)/(1+h*h))
 p=4*(A+B)/math.pi-3
 freq=np.mean(count==8);sdev=math.sqrt(p*(1-p)/len(G))
 assert abs(p-freq)<5*sdev,(h,p,freq)
 print('family',h,p,freq,'expected_N',6+2*p,flush=True)
print('FAMILY_CHECK_OK')
