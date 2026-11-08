"""Independent floating-point section construction, with fixed-seed integration check."""
import numpy as np,math
from scipy.spatial import ConvexHull
rng=np.random.default_rng(260411)
t=2**.25
V=np.array([(2,0,t),(0,2,t),(-2,0,t),(0,-2,t),(-t*t,-t*t,-t),(-t*t,t*t,-t),(t*t,-t*t,-t),(t*t,t*t,-t)],float)
E=[(i,j) for i in range(8) for j in range(i+1,8) if abs(np.dot(V[i]-V[j],V[i]-V[j])-8)<1e-10]
assert len(E)==16
angles=[]
N=300000
U=rng.normal(size=(N,3));U/=np.linalg.norm(U,axis=1)[:,None]
S=U@V.T
c=np.zeros(N,dtype=int)
for i,j in E:c+=(S[:,i]*S[:,j]<0)
assert set(np.unique(c))=={6,8}
prob=(c==8).mean(); exact=8/math.pi*math.acos((2*math.sqrt(2)-1)/7)-3
se=math.sqrt(exact*(1-exact)/N)
assert abs(prob-exact)<5*se
# independent polygon reconstruction for a subset of normals
for u,co in zip(U[:300],c[:300]):
 hits=[]
 for i,j in E:
  aa=np.dot(V[i],u); bb=np.dot(V[j],u)
  if aa*bb<0: hits.append(V[i]+aa/(aa-bb)*(V[j]-V[i]))
 pts=np.array(hits)
 # actual independent hull in local plane, vertices distinct
 base=np.cross(u,[0,0,1])
 if np.linalg.norm(base)<1e-8:base=np.cross(u,[0,1,0])
 base/=np.linalg.norm(base); another=np.cross(u,base)
 H=ConvexHull(np.column_stack((pts@base,pts@another)))
 assert len(H.vertices)==co
print('NUMERIC_CHECK_OK',N,300,'p_octagon',prob,'exact',exact,'SE',se)
