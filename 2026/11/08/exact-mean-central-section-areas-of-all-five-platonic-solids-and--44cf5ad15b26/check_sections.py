"""Independent numerical checks for central-plane section means of the Platonic solids.
Requires numpy and scipy. No external data or private state.
"""
import itertools, math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad
phi=(1+math.sqrt(5))/2
v={
 'tetra':np.array([(a,b,c) for a,b,c in itertools.product([-1,1],repeat=3) if a*b*c==1],float)/(2*math.sqrt(2)),
 'cube':np.array(list(itertools.product([-1,1],repeat=3)),float)/2,
 'octa':np.vstack((np.eye(3),-np.eye(3)))/math.sqrt(2),
 'icosa':np.array([(0,s,t*phi) for s,t in itertools.product([-1,1], repeat=2)]+[(s,t*phi,0) for s,t in itertools.product([-1,1],repeat=2)]+[(t*phi,0,s) for s,t in itertools.product([-1,1],repeat=2)],float)/2,
 'dodeca':np.array(list(itertools.product([-1,1],repeat=3))+[(0,s/phi,t*phi) for s,t in itertools.product([-1,1], repeat=2)]+[(s/phi,t*phi,0) for s,t in itertools.product([-1,1],repeat=2)]+[(t*phi,0,s/phi) for s,t in itertools.product([-1,1],repeat=2)],float)*phi/2,
}
solidinfo={'tetra':(4,3,math.sqrt(6)/12),'cube':(6,4,.5),'octa':(8,3,math.sqrt(6)/6),'dodeca':(12,5,math.sqrt(250+110*math.sqrt(5))/20),'icosa':(20,3,math.sqrt(3)*(3+math.sqrt(5))/12)}

def formula(F,p,h):
    c=math.pi/p; a=1/(2*math.tan(c));T=math.tan(c)
    I=a*math.asinh(a*T/math.hypot(h,a))+h*math.atan(h*T/math.sqrt(h*h+a*a*(1+T*T)))
    J=2*p*(I-h*c)
    directJ=2*p*quad(lambda z:math.sqrt(h*h+a*a/(math.cos(z)**2))-h,0,c,epsabs=1e-13)[0]
    assert abs(directJ-J)<2e-12
    return F*h*J/4

def section_area(pts,edges, normal):
    dots=pts@normal
    intersections=[]
    for i,j in edges:
      z1,z2=dots[i],dots[j]
      if z1*z2>0:continue
      point=(z2*pts[i]-z1*pts[j])/(z2-z1)
      intersections.append(point)
    q=np.array(intersections)
    a=np.cross(normal,[1,0,0])
    if np.linalg.norm(a)<.01:a=np.cross(normal,[0,1,0])
    a/=np.linalg.norm(a);b=np.cross(normal,a)
    proj=np.stack([q@a,q@b],axis=1)
    return ConvexHull(proj).volume

rng=np.random.default_rng(3712)
for name,points in v.items():
    F,p,h=solidinfo[name]
    ed=[(i,j) for i in range(len(points)) for j in range(i+1,len(points)) if abs(np.linalg.norm(points[i]-points[j])-1)<1e-8]
    # The polytope's geometric inradius follows from actual face planes.
    hull=ConvexHull(points)
    face_h=np.min(np.abs(hull.equations[:,3]))
    assert abs(face_h-h)<1e-10,(name,face_h,h)
    pred=formula(F,p,h)
    sumareas=0; nums=1200
    for k in range(nums):
       N=rng.standard_normal(3);N/=np.linalg.norm(N)
       sumareas+=section_area(points,ed,N)
    sim=sumareas/nums
    rel=abs(sim-pred)/pred
    print(name,'nverts',len(points),'nedges',len(ed),'mean',format(pred,'.12f'),'direct',format(sim,'.12f'),'rel',format(rel,'.4%'))
    assert rel<.035
print('CENTRAL_PLATONIC_SECTION_CHECKS_OK')
