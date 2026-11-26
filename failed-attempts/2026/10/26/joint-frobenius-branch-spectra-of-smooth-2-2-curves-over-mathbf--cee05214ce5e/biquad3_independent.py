# Independent full-form smoothness and branch-splitting census for scalar-normalized (2,2)-forms over F3.
# Arithmetic uses only integer vectors mod 3, Euclidean gcd, and monic finite-field factoring by divisibility.
from collections import Counter
from itertools import product
from pathlib import Path
import json
P=3; ex2=[(2,0),(1,1),(0,2)]

def trim(a):
 while len(a)>1 and a[-1]%3==0:a.pop()
 return a

def mul(a,b):
 r=[0]*(len(a)+len(b)-1)
 for i,ai in enumerate(a):
  for j,bj in enumerate(b):r[i+j]=(r[i+j]+ai*bj)%3
 return trim(r)
def sub(a,b):
 l=max(len(a),len(b));return trim([((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%3 for i in range(l)])
def divrem(a,b):
 a=trim(list(a));b=trim(list(b));assert b!=[0]
 q=[0]*max(1,len(a)-len(b)+1)
 while a!=[0] and len(a)>=len(b):
  k=len(a)-len(b);coef=(a[-1]*pow(b[-1],-1,3))%3;q[k]=coef
  for i in range(len(b)):a[k+i]=(a[k+i]-coef*b[i])%3
  trim(a)
 return trim(q),a
def gcd(a,b):
 while b!=[0]:a,b=b,divrem(a,b)[1]
 return a

def derivative(a):return trim([(i*a[i])%3 for i in range(1,len(a))] or [0])
def smoothquart(d):
 d=trim(d)
 return len(d)>=4 and gcd(d,derivative(d))!=[0] and len(gcd(d,derivative(d)))==1

def disc(ds,dir):
 if dir==0:
  A=ds[0:3];B=ds[3:6];C=ds[6:9]
 else:
  A=ds[0:9:3];B=ds[1:9:3];C=ds[2:9:3]
 return sub(mul(B,B),mul(A,C))
# Factor monic poly deg up to4 by testing monic irreducibles degrees1..4, simpler exact all monic candidates.
def split(d):
 d=trim(list(d));dd=[1]*(5-len(d))
 for k in range(1,5):
  for c in product(range(3),repeat=k):
   f=list(c)+[1]
   if any(divrem(f,g)[1]==[0] for j in range(1,k//2+1) for c2 in product(range(3),repeat=j) for g in [list(c2)+[1]]):continue
   while len(d)>1 and divrem(d,f)[1]==[0]:
    d=divrem(d,f)[0];dd.append(k)
 assert len(d)==1 and d[0]!=0,(dd,d)
 return tuple(sorted(dd))

def calcN(ds):
 dirs=((1,0),(0,1),(1,1),(1,2));ans=0
 for (u,v),(r,t) in product(dirs,dirs):
  xx=[u*u%3,u*v%3,v*v%3];yy=[r*r%3,r*t%3,t*t%3]
  ans+=sum(ds[3*i+j]*xx[i]*yy[j] for i in range(3) for j in range(3))%3==0
 return ans
counts=Counter();points=Counter();smooth=0;witness=[]
for num in range(1,3**9):
 ds=[];i=num
 for _ in range(9):ds.append(i%3);i//=3
 i=next(j for j,c in enumerate(ds) if c)
 if ds[i]!=1:continue
 Dx=disc(ds,0);Dy=disc(ds,1)
 if not smoothquart(Dx):continue
 if not smoothquart(Dy):continue
 smooth+=1
 bp=tuple(sorted([split(Dx),split(Dy)]));counts[bp]+=1;points[calcN(ds)]+=1
 if len(witness)<10:witness.append((num,bp))
print('SMOOTH',smooth)
print('BRANCH_COUNTS',sorted((str(k),v) for k,v in counts.items()))
print('POINT_COUNTS',sorted(points.items()))
print('WITNESS',witness)
Path(str(Path(__file__).resolve().parent / 'biquad3_independent.json')).write_text(json.dumps({'smooth':smooth,'branch_counts':{str(k):v for k,v in counts.items()},'point_counts':dict(points),'witness':[(n,str(b)) for n,b in witness]},indent=2))
