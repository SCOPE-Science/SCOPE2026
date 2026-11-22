"""Exact finite-field verifier for the Hurwitz quintic flex-tangent arrangement over F5.
Requires Python 3 standard library only. All projective points and lines are constructed in F_(5^12).
"""
from collections import Counter,defaultdict
p=5; d=12; Q=5**12
# t^12+2t^11-t^10+2t^9+t^7-2t^6+t^5-2t^3+t^2-2t+1
co=[1,-2,1,-2,0,1,-2,1,0,2,-1,2]
zero=(0,)*d; one=(1,)+(0,)*(d-1);t=(0,1)+(0,)*(d-2)
def c(n):return (n%p,)+(0,)*(d-1)
def add(a,b):return tuple((x+y)%p for x,y in zip(a,b))
def sub(a,b):return tuple((x-y)%p for x,y in zip(a,b))
def neg(a):return tuple((-x)%p for x in a)
def mul(a,b):
 r=[0]*23
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:r[i+j]+=x*y
 for k in range(22,11,-1):
  z=r[k]%p
  if z:
   for j,v in enumerate(co):r[k-12+j]-=z*v
 return tuple(x%p for x in r[:12])
def pw(a,n):
 r=one
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a); n>>=1
 return r
def inv(a):
 assert a!=zero
 return pw(a,Q-2)
def eq(a,b):return a==b
def cross(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
def proj(a):
 for x in a:
  if x!=zero:
   y=inv(x)
   return tuple(mul(y,z) for z in a)
 raise ValueError('zero vector')
def grad(P):
 x,y,z=P
 return (add(pw(y,4),mul(c(4),mul(pw(x,3),z))), add(mul(c(4),mul(x,pw(y,3))),pw(z,4)), add(mul(c(4),mul(y,pw(z,3))),pw(x,4)))
def eval_line(L,P):return add(add(mul(L[0],P[0]),mul(L[1],P[1])),mul(L[2],P[2]))
# Rabin irreducibility test for the degree-twelve polynomial defining the field.
def trim(a):
 a=[int(x)%5 for x in a]
 while a and a[-1]==0:a.pop()
 return a
def rem(a,b):
 a=trim(a);b=trim(b)
 assert b
 while len(a)>=len(b):
  v=a[-1]*pow(b[-1],-1,5)%5; shift=len(a)-len(b)
  for i,x in enumerate(b):a[i+shift]=(a[i+shift]-v*x)%5
  a=trim(a)
 return a
def pgcd(a,b):
 a,b=trim(a),trim(b)
 while b:a,b=b,rem(a,b)
 if not a:return a
 c=pow(a[-1],-1,5)
 return [(x*c)%5 for x in a]
F=[x%5 for x in co]+[1]
h=t
for k in range(1,13):
 h=pw(h,5)
 if k in (4,6):assert pgcd(F,sub(h,t))==[1]
 if k==12:assert h==t
assert pw(t,Q)==t
assert add(add(pw(t,39),mul(c(2),pw(t,13))),neg(one))==zero
s=pw(t,13); lam=add(c(4),add(mul(c(4),s),mul(c(2),mul(s,s))))
assert add(add(pw(lam,3),pw(lam,2)),sub(neg(mul(c(2),lam)),one))==zero
assert add(add(mul(pw(lam,4),s),lam),one)==zero
zeta=zero
for i in range(1,10):
 e=add(t,c(i)); zz=pw(e,(Q-1)//13)
 if zz!=one:
  zeta=zz;break
assert zeta!=zero and pw(zeta,13)==one and zeta!=one

pts=[]
for k in range(13):
 x=mul(t,pw(zeta,(-3*k)%13));y=mul(mul(lam,pw(t,4)),pw(zeta,k))
 pts.extend([proj((x,y,one)), proj((y,one,x)), proj((one,x,y))])
pts.extend([proj((one,zero,zero)),proj((zero,one,zero)),proj((zero,zero,one))])
assert len(pts)==42 and len(set(pts))==42
for P in pts:
 x,y,z=P
 assert add(add(mul(x,pw(y,4)),mul(y,pw(z,4))),mul(pw(x,4),z))==zero
L=[proj(grad(P)) for P in pts]
assert len(set(L))==42
for ell,P in zip(L,pts):assert eval_line(ell,P)==zero

# group all pair intersections
mult=defaultdict(list)
for i in range(42):
 for j in range(i+1,42):
  pp=proj(cross(L[i],L[j]));mult[pp].append((i,j))
profile=Counter()
for point,pairs in mult.items():
 n=len(set(v for pair in pairs for v in pair))
 assert n*(n-1)//2==len(pairs)
 profile[n]+=1
assert profile=={2:861}
assert sum(v for k,v in profile.items() if k>=3)==0
# Second, independent determinant test of all 11,480 triples.
checks=0
for i in range(42):
 for j in range(i+1,42):
  ij=cross(L[i],L[j])
  for k in range(j+1,42):
   checks+=1
   assert eval_line(L[k],ij)!=zero
assert checks==11480
# incidence of flex points on other flex tangents
on=Counter(); onpoints=Counter()
for i,P in enumerate(pts):
 meeting=[j for j,ell in enumerate(L) if eval_line(ell,P)==zero]
 on[len(meeting)]+=1

assert on=={1:39,2:3}
# Frobenius orbit lengths on concurrency loci and tangent lines
for label,S in [('intersections',set(mult)),('lines',set(L))]:
 seen=set();orb=Counter()
 for a in S:
  if a in seen:continue
  b=a; l=0
  while b not in seen:
   seen.add(b);l+=1
   b=proj(tuple(pw(e,5) for e in b))
  assert b==a
  orb[l]+=1

 if label=='intersections':assert orb=={1:3,3:4,6:3,12:69}
 else:assert orb=={1:3,3:1,12:3}

print("HURWITZ_F5_FLEX_ARRANGEMENT_VERIFIED lines=42 double_points=861 triple_points=0 triples_tested=11480 frobenius=1^3,3^4,6^3,12^69")
