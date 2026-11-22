"""An explicit vertex isomorphism between affine-incidence and LCF Pappus models.
Run: python3 verify_isomorphism.py
"""
points=[(x,y) for x in range(3) for y in range(3)]
lines=[(family,c) for family in range(3) for c in range(3)]
incidence=set()
for i,(x,y) in enumerate(points):
 for j,(family,c) in enumerate(lines):
  value=x if family==0 else y if family==1 else (y-x)%3
  if value==c:incidence.add(tuple(sorted((i,9+j))))
assert len(incidence)==27
lcf=set(tuple(sorted((i,(i+1)%18))) for i in range(18))
shifts=[5,7,-7,7,-7,-5]*3
for i in range(18):lcf.add(tuple(sorted((i,(i+shifts[i])%18))))
assert len(lcf)==27
mapping=(0,2,8,16,4,14,12,10,6,1,15,11,17,3,7,5,13,9)
assert len(set(mapping))==18
image={tuple(sorted((mapping[u],mapping[v]))) for u,v in incidence}
assert image==lcf
print('Explicit Pappus affine-incidence to LCF isomorphism verified on all 27 edges')
print('Affine vertex 0..17 maps to LCF vertices:',','.join(map(str,mapping)))
