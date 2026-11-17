"""Numerical consistency checks for joint acuteness and center enclosure.
Analytic arguments, not simulation, prove the stated limit.
"""
import math
import numpy as np
from scipy.integrate import quad

C = 6*math.log(2)/math.pi**2
# Pair-kernel integral, evaluated by independent outer numerical quadrature.
J = 4*quad(lambda z: math.log(2)/math.sqrt(1-z*z),0,1,epsabs=1e-11)[0]
assert abs(J-2*math.pi*math.log(2))<1e-9
assert abs(3*J/math.pi**3-C)<1e-12

rng=np.random.default_rng(20261113)
for L in (5,10,20):
    n=2_000_000
    joint=acute_n=inside_n=0
    r_sum=ratio_sum=0.0
    for _ in range(n//100_000):
        theta=rng.uniform(0,2*math.pi,size=(100_000,3))
        theta.sort(axis=1)
        gap=np.diff(np.concatenate((theta,theta[:,:1]+2*math.pi),axis=1),axis=1)
        contained=gap.max(axis=1)<math.pi
        x=np.cos(theta)
        y=np.sin(theta)
        acute=np.ones(100_000,dtype=bool)
        for i,j,k in ((0,1,2),(1,0,2),(2,0,1)):
            acute &= L*L*(x[:,j]-x[:,i])*(x[:,k]-x[:,i])+(y[:,j]-y[:,i])*(y[:,k]-y[:,i])>0
        hit=acute&contained
        inside_n+=int(contained.sum());acute_n+=int(acute.sum());joint+=int(hit.sum())
        if L==20:
            xx=x[hit]
            d=np.abs(xx[:,:,None]-xx[:,None,:])
            d[:,np.arange(3),np.arange(3)]=float('inf')
            pair=np.argmin(d.reshape(-1,9),axis=1)
            i=pair//3;j=pair%3
            third=3-i-j
            row=np.arange(len(i))
            c=np.abs((xx[row,i]+xx[row,j])/2)
            r=np.abs(xx[row,third])
            good=r>c
            r_sum+=float(r[good].sum())
            ratio_sum+=float((c[good]/r[good]).sum())
    prob=joint/n
    print(f'axis_ratio={L}, acute={acute_n/n:.8f}, center={inside_n/n:.8f}, joint={prob:.8f}, scaled_joint={L*L*prob:.8f}, predicted={C:.8f}')
    assert abs(inside_n/n-0.25)<0.002
    assert abs(L*L*prob-C)<0.08
    if L==20:
        print('conditional_mark_means',r_sum/joint,ratio_sum/joint,'expected',2/math.pi,1/math.log(2)-1)
        assert abs(r_sum/joint-2/math.pi)<0.05
        assert abs(ratio_sum/joint-(1/math.log(2)-1))<0.05
print('ELLIPSE_JOINT_ACUTE_CENTER_CHECKS_OK')
