"""Geometric numerical diagnostics for a right circular cone's projected boundary length.
Scientific proof is analytical; these tests only check selected instances.
Requires numpy and scipy. Run: python check_cone_shadow.py
"""
import math
import numpy as np
from scipy.special import ellipe, ellipeinc, ellipk, ellipkinc
from scipy.optimize import root
from scipy.spatial import ConvexHull

checks=0

def ck(cond,what):
 global checks
 checks+=1
 if not cond:
  raise AssertionError(what)

def perimeter_formula(c,h):
 assert 0<=c<=1 and h>0
 s=math.sqrt(max(0.,1-c*c))
 m=1-c*c
 if h*s<=c:
  return 4*ellipe(m)
 z=math.sqrt(h*h*s*s-c*c)
 alpha=math.atan2(1.,z)
 return 2*ellipe(m)+2*ellipeinc(alpha,m)+2*h*s*(z/(s*math.sqrt(1+h*h)))

def derivative_c(c,h):
 s=math.sqrt(1-c*c);m=1-c*c
 J=(ellipk(m)-ellipe(m))/m
 if h*s<=c:return 4*c*J
 z=math.sqrt(h*h*s*s-c*c)
 alpha=math.atan2(1.,z)
 J0=(ellipkinc(alpha,m)-ellipeinc(alpha,m))/m
 return 2*c*(J+J0-h*z/(s*s*math.sqrt(1+h*h)))

def p_hull(c,h,count=2048):
 t=np.arange(count)*(2*math.pi/count)
 s=math.sqrt(1-c*c)
 # Project physical 3D rim and apex on orthonormal plane coordinates.
 rim=np.column_stack((np.sin(t),-c*np.cos(t)))
 apex=np.array([[0.,h*s]])
 coords=np.concatenate([rim,apex],axis=0)
 hull=ConvexHull(coords)
 q=coords[hull.vertices]
 return np.linalg.norm(q-np.roll(q,-1,axis=0),axis=1).sum()

rng=np.random.default_rng(17026)
for _ in range(180):
 h=float(np.exp(rng.uniform(np.log(.15),np.log(8))))
 c=float(rng.uniform(0.0004,.9996))
 ans=perimeter_formula(c,h)
 independent=p_hull(c,h)
 ck(abs(ans-independent)<1.0e-4, ('hull',h,c,ans,independent))
for h in [.25,.5,1.,1.4,1.6,2.,3.,5.]:
 ck(abs(perimeter_formula(0.,h)-(2+2*math.sqrt(1+h*h)))<1e-12,'side')
 ck(abs(perimeter_formula(1.,h)-2*math.pi)<1e-12,'face')
 for c in np.linspace(.04,.98,20):
  fd=(perimeter_formula(float(c)+1e-5,h)-perimeter_formula(float(c)-1e-5,h))/2e-5
  ck(abs(fd-derivative_c(float(c),h))<2e-4,('derivative',h,c,fd,derivative_c(float(c),h)))
for h in [.2,.5,.99,1.]:
 vals=[perimeter_formula(float(c),h) for c in np.linspace(0,1,301)]
 ck(all(y>x-1e-10 for x,y in zip(vals,vals[1:])),('short-cone-increasing',h))
for h in [.5,1.,1.5,1.6015,2.,4.]:
 for c in [.005,.01,.02,.04]:
  d=perimeter_formula(c,h)-perimeter_formula(0,h)
  # local c^2 log, approximate ratio improves as c->0
  ck(d>0,('strict-local-side',h,c,d))
sol=root(lambda z:(perimeter_formula(z[0],z[1])-perimeter_formula(0,z[1]), derivative_c(z[0],z[1])),[.7957,1.6015],tol=1e-12)
ck(sol.success and np.linalg.norm(sol.fun)<2e-12,'root')
c0,h0=sol.x
ck(abs(c0-.7957267670648)<1e-9 and abs(h0-1.6014993044983)<1e-9,'critical numeric')
ck(perimeter_formula(c0,h0+.02)<perimeter_formula(0,h0+.02),'oblique beats side')
ck(perimeter_formula(c0,h0-.02)>perimeter_formula(0,h0-.02),'side beats candidate')
for c in np.linspace(.02,1,70):
 for h in [.25,.75,1.25,1.8,3.]:
  d=1e-4
  f=(perimeter_formula(float(c),h+d)-perimeter_formula(float(c),h-d))/(2*d)
  side=(2*(h+d)/math.sqrt(1+(h+d)**2))
  ck(f<side+1e-5,('relative slope',c,h,f,side))
print('PASS',checks,'checks; oblique tie h=',format(h0,'.13f'),'c=',format(c0,'.13f'))
