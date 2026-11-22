import math
import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull
PI=math.pi
PMID=2+2*math.sqrt(2)
C=3/(PI*math.sqrt(2-math.sqrt(2)))

def P(u):
  return 2*sum(math.sqrt(max(0.,1-v*v)) for v in u)

def cdf_branch(p,z):
  ss=math.sqrt(max(0.,1-z*z)); lo=2*(ss+z+1)
  hi=2*(ss+math.sqrt(2*(1+z*z)))
  if p<=lo: return 0.
  if p>=hi or z>=1-1e-15: return 1.
  A=p/2-ss
  X=((A*A-(1+z*z))**2-4*z*z)/(1-z*z)**2
  return 2/PI*math.asin(math.sqrt(max(0.,min(1.,X))))

def F(p):
  # break points where p hits lo or hi, no more than a few
  zgrid=np.linspace(0,1,501)
  cuts=[0.,1.]
  for fun in (lambda z: 2*(math.sqrt(1-z*z)+z+1)-p,
              lambda z: 2*(math.sqrt(1-z*z)+math.sqrt(2*(1+z*z)))-p):
    from scipy.optimize import brentq
    aa=[fun(z) for z in zgrid]
    for i in range(len(aa)-1):
      if aa[i]*aa[i+1] <0: cuts.append(brentq(fun,zgrid[i],zgrid[i+1],xtol=1e-13))
  cuts=sorted(set(cuts))
  return sum(quad(lambda z:cdf_branch(p,z),a,b,epsabs=5e-10,epsrel=5e-10,limit=150)[0] for a,b in zip(cuts[:-1],cuts[1:]))

rng=np.random.default_rng(20261116)
N=160000
G=rng.standard_normal((N,3));G/=np.linalg.norm(G,axis=1)[:,None]
V=2*np.sqrt(1-G*G).sum(axis=1)
print('P support',4,2*math.sqrt(6),'saddle',PMID,'log coefficient',C)
print('mc mean',V.mean(), 'analytic',3*PI/2)
for p in [4.10,4.25,4.50,4.70,4.80,PMID,4.85,4.88]:
 ex=F(p);mc=(V<=p).mean();sigma=math.sqrt(mc*(1-mc)/N)
 print('CDF',p,ex,mc,'sd',sigma)
 assert abs(ex-mc)<6*sigma+0.002
for d in [1e-2,5e-3,1e-3,3e-4,1e-4]:
 mass=F(PMID+d)-F(PMID-d)
 print('saddle eps',d,'mass',mass,'mass/(2eps log)',mass/(2*d*math.log(1/d)), 'expected', C)
for eps in [0.02,0.01,0.005]:
 print('lower',eps,F(4+eps)/eps**2, 'limit',3/8)
 print('upper',eps,(1-F(2*math.sqrt(6)-eps))/eps, 'limit',4*math.sqrt(2/3))
# Independent geometric check from actual planar hull of projected 8 vertices
from itertools import product
vertices=np.array(list(product([-.5,.5],repeat=3)))
for u in G[::1000]:
 e=np.array([1.,0.,0.]);
 if abs(np.dot(e,u))>.85: e=np.array([0.,1.,0.])
 e-=np.dot(e,u)*u; e/=np.linalg.norm(e)
 f=np.cross(u,e)
 v=np.column_stack([vertices@e,vertices@f]); hull=ConvexHull(v)
 vv=v[hull.vertices]; per=np.linalg.norm(vv-np.roll(vv,-1,axis=0),axis=1).sum()
 assert abs(per-P(u))<1e-10,(per,P(u))
print('independent convex hull cross-checks passed',len(G[::1000]))
assert 3.1 < (1-F(2*math.sqrt(6)-0.005))/0.005 < 3.5
assert 0.36 < F(4+0.005)/0.005**2 < 0.40
m1=(F(PMID+0.01)-F(PMID-0.01))/(2*0.01)
m2=(F(PMID+0.0001)-F(PMID-0.0001))/(2*0.0001)
cfit=(m2-m1)/math.log(100)
print('log coeff from two finite windows',cfit, 'predicted',C)
assert abs(cfit-C)<0.025
assert abs(F(4))<1e-12 and abs(F(2*math.sqrt(6))-1)<1e-12
assert all(F(a)<=F(b) for a,b in zip(np.linspace(4,2*math.sqrt(6),17)[:-1],np.linspace(4,2*math.sqrt(6),17)[1:]))
print('PASS all deterministic numerical diagnostics')
