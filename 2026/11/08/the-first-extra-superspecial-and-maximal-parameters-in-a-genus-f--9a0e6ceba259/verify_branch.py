"""Finite-field certificate for geometric nonisomorphism of two genus-three quotients.

All branch points lie in F_31^2. Every Mobius map sending one branch
8-set to another is defined over F_31^2, being determined by 3 points.
"""
P=31

def pair(x):return (x%P,x//P)
def rep(a,b):return (a%P)+P*(b%P)
def add(a,b):
 x,y=pair(a);z,w=pair(b);return rep(x+z,y+w)
def neg(a):
 x,y=pair(a);return rep(-x,-y)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 x,y=pair(a);z,w=pair(b);return rep(x*z-y*w,x*w+y*z)
def inv(a):
 x,y=pair(a);d=pow((x*x+y*y)%P,-1,P);return rep(x*d,-y*d)
def div(a,b):return mul(a,inv(b))
def power(a,n):
 out=1
 while n:
  if n&1:out=mul(out,a)
  a=mul(a,a);n>>=1
 return out

def roots(a):
 s={x for x in range(P*P) if power(x,4) in (1,a)}
 assert len(s)==8, (a,len(s))
 return sorted(s)

def unique_map(x,y):
 # Solve 3x4 homogeneous system with 1-dimensional nullspace.
 rows=[[a,1,neg(mul(b,a)),neg(b)] for a,b in zip(x,y)]
 rank=0; pivots=[]
 for col in range(4):
  pick=next((j for j in range(rank,3) if rows[j][col]),None)
  if pick is None:continue
  rows[rank],rows[pick]=rows[pick],rows[rank]
  d=inv(rows[rank][col]);rows[rank]=[mul(u,d) for u in rows[rank]]
  for j in range(3):
   if j!=rank and rows[j][col]:
    v=rows[j][col];rows[j]=[sub(rows[j][k],mul(v,rows[rank][k])) for k in range(4)]
  pivots.append(col);rank+=1
  if rank==3:break
 assert rank==3
 free=next(c for c in range(4) if c not in pivots)
 sol=[0]*4;sol[free]=1
 for i,pivot in enumerate(pivots):sol[pivot]=neg(rows[i][free])
 A,B,C,D=sol
 assert sub(mul(A,D),mul(B,C))!=0
 return sol

def maps(source,target):
 src=roots(source);tgt=roots(target);base=src[:3];found=[]
 for i in range(8):
  for j in range(8):
   if i==j:continue
   for k in range(8):
    if k==i or k==j:continue
    A,B,C,D=unique_map(base,(tgt[i],tgt[j],tgt[k]))
    values=[]
    for x in src:
     den=add(mul(C,x),D)
     if den==0:break # no finite target image
     values.append(div(add(mul(A,x),B),den))
    if len(values)==8 and set(values)==set(tgt):found.append((A,B,C,D))
 return found

if __name__=='__main__':
 a=-1%P;b=14;c=20
 assert mul(14,20)==1
 assert len(maps(a,a))>0
 assert len(maps(b,b))>0
 assert len(maps(a,b))==0
 assert len(maps(b,c))>0
 print('Branch-set Mobius self symmetry orders:',len(maps(a,a)),len(maps(b,b)),len(maps(c,c)))
 print('H_-1 not geometrically isomorphic to H_14: YES')
 print('H_14 geometrically isomorphic to H_20: YES')
 print('HOWE31_BRANCH_CERTIFICATE_PASS')
