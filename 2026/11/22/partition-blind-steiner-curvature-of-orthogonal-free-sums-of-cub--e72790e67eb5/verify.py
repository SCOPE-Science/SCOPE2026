import itertools, math
import numpy as np
from scipy.spatial import ConvexHull

def calc(parts):
 d=sum(parts); m=len(parts)
 starts=np.cumsum([0]+list(parts[:-1])).tolist()
 verts=[]
 for i,r in enumerate(parts):
  for signs in itertools.product([-1.,1.],repeat=r):
   v=np.zeros(d);v[starts[i]:starts[i]+r]=signs;verts.append(v)
 verts=np.array(verts)
 normals=[]
 for picks in itertools.product(*[[(j,s) for j in range(r) for s in (-1,1)] for r in parts]):
  v=np.zeros(d)
  for i,(j,s) in enumerate(picks):v[starts[i]+j]=s
  normals.append((picks,v))
 vol=ConvexHull(verts).volume if d>=2 else 2
 expected_vol=2**d*math.prod(math.factorial(r) for r in parts)/math.factorial(d)
 assert abs(vol-expected_vol)<1e-7,(parts,vol,expected_vol)
 facets=[np.where(np.abs(verts@v-1)<1e-7)[0] for p,v in normals]
 areas=[];ang=[];ridgerows=[]
 for k,l in itertools.combinations(range(len(normals)),2):
  ids=np.intersect1d(facets[k],facets[l])
  if len(ids)<d-1:continue
  pts=verts[ids]; p0=pts[0]; _u,_s,vt=np.linalg.svd(pts-p0, full_matrices=False)
  rank=int(sum(_s>1e-8))
  if rank!=d-2:continue
  if rank==0:A=1.
  elif rank==1:
   coords=(pts-p0)@vt[:1].T
   A=float(coords.max()-coords.min())
  else:
   coords=(pts-p0)@vt[:rank].T
   A=ConvexHull(coords).volume
  cos=float(np.dot(normals[k][1],normals[l][1])/m)
  alpha=math.acos(max(-1,min(1,cos)))
  changed=sum(1 for a,b in zip(normals[k][0],normals[l][0]) if a!=b)
  assert changed==1, (parts,normals[k],normals[l],changed)
  index=next(i for i,(a,b) in enumerate(zip(normals[k][0],normals[l][0])) if a!=b)
  ri=parts[index]
  if ri==1:
   typ='singleton'
   expected_area=(math.sqrt(m-1)*2**(d-m)*math.prod(math.factorial(rr-1) for j,rr in enumerate(parts) if j!=index)/math.factorial(d-2))
  else:
   typ='non-singleton'
   expected_area=(math.sqrt(2*m-1)*2**(d-m-1)*math.factorial(ri-2)*math.prod(math.factorial(rr-1) for j,rr in enumerate(parts) if j!=index)/math.factorial(d-2))
  assert abs(A-expected_area)<1e-7,(parts, A, expected_area,ids,k,l)
  areas.append(A);ang.append(alpha);ridgerows.append(typ)
 s=parts.count(1)
 target_ridges=math.prod(2*r for r in parts)*(d-m+s/2)
 assert len(areas)==target_ridges,(parts,len(areas),target_ridges)
 c2=0.5*sum(a*w for a,w in zip(areas,ang))
 alpha2=math.acos((m-1)/m)
 alpha1=math.acos((m-2)/m)
 target_c2=expected_vol*d*(d-1)/4*((m-s)*math.sqrt(2*m-1)*alpha2+s*math.sqrt(m-1)*alpha1)
 assert abs(c2-target_c2)<1e-6,(parts,c2,target_c2)
 sarea=ConvexHull(verts).area
 assert abs(sarea-expected_vol*d*math.sqrt(m))<1e-6,(parts,sarea,expected_vol*d*math.sqrt(m))
 print(parts, 'vertices',len(verts),'facets',len(facets),'ridges',len(areas),'volume',round(vol,6),'surface',round(sarea,6),'C2',round(c2,6),'types', {t:ridgerows.count(t) for t in set(ridgerows)})

if __name__=='__main__':
 for p in [(2,), (3,), (4,), (1,1),(1,2),(1,3),(2,2),(1,1,1),(1,1,2),(1,2,2),(2,3),(1,1,3),(1,1,1,1)]:
  calc(p)
 print('HANNER_STEINER_CHECK_PASS')
