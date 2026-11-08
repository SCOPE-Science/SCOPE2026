# Reproducible GF(4) character checks; requires Python 3 standard library only.
# Finite checks are not a proof of the all-field assertion.
import itertools,random
add=lambda a,b:a^b
def mul(a,b):
 a0,a1=a&1,a>>1;b0,b1=b&1,b>>1
 return ((a0*b0)^(a1*b1))|(((a0*b1)^(a1*b0)^(a1*b1))<<1)
def rank(A):
 A=[r.copy() for r in A];m=len(A);r=0
 inv=[0,1,3,2]
 for j in range(m):
  pivot=next((k for k in range(r,m) if A[k][j]),None)
  if pivot is None:continue
  A[pivot],A[r]=A[r],A[pivot]
  k=inv[A[r][j]];A[r]=[mul(k,v) for v in A[r]]
  for i in range(m):
   if i!=r and A[i][j]:
    x=A[i][j];A[i]=[a^mul(x,b) for a,b in zip(A[i],A[r])]
  r+=1
 return r
n=4;h=2;ij=list(itertools.combinations(range(n),2))
O=[[0]*n for _ in range(n)]
for i in range(h):O[i][h+i]=O[h+i][i]=1
allv=list(itertools.product(range(4),repeat=n));S=set()
for u in allv:
 for v in allv:
  form=0
  for i in range(h):form^=mul(u[i],v[h+i])^mul(u[h+i],v[i])
  if form:continue
  w=tuple(mul(u[i],v[j])^mul(u[j],v[i]) for i,j in ij)
  if any(w):S.add(w)
assert len(S)==255
random.seed(439)
for i in range(50):
 b=[random.randrange(4) for _ in ij] if i else [0]*len(ij)
 B=[[0]*n for _ in range(n)]
 for (a,c),v in zip(ij,b):B[a][c]=B[c][a]=v
 direct=0
 for w in S:
  z=0
  for bb,ww in zip(b,w):z^=mul(bb,ww)
  trace=(z>>1) # Tr(z) for this field
  direct+=-1 if trace else 1
 K=sum(4**(n-rank([[B[x][y]^(mul(t,O[x][y])) for y in range(n)] for x in range(n)])) for t in range(4))-4*5
 assert (4**(n-2)*K+1)%15==0
 formula=(4**(n-2)*K+1)//15
 assert direct==formula,(i,direct,formula)
print('GF4_ISOTROPIC_BIVECTOR_PASS support=255 checks=50')
