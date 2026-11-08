"""Independent coordinate and matrix verification of power-image membership."""
from itertools import product
from collections import Counter

def matpower(N,p,q):
 n=p+3
 R=[[int(i==j) for j in range(n)] for i in range(n)]
 # R=N^0, multiply p times
 for _ in range(p):
  R=[[sum(R[i][k]*N[k][j] for k in range(i,j+1))%q if j>i else 0 for j in range(n)] for i in range(n)]
 return tuple(R[i][j] for i,j in [(0,p),(1,p+1),(2,p+2),(0,p+1),(1,p+2),(0,p+2)])

def getN(p,a,b,c):
 n=p+3;N=[[0]*n for i in range(n)]
 for t,v in enumerate(a):N[t][t+1]=v
 for t,v in enumerate(b):N[t][t+2]=v
 for t,v in enumerate(c):N[t][t+3]=v
 return N

def ismember(x,q):
 A,B,C,D,E,F=x
 return not ((B==0 and A*C!=0) or (B!=0 and A==C==0 and (B*F-D*E)%q!=0))

def construct(p,x,q):
 A,B,C,D,E,F=x
 z=lambda n:[0]*n
 a=z(p+2);b=z(p+1);c=z(p)
 if B:
  for i in range(1,p):a[i]=1
  a[p]=B;a[0]=A;a[p+1]=C*pow(B,-1,q)%q
  b[0]=D*pow(B,-1,q)%q;b[p]=E
  diff=(F-D*E*pow(B,-1,q))%q
  if C:c[0]=diff*pow(C,-1,q)%q
  elif A:c[p-1]=diff*pow(A,-1,q)%q
  else: assert diff==0
 elif A:
  for i in range(p):a[i]=1
  a[0]=A;a[p]=0;a[p+1]=1
  b[p-1]=D*pow(A,-1,q)%q
  b[p]=(E-b[p-1])%q
  c[p-1]=F*pow(A,-1,q)%q
 elif C:
  a[0]=1;a[1]=0
  for i in range(2,p+2):a[i]=1
  a[p+1]=C
  b[1]=E*pow(C,-1,q)%q
  b[0]=(D-b[1])%q
  c[0]=F*pow(C,-1,q)%q
 elif D and E:
  a[0]=D;a[p+1]=E
  for i in range(1,p+1):a[i]=1
  a[2]=0
  b[1]=1
  c[1]=F*pow(D*E,-1,q)%q
 elif D:
  for i in range(2,p+1):a[i]=1
  b[0]=D;b[p]=F*pow(D,-1,q)%q
 elif E:
  for i in range(1,p):a[i]=1
  b[0]=F*pow(E,-1,q)%q;b[p]=E
 else:
  for i in range(2,p):a[i]=1
  b[0]=F;b[p]=1
 return getN(p,a,b,c)

def check():
 for p,q in [(3,3),(5,5)]:
  total=0
  for vals in product(range(q), repeat=6):
   # field integer modulo p, hence q=p here
   x=tuple(vals)
   if ismember(x,q):
    N=construct(p,x,q)
    got=matpower(N,p,q)
    assert x==got,(p,x,got)
    total+=1
  want=q**6-q**5+q**4+q**3-q**2
  assert total==want,(p,total,want)
  print(f'ALL_TARGET_CONSTRUCTIONS_PASS p={p} q={q} images={total}')
 # independent full source enumeration for p=3, q=3: only first three diagonals matter
 p=3;q=3
 cnt=Counter()
 for a in product(range(q),repeat=5):
  for b in product(range(q),repeat=4):
   for c in product(range(q),repeat=3):
    N=getN(p,a,b,c)
    y=matpower(N,p,q)
    cnt[y]+=1
 assert len(cnt)==585,len(cnt)
 assert all(ismember(y,q) for y in cnt)
 print('EXHAUSTIVE_POWER_IMAGE_PASS p=3 q=3 effective_sources=531441 images=585')
 print('ALL_FIRST_WIDTH_TWO_POWER_CHECKS_PASS')
if __name__=='__main__':check()
