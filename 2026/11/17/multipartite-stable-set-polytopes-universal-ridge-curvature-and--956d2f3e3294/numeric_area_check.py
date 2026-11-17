import itertools, numpy as np, math
from scipy.spatial import ConvexHull

for ns in [(1,1,2),(1,2,2),(1,1,1,2,2),(1,1,1,2,3)]:
 k=len(ns); N=sum(ns); blocks=[];off=0
 for n in ns:blocks.append(list(range(off,off+n)));off+=n
 vs=[tuple([0]*N)]
 for b in blocks:
  for mask in range(1,2**len(b)):
   v=[0]*N
   for j,i in enumerate(b):v[i]=(mask>>j)&1
   vs.append(tuple(v))
 vs=np.array(vs);facets=[]
 for j in range(N):
  n=np.zeros(N,dtype=int);n[j]=-1
  facets.append(('L',j,n,0))
 for c in itertools.product(*blocks):
  n=np.zeros(N,dtype=int);n[list(c)]=1
  facets.append(('U',c,n,1))
 C=math.prod(math.factorial(v) for v in ns)/math.factorial(N-2);Q=math.prod(ns)
 by_kind={}
 for f,g in itertools.combinations(facets,2):
  face=vs[(vs@f[2]==f[3]) & (vs@g[2]==g[3])].astype(float)
  if len(face)<N-1:continue
  proj=face-face[0];u,s,vh=np.linalg.svd(proj,full_matrices=False)
  if sum(s>1e-7)!=N-2:continue
  z=proj@vh[:N-2].T
  if N-2==2: vol=ConvexHull(z).volume
  else:vol=ConvexHull(z).volume
  if f[0]=='L' and g[0]=='L':
   t='LL';i=next(i for i,b in enumerate(blocks) if f[1] in b); j=next(j for j,b in enumerate(blocks) if g[1] in b)
   expected=C/(ns[i]*(ns[i]-1)) if i==j else C/(ns[i]*ns[j])
  elif f[0]=='L' and g[0]=='U':
   i=next(i for i,b in enumerate(blocks) if f[1] in b)
   if f[1] in g[1]:t='LU_acute';expected=math.sqrt(k-1)*C/Q
   else:t='LU_right';expected=math.sqrt(k)*C/(Q*(ns[i]-1))
  else:
   t='UU';i=next(i for i,b in enumerate(blocks) if f[1][i]!=g[1][i]);expected=math.sqrt(2*k-1)*C/(Q*(ns[i]-1))
  assert abs(vol-expected)<2e-7,(ns,t,vol,expected)
  by_kind[t]=by_kind.get(t,0)+1
 print('AREA_PASS',ns,by_kind,'C=',C)
print('NUMERIC_RIDGE_MEASURES_PASS')
