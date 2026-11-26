"""Exact exhaustive projective orbit verification for smooth F3 quartics with a fixed six-point blocking set."""
from itertools import product,combinations
from collections import Counter
P=sorted({tuple(t*pow(next(x for x in v if x),-1,3)%3 for t in v) for v in product(range(3),repeat=3) if any(v)})
assert len(P)==13
idx={p:i for i,p in enumerate(P)}
MASK=311
L=[sum(1<<i for i,p in enumerate(P) if sum(a[j]*p[j] for j in range(3))%3==0) for a in P]
B6=[sum(1<<j for j in inds) for inds in combinations(range(13),6) if all(sum(1<<j for j in inds)&li for li in L) and all((sum(1<<j for j in inds)&li)!=li for li in L)]
assert len(B6)==234 and MASK in B6
M4=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
polys=[''.join(map(str,x.strip())) for x in open('verification/smooth_coefficients.txt')]
assert len(polys)==444
normalized={tuple(int(z)* (1 if next(x for x in poly if int(x))=='1' else 2)%3 for z in poly) for poly in polys}
assert len(normalized)==222
# Complete PGL3(F3) group (projective matrix normalized by first nonzero entry).
matrices=[];stabilizers=[];masks=set()
for v in product(range(3),repeat=9):
 if not any(v):continue
 if next(x for x in v if x)!=1:continue
 a,b,c,d,e,f,g,h,i=v
 det=(a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3
 if not det:continue
 perm=[]
 for p in P:
  w=(sum(v[3*r+j]*p[j] for j in range(3))%3 for r in range(3))
  w=tuple(w)
  scale=pow(next(z for z in w if z),-1,3)
  perm.append(idx[tuple(z*scale%3 for z in w)])
 newmask=sum(1<<perm[j] for j in range(13) if MASK>>j&1)
 masks.add(newmask);matrices.append(v)
 if newmask==MASK:stabilizers.append(v)
assert len(matrices)==5616 and len(stabilizers)==24 and masks==set(B6)
# polynomial transformation c' = matrix(c) representing F(MX)
def mul(A,B):
 C={}
 for x,u in A.items():
  for y,v in B.items():
   k=tuple(x[t]+y[t] for t in range(3));C[k]=(C.get(k,0)+u*v)%3
 return {k:v for k,v in C.items() if v}
def transform(v,c):
 forms=[{tuple(int(t==j) for t in range(3)):v[3*r+j] for j in range(3) if v[3*r+j]} for r in range(3)]
 d={}
 for coeff,e in zip(c,M4):
  if not coeff:continue
  s={(0,0,0):coeff}
  for r in range(3):
   for _ in range(e[r]):s=mul(s,forms[r])
  for k,a in s.items():d[k]=(d.get(k,0)+a)%3
 out=tuple(d.get(e,0) for e in M4)
 scale=pow(next(x for x in out if x),-1,3)
 return tuple(x*scale%3 for x in out)
# Check all transformations preserve the candidate set
orb={};reps=[];unseen=set(normalized)
while unseen:
 rep=min(unseen)
 orbit={transform(v,rep) for v in stabilizers}
 assert orbit<=normalized
 assert len(orbit) in [1,2,3,4,6,8,12,24]
 unseen.difference_update(orbit)
 reps.append((rep,len(orbit)))
print('PGL=',len(matrices),'six-blocking masks=',len(B6),'single orbit=',len(masks)==len(B6),'stabilizer=',len(stabilizers))
print('Smooth coefficient vectors per mask=',len(polys),'normalized equations=',len(normalized))
print('Total smooth equations=',len(normalized)*len(B6),'PGL orbits=',len(reps),'sizes distribution=',dict(sorted(Counter(n for _,n in reps).items())))
print('Aut orders distribution=',dict(sorted(Counter(24//n for _,n in reps).items())))
with open('verification/orbit_representatives.txt','w') as f:
 f.write('# quartic coeffs in lexicographic monomial order; orbit sizes under the stabilizer of the fixed rational six-set\n')
 for r,n in reps:f.write(''.join(map(str,r))+' '+str(n)+'\n')
print('representatives', [''.join(map(str,r)) for r,n in reps])
