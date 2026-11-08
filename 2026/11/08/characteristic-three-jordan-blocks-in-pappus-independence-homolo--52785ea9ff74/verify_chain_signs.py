# Independent direct check that signed vertex permutation commutes with simplicial boundary.
from itertools import combinations
n=18;lcf=(5,7,-7,7,-7,-5)*3
ed={tuple(sorted((i,(i+1)%18))) for i in range(18)}|{tuple(sorted((i,(i+s)%18))) for i,s in enumerate(lcf)}
for k in (4,5,6):
 faces=[x for x in combinations(range(n),k) if not any(a in x and b in x for a,b in ed)]
 def transform_simplex(x,shift):
  img=[(v+shift)%18 for v in x]
  inv=sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
  return tuple(sorted(img)),(-1)**inv
 for shift in (6,12):
  for x in faces:
   sx,sgn=transform_simplex(x,shift)
   a={}
   for j in range(k):
    tx,tgn=transform_simplex(x[:j]+x[j+1:],shift)
    a[tx]=a.get(tx,0)+((-1)**j)*tgn
   b={sx[:j]+sx[j+1:]:sgn*((-1)**j) for j in range(k)}
   assert a==b,(k,shift,x)
 print('equivariant boundary check degree',k-1,'faces',len(faces))
print('PAPPUS_SIGNED_CHAIN_EQUIVARIANCE_PASS')
