import numpy as np,itertools,math
from scipy.spatial import ConvexHull
from math import comb, factorial

def poly(c,m):
 N=c+m
 vs=[]
 for i in range(c):
  v=np.zeros(N);v[i]=1;vs.append(v)
 for bit in itertools.product((0,1),repeat=m):
  v=np.zeros(N);v[c:]=bit;vs.append(v)
 vs=np.array(vs)
 facets=[]
 for i in range(c):
  a=np.zeros(N);a[i]=-1;facets.append(('A',i,a,0))
 for j in range(m):
  a=np.zeros(N);a[c+j]=-1;facets.append(('B',j,a,0))
 for j in range(m):
  a=np.zeros(N);a[:c]=1;a[c+j]=1;facets.append(('C',j,a,1))
 return vs,facets

def intrinsic_vol(vs):
 if len(vs)==0:return 0,0
 p=vs[0];u,s,vt=np.linalg.svd(vs-p)
 d=int(np.sum(s>1e-7));
 if d==0:return 0,1
 q=(vs-p)@vt[:d].T
 if d==1:return d,float(np.ptp(q[:,0]))
 return d,ConvexHull(q).volume

def checks(c,m):
 vs,facets=poly(c,m);N=c+m
 dim,v=intrinsic_vol(vs)
 assert dim==N
 vol=factorial(m)/factorial(N)
 assert abs(v-vol)<1e-8,(c,m,v,vol)
 area=0;sum_angle=0;typeridge={}
 for f in facets:
  a=f[2];off=f[3]
  face=vs[np.abs(vs@a-off)<1e-9]
  fd,fa=intrinsic_vol(face)
  assert fd==N-1,(c,m,f,fd)
  area+=fa
 for i,f in enumerate(facets):
  for g in facets[i+1:]:
   mask=(np.abs(vs@f[2]-f[3])<1e-9)&(np.abs(vs@g[2]-g[3])<1e-9)
   d,a=intrinsic_vol(vs[mask]);
   if d!=N-2:continue
   co=np.dot(f[2],g[2])/(np.linalg.norm(f[2])*np.linalg.norm(g[2]));angle=math.acos(np.clip(co,-1,1))
   sum_angle+=a*angle
   ty= ''.join(sorted((f[0],g[0])))
   typeridge.setdefault(ty,[]).append((a,angle))
 expected_area=vol*N*(c+1+math.sqrt(c+1))
 assert abs(area-expected_area)<1e-7,(c,m,area,expected_area)
 K=(c*c+c+1+2*math.sqrt(c+1))/8+c*math.sqrt(c)*math.acos(-1/math.sqrt(c+1))/(2*math.pi)+math.sqrt(2*c+1)*math.acos(c/(c+1))/(4*math.pi)
 expected_v2=vol*N*(N-1)*K
 measured_v2=sum_angle/(2*math.pi)
 assert abs(expected_v2-measured_v2)<1e-7,(c,m,expected_v2,measured_v2)
 expected_counts={"AA":comb(c,2),"AB":c*m,"AC":c*m,"BB":comb(m,2),"BC":m*(m-1),"CC":comb(m,2)}
 for k,cnt in expected_counts.items():assert len(typeridge.get(k,[]))==cnt,(c,m,k,cnt,len(typeridge.get(k,[])))
 print('PROFILE',c,m,'vertices',len(vs),'facets',len(facets),'ridges',sum(map(len,typeridge.values())),'volume',vol,'area',round(area,7),'V_N-2',round(measured_v2,7))

if __name__=='__main__':
 for c,m in [(1,2),(1,3),(2,2),(2,3),(3,2),(2,4),(4,2)]:checks(c,m)
 print('SPLIT_STEINER_DIRECT_PASS')
