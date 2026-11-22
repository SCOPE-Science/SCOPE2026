"""Independent finite diagnostics for exact inverse-valence theorem (not an infinite proof)."""
import math
import sympy as s
from scipy.optimize import brentq
x,y,z,a,b,k=s.symbols('x y z a b k', real=True)
S=s.symbols('S', real=True)
J=s.Matrix([[-a*S,1,0],[b,k*s.sin(z),k*y*s.cos(z)],[0,1,1]])
assert s.simplify(J.det()+b+a*S*k*(s.sin(z)-y*s.cos(z)))==0
u,X,Y,Z,c=s.symbols('u X Y Z c',real=True)
for sign in (-1,1):
 H=sign*c*(u+1-X)+k*u*s.sin(Z-u)
 assert s.simplify(s.diff(H,u)-(sign*c+k*s.sin(Z-u)-k*u*s.cos(Z-u)))==0
 print('symbolic inverse', sign, 'PASS')

def h(u,sgn,a,b,k,X,Y,Z):
 return sgn*(b/a)*(u+1-X)+k*u*math.sin(Z-u)-Y

def roots_at_centers(a,b,k,X,Y,Z,sgn,center_type,lower_n=40,upper_n=65):
 # Evaluate the high-cell signs and find roots at each monotonic small half-phase vicinity.
 roots=[]
 for n in range(lower_n,upper_n):
  center=Z+(math.pi/2 if center_type=='min' else -math.pi/2)+2*math.pi*n
  if center < max(1., X-1)+4: continue
  c=b/a
  C=sgn*c*(1-X)
  def stable_local(u):
   delta=u-center
   return C-Y+sgn*c*u*(2*math.sin(delta/2)**2)
  v0=C-Y
  for l,r in ((center-.5,center),(center,center+.5)):
   vl,vr=stable_local(l),stable_local(r)
   if vl*vr<0:
    rt=brentq(stable_local,l,r,xtol=1e-12)
    xx=sgn*(rt+1-X)/a
    zz=Z-rt
    F=(1-a*abs(xx)+rt, b*xx+k*rt*math.sin(zz), zz+rt)
    assert max(abs(F[j]-[X,Y,Z][j]) for j in range(3))<2e-9
    roots.append(rt)
  if v0==0:
   rt=center;xx=sgn*(rt+1-X)/a;zz=Z-rt
   assert abs(b*xx+k*rt*math.sin(zz)-Y)<2e-10
   roots.append(rt)
 return roots

# Critical cases: center minima for +, maxima for -; count roots per 2pi per branch.
for X,Y,expected in [(0.,0.,(0,0)),(0.,.8,(2,0)),(0.,.4,(1,0)),(0.,-.8,(0,2)),(2.,0.,(2,2))]:
 a,b,k,Z=1.,.4,.4,.27
 counts=[]
 for sg,ct in [(1,'min'),(-1,'max')]:
  roots=roots_at_centers(a,b,k,X,Y,Z,sg,ct)
  counts.append(len(roots))
 assert counts==[25*expected[0],25*expected[1]], (X,Y,counts,expected)
 print('critical X,Y',X,Y,'roots',counts,'PASS')
# Supercritical: one simple root near each of 2 phase solutions / sign / 2pi.
for X,Y,Z in [(0.,0.,.27),(4.,-18.,.9)]:
 a,b,k=1.,.4,.8; c=b/a; total=0
 for sign in (1,-1):
  for n in range(40,65):
   # sin(Z-u)=-sign*c/k plus small correction. phase near asin(target), and pi - asin(target)
   v=math.asin(-sign*c/k)
   for angle in (v,math.pi-v):
    center=Z-angle+2*math.pi*n
    if center<0:continue
    l,r=center-.2,center+.2
    assert h(l,sign,a,b,k,X,Y,Z)*h(r,sign,a,b,k,X,Y,Z)<0
    rt=brentq(lambda t:h(t,sign,a,b,k,X,Y,Z),l,r)
    xx=sign*(rt+1-X)/a
    zz=Z-rt
    assert max(abs(u-v) for u,v in zip((1-a*abs(xx)+rt,b*xx+k*rt*math.sin(zz),zz+rt),(X,Y,Z)))<1e-8
    total+=1
 assert total==100
 print('supercritical target',X,Y,Z,'high-cell ancestors',total,'PASS')
# Check leading inverse split law on critical + branch Y above fold.
a,b,k,X,Y,Z=1.,.4,.4,0.,.8,.27
c=b/a
for n in [100,1000,10000]:
 center=Z+math.pi/2+2*math.pi*n
 delta=Y-c*(1-X)
 predicted=(2*delta/(c*center))**.5
 left=brentq(lambda t:h(t,1,a,b,k,X,Y,Z),center-1.,center)
 right=brentq(lambda t:h(t,1,a,b,k,X,Y,Z),center,center+1.)
 assert abs((right-center)/predicted-1)<0.02
 assert abs((center-left)/predicted-1)<0.02
 print('fold split n',n,'ratios',round((right-center)/predicted,8),round((center-left)/predicted,8))
print('ALL DIAGNOSTICS PASS')
