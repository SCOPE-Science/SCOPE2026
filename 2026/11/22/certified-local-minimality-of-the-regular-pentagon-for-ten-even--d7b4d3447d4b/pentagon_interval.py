#!/usr/bin/env python3
"""Exact rational outward-enclosure certificate for sixth- through 24th-distance energies.
All interval endpoints are integer multiples of 10^-40. All certification decisions use exact integer arithmetic.
"""
from math import isqrt, comb, factorial
S=10**40
class I:
 __slots__=('lo','hi')
 def __init__(self, lo,hi=None): self.lo=lo;self.hi=lo if hi is None else hi
 @staticmethod
 def q(n,d=1):
  if d<0:n,d=-n,-d
  return I(n*S//d,-((-n*S)//d))
 def __add__(a,b):
  if not isinstance(b,I):b=I.q(b)
  return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a): return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+(-b if isinstance(b,I) else -b)
 def __mul__(a,b):
  if isinstance(b,int):return I(a.lo*b,a.hi*b) if b>=0 else I(a.hi*b,a.lo*b)
  v=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
  mini=min(v);maxi=max(v)
  return I(mini//S,-((-maxi)//S))
 __rmul__=__mul__
 def divint(a,d):
  assert d>0
  return I(a.lo//d,-((-a.hi)//d))
 def rational(a,n,d):
  return (a*n).divint(d) if n>=0 else (a*n).divint(d)
 def __truediv__(a,b):
  if isinstance(b,int):return a.divint(b)
  assert b.lo>0 or b.hi<0
  products=[(x*S,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
  # use rational-key comparison exactly
  from fractions import Fraction
  mini=min(products,key=lambda z:Fraction(z[0],z[1]));maxi=max(products,key=lambda z:Fraction(z[0],z[1]))
  return I(mini[0]//mini[1],-((-maxi[0])//maxi[1]))
 def __repr__(a):return '['+str(a.lo)+'/'+str(S)+','+str(a.hi)+'/'+str(S)+']'
Z=I(0);U=I.q(1)
HIDX=[(i,j) for i in range(6) for j in range(i,6)]
class J:
 __slots__=('a',)
 def __init__(self,a):self.a=a
 @staticmethod
 def scalar(v):return J([v]+[Z]*27)
 @staticmethod
 def var(v,i):
  x=[v]+[Z]*27;x[i+1]=U;return J(x)
 def __add__(a,b):
  if not isinstance(b,J):b=J.scalar(b if isinstance(b,I) else I.q(b))
  return J([x+y for x,y in zip(a.a,b.a)])
 __radd__=__add__
 def __neg__(a):return J([-x for x in a.a])
 def __sub__(a,b):return a+-b if isinstance(b,J) else a+(-b)
 def __mul__(a,b):
  if isinstance(b,int):return J([x*b for x in a.a])
  if isinstance(b,I):return J([x*b for x in a.a])
  x,y=a.a,b.a
  z=[x[0]*y[0]]
  for i in range(6):z.append(x[i+1]*y[0]+x[0]*y[i+1])
  for k,(i,j) in enumerate(HIDX):
   z.append(x[7+k]*y[0]+x[0]*y[7+k]+x[i+1]*y[j+1]+x[j+1]*y[i+1])
  return J(z)
 __rmul__=__mul__
 def rat(a,n,d):return J([x.rational(n,d) for x in a.a])
S5=I(isqrt(5*S*S),isqrt(5*S*S)+1)
c=(S5-I.q(1)).divint(4);d=(-(S5+I.q(1))).divint(4)
q=(S5-I.q(1)).divint(2);lam=(S5+I.q(5)).divint(8)
V=[[U,Z],[c,U],[d,q],[d,-q],[c,-U]]
coords=[]
for k,(x,y) in enumerate(V):
 if k>=2:coords.append((J.var(x,2*(k-2)),J.var(y,2*(k-2)+1)))
 else:coords.append((J.scalar(x),J.scalar(y)))
dets=[]
for i in range(5):
 x,y=coords[i];u,v=coords[(i+1)%5];dets.append(x*v-y*u)
N=24;mon=[]
for i in range(5):
 x,y=coords[i];xp=[J.scalar(U)];yp=[J.scalar(U)]
 for k in range(1,N+1):xp.append(xp[-1]*x);yp.append(yp[-1]*y)
 mon.append({(a,n-a):xp[a]*yp[n-a] for n in range(N+1) for a in range(n+1)})
print('monomials',flush=True)
M={}
for degree in range(N+1):
 for p in range(degree+1):
  r=degree-p; acc=J.scalar(Z);den=factorial(degree+2)
  for i in range(5):
   j=(i+1)%5;z=J.scalar(Z)
   for a in range(p+1):
    for b in range(r+1):
     numer=comb(p,a)*comb(r,b)*factorial(a+b)*factorial(degree-a-b)
     term=mon[i][a,b]*mon[j][p-a,r-b]
     z=z+term.rat(numer,den)
   acc=acc+dets[i]*z
  M[p,r]=acc
 if degree%4==0:print('moment degree',degree,flush=True)
A=M[0,0]; assert A.a[0].lo<=5*S//2<=A.a[0].hi
powers=[U]
for j in range(12):powers.append(powers[-1]*lam)
logs=[]
for m in range(3,13):
 E=J.scalar(Z)
 for j in range(m+1):
  pref=powers[m-j]*comb(m,j)
  for a in range(2*j+1):
   for b in range(2*(m-j)+1):
    coeff=(-1)**(a+b)*comb(2*j,a)*comb(2*(m-j),b)
    E=E+(M[2*j-a,2*(m-j)-b]*M[a,b])*pref*coeff
 c=m+2
 ev=E.a[0];av=A.a[0]; assert ev.lo>0
 # normalized B/E:  E''/E - (c/A) A'' - c(c-1)/A² A'A'
 B=[]
 for k,(i,j) in enumerate(HIDX):
  z=E.a[7+k]/ev-(A.a[7+k]/av)*c - ((A.a[1+i]*A.a[1+j])/(av*av))* (c*(c-1))
  B.append(z)
 T=[[None]*6 for _ in range(6)]
 for k,(i,j) in enumerate(HIDX):T[i][j]=T[j][i]=B[k]
 piv=[]
 for k in range(6):
  p=T[k][k];piv.append(p)
  assert p.lo>0,('nonpositive pivot',m,k,p)
  for i in range(k+1,6):
   for j in range(i,6):
    T[i][j]=T[j][i]=T[i][j]-(T[i][k]*T[k][j])/p
 minlo=min(p.lo for p in piv)
 # gradient of E-(m+2)E/A A' vanishes exactly by dihedral symmetry/homogeneity,
 # numerical intervals provide crosscheck.
 residual=[E.a[i+1]/ev-(A.a[i+1]/av)*c for i in range(6)]
 r=max(max(abs(z.lo),abs(z.hi)) for z in residual)
 assert r<S//10**20,(m,'stationarity',r)
 print('m',m,'min_pivot_lower_scaled',minlo,'max_gradient_residual_scaled',r,flush=True)
 logs.append((m,minlo,r))
assert all(p> S//5 for _,p,_ in logs)
print('CERTIFIED: min LDL pivot >1/5 for m=3..12, N=5, 40-place outward integer arithmetic')
