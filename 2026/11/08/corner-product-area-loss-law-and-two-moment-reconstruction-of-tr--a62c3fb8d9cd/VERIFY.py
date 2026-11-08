#!/usr/bin/env python3
"""Numerical cross-checks of the polygon boundary-sample area-loss theorem."""
import math
import numpy as np
from scipy.spatial import ConvexHull

rng=np.random.default_rng(482731)

def setting(vertices):
    pts=np.array(vertices,dtype=float); vs=np.roll(pts,-1,axis=0)-pts
    lens=np.linalg.norm(vs,axis=1); P=lens.sum(); area=ConvexHull(pts).volume
    sins=[]
    for i in range(len(pts)):
        left=pts[i-1]-pts[i];right=pts[(i+1)%len(pts)]-pts[i]
        s=abs(np.linalg.det(np.array([left,right])))/np.linalg.norm(left)/np.linalg.norm(right)
        sins.append(s)
    return pts,vs,lens,P,area,np.array(sins)

def sample(vertices,N):
    pts,vs,lens,P,area,sins=setting(vertices)
    u=np.sort(rng.uniform(0,P,N)); edges=np.searchsorted(np.cumsum(lens),u,side='right')
    prev=np.r_[0,np.cumsum(lens)[:-1]]
    locations=pts[edges]+(u-prev[edges])[:,None]/lens[edges,None]*vs[edges]
    exact=None
    if np.all(np.bincount(edges,minlength=len(lens))>=2):
        L=[];R=[]
        for j in range(len(lens)):
            sj=u[edges==j]-prev[j]
            L.append(float(sj[0]));R.append(float(lens[j]-sj[-1]))
        # vertex i: distance from vertex i on left edge = R[i-1]; on right edge = L[i]
        exact=sum(.5*sins[i]*R[i-1]*L[i] for i in range(len(lens)))
    hull_loss=area-ConvexHull(locations).volume
    return hull_loss,exact

def exact_inversion(sides):
    a,b,c=map(float,sides);P=a+b+c
    assert a+b>c and b+c>a and c+a>b
    area=math.sqrt((P/2)*(P/2-a)*(P/2-b)*(P/2-c))
    R=a*b*c/(4*area)
    mu=P**3/(4*R)
    var=3*P**4/(16*R**2)*(a*a+b*b+c*c)
    R2=P**3/(4*mu)
    e2=(P*P-P*P*var/(3*mu*mu))/2
    disc=16*P*P*R2**4+R2*R2*(4*P*P*e2-P**4)
    e3=-4*P*R2*R2+math.sqrt(disc)
    roots=sorted(np.roots([1,-P,e2,-e3]).real)
    assert np.allclose(roots,sorted(sides),rtol=2e-5,atol=2e-5)
    return mu,var,roots

triangles=[(3,4,5),(1,1,1),(2,2,3),(1,1,math.sqrt(2)),(0.5,0.7,1.0)]
for s in triangles:
    mu,var,root=exact_inversion(s)
    assert var/(mu*mu)>1-1e-10
print('exact inversions:',len(triangles))

shapes=[[(0,0),(3,0),(0,4)],[(0,0),(1,0),(0.5,math.sqrt(3)/2)],[(0,0),(4,0),(4,1),(0,1)],[(0,0),(3,0),(4,2),(1,3)]]
count=0
for vertices in shapes:
    pts,vs,lens,P,area,sins=setting(vertices)
    for _ in range(120):
        loss,cap=sample(vertices,120)
        assert cap is not None
        assert abs(loss-cap)<5e-12*max(area,1)
        count+=1
    # sample near-asymptotic law of corner products at fixed N
    C=P*P/2*sins
    target_mean=float(sum(C))
    target_var=float(3*sum(C*C))
    assert sum(sins)<=len(sins)*math.sin(2*math.pi/len(sins))+1e-10
    Z=[]
    for _ in range(1600):
        loss,cap=sample(vertices,600)
        Z.append(loss*600**2)
    avg=float(np.mean(Z)); v=float(np.var(Z))
    # tight tolerance for mean; variance is noisy due to EF heavy tails
    assert abs(avg/target_mean-1)<0.17,(vertices,avg,target_mean)
    assert abs(v/target_var-1)<0.45,(vertices,v,target_var)
    print('shape',len(vertices),'mean scaled',round(avg,3),'theory',round(target_mean,3), 'var ratio',round(v/target_var,3))
print('VERIFY_OK triangle_inversions=5 exact_cap_hull_identities=',count,'scaled_area_trials=',4*1600)
