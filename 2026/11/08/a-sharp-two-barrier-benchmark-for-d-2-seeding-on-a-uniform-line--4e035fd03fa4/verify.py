"""Standalone exact and numerical checks of two-seed D-squared uniform-line k-means benchmark."""
from fractions import Fraction as F
from math import pi,sqrt,isclose

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return c
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def integ(a,lo,hi):return sum(v*(hi**(i+1)-lo**(i+1))/F(i+1) for i,v in enumerate(a))
def cpoly(x,reverse=False):
 # polynomial in y of C(x,y) where x<=y, or with x,y exchanged when y<=x
 if reverse: # C(y,x)= [3y^3+3y²x-3yx²-3x³+12x²-12x+4]/12
  return [(-3*x**3+12*x*x-12*x+4)/12,-x*x/4,x/4,F(1,4)]
 # C(x,y) = [3x³+3x²y-3xy²-3y³+12y²-12y+4]/12
 return [(3*x**3+4)/12,(3*x*x-12)/12,(12-3*x)/12,F(-1,4)]
def q_direct(x):
 w=[x*x,-2*x,F(1)]
 return integ(mul(cpoly(x,True),w),F(0),x)+integ(mul(cpoly(x,False),w),x,F(1))
def q_poly(x):return (-66*x**6+198*x**5-135*x**4-60*x**3+105*x*x-42*x+7)/360
def v(x):return x*x-x+F(1,3)
def p_poly(x):return (-198*x**4+396*x**3+57*x*x-255*x+41)/1080
checks=0
for d in range(2,35):
 for k in range(d+1):
  x=F(k,d)
  assert q_direct(x)==q_poly(x),(x,q_direct(x),q_poly(x))
  assert q_poly(x)==v(x)*p_poly(x)+F(11,1620)
  checks+=2
# Exact integral of P(x):
assert sum(c/F(i+1) for i,c in enumerate([F(41,1080),F(-255,1080),F(57,1080),F(396,1080),F(-198,1080)]))==-F(3,400)
checks+=1
E=11*sqrt(3)*pi/1215-3/400
R=48*E
assert 2<R<2.01
assert (157*433)*176*25>(59*405)*(50*250)
checks+=2

def cfun(x,y):
 if x>y:x,y=y,x
 return (3*x**3+3*x*x*y-3*x*y*y-3*y**3+12*y*y-12*y+4)/12

def simpson(f,n=1000):
 h=1/n
 return h/3*(f(0)+f(1)+4*sum(f(i*h) for i in range(1,n,2))+2*sum(f(i*h) for i in range(2,n,2)))
E1=simpson(lambda x:float(q_poly(x)/v(x)),1000)
assert abs(E1-E)<2e-11,(E1,E)
checks+=1
# Independent nested integration of actual Voronoi costs
E2=simpson(lambda x: simpson(lambda y:(y-x)**2*cfun(x,y),160)/float(v(x)),160)
assert abs(E2-E)<2e-9,(E2,E)
checks+=1
for n in [5,9,17,33,65,129]:
 xs=[i/(n-1) for i in range(n)]
 total=0
 for x in xs:
  denom=sum((y-x)**2 for y in xs)
  for y in xs:
   if x!=y:
    cost=sum(min((z-x)**2,(z-y)**2) for z in xs)/n
    total+=(y-x)**2/denom*cost/n
 assert total>0
 if n==129:assert abs(total-E)<0.002,(total,E)
 print('grid_n',n,'expected_cost',format(total,'.12f'))
 checks+=1
print('continuum_expected_cost',format(E,'.15f'))
print('continuum_ratio_to_optimal',format(R,'.15f'))
print('CHECKS_PASSED',checks)
