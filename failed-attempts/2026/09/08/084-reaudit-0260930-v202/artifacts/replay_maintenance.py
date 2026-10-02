"""Independent GF(2) orbit, endomorphism and idempotent census."""
import itertools,json,time
from collections import Counter
from pathlib import Path
def multiply(x,y,r,s,t):
 return sum((sum(((x>>(i*s+k))&1)*((y>>(k*t+j))&1) for k in range(s))%2)<<(i*t+j) for i in range(r) for j in range(t))
def identity(n):return sum(1<<(i*n+i) for i in range(n))
def rank(rows,n):
 rows=list(rows);p=0
 for col in range(n):
  j=next((j for j in range(p,len(rows)) if rows[j]>>col&1),None)
  if j is None:continue
  rows[p],rows[j]=rows[j],rows[p]
  for j in range(len(rows)):
   if j!=p and rows[j]>>col&1:rows[j]^=rows[p]
  p+=1
 return p,rows[:p]
def gl(n):return [x for x in range(1<<(n*n)) if rank([(x>>(i*n))&((1<<n)-1) for i in range(n)],n)[0]==n]
def invert(x,n,G):return next(y for y in G if multiply(x,y,n,n,n)==identity(n))
def endos(mats,a,b):
 n=a*a+b*b;eq=[]
 for A in mats:
  for i in range(b):
   for j in range(a):
    row=0
    for k in range(b):
     if A>>(k*a+j)&1:row^=1<<(a*a+i*b+k)
    for k in range(a):
     if A>>(i*a+k)&1:row^=1<<(k*a+j)
    eq.append(row)
 r,eq=rank(eq,n);piv=[next(i for i in range(n) if row>>i&1) for row in eq]
 free=[i for i in range(n) if i not in piv];basis=[]
 for i in free:
  v=1<<i
  for col,row in zip(piv,eq):
   if row>>i&1:v|=1<<col
  basis.append(v)
 E=[0]
 for v in basis:E += [w^v for w in E]
 return E,n-r
out={};start=time.monotonic()
for a,b in [(2,2),(2,3)]:
 width=a*b;mask=(1<<width)-1;N=1<<(3*width);seen=bytearray(N);GA=gl(a);GB=gl(b);GI=[invert(x,a,GA) for x in GA]
 actions=[[multiply(multiply(h,A,b,b,a),g,b,a,a) for A in range(1<<width)] for h in GB for g in GI]
 orbit_sizes=Counter();dimensions=Counter();nind=nabs=bricks=locals2=field2=classes=mass=0
 for rep in range(N):
  if seen[rep]:continue
  mats=[(rep>>(k*width))&mask for k in range(3)]
  orbit={T[mats[0]]+(T[mats[1]]<<width)+(T[mats[2]]<<(2*width)) for T in actions}
  assert not any(seen[z] for z in orbit)
  for z in orbit:seen[z]=1
  classes+=1;mass+=len(orbit);orbit_sizes[len(orbit)]+=1
  E,d=endos(mats,a,b);dimensions[d]+=1;whole=identity(a)|(identity(b)<<(a*a));split=False
  for e in E:
   if e in (0,whole):continue
   X=e&((1<<(a*a))-1);Y=e>>(a*a)
   if multiply(X,X,a,a,a)==X and multiply(Y,Y,b,b,b)==Y:split=True;break
  if split:continue
  nind+=1
  if d==1:nabs+=1;bricks+=1
  else:
   assert d==2
   field=all(rank([(e>>(i*a))&((1<<a)-1) for i in range(a)],a)[0]==a and rank([((e>>(a*a))>>(i*b))&((1<<b)-1) for i in range(b)],b)[0]==b for e in E if e)
   if field:field2+=1
   else:nabs+=1;locals2+=1
 assert mass==N and all(seen)
 expected=(148,98,91,70,21,7) if b==2 else (402,204,204,183,21,0)
 assert (classes,nind,nabs,bricks,locals2,field2)==expected
 out[str((a,b))]={'representations':N,'classes':classes,'indecomposable':nind,'absolutely_indecomposable':nabs,'bricks':bricks,'local_end2':locals2,'field_end2':field2,'orbit_sizes':dict(orbit_sizes),'endomorphism_dimensions':dict(dimensions)}
out['elapsed_seconds']=time.monotonic()-start
print(json.dumps(out,indent=2));print('COMPLETE_KAC_ORBIT_REPLAY_OK')
