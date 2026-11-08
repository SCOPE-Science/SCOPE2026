import numpy as np, math
from scipy.spatial import ConvexHull
c=0; failures=[]; active=0; idle=0
for n in range(3,40):
 a=2*math.pi/n;b=a/2;C=math.cos(b)
 for rho in [0.12,C-0.001,C,C+0.001,(1+C)/2,0.999,1.0]:
  if not (0<rho<=1): continue
  for k in range(41):
   delta=k*b/40
   outer=np.array([(math.cos(j*a),math.sin(j*a)) for j in range(n)])
   inner=np.array([(rho*math.cos(j*a+delta),rho*math.sin(j*a+delta)) for j in range(n)])
   pts=np.vstack([outer,inner]); hull=ConvexHull(pts)
   AA=hull.volume;PP=hull.area
   x=rho*math.cos(b-delta)
   A=n*math.sin(b)*max(C,x)
   P=n*2*math.sin(b) if x<=C else n*(math.sqrt(1+rho*rho-2*rho*math.cos(delta))+math.sqrt(1+rho*rho-2*rho*math.cos(a-delta)))
   c+=1
   if x>C: active+=1
   else: idle+=1
   if abs(AA-A)>2e-7 or abs(PP-P)>2e-7: failures.append((n,rho,delta,AA,A,PP,P));
print('ROTATIONAL_HULL_PROFILE_TESTS',c,'active',active,'inactive',idle,'failures',len(failures))
print(failures[:5])
if failures:raise SystemExit(1)
