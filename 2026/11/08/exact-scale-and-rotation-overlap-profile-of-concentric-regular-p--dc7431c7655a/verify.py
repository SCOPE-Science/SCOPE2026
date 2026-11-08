import math,random

def vertices(n,apothem,rot):
 c=math.pi/n
 return [(apothem/math.cos(c)*math.cos(rot+(2*k+1)*c),apothem/math.cos(c)*math.sin(rot+(2*k+1)*c)) for k in range(n)]

def clip(poly, normal,h):
 out=[]
 if not poly:return out
 for p,q in zip(poly,poly[1:]+poly[:1]):
  a=p[0]*normal[0]+p[1]*normal[1]-h
  b=q[0]*normal[0]+q[1]*normal[1]-h
  if a<=1e-12:out.append(p)
  if (a< -1e-12 and b>1e-12) or (a>1e-12 and b< -1e-12):
   t=a/(a-b)
   out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
 return out

def area(poly):
 return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1]))/2)

def direct(n,a,b,phi):
 poly=vertices(n,b,phi)
 for k in range(n):
  ang=2*k*math.pi/n
  poly=clip(poly,(math.cos(ang),math.sin(ang)),a)
 return area(poly)

def formula(n,a,b,phi):
 c=math.pi/n
 q=b/a;C=math.cos(c);x=math.cos(c-phi)
 full=n*b*b*math.tan(c)
 if q*x<=C or abs(x-C)<1e-12:return full
 return full-n*a*a*math.sin(2*c)/(2*C*C)*(q*x-C)**2/(x*x-C*C)

random.seed(7)
maxe=0
for n in range(3,51):
 for i in range(150):
  a=0.5+random.random()*2
  b=a*random.uniform(0.01,1)
  phi=random.random()*math.pi/n
  exact=formula(n,a,b,phi);v=direct(n,a,b,phi)
  e=abs(exact-v)/max(1,exact)
  maxe=max(e,maxe)
  if e>2e-9:raise AssertionError((n,a,b,phi,exact,v,e))
print('ALL_OK',48*150,'max_relative',maxe)

# Endpoint and onset tests, independent of the random comparisons above.
for n in (3,4,5,7,12,50):
 c=math.pi/n; C=math.cos(c); a=1.3
 for q in (0.2*C, C, (1+C)/2, 1.0):
  b=a*q
  pmin=formula(n,a,b,c)
  predicted=n*b*b*math.tan(c)-n*max(0,b-a*C)**2/(C*math.sin(c))
  assert abs(pmin-predicted) < 2e-11
  # The first branch must include the complete containment plateau.
  if q<=C: assert abs(formula(n,a,b,c)-n*b*b*math.tan(c))<1e-12
  elif q<1:
   ph0=c-math.acos(C/q)
   assert abs(formula(n,a,b,ph0)-n*b*b*math.tan(c))<1e-11
   assert formula(n,a,b,(ph0+c)/2)<formula(n,a,b,ph0)
  else: assert formula(n,a,b,0)>formula(n,a,b,c)
print('PHASE_AND_ENDPOINTS_OK')
