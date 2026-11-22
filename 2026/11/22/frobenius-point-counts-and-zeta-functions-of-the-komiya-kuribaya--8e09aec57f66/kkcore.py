from collections import Counter,defaultdict
from itertools import combinations
from sympy import factorint
Z=(0,0,0,0);E=(1,0,0,0);I=(0,1,0,0);R=(0,0,1,0);IR=(0,0,0,1)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def scale(a,n):return tuple(n*x for x in a)
def mul(a,b):
 A,B,C,D=a;W,X,Y,V=b
 return (A*W-B*X+5*C*Y-5*D*V,A*X+B*W+5*C*V+5*D*Y,A*Y-B*V+C*W-D*X,A*V+B*Y+C*X+D*W)
def norm(a):
 A,B,C,D=a; e=A*A-B*B-5*(C*C-D*D);f=2*(A*B-5*C*D)
 return e*e+f*f
def det(a,b,c):
 return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))
alpha=add(R,scale(IR,2));beta=sub(scale(IR,2),R)
def line(x=Z,y=Z,z=Z):return (x,y,z)
L=[line(y=neg(alpha),z=scale(E,5)),line(y=neg(beta),z=scale(E,5)),line(y=beta,z=scale(E,5)),line(y=alpha,z=scale(E,5)),
   line(x=neg(E),y=neg(E),z=E),line(x=neg(E),y=E,z=E),line(x=neg(E),y=scale(I,-2),z=E),line(x=neg(E),y=scale(I,2),z=E),line(x=E,y=neg(E),z=E),line(x=E,y=E,z=E),line(x=E,y=scale(I,-2),z=E),line(x=E,y=scale(I,2),z=E),
   line(x=scale(I,-2),y=neg(E),z=E),line(x=scale(I,-2),y=E,z=E),line(x=neg(I),y=neg(I),z=scale(E,2)),line(x=neg(I),y=I,z=scale(E,2)),line(x=I,y=neg(I),z=scale(E,2)),line(x=I,y=I,z=scale(E,2)),line(x=scale(I,2),y=neg(E),z=E),line(x=scale(I,2),y=E,z=E),
   line(x=neg(alpha),z=scale(E,5)),line(x=neg(beta),z=scale(E,5)),line(x=beta,z=scale(E,5)),line(x=alpha,z=scale(E,5)),
   line(x=neg(alpha),y=scale(E,5)),line(x=neg(beta),y=scale(E,5)),line(x=beta,y=scale(E,5)),line(x=alpha,y=scale(E,5))]
assert len(L)==28
norms=Counter();D={};
for i,j,k in combinations(range(28),3):
 d=det(L[i],L[j],L[k]);D[i,j,k]=d
 if d!=Z:
  for p in factorint(norm(d)):norms[p]+=1
print('norm primes',norms)
ps=[]
for i,j in combinations(range(28),2):
 ss=frozenset(k for k in range(28) if k in (i,j) or D[tuple(sorted((i,j,k)))]==Z)
 ps.append(ss)
base=set(ps)
print('charzero',len(base),Counter(map(len,base)),'pairs',sum(len(z)*(len(z)-1)//2 for z in base))
for p in sorted(norms):
 if p in (2,3,5):continue
 # compute in K tensor mod p: at bad primes may need choose prime embedding; count how many determinants reduce to zero in at least one prime
 nz=[(i,j,k,d) for (i,j,k),d in D.items() if d!=Z and norm(d)%p==0]
 print(p,'candidate new triple',len(nz),'e.g.',[(i+1,j+1,k+1) for i,j,k,d in nz[:8]])

def modfield(p):
 def leg(n):return pow(n%p,(p-1)//2,p)
 def sqroot(n):
  n%=p
  for u in range(p):
   if u*u%p==n:return u
  return None
 ir=sqroot(-1);rr=sqroot(5)
 if ir is None:
  d=-1%p;Ival=(0,1)
  if rr is None:
   c=sqroot(-5)
   assert c is not None
   Rval=(0,c)
  else:Rval=(rr,0)
 else:
  Ival=(ir,0)
  if rr is None:
   d=5;Rval=(0,1)
  else:d=1;Rval=(rr,0)
 def mm(a,b):return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
 def aa(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
 def nn(a):return ((-a[0])%p,(-a[1])%p)
 iv=Ival;rv=Rval;irv=mm(iv,rv)
 def cv(x):return ((x[0]+x[1]*iv[0]+x[2]*rv[0]+x[3]*irv[0])%p,(x[1]*iv[1]+x[2]*rv[1]+x[3]*irv[1])%p)
 V=[tuple(cv(v) for v in l) for l in L]
 zz=(0,0)
 def dd(a,b,c):
  return aa(aa(mm(a[0],aa(mm(b[1],c[2]),nn(mm(b[2],c[1])))),nn(mm(a[1],aa(mm(b[0],c[2]),nn(mm(b[2],c[0])))))),mm(a[2],aa(mm(b[0],c[1]),nn(mm(b[1],c[0])))))
 P=set()
 for i,j in combinations(range(28),2):
  ss=frozenset(k for k in range(28) if k in (i,j) or dd(V[i],V[j],V[k])==zz)
  P.add(ss)
 counts=Counter(map(len,P)); print('p',p,'ir/r/d',ir,rr,d,'incidence',len(P),sorted(counts.items()),'check',sum(k*(k-1)//2*v for k,v in counts.items()),'max',max(counts))
 print('   profiles',Counter((len(S),sum(i<12 for i in S)) for S in P))
 return P
if __name__=='__main__':
 for p in [7,11,13,17,19,29,41,61,101,109,127]:modfield(p)
