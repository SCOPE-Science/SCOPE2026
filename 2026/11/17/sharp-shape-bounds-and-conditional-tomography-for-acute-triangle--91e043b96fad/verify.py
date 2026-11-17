"""Numerical corroboration of acute-triangle limits for two convex thin lenses."""
import numpy as np
rng=np.random.default_rng(20261110)

def check(name,h,dh_abs,coefficient,eps=0.02,n=3_000_000):
    count=0.;nobs=0;good_mx2=0.;sign_supp=0.
    for _ in range((n+199999)//200000):
        k=min(200000,n-nobs)
        x=rng.uniform(-1,1,size=(k,3))
        s=np.where(rng.random((k,3))<.5,-1,1)
        speed=np.sqrt(1+(eps*dh_abs(x))**2)
        # exact marginal uniform arclength importance weights (normalization via Gauss-Legendre)
        pts,ws=np.polynomial.legendre.leggauss(80)
        J=np.sum(ws*np.sqrt(1+(eps*dh_abs(pts))**2))
        weights=np.prod(speed*2/J,axis=1)
        ix=np.argsort(x,axis=1)
        x=np.take_along_axis(x,ix,axis=1)
        s=np.take_along_axis(s,ix,axis=1)
        y=eps*s*h(x)
        u=x[:,1]-x[:,0];v=x[:,2]-x[:,1]
        a=y[:,1]-y[:,0];b=y[:,2]-y[:,1]
        acute=(-u*v-a*b>0)&(u*(u+v)+a*(a+b)>0)&(v*(u+v)+b*(a+b)>0)
        c=weights*acute
        count+=c.sum();good_mx2+=np.dot(c,x[:,1]**2)
        sign_supp+=np.dot(c,(s[:,0]==s[:,2])&(s[:,0]!=s[:,1]))
        nobs+=k
    prob=count/nobs;lead=coefficient*eps**2*np.log(1/eps)
    print(name,'eps',eps,'mc',prob,'lead',lead,'ratio',prob/lead,'opposite-mid-share',sign_supp/count,'conditional-mid-x2',good_mx2/count)
    assert 0.80 <prob/lead<1.15
    assert sign_supp/count>0.85

def parabola(x):return 1-x*x
def parabola_d(x):return 2*np.abs(x)
def tent(x):return 1-np.abs(x)
def tent_d(x):return np.ones_like(x)
assert abs(1.5*16/15-1.6)<1e-12
assert abs(1.5*2/3-1)<1e-12
check('parabolic',parabola,parabola_d,1.6)
check('tent',tent,tent_d,1.)
print('THIN_LENS_ACUTENESS_TWO_SHAPES_OK')
