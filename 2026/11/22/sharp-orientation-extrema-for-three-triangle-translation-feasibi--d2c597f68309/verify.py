import numpy as np, math
from scipy.spatial import ConvexHull
pi=math.pi
T=np.array([[math.cos(2*pi*j/3),math.sin(2*pi*j/3)] for j in range(3)])
A=ConvexHull(T).volume
rng=np.random.default_rng(20261120)
def rot(t):
 c,s=np.cos(t),np.sin(t);return np.array([[c,-s],[s,c]])
def empirical(scales,theta):
 polys=[s*T@rot(t).T for s,t in zip(scales,theta)]
 p=np.array([np.r_[u-v,u-w]for u in polys[0] for v in polys[1] for w in polys[2]])
 return ConvexHull(p).volume
def formula(scales,theta):
 a,b,c=scales
 delta=lambda x:abs((x+pi/3)%(2*pi/3)-pi/3)
 pair=[c*math.cos(delta(theta[0]-theta[1])),b*math.cos(delta(theta[0]-theta[2])),a*math.cos(delta(theta[1]-theta[2]))]
 return A*A*(a*a*b*b+a*a*c*c+b*b*c*c+4*a*b*c*sum(pair))
for i in range(250):
 a=rng.uniform(.2,3,size=3); th=rng.uniform(-10,10,size=3)
 v=empirical(a,th); t=formula(a,th)
 assert abs(v-t) <= 3e-8*max(t,1), (i,v,t)
for ss in [(1,1,1),(.75,1.5,2),(2,2,.5),(4,2,1)]:
 arr=np.array(ss,dtype=float)
 j=int(np.argmin(arr))
 th=np.zeros(3); th[j]=np.pi/3
 v=empirical(arr,th)
 base=A*A*sum(arr[i]**2*arr[j]**2 for i in range(3) for j in range(i+1,3))
 tmin=base+2*A*A*np.prod(arr)*(sum(arr)+min(arr))
 tmax=base+4*A*A*np.prod(arr)*sum(arr)
 assert abs(v-tmin)<1e-8
 assert abs(empirical(arr,[0,0,0])-tmax)<1e-8
 print('scales',ss,'min',round(tmin/A**2,9),'max',round(tmax/A**2,9))
print('PASS 250 randomized 4D convex-hull formula checks and eight sharp extrema')
