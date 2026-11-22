#!/usr/bin/env python3
"""Exact four-coordinate complementary chainlink section facet-census sanity check.
No nonstandard dependencies.  This is a finite check, not a substitute for the theorem."""
from fractions import Fraction as Q
from itertools import combinations
from math import isqrt

def det(M):
 n=len(M)
 if n==1:return M[0][0]
 if n==2:return M[0][0]*M[1][1]-M[0][1]*M[1][0]
 return sum((-1)**j*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(n))

def solve(M,b):
 d=det(M)
 if not d: return None
 return tuple(Q(det([row[:j]+[b[i]]+row[j+1:] for i,row in enumerate(M)]),d) for j in range(len(M)))

def face_data(a,l,t):
 n=len(a);m=n-1
 # x_0,...,x_{m-1} free; x_m=t-sum(free)
 off=[0]*m+[t]
 emb=[[int(i==j)-(int(i==m)) for j in range(m)] for i in range(n)]
 unit=[[int(i==j) for j in range(n)] for i in range(n)]
 raw=[]
 for i in range(n):
  raw += [('box',[-v for v in unit[i]],0),('box',unit[i],a[i])]
 for i in range(n):
  raw += [('link',[unit[i][k]-unit[(i+1)%n][k] for k in range(n)],a[i]-l)]
 hs=[]
 for kind,norm,c in raw:
  row=[sum(norm[k]*emb[k][j] for k in range(n)) for j in range(m)]
  hs.append((kind,norm,row,c-sum(norm[k]*off[k] for k in range(n))))
 points=set()
 for ids in combinations(range(len(hs)),m):
  mat=[hs[i][2] for i in ids]
  sol=solve(mat,[hs[i][3] for i in ids]);
  if sol is None:continue
  if all(sum(v*x for v,x in zip(row,sol))<=b for _,_,row,b in hs):
   points.add(tuple([*sol, t-sum(sol)]))
 pts=sorted(points)
 totals={'box':Q(0),'link':Q(0)}
 faces=[]
 for idx,(kind,norm,row,c) in enumerate(hs):
  vertices=[p for p in pts if sum(norm[i]*p[i] for i in range(n))==c+sum(norm[i]*off[i] for i in range(n))]
  if len(vertices)<3: continue
  # tangent basis with integer normal constraints sum(v)=0,norm dot v=0
  piv=None
  for i,j in combinations(range(n),2):
   mat=[[1,1],[norm[i],norm[j]]]
   if det(mat):piv=(i,j,mat);break
  i,j,mat=piv
  free=[k for k in range(n) if k not in (i,j)]
  Bs=[]
  for f in free:
   v=[Q(0)]*n;v[f]=1
   vals=solve(mat,[-1,-norm[f]])
   v[i],v[j]=vals
   Bs.append(v)
  gram=[[sum(x*y for x,y in zip(Bs[r],Bs[s])) for s in range(2)] for r in range(2)]
  g=det(gram)
  Csq=(n-1 if kind=='box' else 2*n)
  rat=g/Csq
  # sqrt(rat) exact
  scale=Q(isqrt(rat.numerator),isqrt(rat.denominator))
  assert scale**2==rat,(rat,kind)
  origin=vertices[0]
  xy=[]
  bi,bj=next((u,v) for u,v in combinations(range(n),2) if det([[Bs[0][u],Bs[1][u]],[Bs[0][v],Bs[1][v]]]))
  bmat=[[Bs[0][bi],Bs[1][bi]],[Bs[0][bj],Bs[1][bj]]]
  for p in vertices:
   diff=[p[k]-origin[k] for k in range(n)]
   xy.append(solve(bmat,[diff[bi],diff[bj]]))
  xy=sorted(set(xy))
  def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
  lower=[]
  for p in xy:
   while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
   lower.append(p)
  upper=[]
  for p in reversed(xy):
   while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
   upper.append(p)
  hull=lower[:-1]+upper[:-1]
  ar=abs(sum(hull[k][0]*hull[(k+1)%len(hull)][1]-hull[k][1]*hull[(k+1)%len(hull)][0] for k in range(len(hull))))/2
  if ar:
   normal_area=ar*scale
   totals[kind]+=normal_area
   faces.append((idx,kind,normal_area))
 return pts,totals,faces

if __name__=='__main__':
 tests=[((4,5,6,7),2,9),((4,4,5,6),2,8),((4,5,6,7),1,9),((5,6,7,8),2,12),((6,4,5,7),2,9),((4,5,7,9),2,11)]
 for a,l,t in tests:
  v,q,f=face_data(a,l,t);w,r,g=face_data(a,l,sum(a)-t)
  print(a,l,t,'vertices',len(v),len(w),'area/√3 box',q['box'],r['box'],'area/√8 link',q['link'],r['link'])
  assert q==r,(a,l,t,q,r)
 assert len(face_data((4,5,6,7),2,9)[0])==16
 assert len(face_data((4,5,6,7),2,13)[0])==15
 print('CHAINLINK_FACET_CLASS_EXACT_PASS cases=6')
