#!/usr/bin/env python3
"""Reproduce angular-density, area-ratio identity and endpoint estimates for random circle triangles.
Python 3; numpy. Monte Carlo supports but does not prove the analytic endpoint laws.
"""
import math
import numpy as np
rng=np.random.default_rng(20261113)
# All ordered interior angles are uniformly distributed over the angle simplex.
N=3_000_000
x=rng.exponential(size=(N,3)); x*=math.pi/x.sum(axis=1,keepdims=True)
q=2*np.abs(np.cos(x).prod(axis=1))
assert q.min()>=0 and q.max()<2
mean=0.25+3/math.pi**2
assert abs(q.mean()-mean)<0.003
for t in (0.02,0.01):
    lower=(q<=t).mean()
    asym=6/math.pi**2*t*math.log(1/t)
    # Log-cusp has an O(t) correction and converges slowly.
    assert 0.65 < lower/asym < 1.85, (t,lower/asym)
    upper=(q>2-t).mean()
    asym_upper=t/(math.pi*math.sqrt(3))
    assert abs(upper/asym_upper-1)<0.17,(t,upper/asym_upper)
# Direct projection identity for nondegenerate triangles, including obtuse ones.
for _ in range(100):
    angles=np.sort(rng.uniform(0,2*math.pi,3))
    pts=np.stack((np.cos(angles),np.sin(angles)),axis=1)
    feet=[]
    for j in range(3):
        u=pts[j];v=pts[(j+1)%3];w=pts[(j+2)%3]; d=w-v
        feet.append(v+d*(np.dot(u-v,d)/np.dot(d,d)))
    feet=np.array(feet)
    def area(z): return 0.5*abs(np.linalg.det(np.stack((z[1]-z[0],z[2]-z[0]))))
    A=np.array([(angles[2]-angles[1])/2,(2*math.pi-angles[2]+angles[0])/2,(angles[1]-angles[0])/2])
    assert abs(area(feet)/area(pts)-2*abs(np.cos(A).prod()))<2e-9
print('ORTHIC_AREA_RATIO_CHECKS_OK')
print('sample_mean',q.mean(),'exact_mean',mean)
for t in (0.02,0.01):
 print('t',t,'lower_ratio',(q<=t).mean()/(6/math.pi**2*t*math.log(1/t)),'upper_ratio',(q>2-t).mean()/(t/(math.pi*math.sqrt(3))))
