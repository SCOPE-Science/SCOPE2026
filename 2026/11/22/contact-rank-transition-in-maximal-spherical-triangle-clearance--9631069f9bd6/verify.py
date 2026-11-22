import math, numpy as np, mpmath as mp
from scipy.integrate import quad
mp.mp.dps=65

def normals(a):
 return np.array([[1.,0,0],[0,1.,0],[a,a,math.sqrt(1-2*a*a)]])

def classify(N):
 G=N@N.T
 candidates=[]
 for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:
  c=G[i,j];r=math.sqrt((1+c)/2)
  p=(N[i]+N[j])/math.sqrt(2+2*c)
  v=float(N[k]@p-r)
  candidates.append(((i,j),v,r))
 acceptable=[z for z in candidates if z[1]>=-1e-12]
 if acceptable:
  i,j=acceptable[0][0];r=acceptable[0][2]
  return ('critical' if abs(acceptable[0][1])<1e-12 else 'two',r, (i,j),candidates)
 lamb=np.linalg.solve(G,np.ones(3));lamb=lamb/lamb.sum()
 r=1/math.sqrt(np.ones(3)@np.linalg.solve(G,np.ones(3)))
 return ('three',r,lamb,candidates)

def A3(N,s):
 # exact 3-facet Gauss-Bonnet formula with mp precision
 M=[[mp.mpf(str(v)) for v in row] for row in N]
 s=mp.mpf(s)
 c=lambda i,j:sum(M[i][z]*M[j][z] for z in range(3))
 def cross(a,b):
  return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
 def dot(a,b):return sum(x*y for x,y in zip(a,b))
 v={}
 for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:
  ci=c(i,j); h=[s*(M[i][h]+M[j][h])/(1+ci) for h in range(3)]
  z=cross(M[i],M[j]);norm=mp.sqrt(dot(z,z));z=[x/norm for x in z]
  w=mp.sqrt(1-dot(h,h));vv=[[h[m]+sign*w*z[m] for m in range(3)] for sign in [+1,-1]]
  v[i,j]=max(vv,key=lambda u:dot(M[k],u))
 sides=[]
 for i in range(3):
  j,k=[x for x in range(3) if x!=i]
  u=v[min(i,j),max(i,j)];w=v[min(i,k),max(i,k)]
  sides.append(mp.acos((dot(u,w)-s*s)/(1-s*s)))
 return 2*mp.pi-sum(mp.acos((c(i,j)-s*s)/(1-s*s)) for i,j in [(0,1),(0,2),(1,2)])-s*sum(sides)

def lens(e):
 r=1/mp.sqrt(2);b=r;rho=mp.asin(r); s=mp.sin(rho-mp.mpf(e));
 alpha=mp.pi-mp.acos(-s*s/(1-s*s))
 delta=mp.acos((2*(s/r)**2-1-s*s)/(1-s*s))
 return 2*alpha-2*s*delta

def critical(e):
 r=math.sqrt(.5);b=r;h=math.sqrt(.5)
 rho=math.asin(r);s=math.sin(rho-e)
 Y=math.sqrt(1-(s/r)**2)
 def xlim(y):
  out=r*math.sqrt(max(0.,1-s*s-y*y))-s*b
  if y<0:
   z=1-y*y-((s-h*y)/r)**2
   if z<=0:return 0
   out=min(out,math.sqrt(z))
  return max(0.,out)
 def f(y):return 2*math.asin(min(1,max(0,xlim(y)/math.sqrt(1-y*y))))
 return quad(f,-Y,0,epsabs=1e-13)[0]+quad(f,0,Y,epsabs=1e-13)[0]

for a in [.35,.5,.6]:
 N=normals(a);role,r,pair,candidates=classify(N);rho=math.asin(r)
 print('a',a,'role',role,'rho',rho,'pair gaps',[(x[0],round(x[1],5)) for x in candidates]);
 if role=='three':
  o=np.linalg.solve(N,np.ones(3));o/=np.linalg.norm(o)
  b=math.sqrt(1-r*r)
  c=N@N.T
  alpha=[math.pi-math.acos((c[i,j]-r*r)/(b*b)) for i,j in [(0,1),(0,2),(1,2)]]
  C=sum(1/math.tan(v/2) for v in alpha)
 else:
  b=math.sqrt(1-r*r)
  C=(8/3)*math.sqrt(2*b/r)*(0.5 if role=='critical' else 1.)
 for e in [.015,.005,.0015]:
  if role=='three':
   A=A3(N,mp.sin(mp.mpf(str(rho-e))))
   ratio=float(A)/e**2
  elif role=='two':ratio=float(lens(e))/e**1.5
  else: ratio=critical(e)/e**1.5
  print(' eps',e,'ratio',ratio,'target',C)

# Diagnostic convergence assertions for all three distinct regimes.
for aa, expected, power, tolerance in [(0.35,6.746192341692526,2,0.08),(0.5,1.8856180831641265,1.5,0.11),(0.6,3.771236166328253,1.5,0.01)]:
 N=normals(aa); role,r,_,_=classify(N)
 eps=0.0015
 value=(float(A3(N,mp.sin(mp.mpf(str(math.asin(r)-eps))))) if role=='three' else critical(eps) if role=='critical' else float(lens(eps))) / eps**power
 assert abs(value-expected)<tolerance, (aa,role,value,expected)
# Non-symmetric critical configuration: the unused tight normal can have a tangential component along the active pair.
NN=np.array([[1.,0.,0.],[0.,1.,0.],[0.3,0.7,math.sqrt(0.42)]])
role,rr,pair,_=classify(NN)
assert role=='critical' and pair==(0,1)
assert abs(float((NN[2]@(NN[0]-NN[1]))/(2*math.sqrt(1-rr*rr))))>0.1
print('PASS: three contact regimes, asymmetric critical normal, and independent spherical area diagnostics')
