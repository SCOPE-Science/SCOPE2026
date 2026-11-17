"""Reproducible finite-sample checks of the surface-volume orthogonal projection law."""
import math
import numpy as np

pi=math.pi
rng=np.random.default_rng(130261)
v2=8/3-pi*pi/4
v3=pi*pi/32-5/18
assert 0<v2 and 0<v3


def sample(n):
    a=rng.normal(size=(n,3))
    return a/np.linalg.norm(a,axis=1)[:,None]


def observed(a):
    n=len(a)
    s=0.; v=0.; residual=0.
    for i in range(n):
        for j in range(i+1,n):
            s+=2*np.linalg.norm(np.cross(a[i],a[j]))
            for k in range(j+1,n):
                cross=np.cross(a[i],a[j])
                det=abs(np.dot(cross,a[k]))
                ss=(np.linalg.norm(cross)+np.linalg.norm(np.cross(a[i],a[k]))+
                     np.linalg.norm(np.cross(a[j],a[k])))
                v+=det
                residual+=det-0.5*ss+pi/4
    e_s=(pi/2)*math.comb(n,2)
    e_v=(pi/8)*math.comb(n,3)
    assert abs((v-e_v)-(n-2)/4*(s-e_s)-residual)<1e-8
    return s,v,residual

for n,rep in [(3,16000),(5,7000),(8,3500)]:
    vals=np.array([observed(sample(n)) for _ in range(rep)])
    s,v,res=vals.T
    var_s=math.comb(n,2)*v2
    var_res=math.comb(n,3)*v3
    covariance=(n-2)/4*var_s
    var_v=((n-2)**2/16)*var_s+var_res
    rho=(1+16*v3/(3*(n-2)*v2))**(-0.5)
    assert abs(np.mean(s)-(pi/2)*math.comb(n,2))<7*math.sqrt(var_s/rep)
    assert abs(np.mean(v)-(pi/8)*math.comb(n,3))<7*math.sqrt(var_v/rep)
    assert abs(np.var(s)-var_s)<0.08*var_s
    print("n",n,"sample var_res",np.var(res),"claimed",var_res,"cov",np.cov(s,v,bias=True)[0,1],"pred",covariance,flush=True)
    assert abs(np.var(res)-var_res)<0.15*var_res
    assert abs(np.cov(s,v,bias=True)[0,1]-covariance)<0.1*covariance
    assert abs(np.corrcoef(s,v)[0,1]-rho)<0.055
print('SPHERICAL_ZONOTOPE_JOINT_MOMENT_AND_ORTHOGONALITY_CHECKS_PASSED')
