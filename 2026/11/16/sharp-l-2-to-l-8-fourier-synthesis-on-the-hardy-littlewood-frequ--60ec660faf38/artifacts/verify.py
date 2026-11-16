import sympy as sp
from collections import defaultdict
from math import comb
from time import monotonic
x,y=sp.symbols('x y', real=True)
a,b,c=sp.symbols('a b c')
p={0:a,1:b,3:c}
q={0:1}
for _ in range(4):
 d=defaultdict(lambda:0)
 for j,z in q.items():
  for k,v in p.items():d[j+k]+=z*v
 q=d
F=sp.expand(sum(z*z for z in q.values()))
S=a*a+b*b+c*c
# H =5F-46S^4; H<0 outside region, lower bound=46/5
H=sp.Poly(sp.expand((5*F-46*S**4).subs({a:x,b:y,c:1-x-y}, simultaneous=True)),x,y)
coeff=[(tuple(map(int,ij)),int(v)) for ij,v in H.terms()]
terms=[]
for (p,q),v in coeff:
 for i in range(p+1):
  for j in range(q+1):
   terms.append((i,j,p-i,q-j,8-p-q,v*comb(p,i)*comb(q,j)))

def upper(d,ix,iy):
 M=2**(d+1); A=2*ix+1; B=2*iy+1
 ap=[A**i for i in range(9)];bp=[B**i for i in range(9)];mp=[M**i for i in range(9)]
 z=[0]*81
 for i,j,p,q,m,v in terms:z[i*9+j]+=v*ap[p]*bp[q]*mp[m]
 return z[0]+sum(abs(t) for t in z[1:])

def within(d,ix,iy):
 # region x,y each [27/100, 40/100]
 M=2**d
 return 100*ix>=27*M and 100*(ix+1)<=40*M and 100*iy>=27*M and 100*(iy+1)<=40*M

def outside(d,ix,iy):return ix+iy>=2**d

def prune():
 stack=[(0,0,0)];count=0;kept=0;maxd=0;outsidec=0
 t=monotonic()
 while stack:
  d,ix,iy=stack.pop();count+=1;maxd=max(maxd,d)
  if outside(d,ix,iy):outsidec+=1;continue
  if within(d,ix,iy):kept+=1;continue
  if upper(d,ix,iy)<0:continue
  if d>=19:raise ValueError(('maxdepth',d,ix,iy,count))
  stack.extend([(d+1,2*ix+u,2*iy+v) for u in (0,1) for v in (0,1)])
 print('prune',count,kept,outsidec,maxd,'time',monotonic()-t)
prune()
from functools import lru_cache
W=sp.expand(F.subs({a:x,b:y,c:1-x-y},simultaneous=True));S=sp.expand(S.subs({a:x,b:y,c:1-x-y},simultaneous=True));
Fi=[sp.diff(W,v) for v in (x,y)];Si=[sp.diff(S,v) for v in (x,y)]
Ns={}
for i in range(2):
 for j in range(i,2):
  ij=sp.expand(sp.diff(Fi[i],(x,y)[j])*S*S-4*S*(Fi[i]*Si[j]+Fi[j]*Si[i]+W*sp.diff(Si[i],(x,y)[j]))+20*W*Si[i]*Si[j])
  Ns[i,j]=ij
D=sp.expand(Ns[0,0]*Ns[1,1]-Ns[0,1]**2)
print('degrees',[(k,sp.Poly(t,x,y).total_degree(),len(sp.Poly(t,x,y).terms())) for k,t in Ns.items()],'det',sp.Poly(D,x,y).total_degree(),len(sp.Poly(D,x,y).terms()))

def positive_on_region(poly,sign):
 # verify sign*poly>0 using Taylor on dyadic boxes of [27/100,40/100]^2
 poly=sp.Poly(sp.expand(sign*poly),x,y)
 dg=poly.total_degree()
 terms2=[]
 for (p,q),val in poly.terms():
  val=int(val)
  for i in range(p+1):
   for j in range(q+1):
    terms2.append((i,j,p-i,q-j,dg-p-q,i+j,val*comb(p,i)*comb(q,j)))
 def upper2(d,ix,iy):
  M=2**(d+1); A=27*M+13*(2*ix+1); B=27*M+13*(2*iy+1);den=100*M
  ap=[A**i for i in range(dg+1)];bp=[B**i for i in range(dg+1)];mp=[den**i for i in range(dg+1)]; rp=[13**i for i in range(dg+1)]
  z=[0]*((dg+1)**2)
  for i,j,p,q,m,rad,v in terms2:z[i*(dg+1)+j]+=v*ap[p]*bp[q]*mp[m]*rp[rad]
  return z[0]+sum(abs(t) for t in z[1:])
 stack=[(0,0,0)];seen=0;maxd=0;t=monotonic()
 while stack:
  d,ix,iy=stack.pop();seen+=1;maxd=max(maxd,d)
  if upper2(d,ix,iy)<0:continue
  if d>=14:raise ValueError(('hessian certificate failed',d,ix,iy,seen))
  stack.extend([(d+1,2*ix+u,2*iy+v) for u in (0,1) for v in (0,1)])
 print('proved',dg,seen,'cells',maxd,'depth',round(monotonic()-t,2),'sec')

positive_on_region(Ns[0,0],1)
positive_on_region(Ns[1,1],1)
positive_on_region(D,-1)

# Unique root existence already proved by localization and strict Hessian. Numerical values are illustrative.
Jx=sp.diff(W,x)*S-4*W*sp.diff(S,x)
Jy=sp.diff(W,y)*S-4*W*sp.diff(S,y)
r=sp.nsolve((Jx,Jy),(x,y),(sp.Rational(1,3),sp.Rational(7,20)),prec=40)
xx,yy=[float(t) for t in r];zz=1-xx-yy
assert 0.27<xx<0.4 and 0.27<yy<0.4
K8=float((W/S**4).subs({x:xx,y:yy}))
assert abs(K8-9.22177072362030)<1e-10
assert float(F.subs({a:1000,b:1050,c:951})/(1000**2+1050**2+951**2)**4)>9.2
print('VERIFY_OK rational_localization=253 hessian_certs=7 positive_root',xx,yy,zz,'K8power',K8,'K8',K8**.125)
