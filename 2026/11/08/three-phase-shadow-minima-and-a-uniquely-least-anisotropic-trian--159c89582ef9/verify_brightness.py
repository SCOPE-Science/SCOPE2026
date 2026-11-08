import math, random
SQ=math.sqrt(3)
e=[(math.cos(2*math.pi*j/3),math.sin(2*math.pi*j/3)) for j in range(3)]
def area_formula(h,u):
 x,y,z=u
 return SQ/2*sum(max(h*abs(x*a+y*b),abs(z)/2) for a,b in e)
def area_hull(h,u):
 x,y,z=u
 if abs(z)<.8:v=(-y,x,0)
 else:v=(0,z,-y)
 norm=math.sqrt(sum(t*t for t in v));v=tuple(t/norm for t in v)
 w=(y*v[2]-z*v[1],z*v[0]-x*v[2],x*v[1]-y*v[0])
 pts=[(a*v[0]+b*v[1],a*w[0]+b*w[1]) for a,b in e]+[(h*v[2],h*w[2]),(-h*v[2],-h*w[2])]
 pts=sorted(pts)
 def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 lo=[]
 for p in pts:
  while len(lo)>1 and cross(lo[-2],lo[-1],p)<=1e-12:lo.pop()
  lo.append(p)
 hi=[]
 for p in pts[::-1]:
  while len(hi)>1 and cross(hi[-2],hi[-1],p)<=1e-12:hi.pop()
  hi.append(p)
 hull=lo[:-1]+hi[:-1]
 return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(hull,hull[1:]+hull[:1])))/2

def extrema(h):
 return min(1.5*h,SQ*h/math.sqrt(1+h*h),9*h/(4*math.sqrt(1+3*h*h))),max(3*SQ/4,SQ*h)
r=random.Random(4328813)
for h in [0.05,0.2,0.5,1/math.sqrt(3),.65,math.sqrt(11/21),.75,1,2,10]:
 low,high=extrema(h)
 amin=1e99;amax=0
 for it in range(20000):
  z=2*r.random()-1
  theta=r.random()*2*math.pi
  s=math.sqrt(1-z*z);u=(s*math.cos(theta),s*math.sin(theta),z)
  a=area_formula(h,u)
  if it<50:
   b=area_hull(h,u)
   assert abs(a-b)<1e-9,(h,u,a,b)
  amin=min(amin,a);amax=max(amax,a)
  assert low-1e-9 <=a<= high+1e-9,(h,a,low,high)
 print('h',h,'bounds',low,high,'observed',amin,amax)
print('BIPYRAMID_SHADOW_BOUNDS_CHECKS_PASSED')

# Independently enumerate every cross-product direction of two facet
# normal planes, and every sign sum of the six facet area vectors.
import itertools

def norm(v): return math.sqrt(sum(x*x for x in v))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
for h in [.04,.25,.5,1/math.sqrt(3),.66,math.sqrt(11/21),.75,1,3,15]:
 normals=[(h*a,h*b,sgn*.5) for a,b in e for sgn in (-1,1)]
 rays=[]
 for a,b in itertools.combinations(normals,2):
  v=cross(a,b)
  if norm(v)>1e-12:
   rays.append(tuple(x/norm(v) for x in v))
 least=min(area_formula(h,r) for r in rays)
 greatest=max(norm(tuple(SQ/4*sum(s[i]*normals[i][j] for i in range(6)) for j in range(3))) for s in itertools.product((-1,1),repeat=6))
 a,b=extrema(h)
 assert abs(least-a)<1e-10,(h,least,a)
 assert abs(greatest-b)<1e-10,(h,greatest,b)
assert abs(extrema(.75)[1]/extrema(.75)[0]-math.sqrt(129)/9)<1e-12
print('FULL_FACET_PAIR_AND_SIGN_VECTOR_CERTIFICATES_PASSED')
