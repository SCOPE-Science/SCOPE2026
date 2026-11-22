from fractions import Fraction as F
from itertools import product,combinations
from math import atan2, sqrt

def cross(a,b):return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def det3(a,b,c):return dot(a,cross(b,c))
def covariance_pred(w):
 r=len(w); dim=r-1; H=sum(1/x for x in w)
 b=[tuple(F(int(j==i)) for j in range(dim)) for i in range(dim)]+[tuple(F(-1) for _ in range(dim))]
 return [[sum((w[k]*w[k]/12+w[k]/(6*H))*b[k][i]*b[k][j] for k in range(r)) for j in range(dim)] for i in range(dim)]
def add_moment(acc,v,weight,denom):
 d=len(v[0]); ss=[sum(q[i] for q in v) for i in range(d)]
 for i in range(d):
  for j in range(d):acc[i][j]+=weight*(sum(q[i]*q[j] for q in v)+ss[i]*ss[j])/denom

def exact_cycle_cov(w):
 r=len(w); dim=r-1
 assert dim in (2,3)
 pts=[]
 for z in product((0,1),repeat=r):
  p=tuple(sum((F(z[i])*w[i] if i==k else F(0)) for i in range(dim))-F(z[dim])*w[dim] for k in range(dim))
  p=tuple(p[i]-(w[i]-w[-1])/2 for i in range(dim))
  if p not in pts:pts.append(p)
 d=dim; cov=[[F(0) for j in range(d)] for i in range(d)];mean=[F(0)]*d; volume=F(0)
 if dim==2:
  ps=sorted(pts)
  def cr(a,b,c):u=sub(b,a);v=sub(c,a);return u[0]*v[1]-u[1]*v[0]
  low=[];up=[]
  for p in ps:
   while len(low)>=2 and cr(low[-2],low[-1],p)<=0:low.pop()
   low.append(p)
  for p in ps[::-1]:
   while len(up)>=2 and cr(up[-2],up[-1],p)<=0:up.pop()
   up.append(p)
  hull=low[:-1]+up[:-1]
  for a,b in zip(hull,hull[1:]+hull[:1]):
   v=[(F(0),F(0)),a,b]; vol=abs(a[0]*b[1]-a[1]*b[0])/2
   volume+=vol;add_moment(cov,v,vol,F(12))
   for i in range(d):mean[i]+=vol*sum(q[i] for q in v)/3
 else:
  faces={}
  for ii,jj,kk in combinations(range(len(pts)),3):
   a,b,c=pts[ii],pts[jj],pts[kk]; normal=cross(sub(b,a),sub(c,a))
   if normal==(0,0,0):continue
   sides=[dot(normal,sub(p,a)) for p in pts]
   if not (all(x>=0 for x in sides) or all(x<=0 for x in sides)):continue
   face=frozenset(i for i,s in enumerate(sides) if s==0)
   if len(face)>=3:faces[face]=normal
  for fi,normal in faces.items():
   fpts=[pts[i] for i in fi]
   center=[sum(p[i] for p in fpts)/len(fpts) for i in range(d)]
   u=sub(fpts[0],center);v=cross(normal,u)
   ordered=sorted(fpts,key=lambda p:atan2(float(dot(sub(p,center),v)),float(dot(sub(p,center),u))))
   for k in range(1,len(ordered)-1):
    a,b,c=ordered[0],ordered[k],ordered[k+1]
    vol=abs(det3(a,b,c))/6
    volume+=vol;add_moment(cov,[(F(0),)*d,a,b,c],vol,F(20))
    for i in range(d):mean[i]+=vol*(a[i]+b[i]+c[i])/4
 for i in range(d):mean[i]/=volume
 for i in range(d):
  for j in range(d):cov[i][j]=cov[i][j]/volume-mean[i]*mean[j]
 return cov,volume,len(pts)
for ws in ([1,2,3],[2,3,5],[1,1,1],[1,2,3,4],[2,3,5,7],[1,1,1,1],[1,3,5,8]):
 w=[F(x) for x in ws]
 got,vol,np=exact_cycle_cov(w); exp=covariance_pred(w)
 assert got==exp, (ws,got,exp)
 print(ws, 'OK', 'vol',vol,'corners',np)
 # Exact inverse consistency: the harmonic scalar solves the stated equations.
 H=sum(1/a for a in w); t=1/H
 for a in w:
  c=a*a/12+a*t/6
  assert (a+t)**2==t*t+12*c
 assert t*sum(1/a for a in w)==1
print('WEIGHTED_CACTUS_COVARIANCE_AND_INVERSE_PASS')
